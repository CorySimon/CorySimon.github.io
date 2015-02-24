---
layout: post
title: Does having a PhD hurt your dating prospects?
excerpt: "Dating app Coffee Meets Bagel releases data on percentage of times a person is liked given his or her level of education."
comments: false
categories: articles
share: true
tags: [statistics]
---

Coffee meets bagel (CMB) is a dating app where, each day, you are presented with a potential match. Based on that person's photos and profile, you then click "Like" or "Pass". If you both "Like" each other, the app then allows you message each other.

In a recent [blog post](https://coffeemeetsbagel.com/blog/index.php/dating-statistics/appeal-education-degree-stacks-dating/), CMB posted the percentage of times that men and women are liked based on their level of education. My recreation of their data is in the bar chart below, which shows the percentage of times a man/woman is expected to be "Liked" given their highest education. Men are represented by the blue bars and women are represented by the red bars.

<html>
<head>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript">
google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);
function drawChart() {
    var data = google.visualization.arrayToDataTable([
            ['Highest Degree', 'Men', 'Women'],
            ['Bachelor',  27, 42],
            ['MD',  35, 41],
            ['JD',  32, 40],
            ['MBA',  33, 39],
            ['PhD',  28, 38],
            ['Master', 26, 37]
            ]);

    var options = {
title: 'Percentage of times liked',
       vAxis: {title: 'Highest degree'}
    };

    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));

    chart.draw(data, options);
}
</script>
</head>
<body>
<div id="chart_div" style="width: 900px; height: 500px;"></div>
</body>
</html>

Note the following:
	
  * Overall, women on CMB are more selective than men on CMB; for every level of education, women are liked a higher percentage of the time than the men.

	
  * For men on CMB, those with an MD, MBA, or JD are more likely to be liked than those with only a Bachelor's, Master's, or PhD.

	
  * For women on CMB, those with only a bachelor's degree-- the _lowest_ level of education-- are most likely to be liked.


Still, from a scientific standpoint, it is difficult to make any sound conclusions from these data.

First, notice that I qualified all of the statements above with "men/women _on CMB_". There is a selection bias here; CMB users are not a random sample of the population at large. The CMB blog even points out that 25% of CMB users have a higher degree in comparison to 12% of the population at large; the CMB user base is not representative of the singles in the US.

This selection bias could account for many of these differences. For example, if only the ugliest men in PhD programs registered for CMB, whereas the better-looking men chose to meet girls on campus instead, this could explain why men with PhDs on CMB are less likely to be liked than the MDs, MBAs, and JDs.

Further, we cannot make claims such as "getting a PhD hurts you in dating" or "getting an MD helps you in dating". This is assuming causation; there are many other variables at play. People who choose to pursue an MBA are different than people who choose to pursue a PhD. As an example, a talkative, social person is probably more likely to pursue an MBA than choose to sit at a computer in a basement by himself or herself for five years working on a PhD. And, I'm speculating here, being a gregarious person would probably help your cause in dating.

Finally, as women with only a bachelor's degree are liked the most, does getting a higher education _hurt_ a woman's prospects in dating? I speculate not, and age could be a lurking variable here that explains why.

In the book Dataclysm by Christian Rudder, the cofounder of OkCupid, two plots based on OkCupid data depict the age people find most attractive. The chart below show a woman's age on the rows and, in the columns, the age of the man she finds most attractive. The diagonal line represents equality, where women prefer men of their own age. For the most part, women find men that are similar to their own age the most attractive.

![](https://espnfivethirtyeight.files.wordpress.com/2014/09/chart_men.jpg?w=1024)

On the other hand, if we look at _men_ and what age women _they_ find most attractive, men consistently find 20-24 year old women the most attractive, regardless of their age.

![](http://espnfivethirtyeight.files.wordpress.com/2014/09/chart_women.jpg?w=1024)

This difference in age preference can explain why women with bachelor's degrees are getting liked a higher percentage of the time: they are younger than those pursuing MD's, MBAs, and PhDs.

It is difficult to make sound conclusions based on observational data because of selection bias and lurking variables. It is a lot of fun to speculate about the reasons we observe these trends, but ultimately we require an A/B test to be sure. For example, we can ask the question: does the _idea_ of a man having an MD attract a woman, or is it some lurking quality that most men who are pursuing an MD have that makes them more attractive? To test this, we can randomly partition the CMB user base of women into two random groups: A and B. For group A, we show a man's profile along with the statement "I have an MD". For group B, we could show the _exact_ same profile, with the only difference being "I have a PhD" instead of "I have an MD". Then, compare the percentage of times these profiles were liked among groups A and B. This experiment controls for factors that may be different from PhDs and MDs by keeping all other aspects of the two profiles the same.
