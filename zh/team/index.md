---
lang: zh-CN
translation_key: team
title: 团队成员
nav:
  order: 3
  tooltip: 了解我们的团队
---

# {% include icon.html icon="fa-solid fa-users" %}团队成员

临床医生与科研工作者携手合作，共同探索医学前沿。

{% include section.html %}

## 团队负责人

{% assign leaders = site.members | where: "role", "pi" | sort: "order" %}
{% for leader in leaders %}
{% include portrait.html lookup=leader.slug %}
{% endfor %}

## 团队成员

### 博士后

{% include list.html data="members" component="portrait" filters="role: ^postdoc$" %}

### 博士研究生

{% include list.html data="members" component="portrait" filters="role: ^phd$" %}

### 硕士研究生

{% include list.html data="members" component="portrait" filters="role: ^master$" %}

### 八年制临床医学学生

{% include list.html data="members" component="portrait" filters="role: ^clinical_medicine$" %}

## 科研助理

{% include list.html data="members" component="portrait" filters="role: ^assistant$" %}
