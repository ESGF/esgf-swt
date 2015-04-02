---
layout: post                     #<-- don't touch
title:  "I got a 'md5sum: command not found'" #<-- keep the quotes " ... "
categories: download, wget       #<-- No quotes, comma separated tags
date:   2015-03-31 11:30:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

ESGF download scripts ("wget scripts") need the command line tool md5sum. Please install it. Under Linux, md5sum is usually in one of the standard packages. mdsum5 is used for calculating a checksum after download. This checksum is compared with the checksum in the file list. In this way it is ensured that the file has been properly downloaded, i.e. is unchanged.


