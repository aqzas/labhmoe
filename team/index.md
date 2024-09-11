---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

The first paragraph in team, below the Title

{% include section.html %}

## Team Leader

{% include list.html data="members" component="portrait" filters="role: pi" %}

## Members

### Postdoct

{% include list.html data="members" component="portrait" filters="role: postdoc" %}

### Phd

{% include list.html data="members" component="portrait" filters="role: phd" %}

### Master

{% include list.html data="members" component="portrait" filters="role: undergrad" %}

## Assisant

{% include list.html data="members" component="portrait" filters="role: assistant" %}

## Ungrouped

{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)(?!postdoc$)" %}

{% include section.html background="images/background.jpg" dark=true %}

The second paragraph in team, below the Title

{% include section.html %}

{% capture content %}

<!-- {% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %} -->

{% endcapture %}

{% include grid.html style="square" content=content %}
