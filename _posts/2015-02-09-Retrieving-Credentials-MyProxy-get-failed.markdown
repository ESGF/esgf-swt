---
layout: post
title:  "Retrieving Credentials MyProxy get failed"
categories: download, wget
date: 2015-05-04 20:50:00
author: Torsten Rathmann, Matthew Harris
---

    [Caused by: Authentication failed [Caused by: org.ietf.jgss.GSSException, major code: 11, minor code: 0]]

Example error message:

    Please give your OpenID (hit ENTER to accept default) 
    [https://myserver/example/username]? https://pcmdi9.llnl.gov/esgf-idp/openid/....... 
    MyProxy Password? 
    Retrieving Credentials...
    MyProxy get failed. [Caused by: Authentication failed 
    [Caused by: org.ietf.jgss.GSSException, major code: 11, minor code: 0 major string: General failure, unspecified at GSSAPI level minor string: None 
    [Caused by: Bad certificate (java.security.SignatureException: SHA-1/RSA/PKCS#1: Not initialized)]]] Use --help to display help. Certificate could not be retrieved

Two solutions are possible in case of this Java issue:

**Solution 1:** Run the wget script with the -H option.

     bash wget-################.sh -H

Then authentication will be tried without certificates. This easy solution should work, if

* The ESGF portal you use for script generation runs version 1.8 of ESGF software (The version is shown in the brown rectangle at the bottom of the Home page)
* The data you need are not from ESGF NCAR data node tds.ucar.edu (error message: "http request to OpenID Relying Party service failed.")

**Solution 2:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.)

