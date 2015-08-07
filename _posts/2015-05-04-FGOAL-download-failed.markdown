---
layout: post                     #<-- don't touch
title:  "Cannot download FGOALS data" #<-- keep the quotes " ... "
categories: download             #<-- No quotes, comma separated tags
date:   2015-05-04 20:15:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

CMIP5 FGOALS data are allocated to two ESGF data nodes: aims3.llnl.gov is not properly working but the Chinese node esg.lasg.ac.cn is. Please try a download from the latter or search for a replica.

You can see replicas in your search results list if you enable all three checkboxes "Search All Sites", "Show All Replicas" and "Show All Versions", the latter if you want to include the tape based node wdcc-esgf.dkrz.de, which behaves different from a normal ESGF data node and needs an additionally enabled "Show All Versions".

You can confirm the replica is identical by checking the md5 sum against that of the file you were unable to access as listed in the ESGF through the HTTP download interface.


