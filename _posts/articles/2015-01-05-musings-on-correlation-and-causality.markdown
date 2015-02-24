---
layout: post
title: Musings on correlation and causality
excerpt: "Correlation does not include causation."
comments: false
categories: articles
share: true
tags: [statistics]
---

_Post hoc ergo propter hoc_. Latin for "After this, therefore because of this", a common logical fallacy. 


> She didn't respond to my text after our date. It must have been because I ate my desert with a fork instead of a spoon.
> 
> \-- An example of post hoc ergo propter hoc


Similarly, often we observe a correlation between two variables X and Y and fallaciously extrapolate to the conclusion that X *causes* Y. This extrapolation could be false for several reasons.

**Reverse causation**. Smoking is correlated with lung cancer. Instead of proposing that smoking is a risk factor for lung cancer, an alternative conclusion is that lung cancer elicits the desire to breathe smoke into one's lungs. More on this later.

**A chance correlation**. When mining large data sets, it is almost inevitable that one will discover spurious correlations by *chance*, even though the two variables are completely unrelated in reality. As an example, are Mexican lemons making our highways safer? [1] A myriad of ridiculous spurious correlations: [here](http://www.tylervigen.com/).

![](http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jcisd8/2008/jcisd8.2008.48.issue-1/ci700332k/production/images/medium/ci700332kn00001.gif){: .center-image }



**Lurking variables**. Often two variables are correlated because of a third, underlying factor that we hadn't thought about-- the *lurking variable*. For example, shoe size is probably correlated with reading ability. This is because of a lurking variable: age; children have small feet and are still developing their reading skills [2].

The lurking variable scenario is different than the above chance correlation because the two variables are, albeit indirectly, indeed related. If we performed an experiment to see if importing lemons reduces highway fatalities, we likely would not reproduce this correlation since it arose by chance; both lemon imports and highway fatalities _happened_ to decrease together from 1996 to 2000-- they are not related. On the other hand, we could measure shoe size and reading ability in every city in the US and reproduce this correlation over and over. When a lurking variable is involved, one must delve more deeply into the design of the experiment to negate the causal conclusion [if indeed false]. Only until we identify what confounding factors may be present can we design an experiment that controls for age, which will negate the causal conclusion that big feet endow people with better reading skills.



* * *



**Observational data vs. Experimental data**. There is a very important distinction between data _observed_ in the natural world and data collected during a _controlled experiment_.

Consider measuring advil consumption and headaches. In the observational setting, we look at all people that are taking advil and note that they also have headaches. To aliens that didn't know that people took advil to combat headaches, this suggests the hypothesis that taking advil _causes_ headaches. On the other hand, a controlled experiment would take two _random_ groups of people and force one of the groups to take advil and keep the other group advil-free. Then, by observing the incidence of headaches in the two groups, the correlation between taking advil and headaches would disappear since we _controlled_ for the fact that the people who _choose_ to take advil are different from those who choose not to. In fact, we would likely find the opposite correlation of the observational study: those who took advil were _less_ likely to have a headache.

* * *

So, what is the point of looking at correlations in observational data if we cannot logically conclude causation?

The first reason is that we can harness predictive value from a [non-chance] correlation, even in the absence of a causal relationship. If I were looking for someone to read me a story and only had a list of candidates and their shoe sizes, my best bet is to choose someone who has a shoe size of 10 over someone with a shoe size of 5, since the latter is probably a kid who reads very poorly. We can exploit this correlation for predicting reading ability regardless of whether big feet actually endow one with reading skills.

The second reason is that very often two variables X and Y are correlated *indeed* because X *causes* Y. Exploratory data analysis could thus lead us to first discover a causal relationship between two variables, particularly when the cause-effect relationship is subtle [5]. Of course, further investigation and study is required for a sound scientific conclusion, but the correlation is what initially _raised the question_. So, we shouldn't always ignore a correlation between two variables, of course.

For example, John Snow observed that many deaths from a cholera outbreak occurred in proximity with a particular water pump, which may have led him to discover that cholera was acquired from the water at this pump and transmitted in water generally. [3]

And, yeah, that smoking cigarettes is a risk factor for lung cancer is supported by the higher incidence of lung cancer in smokers than in non-smokers:


> The simple correlation is not enough to arrive at a conclusion of causation, but multiple correlations all triangulating on the conclusion that smoking causes lung cancer, combined with biological plausibility, does.
>
> The duration of smoking increases risk of cancer (a dose response relationship), stopping smoking reduces the risk of cancer, greater intensity of smoking increases risk, and smoking unfiltered vs filtered cigarettes is associated with higher risk. These various correlations only make sense if smoking causes lung cancer. Further, tobacco smoke contains substances demonstrated to be carcinogens – so there is biological plausibility.
>
> \-- Steven Novella


Discovery of _correlations_ often incites further data collection and controlled studies to confirm the correlation, rule out lurking variables, and investigate mechanisms for a causal relationship. Still, data collection is often prohibitively expensive and controlled studies are often impractical/unethical, such as forcing people to smoke for 20 years to see if they get lung cancer. So, often correlations from observational data are used as [albeit sometimes weak] scientific support, particularly when one cannot offer a reasonable alternative explanation and there are plausible physical mechanisms for the causation.

Furthermore, studies to scientifically evaluate a causal conclusion take time. This yields difficulties: if we have a _reasonable_ explanation for causation and additionally observe a correlation in observational data, a swift policy decision might need to be made, essentially weighing how much we can rule out lurking variables. For example, a statistically significant effect was found between childhood leukemia rates and living within 5 km of a nuclear power plant in Germany [6]. Should Germany take action by shutting down its nuclear power plants or move everyone within a 5 km radius of them? Exposure to radiation from the plant is a plausible mechanism for elevated risks of childhood leukemia. But what about any lurking variables? How about the site chosen for a power plant? "One obvious possibility is that nuclear power plants are situated in low income areas that have higher cancer rates than suffered by the general population" [5].

Here's the take-home message: sound data analysis and good science requires conscientious, thorough thinking, attention to detail, and raising questions with an open mind.

[1] [http://pubs.acs.org/doi/abs/10.1021/ci700332k](http://pubs.acs.org/doi/abs/10.1021/ci700332k)

[2] [http://rationalwiki.org/wiki/Correlation_does_not_imply_causation](http://rationalwiki.org/wiki/Correlation_does_not_imply_causation)

[3] [http://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak](http://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak)

[4] [http://www.sciencebasedmedicine.org/evidence-in-medicine-correlation-and-causation/](http://www.sciencebasedmedicine.org/evidence-in-medicine-correlation-and-causation/)

[5] [https://www.utexas.edu/courses/bio301d/Topics/Correlation/Text.html](https://www.utexas.edu/courses/bio301d/Topics/Correlation/Text.html)

[6] [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2757021/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2757021/)


