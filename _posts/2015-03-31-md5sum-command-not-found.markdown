---
layout: post                     #<-- don't touch
title:  "md5sum: command not found" #<-- keep the quotes " ... "
categories: download, wget       #<-- No quotes, comma separated tags
date:   2015-04-29 18:50:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

ESGF download scripts ("wget scripts") need the command line tool md5sum. Please install it. Under Linux, md5sum is usually in one of the standard packages. mdsum5 is used for calculating a checksum after download. This checksum is compared with the checksum in the file list. In this way, a proper download is ensured, i.e. the file is unchanged.


