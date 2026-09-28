# News 与 GCP 内容维护

顶部导航按 Research、Projects、Team、News、GCP、Contact 排列。旧 `/blog/` 地址重定向到 `/news/`。新闻继续使用 Jekyll `_posts`，临床试验使用 `_trials` collection。

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

News 页面自动按时间展示新闻；首页自动展示最新三条。列表支持 `<!-- excerpt start -->` 和 `<!-- excerpt end -->` 之间的摘要，未提供时使用 Jekyll 默认摘要。新闻详情保留现有 post 布局。列表搜索支持标题、正文、作者和标签。

## 新增临床试验

复制 `_trials/example-cart-sle.md` 为 `_trials/实际试验英文短名.md`。新文件会生成 `/gcp/实际试验英文短名/` 详情页。

| 字段 | 内容 |
| --- | --- |
| `title` | 已核实的研究名称 |
| `published` | 编辑期间设为 `false`，确认后设为 `true` |
| `disease` | 疾病或适应证 |
| `therapy` | 治疗类型，例如 CAR-T、TCE |
| `status` | 按下方约定填写真实研究状态 |
| `study_type` | 研究类型 |
| `pi` | 已确认可公开的主要研究者 |
| `registration` | 已确认的注册号 |
| `site` | 已确认的研究中心 |

未知字段保留空字符串 `""`，页面不显示空字段。正文按 Study Overview、Eligibility、Study Site 等章节填写真实资料，不写入患者信息或内部备注。示例中的疾病和疗法仅用于说明结构，不能视为实验室正在开展该项试验的证据。

状态决定 GCP 页面分组，注意大小写：

- `Recruiting`、`Active, not recruiting`、`Not yet recruiting`：Ongoing Trials。
- `Completed`：Completed Trials。
- 其他状态（如 `Suspended`、`Terminated`）或尚未填写状态：Other Studies。

仅在真实状态确认后填写状态；没有已发布研究时页面显示待更新说明，不展示示例招募信息。CAR-T、TCE 使用相同结构，通过 `therapy` 字段区分。

## 图片与样式

首页 Clinical Trials 模块优先使用 `images/home/gcp.jpg`，缺失时使用现有 `images/fallback.svg`。上传真实配图到该路径即可替换。

新组件为 `_includes/news-excerpt.html`、`trial-card.html`、`trial-fields.html`，对应样式为 `_styles/news-excerpt.scss`、`trial-card.scss`。现有 `_includes/styles.html` 自动收集带 front matter 的 SCSS 文件，无需修改 `_styles/all.scss`。

## 本地预览

安装与项目兼容的 Ruby 和 Bundler 后，在项目根目录运行：

```sh
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

默认预览地址为 `http://localhost:4000`。发布前检查 `/news/`、`/gcp/`、新闻和试验详情页，以及手机宽度下的布局。正式构建不要开启 `--unpublished`，以免公开编辑中的示例。

本维护说明所在 `docs/` 目录已从网站构建输出排除。
