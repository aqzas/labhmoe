---
lang: zh-CN
translation_key: gcp
title: 临床试验 / GCP
nav:
  order: 5
  tooltip: 临床试验与临床研究
---

# {% include icon.html icon="fa-solid fa-notes-medical" %}临床试验 / GCP

本页面展示课题组开展或参与的风湿免疫相关临床研究项目，涵盖细胞治疗及 T 细胞衔接器等创新治疗方向。

{% include section.html %}

{% include i18n.html %}

{% assign trials = site.data.trials | sort: "sequence" %}
{% assign product_types = trials | map: "product_type" | uniq %}

<div class="trial-list" data-trial-list lang="{{ site_lang }}">
  <div class="trial-filters" role="group" aria-label="{{ ui.filter_trials }}" hidden>
    <button type="button" class="button trial-filter" data-filter-all aria-pressed="true" aria-controls="trial-grid">{{ ui.all }}</button>
    {% for product_type in product_types %}
    <button type="button" class="button trial-filter" data-product-type="{{ product_type | escape }}" aria-pressed="false" aria-controls="trial-grid">{{ product_type | escape }}</button>
    {% endfor %}
  </div>
  <div class="trial-grid" id="trial-grid">
    {% for trial in trials %}
    {% include trial-card.html trial=trial %}
    {% endfor %}
  </div>
</div>
