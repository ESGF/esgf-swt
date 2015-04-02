---
layout: post
title:  "Java Errors with wget scripting"
categories: download, wget
date: 2015-04-01 21:00:00
author: Torsten Rathmann, Matthew Harris
---

Java error 1:

     java.security.NoSuchAlgorithmException: algorithm/RSA/ECB/PKCS1Padding is not available from provider Cryptix

Java error 2:

     Received fatal alert: handshake_failure

Two solutions are possible in both cases:

1. Run the wget script with the -H option.

     bash wget-################.sh -H

This easy solution should work, if
* You use Oracle Java 1.7+ or Oracle Java 1.7+
* The ESGF portal you use for script generation runs version 1.8 of ESGF software (The version is shown in the brown rectangle at the bottom of the Home page)
* The data you need are not from NCAR

2. Install Oracle Java 1.7+ and add it to your environment (define JAVA_HOME etc.)

