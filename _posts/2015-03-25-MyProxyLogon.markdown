---
layout: post                     #<-- don't touch
title:  "I have a problem running MyProxyLogon application" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2015-03-25 16:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

MyProxyLogon application may be used to prepare a download script run (wget script run) but this is error prone. Under Linux or MacOSX this is also outdated since wget scripts are itself able to fetch the necessary credentials and to inquire OpenID and password.

Please try running the wget script alone. Before you try it again, remove your credentials directory .esg since your credentials may be damaged due to the MyProxyLogon failure. ESGF wget scripts will automatically rebuild the credentials directory if it is missing.
