---
lang: en
translation_key: team
title: Research Members
nav:
  order: 2
  tooltip: Research members and clinical leads
---

# {% include icon.html icon="fa-solid fa-users" %}Research Members

A collaborative team of clinicians and scientists working together to advance medical frontiers.

{% include section.html %}

## Team Leader

{% assign leaders = site.members | where: "role", "pi" | sort: "order" %}
{% for leader in leaders %}
{% include portrait.html lookup=leader.slug %}
{% endfor %}

### Clinical Leads

{% assign clinical_leads = site.members | where: "role", "clinical_lead" | sort: "order" %}
{% for clinical_lead in clinical_leads %}
{% include portrait.html lookup=clinical_lead.slug %}
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

## Clinical Laboratory Leads

{% include list.html data="members" component="portrait" filters="role: ^clinical_laboratory$" %}
