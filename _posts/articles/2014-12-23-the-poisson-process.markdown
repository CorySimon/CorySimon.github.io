---
layout: post
title: The memoryless Poisson process and volcano insurance
excerpt: "The Poisson process is a memoryless point process, where the history has no impact on future outcomes."
comments: false
categories: articles
share: true
tags: [statistics]
---

In an episode of Family Guy, an insurance salesman tries to sell Peter volcano insurance. Reluctant to buy the volcano insurance, Peter said "I'm pretty sure we've never had a volcano". The salesman responded "Don't you think we're overdue for one?", which convinced Peter.

<iframe width="420" height="315" src="https://www.youtube.com/embed/gs6xxuBR0vI" frameborder="0" allowfullscreen></iframe>

We can model an event such as a volcano eruption as a *point process* when the duration of the event is negligibly small compared to the time window of observation and the time between events. We can visualize a point process as points on a timeline:

<figure>
	<img src="/images/timeline.png" alt="image">
</figure>

The point process of some events indeed behaves like the volcano insurance salesman suggests about volcanoes: as more time elapses from a previous event, it becomes more likely that another event will occur soon. As an example, consider a truck making a cross-country road trip where the event is filling up the fuel tank.

On the other hand, a *Poisson process* is a *memoryless* stochastic point process; that an event has *just* occurred or that an event hasn't occurred in a *long* time give us no clue about the likelihood that another event will occur soon. The Poisson process is used to model radioactive decay, requests for documents on the web, and customers ordering/calling/showing up in queuing theory [[list of applications](http://en.wikipedia.org/wiki/Poisson_process#Applications)]. Let $$T$$ be the random variable representing the time that has elapsed since the last event has occurred, the _waiting time_ between events in the Poisson process. This memoryless property of the Poisson process relates the probabilities:

$$P(T > t + s | T > s ) = P(T > t).$$

In words, if we've already waited a time $$s$$ without seeing an event (<span>$$T>s$$</span>), the probability that an event won't occur in the next <span>$$t$$</span> minutes, <span>$$P(T>t+s|T>s)$$</span>, is the same as if we hadn't already waited the time $$s$$, <span>$$P(T>t)$$</span>.

Just by enforcing this memoryless condition, we will discover that the waiting time $$T$$ is necessarily exponentially distributed, $$P(T >t) = e^{-\lambda t}$$.

Using Bayes' theorem, <span>$$P(T > t + s | T > s ) = P(T > t + s \mbox{ and } T > s) / P(T > s)$$</span>, and we can write the memoryless property as:

<div>$$P(T > t + s ) = P(T > t) P(T > s).$$</div>

Let's call $$P(T>t)$$ the _survival function_ $$S(t)$$ since it is the probability that a volcano hasn't erupted up until time $$t$$. In terms of the survival function, the memoryless property is:

$$S(t+s) = S(t) S(s).$$

From here, the trick is to consider $$s,t=\frac{1}{2}$$. Then,

$$S(1) =S\left(\frac{1}{2}+\frac{1}{2}\right)=S\left(\frac{1}{2}\right)S\left(\frac{1}{2}\right)=S\left(\frac{1}{2}\right)^2.$$

We see a pattern if we split $$1$$ into a different fraction:

$$S(1) = S\left(3\frac{1}{3}\right)=S\left(\frac{1}{3}+\frac{1}{3}+\frac{1}{3}\right)=S\left(\frac{1}{3}\right)S\left(\frac{1}{3}+\frac{1}{3}\right)=S\left(\frac{1}{3}\right)^3.$$

The pattern is that for integers $$n>0$$:

$$S(1)=S\left(\frac{1}{n}\right)^n.$$

We can also write for any integer $$m$$:

$$S\left(m\frac{1}{n}\right)=S\left(\frac{1}{n}+\frac{1}{n}+...+\frac{1}{n}\right)=S\left(\frac{1}{n}+\frac{m-1}{n}\right)=S\left(\frac{1}{n}\right)S\left(\frac{m-1}{n}\right)=...=S\left(\frac{1}{n}\right)^m.$$

Substituting into this our formula above for $$S\left(\frac{1}{n}\right)$$ related to $$S(1)$$:

$$S\left(\frac{m}{n}\right)=[S(1)^\frac{1}{n} ]^m = S(1)^\frac{m}{n}.$$

By choosing $$m$$ and $$n$$, we can approximate any real number $$t>0$$ with $$\frac{m}{n}$$, so we can write

$$S(t) = S(1)^t.$$

Keep in mind that $$S(1)\in(0,1)$$ is just some constant. If we define $$\lambda=-\log S(1)$$ [$$\lambda$$ will be greater than zero since the log of a number between 0 and 1 is negative], we get that the survival function is:

$$S(t) = P(T>t) = e^{-\lambda t}.$$

This is called the _exponential distribution_, and it governs the random variable that represents the _waiting time_ between events in a Poisson process. The parameter $$\lambda$$ determines how fast the exponential will decay with time; a large $$\lambda$$ implies that there is not much probability of survival at large times and thus events generally occur frequently.

We can easily confirm that the survival function for the exponential distribution satisfies the memoryless property:

$$S(t+s) =e^{-\lambda(t+s)} = e^{-\lambda t} e^{-\lambda s} =S(t)S(s).$$

The probability density function $$f(t)$$ of the exponential distribution is the negative derivative of the survival function since $$P(T>t) = 1-\int_0^tf(t)dt$$,

$$f(t)=\lambda e^{-\lambda t}.$$

So a Poisson process is a stochastic point process where the waiting times between events are exponentially distributed. If we ask the question "How many events do we expect to occur during a time interval of length $$\tau$$?", this is a well-posed question because we do not need to know anything about the history of events up until that point-- the Poisson process is memoryless!

Let $$N$$ be the number of events in a Poisson process with parameter $$\lambda$$ that occur in a time interval of length $$\tau$$. What is the probability that $$k$$ events occur in this time window, $$P(N=k)$$?

The easy one is $$P(N=0)$$. If no event occurs in the time interval $$\tau$$, the event must occur after a time $$\tau$$:

$$P(N=0)=\int_\tau^\infty \lambda e^{-\lambda t}dt= e^{-\lambda \tau},$$

where we integrate starting at zero because, why not? It doesn't matter when we start our count of time since history plays no role.

If $$N=1$$, we can consider all possible times $$x\in[0,\tau]$$ that this single event could occur; the probability that it occurs around time $$x$$ has a probability density $$\lambda e^{-\lambda x}$$. Further, a second event must not occur in the rest of the interval $$[x,\tau]$$; i.e. its waiting time since the first event must fall in $$[\tau - x,\infty)$$.

$$P(N=1)=\int_0^\tau \lambda e^{-\lambda x} \left[ \int_{\tau -x}^\infty \lambda e^{-\lambda t} dt \right] dx= \lambda e^{-\lambda t}$$

Moving on to $$ N=2 $$, consider the first event occurs at time $$x$$ and the second at time $$x+y$$. So, the waiting time for the second event is $$y$$, and it belongs somewhere in $$[0,\tau]$$; this is the outermost integral. The first event has a waiting time $$x$$, and given the second has waiting time $$y$$, the first waiting time falls somewhere in $$[0,\tau - y]$$; this is the next inner integral. Finally, we need that the third event's waiting time fall in $$[\tau - x - y, \infty)$$; i.e. its waiting time cannot be less than $$\tau - x -y$$, as this would imply that the third event fell in $$[0,\tau]$$. This is the inner-most integral.

$$P(N=2) = \int_0 ^ \tau \lambda e ^ { - \lambda y} \left[ \int_0^{\tau-y} \lambda e^{-\lambda x} \left( \int_{\tau-x-y}^\infty \lambda e^{-\lambda t}dt \right) dx \right] dy = \frac{(\lambda\tau)^2}{2}e^{-\lambda \tau}$$

Again, there is a recurring pattern here that would be clearer if we consider $$N=3$$:

$$P(N=k)=\frac{(\lambda\tau)^k}{k!} e^{-\lambda \tau}.$$

The above is the probability distribution for observing $$k$$ events in time interval $$\tau$$ in a Poisson process. The factorial in the denominator is not too surprising since $$k$$! counts the number of permutations of $$k$$ events; the order of the events here is immaterial.

To answer our question of the expected number of events that occur in a time interval of length $$\tau$$ in a Poisson process with parameter $$\lambda$$:

$$\langle N \rangle = \displaystyle \sum_{k=0}^\infty P(N=k) k =\displaystyle \sum_{k=0}^\infty k \frac{(\lambda \tau)^k}{k!}e^{-\lambda \tau}. $$

Simplifying and noting that the $$k=0$$ term drops out:

$$ \langle N \rangle =e^{-\lambda \tau} \displaystyle \sum_{k=1}^\infty \frac{(\lambda \tau)^k}{(k-1)!}=e^{-\lambda \tau}\lambda \tau \displaystyle \sum_{k=1}^\infty \frac{(\lambda \tau)^{k-1}}{(k-1)!}.$$

Finally, we see the series representing the exponential function by reindexing:

$$ \langle N \rangle =e^{-\lambda \tau}\lambda \tau \displaystyle \sum_{i=0}^\infty \frac{(\lambda \tau)^{i}}{i!}=e^{-\lambda \tau}\lambda \tau e^{\lambda \tau} ,$$

and the expected number of events that occurs in a time interval $$\tau$$ is $$\langle N \rangle = \lambda \tau$$. This is in line with our earlier interpretation that a larger $$ \lambda$$ implies that events happen more frequently, since $$\langle N \rangle$$ scales proportionally with the size of $$\lambda$$.

I find it interesting how we can start with the memoryless property, and the exponential distribution of waiting times and the Poisson process follow naturally.
