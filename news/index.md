---
lang: en
translation_key: news
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

{% include section.html %}

## WeChat articles

The linked articles are in Chinese.

<ul>
  <li><a href="https://mp.weixin.qq.com/s/NUg177wCw1R9iMrAW3cCzA" target="_blank" rel="noopener noreferrer">Frontiers at Wuhan Union Hospital: 160th Hospital Anniversary, 30th Rheumatology Department Anniversary, and the Second Union Hospital–Qilu Stem Cell Joint Laboratory Symposium</a></li>
  <li><a href="https://mp.weixin.qq.com/s/9rmJSlJ1EAgnqmMTMvJ1eg" target="_blank" rel="noopener noreferrer">Wuhan Union Hospital Rheumatology Forum, Stem Cell and EV Translational Research Conference, and Inauguration of the Union Hospital–Qilu Stem Cell Joint Laboratory</a></li>
  <li><a href="https://mp.weixin.qq.com/s/Bg9SPEj_QI0vKhZz8R3PHw" target="_blank" rel="noopener noreferrer">2025 Wuhan Union Hospital Rheumatology and Immunology Annual Conference</a></li>
</ul>
