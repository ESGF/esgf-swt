---
layout: post
title:  "Handschake ERROR:"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

     Received fatal alert: handshake_failure

* The problem is again that the wget script needs Oracle Java 1.7 or newer to work. Because of security reasons one of the SSL protocol versions had to be disabled on ESGF servers. If your Java cannot switch to another protocol version, a handshake is not possible. Try running "java -showversion" to check your Java.
