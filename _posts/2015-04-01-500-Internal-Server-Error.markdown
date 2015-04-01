---
layout: post
title:  "500 Internal Server Error"
categories: login, download, wget
date: 2015-04-01 20:20:00
author: Matthew Harris, Torsten Rathmann
---

The **registration workflow** doesn't work very well on Windows machines, even when using a recent version of FireFox. You may find that after being redirected to the registration page, clicking on the registration button causes the following error:

    HTTP Status 500 - java.lang.Exception: HTTP POST request failed: url= https://pcmdi9.llnl.gov/esgf-idp/secure/registrationService.htm error=HTTP/1.1 500 Internal Server Error

Possible solutions for registration issues:

* Quit FireFox, empty its cache, try again
* Restart FireFox, open a "New Private Window" (FireFox does not remember its cache and cookies in this mode)
* Use Internet Explorer on Windows
* In case you want to register to a group, log onto your ESGF portal, go to the Account page and register there

If you use a **wget script** and see a "500 Internal Server Error", this is a server issue. Please try finding a replica (enable the checkbox "Show All Replicas").


