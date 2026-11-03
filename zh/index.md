---
lang: zh-CN
translation_key: home
---

# UnionCell lab

{% include section.html background="images/home/image2.JPG" dark=false %}

面向复杂疾病，探索无细胞疗法与细胞治疗的创新路径。

## 研究方向

{% capture text %}
<em>贯通疾病机制、治疗研发与临床转化。</em>

{%
  include button.html
  link="/zh/projects/"
  text="了解研究方向"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/home/projectimage.jpg"
  link="/zh/projects/"
  title="研究方向"
  text=text
%}

## 研究成员

{% capture text %}
<em>由临床医生、科研工作者和临床负责人组成的多学科团队，致力于医学创新。</em>

{%
  include button.html
  link="/zh/team/"
  text="了解研究成员"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/home/teamimage.png"
  link="/zh/team/"
  title="研究成员"
  flip=true
  text=text
%}

## 研究成果

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

## 研究动态

{% assign nature_medicine_news = site.posts | where: "translation_key", "news-tce-sle" | where: "lang", page.lang %}
{% for post in nature_medicine_news %}
{% include news-excerpt.html post=post %}
{% endfor %}

{% include button.html link="/zh/news/" text="查看全部研究动态" icon="fa-solid fa-arrow-right" flip=true style="bare" %}
