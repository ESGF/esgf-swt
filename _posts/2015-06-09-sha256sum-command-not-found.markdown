---
layout: post                     #<-- don't touch
title:  "sha256sum: command not found" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2016-03-16 11:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

ESGF Wget scripts for data download need the command line tool sha256sum under Linux. Please install it. sha256sum is used for calculating a checksum after download. This checksum is compared with the checksum in the file list. In this way, a proper download, i.e. an unchanged file, is ensured.

Under Mac OS X, SHA software is not standard and is deployed under a different name. As a Mac user, please install GNU SHA2. The easiest way to do this is utilization of Homebrew:

     brew install sha2

Homebrew itself can be installed with the command

     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

