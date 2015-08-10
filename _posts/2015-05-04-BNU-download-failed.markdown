---
layout: post                     #<-- don't touch
title:  "Cannot download BNU data" #<-- keep the quotes " ... "
categories: download             #<-- No quotes, comma separated tags
date:   2015-05-04 20:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

BNU ESGF data node esg.bnu.edu.cn is not properly working. 

**Solution 1:** 

Try downloading a replica. You can see replicas in your search results list if you enable all three checkboxes "Search All Sites", "Show All Replicas" and "Show All Versions", the latter if you want to include the tape based node wdcc-esgf.dkrz.de, which behaves different from a normal ESGF data node and needs an additionally enabled "Show All Versions".

You can confirm the replica is identical by checking the md5 sum against that of the file you were unable to access as listed in the ESGF through the HTTP download interface.

**Solution 2:**

If you need data which are not available as a replica, we may send you an OpenID that is still working. Please contact our [support email list][esgf-user].

[esgf-user]: esgf-user@lists.llnl.gov

