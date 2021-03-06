---
layout: post                     #<-- don't touch
title:  "I don't find the expected data" #<-- keep the quotes " ... "
categories: search               #<-- No quotes, comma separated tags
date:   2016-01-19 16:20:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

There might be several reasons and solutions for this issue:

**Solution 1:** Make sure the checkbox `Search All Sites` is checked. Otherwise only local data are listed in the Results.

**Solution 2:** Use Firefox, Chrome or Internet Explorer. Enable JavaScript. Firefox should be used in a New Private Window (in the main menu of Firefox). In this way you can avoid cookie mismatch and disturbance by old cache content.

**Solution 3/4:** ESGF is a worldwide Grid with more than 40 data nodes. Usually a few of them are not working properly. Many ESGF portal administrators exclude malfunctioning nodes or their datasets from being listed; otherwise these malfunctioning nodes may disturb their portals. Disturbed portals may only list local datasets. As a user you may do the following:

  * Try another ESGF portal.

  * Enable the checkbox `Show All Replicas`. Many data are also available as replicas, especially most CMIP5 data. 

**Solution 5:** Look into the *errata* of the project whether the data you need are withdrawn. Links to CMIP5 and CORDEX errata pages are in the [ENES portal][ENES portal].

**Solution 6:** Not all variables, times, altitude levels have been archived for all time frequencies and experiments. For example, CMIP5 RCP daily time series are only available for the years 2006-2100, 2181-2200, and 2281-2300. Which CMIP5 data have been required for which time frequency and experiment is tabulated in the [CMIP5 Standard Output document][CMIP5 Standard Output].

**Solution 7:** Seldom metadata have not properly been overtaken from a data node. In this case circumvent portals and try finding data on the data nodes directly. With help of the usual ESGF Search, find out which model simulations have been stored on which data node. Go to the THREDDS catalog of that data node and use the download links there. Links to the THREDDS catalogs of the European data nodes can be found [here][IS-ENES data nodes].

[Data Visibility API]: https://esg-dn1.nsc.liu.se/api/datavisibility
[ENES portal]: https://verc.enes.org/data/enes-model-data
[CMIP5 Standard Output]: http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf
[IS-ENES data nodes]: https://verc.enes.org/data/is-enes-data-infrastructure/enes-data-nodes


