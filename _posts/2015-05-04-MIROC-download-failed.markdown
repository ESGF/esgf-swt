---
layout: post                     #<-- don't touch
title:  "Cannot download MIROC and MRI data with wget script" #<-- keep the quotes " ... "
categories: download, wget       #<-- No quotes, comma separated tags
date:   2015-06-09 11:20:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

**Solution 1:** Additionally use the "insecure" option -i, for example:

     bash wget-################.sh -H -i 

The server certificate will not be checked then.

**Solution 2:** Try downloading a replica. You can see replicas in your search results list if you enable all three checkboxes "Search All Sites" and "Show All Replicas". If you want to include the tape based node wdcc-esgf.dkrz.de, also enable "Show All Versions" since this node behaves different from a normal ESGF data node.

You can confirm the replica is identical by checking the md5 sum against that of the file you were unable to access as listed in the ESGF through the HTTP download interface.

**Solution 3:** Try downloading single files with your browser's download manager. In your Data Cart click on "Show Files" and then on "HTTP". 

