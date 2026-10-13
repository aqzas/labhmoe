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

{% include section.html %}

## 微信文章

<ul>
  <li><a href="https://mp.weixin.qq.com/s/NUg177wCw1R9iMrAW3cCzA" target="_blank" rel="noopener noreferrer">微信文章 1</a></li>
  <li><a href="https://mp.weixin.qq.com/s/9rmJSlJ1EAgnqmMTMvJ1eg" target="_blank" rel="noopener noreferrer">微信文章 2</a></li>
  <li><a href="https://mp.weixin.qq.com/s/Bg9SPEj_QI0vKhZz8R3PHw" target="_blank" rel="noopener noreferrer">微信文章 3</a></li>
</ul>
