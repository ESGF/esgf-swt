---
layout: post                     #<-- don't touch
title:  "Cannot download CSIRO or ACCESS data"    #<-- keep the quotes " ... "
categories: download, wget, HTTP #<-- No quotes, comma separated tags
date:   2015-05-04 20:20:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Original CSIRO-Mk3.6.0 and also ACCESS1.0 and ACCESS1.3 data cannot be downloaded because of a malfunctioning data server. We apologize for the inconvenience. NCI is setting up a new server.

In the meantime, please try downloading a replica from another node than esgnode2.nci.org.au.  You can see replicas in your search results list if you enable all three checkboxes "Search All Sites", "Show All Replicas" and "Show All Versions", the latter if you want to include the tape based node wdcc-esgf.dkrz.de, which behaves different from a normal ESGF data node and needs an additionally enabled "Show All Versions". 

You can confirm the replica is identical by checking the md5 sum against that of the file you were unable to access as listed in the ESGF through the HTTP download interface.

