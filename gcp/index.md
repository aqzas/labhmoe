---
title: Clinical Trials / GCP
nav:
  order: 5
  tooltip: Clinical Trials and GCP
---

# {% include icon.html icon="fa-solid fa-notes-medical" %}Clinical Trials / GCP

本页面展示课题组开展或参与的风湿免疫相关临床研究项目，涵盖细胞治疗及 T 细胞衔接器等创新治疗方向。

{% include section.html %}

{% assign trials = site.data.trials | sort: "sequence" %}
{% assign product_types = trials | map: "product_type" | uniq %}

<div class="trial-list" data-trial-list lang="zh-CN">
  <div class="trial-filters" role="group" aria-label="按产品类型筛选" hidden>
    <button type="button" class="button trial-filter" data-filter-all aria-pressed="true" aria-controls="trial-grid">All</button>
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
