# CitiBike & MTA Exploratory Data Analysis 
#### by Sam Mize, Stephen Cho, and Justin Chan

## Motivations

<p>COVID-19 has impacted our way of life,including public transportation.</p>
<p>This exploratory data analysis aims to show:</p>

<ol>
	<li><strong>Effects of COVID-19 on MTA & CitiBike</strong></li>
	<li><strong>How CitiBike can respond to COVID-19's effects</strong></li>
</ol>


## Data Sources and Time Period

<p>The data is available at the MTA and CitiBike websites linked below</p>

<p>The time periods we chose were January to May 2019/2020. 

<ul>
	<li><a href="http://web.mta.info/developers/turnstile.html">MTA Turnstile Data</a></li>
	<li><a href="https://www.citibikenyc.com/system-data">CitiBike Data</a></li>
</ul>

# 1.Effects of COVID-19 on MTA & CitiBike

![daily_mta_changes](/images/daily_mta_19_20.jpeg)

<h4 align="center"><em>Daily MTA Entries 2019 & 2020 </em></h4> 

<p>There's a pronounced decrease in MTA entries due to COVID-19. It seems like there's a decrease in millions between the EU travel ban announcement and the "15 days" announcement</p>

![daily_citibike_changes](/images/daily_citi_bikes_19_20_total.jpeg)

<h4 align="center"><em>Daily Citibike Entries 2019 & 2020 </em></h4> 

<p>Citibike is also affected,but recovers much better then the MTA </p>


![daily_citibike_percent](/images/daily_pct_chge_mta_bike_19_20.jpeg)

<h4 align="center"><em>Daily CitiBike & MTA Change 2019 - 2020 </em></h4> 

<p>If we take a look at the daily % change in CitiBike & MTA we see a sharp % decrease in daily rides.</p>
<p>However, Citibike seems to be affected less. </p>

![citibike_animationt](/images/citibike_animation.gif)

<h4><em>Citibike's small recovery despite COVID-19 (Animated)**</em></h4> 

<p>Even though COVID-19 affected CitiBike, it still was able to have a small recovery later in the year.</p>
<p><em>**Reload the browser, to see the animation over time</em></p>






# 2.How CitiBike can respond to COVID-19's effects

We wanted to see how the top MTA stations in 2019 were affected by COVID-19.
First, we looked at the top 50 MTA stations in 2019 according to sum of their daily entries.

Then, we calculated the percentage difference between 2019 and 2020 for those top 50 MTA stations.

![mta_largest_avg_weekly_dec](/images/top_mta_station_largest_avg_weekly_dec.jpeg)

<h3 align="center">Top MTA Stations with the largest average weekly % decrease</h3> 

Once we found these affected MTA stations, we looked at the CitiBike data and found which rides had starting stations close to these MTA stations.

Below are the most popular bike stations close to these MTA stations.

<ul>
	<li> E 39 St & 2 Ave </li>
	<li> 8 Ave & W 33 St </li>
	<li> W 33 St & 7 Ave </li>
	<li> Pershing Square North </li>
	<li> 8 Ave & W 31 St </li>
	<li> Broadway & W 60 St</li>
	<li> 6 Ave & W 33 St</li>
	<li> W 26 St & 8 Ave</li>
	<li> Broadway & W 41 St</li>
	<li> W 38 St & 8 Avenue </li>
</ul>


![citi_bike_closest](/images/close_citibike_to_top_mta.svg)

<h4 align="center"><em>Closest CitiBike Stations to affected MTAs</em></h4> 

# Conclusion

Public transportation has been disrupted. Who knows if people will resume riding the MTA? 

What citibike <em>can</em> do, is try to capture the market that MTA lost by focusing on bike stations that are close in proximity to these affected stations.

Citibike can do promotions on these bike stations by offering discounted prices for first time riders.



In addition to that, CitiBike can reassure that these bikes are sanitized by a mobile cleaning crew. 



