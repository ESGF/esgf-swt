---
layout: post                     #<-- don't touch
title:  "How can I verify that the data have not been updated since I downloaded them?" #<-- keep the quotes " ... "
categories: data                 #<-- No quotes, comma separated tags
date:   2015-03-31 21:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

You may compare the version of the data. The version is part of the metadata can be found in the ESGF portals. It is also printed in the NetCDF header. 

Sometimes data producers replace data without updating the version number in case of minor chenges. In ESGF, this is not allowed and fortunately seldom. Ruling out these hidden changes is tedious. You may compare the checksum of your download file with that of a freshly downloaded file. Checksums may be calculated with md5sum:

    md5sum myfile.nc



