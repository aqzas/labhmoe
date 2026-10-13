# News 与 GCP 内容维护

顶部导航按 Research、Projects、Team、News、Clinical Trials / GCP、Contact 排列。旧 `/blog/` 地址重定向到 `/news/`。新闻继续使用 Jekyll `_posts`，临床研究统一从 `_data/trials.yml` 读取。

## 新增新闻

在 `_posts/` 新建 `YYYY-MM-DD-英文短标题.md`，文件名日期为实际发布日期。以下是编辑模板，不是实际新闻：

```markdown
---
title: "填写已核实的新闻标题"
date: 2026-09-28
published: false
# image: images/news/实际图片文件名.jpg
# author: wenxuan-jiang
# tags:
#   - conference
---

<!-- excerpt start -->
填写一两句新闻摘要。
<!-- excerpt end -->

填写真实新闻正文。
```

核对标题、日期、正文及图片后，将 `published` 改为 `true`。不要使用未来日期，否则 Jekyll 默认不会发布。`image`、`author`、`tags` 均可省略；不提供图片时按纯文字列表展示。有图片时可新建 `images/news/` 并填写准确路径。已有三篇 `example-post` 保留为 `published: false` 的模板，不在正式站点展示。

News 页面自动按时间展示新闻；首页在 UNIONCELL LAB 下方的第一个内容板块展示 News，目前按 `slug: tce-sle` 仅选取现有 Nature Medicine 报道。列表支持 `<!-- excerpt start -->` 和 `<!-- excerpt end -->` 之间的摘要，未提供时使用 Jekyll 默认摘要。新闻详情保留现有 post 布局。列表搜索支持标题、正文、作者和标签。

2026-10-08 资料包中的三个微信链接位于 News 页的「微信文章」区域，不加入首页。文章标题已按用户补充的顺序填写，依次为联合实验室第二次学术会议、联合实验室揭牌仪式、2025年武汉协和风湿免疫科学术年会报道；各链接在新标签页打开。

## 新增临床试验

在 `_data/trials.yml` 末尾添加一条记录。保持数据源原文，包括空格、大小写、斜杠、括号及产品类型，不翻译、不纠错、不补全。示例中的占位文字仅用于说明格式，应全部替换为真实来源后再保存：

```yaml
- id: trial-014
  sequence: 14
  title: "粘贴来源中的试验名称原文"
  indication: "粘贴来源中的适应症原文"
  intervention: "粘贴来源中的药物干预手段原文"
  phase: "粘贴来源中的临床分期原文"
  product_type: "粘贴来源中的产品类型原文"
  english_title: "粘贴来源中的临床试验英文名"
  registration_number: "粘贴来源中的注册号"
  registration_url: "粘贴来源中的登记平台链接"
```

`14` 仅用于演示，新增时使用数据源中的实际序号，并为 `id` 选择唯一值。页面按 `sequence` 升序展示，不重编号，原数据缺失序号 5 的情况予以保留。

| 字段 | 内容 |
| --- | --- |
| `id` | 唯一标识，用于卡片锚点 |
| `sequence` | Excel「序号」，保持原始数值 |
| `title` | Excel「试验名称」原文 |
| `indication` | Excel「适应症」原文 |
| `intervention` | Excel「药物干预手段」原文 |
| `phase` | Excel「临床分期」原文，不拆分为研究类型和分期 |
| `product_type` | Excel「产品类型」原文 |
| `english_title` | CSV「临床试验英文名」，显示在中文标题下方 |
| `registration_number` | CSV「注册号」，作为链接文字 |
| `registration_url` | CSV「超链接」，新标签页打开 |

初始数据逐字提取自原接入说明。2026-10-13 根据 `课题组网页更新资料包_2026-10-08` 补充三个字段，并与其中的原始 Excel 核对。新增字段使用技术导入 CSV，保留原有七个字段。CSV 已清除 Excel 英文名中的零宽字符及部分注册号、链接末尾的空格。

产品类型筛选按钮从数据自动生成，保持原文。新增类型无需修改 HTML 或 JavaScript。筛选使用原生 JavaScript；禁用 JavaScript 时仍可阅读全部项目。

不添加招募状态、PI 或来源中没有的其他字段，不生成独立详情页，不显示项目数量。上一版 `_trials` collection、示例和详情组件已移除。当前有 7 个 NCT 注册号指向试验详情页。5 个 CTR 注册号（CTR20254910、CTR20255045、CTR20253359、CTR20260744、CTR20252694）已按用户补充统一替换为 `https://www.chinadrugtrials.org.cn/clinicaltrials.searchlistdetail.dhtml`。该地址未携带试验标识，尚未验证无会话直接访问能否定位各自记录。第一项补充链接的文字为 CTR20263879，本次按指定卡片 CTR20254910 仅更新网址，保留原注册号。

## 招聘与重点论文

Contact 正文来自资料包中的招聘 Word，保留全部分段、标题层级和编号列表，邮箱使用 `mailto:` 链接。校园图为 `images/contact/hust-campus.jpg`，原尺寸 1080 × 1440，替代文字为「华中科技大学校园」。桌面端图片位于介绍文字左侧，手机端上下排列。

Research 的 Highlighted 按 DOI `10.1038/s41591-026-04572-7` 展示 Nature Medicine 论文；TCRdb 继续保留在 All / 2020。元数据写入 `_data/sources.yaml`，并同步至构建使用的 `_data/citations.yaml`，后续自动生成引用时会保留 sources 中的人工元数据。标题、33 位作者、期刊、2026-09-10 日期、卷页和 DOI 均采用实施说明；PDF 是校样，首页发表日期尚为占位符。配图使用 `images/research/a319-sle-nature-medicine.png`。

## 图片与样式

首页 Clinical Trials / GCP 模块优先使用 `images/home/gcp.png`，缺失时使用现有 `images/fallback.svg`。上传真实配图到该路径即可替换。

新闻组件为 `_includes/news-excerpt.html`，对应样式为 `_styles/news-excerpt.scss`。GCP 组件为 `_includes/trial-card.html`，对应样式为 `_styles/trial-card.scss`，筛选脚本为 `_scripts/trial-filter.js`。现有样式和脚本加载器自动加载这些文件，无需改写加载机制。

## 本地预览

安装与项目兼容的 Ruby 和 Bundler 后，在项目根目录运行：

```sh
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

默认预览地址为 `http://localhost:4000`。发布前检查 `/gcp/` 的产品类型筛选、首页入口、完整原文和手机布局。News 仍可按原方式预览；正式构建不要开启 `--unpublished`，以免公开新闻示例。

本维护说明所在 `docs/` 目录已从网站构建输出排除。
