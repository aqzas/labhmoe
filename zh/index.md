---
lang: zh-CN
translation_key: home
---

# UnionCell lab

{% include section.html %}

## 新闻动态

{% assign nature_medicine_news = site.posts | where: "slug", "tce-sle" %}
{% for post in nature_medicine_news %}
{% include news-excerpt.html post=post %}
{% endfor %}

{% include button.html link="/zh/news/" text="查看全部新闻" icon="fa-solid fa-arrow-right" flip=true style="bare" %}

{% include section.html background="images/home/image2.JPG" dark=false %}

面向复杂疾病，探索无细胞疗法与细胞治疗的创新路径。

## 研究与团队

{% capture text %}

<em>探索干细胞生物学、细胞外囊泡与免疫学的交叉领域。</em>

{%
  include button.html
  link="/zh/research/"
  text="查看研究成果"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/researchimage.jpg"
  link="/zh/research/"
  title="研究成果"
  text=text
%}

{% capture text %}

<em>通过细胞外囊泡治疗研究与临床试验，推动基础发现走向临床应用。</em>

{%
  include button.html
  link="/zh/projects/"
  text="浏览研究项目"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/projectimage.jpg"
  link="/zh/projects/"
  title="研究项目"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

<em>由临床医生与科研工作者组成的多学科团队，致力于医学创新。</em>



{%
  include button.html
  link="/zh/team/"
  text="了解我们的团队"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/teamimage.png"
  link="/zh/team/"
  title="团队成员"
  text=text
%}

{% capture text %}

<em>了解面向风湿免疫及自身免疫性疾病的创新细胞治疗与免疫治疗临床研究。</em>

{%
  include button.html
  link="/zh/gcp/"
  text="查看临床试验"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{% assign gcp_image = "images/home/gcp.png" | file_exists | default: "images/fallback.svg" %}
{%
  include feature.html
  image=gcp_image
  link="/zh/gcp/"
  title="临床试验 / GCP"
  flip=true
  text=text
%}
