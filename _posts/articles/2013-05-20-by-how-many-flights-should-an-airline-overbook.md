---
layout: post
title: By how many flights should an airline overbook?
excerpt: "Airlines sell more tickets than the capacity of the flight and hope that just enough customers show up to get a full flight. By how much should the airline oversell to maximize profits?"
comments: false
categories: articles
share: true
tags: [probability, operations research]
---

> Overselling or overbooking is the sale of a volatile good or service in excess of actual capacity. 
> 
> \-- Wikipedia


A fraction of airline flyers do not show up for their flights due to a delay in their preceding connection flight or other circumstances. Let's assume that an airline receives revenue from a passenger equal to the ticket price only when he or she actually takes the flight. In this case, each empty seat is lucidly lost revenue: if the seat is empty, the airline does not receive the revenue from the ticket sale. In anticipation of no-show passengers, airlines overbook the plane (sell more tickets than capacity) and hope that just the right amount of customers show up to get a full plane. This is the airline's attempt to receive the maximal revenue (seat capacity * ticket price) for each flight.

The danger of overbooking-- and this happens often-- is that more passengers show up than what they had anticipated. The airline then angers customers that must be bumped from the flight and compensates them with vouchers. Other times, the airline takes volunteers to take the next flight out, with pricey vouchers as an incentive.

There is an interesting optimization problem here. On a plane with 100 seats, if the airline sells 100 tickets, it will almost surely incur an opportunity cost of lost revenue from the no-show customers. If the airline sells 1,000 tickets, while the flight will almost certainly be full, it must fork out costly vouchers and hotel rooms to the passengers that get bumped from the flight, which *decreases* revenue. The sweet spot that maximizes revenue is somewhere in between selling 100 tickets and selling 1,000 tickets.

So, for this 100-seat flight, by how many seats should the airline overbook the plane? Let's say the ticket price is $250 and the cost of bumping a passenger is $800<sup>1</sup>.

From historical data for this particular flight, we can count the total number of tickets sold to this flight and, of these, the total number of these customers that actually showed up for the flight. Given a future customer who purchases a ticket, we can assume that the probability that he or she will actually show up for their flight is then the fraction, $$p$$, of the ticket-buyers that show up from historical data. We will use $$p=0.9$$, close to [this source](http://www.nytimes.com/2007/05/30/business/30bump.html?pagewanted=print&_r=0) that reports 7-8% of customers are no-shows.

We can model the event that a given customer that purchased the ticket actually shows up for the flight as a Bernouli random variable, assuming he or she is independent of the other passengers. This is akin to saying a given ticket-holder will show up if a coin lands as heads, where this coin is biased to land on heads a fraction $$p$$ of the times that it is flipped.

Our goal here is to find the number of tickets beyond capacity that we should sell, which we call $$x$$. So, we are selling a total of $$100+x$$ tickets. The number of customers $$N$$ that show up for their flight on the 100-seat plane is thus a [binomial random variable](http://en.wikipedia.org/wiki/Binomial_distribution) with $$100+x$$ trials and probability of success $$p$$:

$$P(N=n)=\binom{100+x}{n} p^{n}(1-p)^{100+x-n}.$$

The term $$p^{n}(1-p)^{100+x-n}$$ is the probability of a specific sequence of $$n$$ out of $$100+x$$ customers boarding their flight, whereas the term $$\binom{100+x}{n}$$ gives the number of combinations of such sequences (we don't care which of the customers show up-- just whether they do or not!).

One approach might be to choose $$x$$ such that the expected value of $$N$$ is equal to the number of seats so that just the right amount of customers show up in the long run:

$$E(N)=(100+x)p=100$$.

This approach is short-sighted since it does not take into account the cost of the airline ticket or the voucher award. For example, if the airline gives out $1 million vouchers to overbooked customers, the airline wouldn't overbook at all!

A better approach is to find a formula for the expected value of the revenue of this flight with our policy of overbooking by $$x$$ customers. We can then plot the expected revenue as a function of $$x$$ to see which $$x$$ maximizes revenue. The revenue $$r=r(n)$$ depends on the number of passengers $$n$$ out of $$100+x$$ ticket purchasers that actually show up. We get income from each person that boards the plane and lose income from each person we bump off of the plane in the case that we are over capacity ($$n>100$$):

$$r(n) = 250n$$ if $$n<100$$ [if less than 100 show, we get $250 for each passenger that shows, and we don't lose any revenue since no customers were bumped.]

$$r(n) = (250)(100) - 800(n-100)$$ if $$n\ge 100$$ [if more than 100 show, we get $250 only for first 100 passengers, and we lose $800 for each of the $$(n-100)$$ customers that were bumped.].

Now, the revenue that we expect to make, given an overbooking policy:

$$E(r|x)=\displaystyle \sum _{n=0}^{100+x} P(N=n| x) r(n).$$

The $$P(N=n)$$ is given by the binomial$$(100+x,p)$$ distribution given a few lines above (it is really conditioned on a given $$x$$). Since we are more likely to get a full plane with increasing overbooking $$x$$, we get more and more likely to get the maximum possible income $(250)(100) from the flight as $$x$$ increases. On the other hand, we are more and more likely to go over a full plane as $$x$$ increases, and the $800 cost of bumping passengers starts to erode our revenue stream.

Using the normal approximation to the binomial distribution (with a continuity correction), I plot the expected revenue as a function of overbooking $$x$$ in the graph below. There are a number of remarks from this plot that aid our intuition.

<figure>
	<img src="/images/overbook/overbook2.png" alt="image">
</figure>
	
  * The maximal revenue we can possibly make is if the flight is full, and this maximal revenue would be $250(100 seats)=$25000, the red dashed line on this plot.

	
  * Selling 100 tickets for 100 seats ($$x=0$$) does not maximize the revenue. The maximum expected revenue occurs when we sell 109 tickets! That is, revenue is maximized when we oversell the flight 9 seats beyond capacity. [$$x=9$$ maximizes revenue, and is therefore the best choice.]

	
  * Beyond 109 seats, the revenue decreases because the cost of bumping customers (vouchers, getting the next flight, this customer will fly on a different airline in the future) outweighs the higher certainty of getting a full plane and getting income from 100 full seats. Eventually, when we overbook the plane by 46, the airline is expected to pay more for bumping passengers than it receives in ticket sales! This is seen where the expected revenue is zero, i.e. where the expected revenue curve crosses the blacked dashed line.


This is a first-pass analysis of how airlines choose to overbook flights to maximize their profits. Each empty seat is lost money, but the airline must weigh this against the risk of paying for vouchers and hotels for customers that couldn't fit on the full flight-- and the lost customer loyalty that ensues. One can imagine introducing many other factors such as seasonality, the time before the flight that the ticket was purchased, if tickets were purchased in a group, and customer-specific history. See [this article](http://www.nytimes.com/2007/05/30/business/30bump.html?pagewanted=all&_r=0) for how complicated airline models realistically may be.

This analysis considers only the revenue of the airline. However, there is an externality associated with bumping passengers. Think about how this passenger may lose out on one day of pay, how his or her employer loses out of one day of valuable work, and how the local ice cream shop loses out on one customer that would have otherwise taken his or her family out for ice cream that day.

<sup>1</sup> We can lump all of the following costs of a bumped passenger into one number: airline voucher + hotel room + ticket for next available flight + lost customer loyalty

*UPDATE*: The Python code to generate the expected net revenue plot above is [here](https://github.com/CorySimon/CorySimon.github.io/blob/master/codes/overboarding.py).
