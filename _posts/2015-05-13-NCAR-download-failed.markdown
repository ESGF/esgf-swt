---
layout: post                     #<-- don't touch
title:  "Cannot download NCAR data, e.g. CCSM and CESM" #<-- keep the quotes " ... "
categories: download, wget, HTTP #<-- No quotes, comma separated tags
date:   2015-05-13 14:45:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

NCAR data node tds.ucar.edu is not working properly. 

**Solution 1:** Try downloading a replica.

You can see replicas in your search results list if you enable all three checkboxes "Search All Sites", "Show All Replicas" and "Show All Versions", the latter if you want to include the tape based node wdcc-esgf.dkrz.de, which behaves different from a normal ESGF data node and needs an additionally enabled "Show All Versions".

You can confirm the replica is identical by checking the md5 sum against that of the file you were unable to access as listed in the ESGF through the HTTP download interface.

**Solution 2:** Use an OpenID issued by esg-dn1.nsc.liu.se and follow the "HTTP" download link.

