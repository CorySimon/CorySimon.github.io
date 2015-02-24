---
layout: post
title: The Principle of Maximum Entropy
excerpt: "The principle of maximum entropy is that we should model our process with the probability distribution that contains the most amount of unpredictability. This is under the constraints of the distribution satisfying the information that we do know about our process, of course."
comments: false
categories: articles
share: true
tags: [statistical physics]
---

The principle of maximum entropy is invoked when we have some piece(s) of information about a probability distribution, but not enough to characterize it completely-- likely because we do not have the means or resources to do so. As an example, if all we know about a distribution is its average, we can imagine infinite shapes that yield a particular average. The principle of maximum entropy says that we should humbly choose the distribution that maximizes the amount of unpredictability contained in the distribution, under the constraint that the distribution matches the average that we measured. Taking the idea to the extreme, it wouldn't be scientific to choose a distribution that simply yields the average value 100% of the time. Below, we define entropy and show how it can be interpreted as unpredictability or uninformativeness.

Take a sample space of \\(n\\) events, where event \\(i\\) occurs with probability \\( p_i \\). The surprisal of event \\(i\\) is defined as \\(-\log{p_i}\\). Since \\(p_i \in [0,1]\\), the surprisal runs monontonically from infinity to zero. This is intuitive because, if an event \\(i\\) will occur with certainty (\\(p_i=1\\)), we will be zero surprised when we see it occur; if an event \\(i\\) cannot possibly occur (\\(p_i=0\\)), we will be infinitely surprised. Why choose the logarithm as the monotonically increasing function from zero to infinity? If we have two independent events \\(i\\) and \\(j\\), the probability of, after two observations, seeing event \\(i\\) and then event \\(j\\) is \\(p_i p_j\\). Via the famous property of the logarithm, the surprisal to see this occur is \\(\log{p_i p_j}=\log{p_i}+\log{p_j}\\), making the surprisals additive.

Entropy is a characteristic of not an event, but of the entire probability distribution. Entropy is defined as the average surprisal in the entire distribution \\(<-\log{p_i}>=-\displaystyle \sum _{i=1}^n p_i \log{p_i}\\). The entropy is a measure of how uninformative a given probability distribution is-- a high entropy translates to high unpredictability. Thus, maximizing entropy is consistent with maximizing unpredictability, given the little information we may know about a distribution. The most informative distribution we can imagine is where we know that an event will occur 100% of the time, giving an entropy of zero. The least informative distribution we can imagine is a uniform distribution, where each event in the sample space has an equal chance of occurring, giving an entropy of \\(\log{n}\\). The uniform distribution is the least informative because it treats each event in the sample space equally and gives no information about one event being more likely to occur than another. Next, we show mathematically that, when we know nothing about a probability distribution, the distribution that maximizes the entropy is the uniform distribution. This is the principle of equal a priori probabilities: "in the absence of any reason to expect one event rather than another, all the possible events should be assigned the same probability" [1].

Something we always know about a probability distribution is that it must be normalized so that \\(\displaystyle \sum _{i=1}^n p_i =1\\). So, we maximize the entropy \\(-\displaystyle \sum _{i=1}^n p_i \log{p_i}\\) under the normalization constraint. Using a Lagrangian multiplier, we recast this problem as:

$$\max \left( \displaystyle -\sum _{i=1}^n p_i \log{p_i} +\lambda ( \sum _{i=1}^n p_i-1) \right).$$

Taking the derivative with respect to \\(p_i\\) and setting it equal to zero for a maximum, we find that \\(p_i\\) is the same for every event \\(i\\). By the normalization constraint, this gives us a uniform distribution \\(p_i=\frac{1}{n}\\) and an entropy of \\(\log{n}\\). So the principle of equal a priori probabilities is really a subcase of the principle of maximum entropy!

A more complicated example is when we have a discrete random variable \\(X\\), which can take on a set of \\(n\\) values \\(\{x_i\}\\). We know that the expected value of \\(X\\) is \\( \mu \\). What is the maximum entropy probability distribution \\(\{p_i\}\\) over the sample space \\(\{x_i\}\\) of \\(X\\)? Now, we have two constraints with two Lagrangian multipliers \\(\lambda\\) and \\(\eta\\), one for normalization and one for the known expected value of \\(X\\):

$$\max \left( \displaystyle -\sum _{i=1}^n p_i \log{p_i} +\lambda (\sum _{i=1}^n p_i-1)+\eta(\sum_{i=1}^np_i x_i-\mu)\right).$$

Now, if we take the derivative with respect to \\(p_i\\), we get that $$p_i=e^{-\eta x_i-1-\lambda},$$where the Lagrangian multipliers need to be determined from the normalization constraint and expected value of \\(X\\), \\( \mu \\).

We can write the maximum entropy probability distribution for continuous distributions \\(p(x)\\) as well, but we need a different type of mathematical machinery, the calculus of variations. To derive that a uniform distribution in the continuous setting is the maximum probability distribution, the optimization problem becomes:

$$\max \left( -\int_\Omega p(x) \log{p(x)} dx +\lambda ( \int_\Omega p(x)dx-1)\right).$$

The sums becomes integrals over the sample space \\(\Omega\\) of the continuous random variable \\(x\\). The expression in the brackets is a function**al**-- a function of a function \\(p(x)\\)! Thus, the problem here is to maximize this functional by choosing a function \\(p(x)\\), which is the type of problem that the calculus of variations addresses. The trick in the calculus of variations is to consider adding a small _variation_ \\(f(x)\\) to the maximizer \\(p(x)\\). If we plug \\(p(x) + \epsilon f(x)\\) into the functional above, where \\(\epsilon\\) is a small number, the functional should experience a minimum with respect to \\(\epsilon\\) at \\(\epsilon = 0\\), since adding _any_ variation to the maximizer must decrease the functional. The result is a differential equation called the Euler-Lagrange equation. In this case, we should get a differential equation of the form \\( \frac{dp}{dx} = 0\\), which shows that \\(p(x)\\) must be the same for every \\(x\\), hence, a _uniform_ distribution.

[1] http://www.thefreedictionary.com/Principle+of+equal+a-priori+probability.
