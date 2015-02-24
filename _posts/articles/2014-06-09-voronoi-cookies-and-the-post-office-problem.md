---
layout: post
title: Voronoi cookies and the post office problem
excerpt: "The cookies that I baked formed a Voronoi diagram. The Voronoi diagram is a useful mathematical tool."
comments: false
categories: articles
share: true
tags: [mathematics]
---

In an attempt to bake cookies, I failed to place the balls of dough far enough apart and, instead, a cookie cake formed. The result resembles a very useful diagram in mathematics called a Voronoi tessellation.

<figure>
	<img src="/images/voronoicookies.jpg" alt="image">
</figure>

The exciting part is the boundary that formed between the regions intended to be separate cookies. The regions of space circumscribed around these boundaries (the "intended cookies") are called Voronoi cells. I drew the lines that approximately partition the area of the pan into Voronoi cells. You can also imagine the center of the balls of cookie dough that I placed in the pan before I put it in the oven, marked as red points that I will call *sites* \\(p_k\\).

<figure>
	<img src="/images/voronoicookies_labeled.jpg" alt="image">
</figure>

In a Voronoi diagram, all points on these lines are equidistant from the two sites of the adjoining Voronoi cells. All points inside the regions circumscribed by these lines are thus closer to the site of that Voronoi cell than any other Voronoi cell sites.

This leads to the mathematical definition of a Voronoi cell or region \\(R_k\\) of a site \\(p_k\\) (the cookie centers) as all points \\(x\\) that are closer to site \\(p_k\\) than any other site:

<span>$$R_k:=\{x : d(x,p_k) < d(x,p_j)$$</span> for all <span>$$j \neq k\}.$$</span>

Here, \\(d(x,p_k)\\) is notation for the distance between point \\(x\\) and site \\(p_k\\).

How are Voronoi cells useful? Consider a classic optimization problem called the Post Office Problem. A new city has just built 10 post offices. With the aim of reducing the cost of delivering mail, how can we optimally assign each residence a post office from which to receive mail?

Assuming that the density of residences is spatially uniform, we seek to assign each house to the nearest post office<sup>1</sup>. Thinking of the location of the post offices as sites \\(p_k\\), the solution to the optimization problem is to assign all houses in the Voronoi cell \\(R_k\\) to post office \\(k\\). This is because each point in the Voronoi cell \\(k\\) is by definition closest to post office \\(k\\) (located at \\(p_k\\)) than any other post office.

Another amusing story is that of a physician John Snow, who in London in 1854, suggested with a Voronoi diagram that Cholera was being spread by drinking water instead of through the air, as thought at the time. He plotted the Cholera cases on a map of London and imagined the water pumps as sites \\(p_k\\), drawing the Voronoi diagram of these sites. He noticed that the victims appeared within a Voronoi cell of a certain [infected] water pump. The assumption here is that people get their water primarily from the closest water pump. This suggested that instead Cholera is water-borne and identified the problematic water source [1].


In machine learning, the branch of artificial intelligence that enables self-driving cars and the recommendation algorithms of Netflix, one supervised classification algorithm uses the Voronoi network, called nearest-neighbor classification. Let's say Netflix has a vector of data about you, including your age, gender, and what movies you've watched/how you've rated them. This is some representation of you in higher dimensional space. One strategy for recommending your next movie might be to simply find the person that is "closest" to you in their database, see what movies that person likes (the nearest neighbor), and recommend these movies to you. This corresponds to finding the site \\(p_k\\) (representing the person most like you) in high dimensional space such that you lie in the Voronoi cell \\(R_k\\).




Finally, why did the cookie cake form a Voronoi diagram? I think that one can prove that baking cookies will form a Voronoi network by assuming that each cookie expands from its center at a constant, uniform rate and stops expanding when it meets the surface of another cookie. The points where the boundaries of the intended cookies meet will form the lines in the Voronoi diagram. My cookie cake is not a perfect Voronoi diagram because a) each cookie was not initially the same shape and b) the boundary of the pan does not allow for a radially symmetric cookie expansion.




<sup>1</sup> The problem is realistically more complicated because mailmen must take roads, and these are not straight lines from the post office to the residences. Still, this may be a reasonable approximation.




[1] http://plus.maths.org/content/uncovering-cause-cholera
