---
layout: post                     #<-- don't touch
title:  "sha256sum: command not found" #<-- keep the quotes " ... "
categories: download, wget       #<-- No quotes, comma separated tags
date:   2015-06-09 14:25:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

ESGF download scripts ("wget scripts") need the command line tool sha256sum. Please install it. sha256sum is sometimes used instead of md5sum for calculating a checksum after download. This checksum is compared with the checksum in the file list. In this way, a proper download is ensured, i.e. the file has been downloaded unchanged.


