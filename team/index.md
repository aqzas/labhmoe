---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

A collaborative team of clinicians and scientists working together to advance medical frontiers.

{% include section.html %}

## Team Leader

{% assign leaders = site.members | where: "role", "pi" | sort: "order" %}
{% for leader in leaders %}
{% include portrait.html lookup=leader.slug %}
{% endfor %}

## Members

### Postdoctoral Researchers

{% include list.html data="members" component="portrait" filters="role: ^postdoc$" %}

### PhD Students

{% include list.html data="members" component="portrait" filters="role: ^phd$" %}

### Master's Students

{% include list.html data="members" component="portrait" filters="role: ^master$" %}

### 8-Year Clinical Medicine Program

{% include list.html data="members" component="portrait" filters="role: ^clinical_medicine$" %}

## Assistant

{% include list.html data="members" component="portrait" filters="role: ^assistant$" %}
