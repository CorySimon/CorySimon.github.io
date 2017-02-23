---
layout: post
title: Recall, precision, specificity, and sensitivity
excerpt: "Illustration of recall, precision, specificity, and sensitivity"
comments: true
categories: articles
share: true
tags: [machine learning]
---

When working with classification algorithms, I consistently need to remind myself of the definition of recall, precision, specificity, and sensitivity. So, I created an illustration for reference.

Imagine you're on a fishing boat in the [Great Pacific garbage patch](https://en.wikipedia.org/wiki/Great_Pacific_garbage_patch). You cast your fishing net and retrieve a mix of fish and plastic bottles. A robot on the boat is equipped with a machine learning algorithm to classify each catch as a fish, defined as a positive (+), or a plastic bottle, defined as a negative (-).

{:.center}
<figure>
    <img src="/images/classification_metrics/fish_bottles.png" alt="image">
</figure>

The fish/bottle classification algorithm makes mistakes. To quantify its performance, we define recall, precision, specificity, and selectivity. Each are conditional probabilities. Note that the sensitivity (= recall) and specificity are each conditioned on the true class label.

{:.center}
<figure>
    <img src="/images/classification_metrics/classify.png" alt="image">
</figure>

Consider below the test set of eight fish and four plastic bottles. The algorithm classifies the catches highlighted in green as fish (+'s) and in red as bottles (-'s). The sensitivity (= recall), specificity, and precision are written for this test outcome.

{:.center}
<figure>
    <img src="/images/classification_metrics/metric_example.png" alt="image">
</figure>
