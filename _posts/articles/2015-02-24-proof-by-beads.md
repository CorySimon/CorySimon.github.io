---
layout: post
title: Proof by beads
excerpt: 1+2+...+(n-1)+n+(n-1)+...+2+1=n<sup>2</sup> has a nice geometric proof
comments: false
categories: articles
share: true
tags: [mathematics]
---

$$1 = 1$$

$$1 + 2 + 1= 4 = 2^2$$

$$1 + 2 + 3 + 2 + 1 = 9 = 3^2$$

$$1 + 2 + 3 + 4 + 3 + 2 + 1 = 16 = 4^2$$

See a pattern? It looks like the following formula holds for integers $$n>0$$:

$$1+2+3+\cdots+ (n-1) + n + (n-1) + \cdots + 1 = n^2$$

There is an intuitive geometric explanation for this formula. Consider arranging an $$n$$ by $$n$$ square lattice of beads. There is a total of $$n^2$$ beads in this lattice. We can imagine many different ways to walk through the lattice and count them; all such ways will lead to the answer $$n^2$$. One way to walk through the lattice is to start at a corner and count along the diagonals. If we walk through the entire square lattice of beads like this, for $$n=4$$, we would count $$1+2+3+4+3+2+1$$-- where the $$4$$ contribution comes from the main diagonal and the $$1$$ contributions come from the two opposing corners-- and get $$n^2=16$$ since this is the total number of beads.

Applied Mathematician Steven Strogatz posted a photo on Twitter that illustrates this geometric interpretation of the formula $$1 + 2 + 3 + 4 + 3 + 2 + 1 = 16 = 4^2$$. Each type of bead classifies a diagonal on the square lattice of beads.

<blockquote class="twitter-tweet tw-align-center" lang="en"><p>Proof by beads: 1+2+3+4+3+2+1 = 4^2. Same idea with square of side n shows 1+2+...+ n + ... +2+1 =n^2. <a href="http://t.co/uxKGxwQGAW">pic.twitter.com/uxKGxwQGAW</a></p>&mdash; Steven Strogatz (@stevenstrogatz) <a href="https://twitter.com/stevenstrogatz/status/569524042744664064">February 22, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The more rigorous way to prove

$$S(n):=1+2+3+\cdots+ (n-1) + n + (n-1) + \cdots + 1 = n^2$$

is by [Mathematical induction](http://en.wikipedia.org/wiki/Mathematical_induction).

The base case is $$n=1$$. Of course, $$S(1)=1$$, i.e., $$1=1$$ is true.

The inductive step is to assume that $$S(n)=n^2$$ holds and then show that this implies $$S(n+1)=(n+1)^2$$. 

Somehow, we need to construct $$(n+1)^2$$ on the right-hand side of $$S(n)=n^2$$. Noting that $$(n+1)^2=n^2+2n+1$$, we can add $$2n+1$$ to both sides

$$S(n) + [2n+1]= n^2 + [2n+1] = (n+1)^2.$$

The left-hand side can be rewritten by noting that $$2n+1=n+(n+1)$$:

$$S(n)+ [n+ (n+1)] = 1+2+\cdots+ (n-1) + n + (n+1) +n + (n-1) + \cdots + 1 $$

and thus we have proven that $$S(n+1)=(n+1)^2$$ starting with $$S(n)=n^2$$:

$$1+2+\cdots+ (n-1) + n + (n+1) +n + (n-1) + \cdots + 1=(n+1)^2,$$

completing the proof by induction.

The geometric interpretation is much nicer right?

