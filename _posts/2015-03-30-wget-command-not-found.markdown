---
layout: post                     #<-- don't touch
title:  "wget: command not found" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2016-03-16 10:40:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

For fetching files, ESGF Wget scripts need the command line tool Wget. Please install it. Under Linux, Wget is usually in one of the standard packages. Nevertheless, Wget is not standard under Mac OS X. The easiest way to install Wget under Mac OS X is utilization of Homebrew:

     brew install wget

Homebrew itself can be installed with the command

     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


