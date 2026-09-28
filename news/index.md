---
title: News
nav:
  order: 4
  tooltip: Latest news and activities
redirect_from:
  - /blog/
---

# {% include icon.html icon="fa-regular fa-newspaper" %}News

Latest news, academic activities, conferences, visits, awards, and laboratory updates.

{% include section.html %}

{% if site.posts.size > 0 %}
{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="posts" component="news-excerpt" %}
{% else %}
News and laboratory updates will be posted here.
{% endif %}
