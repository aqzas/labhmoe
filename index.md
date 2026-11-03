---
lang: en
translation_key: home
---

# UnionCell lab

{% include section.html background="images/home/image2.JPG" dark=false %}

Innovating cell-free and cell-based therapies for complex diseases.

## Research Directions

{% capture text %}
<em>Connecting disease mechanisms, therapeutic development and clinical translation.</em>

{%
  include button.html
  link="projects"
  text="Explore our research directions"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/home/projectimage.jpg"
  link="projects"
  title="Research Directions"
  text=text
%}

## Research Members

{% capture text %}
<em>A multidisciplinary group of clinicians, scientists and clinical leads working together on medical innovation.</em>

{%
  include button.html
  link="team"
  text="Meet our research members"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/home/teamimage.png"
  link="team"
  title="Research Members"
  flip=true
  text=text
%}

## Research Results

{% capture text %}
<em>Exploring the intersection of stem cell biology, extracellular vesicles and immunology.</em>

{%
  include button.html
  link="research"
  text="View our research results"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/home/researchimage.jpg"
  link="research"
  title="Research Results"
  text=text
%}

## Research News

{% assign nature_medicine_news = site.posts | where: "translation_key", "news-tce-sle" | where: "lang", page.lang %}
{% for post in nature_medicine_news %}
{% include news-excerpt.html post=post %}
{% endfor %}

{% include button.html link="news" text="View all research news" icon="fa-solid fa-arrow-right" flip=true style="bare" %}
