---
layout: post
title: Matplotlib markers
excerpt: "Visualization of markers in Matplotlib"
comments: true
categories: articles
share: true
tags: [matplotlib]
---

The description of possible markers on the Matplotlib description [here](http://matplotlib.org/api/markers_api.html) does not show what each marker looks like, so I made the visualization below to aid in choosing a marker for scatter plots. The left column displays the marker; the right column shows the corresponding marker label in Matplotlib.

e.g. the code below will use square markers.

{% highlight python %}
import matplotlib.pyplot

plt.plot(x, y, marker='s')
{% endhighlight %}

<figure>
	<img src="/images/MatplotlibMarkers.png" alt="image">
</figure>
