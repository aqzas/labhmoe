---
---

# UnionCell lab

{% include section.html background="images/home/image2.JPG" dark=false %}

Innovating Cell-Free & Cell-Based Therapies for Complex Diseases.

## Highlights

{% capture text %}

<em>Exploring the intersection of stem cell biology, 
extracellular vesicles, and immunology.</em>

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/researchimage.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}

<em>Bridging the gap from bench to bedside 
with EV-based therapeutics and clinical trials.</em>

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/projectimage.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

<em>A multidisciplinary team of clinicians and scientists
dedicated to medical innovation.</em>



{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/home/teamimage.png"
  link="team"
  title="Our Team"
  text=text
%}

{% capture text %}

<em>Advancing innovative cellular and immune therapies through clinical studies and investigator-initiated trials.</em>

{%
  include button.html
  link="gcp"
  text="Explore clinical trials"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{% assign gcp_image = "images/home/gcp.jpg" | file_exists | default: "images/fallback.svg" %}
{%
  include feature.html
  image=gcp_image
  link="gcp"
  title="Clinical Trials"
  flip=true
  text=text
%}

{% include section.html %}

## Latest News

{% assign latest_news = site.posts | sort: "date" | reverse %}
{% for post in latest_news limit: 3 %}
{% include news-excerpt.html post=post style="compact" %}
{% else %}
News and laboratory updates will be posted here.
{% endfor %}

{% include button.html link="news" text="View all news" icon="fa-solid fa-arrow-right" flip=true style="bare" %}
