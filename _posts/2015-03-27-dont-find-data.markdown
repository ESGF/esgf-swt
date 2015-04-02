---
layout: post                     #<-- don't touch
title:  "I don't find the expected data" #<-- keep the quotes " ... "
categories: search, data, CMIP5, CORDEX #<-- No quotes, comma separated tags
date:   2015-03-27 21:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

1. Make sure the checkbox "Search All Sites" is checked. Otherwise only local data are listed in the Results.

2. Use Firefox in a Private Window or use Chrome. Enable JavaScript.

3. ESGF is a worldwide Grid with more than 40 data nodes. Usually a few of them don't work properly. Many ESGF portal administrators exclude malfunctioning nodes and their data from being listed. They do this for the purpose of avoiding a disturbance of their portal. As a user you may do the following:
* Try another portal. For the most important projects, the numbers of datasets "seen" by each portal are listed in the [ESGF Data Visibility table][Data Visibility API]. There, look for part "indexes" since ESGF portals are *index nodes*. The list is refreshed once every four hours.
* Enable the checkbox "Show All Replicas". Many data are also available as a *copy*, especially most CMIP5 data. If you want to include the tape based node wdcc-esgf.dkrz.de, which behaves different from a normal ESGF data node, also enable "Show All Versions".

4. Look into the *errata* of the project whether the data you need are withdrawn. CMIP5 and CORDEX errata pages are listed in the [DKRZ portal][DKRZ portal] under the heading "Errata".

5. Not all variables, times, altitude levels have been archived. For example, 6hr CMIP5 time series are not uninterupted. Which CMIP5 data have been required for which time frequency and experiment is tabulated in the [CMIP5 Standard Output document][CMIP5 Standard Output].

6. If this all didn't help, you may circumvent portals and try finding data on the data nodes directly. From the usual ESGF Search, you know which model simulations are stored on which data node. Go to the *THREDDS catalog* of that data node. Links to the THREDDS catalogs of the European data nodes can be found [here][IS-ENES data nodes].

[Data Visibility API]: https://esg-dn1.nsc.liu.se:8843/api/datavisibility
[DKRZ portal]: http://esgf-data.dkrz.de/esgf-web-fe/
[CMIP5 Standard Output]: http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf
[IS-ENES data nodes]: https://verc.enes.org/data/is-enes-data-infrastructure/enes-data-nodes


