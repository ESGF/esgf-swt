---
layout: post                     #<-- don't touch
title:  "md5sum: command not found" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2015-04-29 11:10:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

ESGF Wget scripts need the command line tool md5sum. Please install it. mdsum5 is sometimes used instead of sha256sum for calculating a checksum after download. This checksum is compared with the checksum in the file list. In this way, a proper download, i.e. an unchanged file, is ensured.

Under Linux, md5sum is usually in one of the standard packages. Under Mac OS X md5sum is not standard. The easiest way to install md5sum on a Mac is utilization of Homebrew:

     brew install md5sha1sum

GNU md5sha1sum contains md5sum besides other checksum software. Homebrew itself can be installed with the command

     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"



