"""生成网站用 WebP 和尺寸索引；保留原图供下载及重新生成。需要 Pillow。"""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'images/optimized'
INDEX = ROOT / '_data/image_assets.json'


def main():
    OUTPUT.mkdir(exist_ok=True)
    text = '\n'.join(
        p.read_text(encoding='utf-8')
        for folder in ['_data', '_members', '_posts', '_includes', '_layouts', 'contact', 'research', 'projects', 'team', 'news', 'gcp']
        for p in (ROOT / folder).rglob('*')
        if p.is_file() and p.suffix in {'.md', '.html', '.yaml', '.yml'}
    ) + (ROOT / 'index.md').read_text(encoding='utf-8') + (ROOT / '_config.yaml').read_text(encoding='utf-8')
    assets = {}
    before = after = 0
    for folder in ['images', 'avatar']:
        for source in sorted((ROOT / folder).rglob('*')):
            if source.suffix.lower() not in {'.jpg', '.jpeg', '.png'} or OUTPUT in source.parents:
                continue
            key = source.relative_to(ROOT).as_posix()
            if key not in text:
                continue
            portrait = '/avatar/' in key or key.startswith('avatar/')
            limit = 800 if portrait else (2400 if 'newspaper' in key else 1920)
            quality = 90 if '/research/' in key or 'newspaper' in key else 82
            digest = hashlib.sha256(source.read_bytes() + f'webp-v1-{limit}-{quality}'.encode()).hexdigest()[:16]
            with Image.open(source) as raw:
                if getattr(raw, 'is_animated', False):
                    continue
                raw.draft('RGB', (limit, limit))
                image = ImageOps.exif_transpose(raw)
                if image.mode not in {'RGB', 'RGBA'}:
                    image = image.convert('RGBA' if 'transparency' in image.info else 'RGB')
                max_width = min(image.width, limit)
                widths = sorted({min(w, max_width) for w in [320, 640, 960, max_width]})
                variants = []
                for width in widths:
                    target = OUTPUT / f'{digest}-{width}.webp'
                    height = round(image.height * width / image.width)
                    if not target.exists():
                        resized = image.resize((width, height), Image.Resampling.LANCZOS)
                        resized.save(target, 'WEBP', quality=quality, method=6)
                    variants.append({'path': target.relative_to(ROOT).as_posix(), 'width': width, 'height': height})
                assets[key] = {'src': variants[-1]['path'], 'small': min(variants, key=lambda v: abs(v['width'] - 960))['path'], 'variants': variants}
                before += source.stat().st_size
                after += (ROOT / assets[key]['src']).stat().st_size
    INDEX.write_text(json.dumps(assets, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(assets)} 张图片：默认版本 {before / 1e6:.2f} MB → {after / 1e6:.2f} MB，减少 {(1-after/before)*100:.1f}%')


if __name__ == '__main__':
    main()
