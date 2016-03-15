---
layout: post
title:  "Retrieving Credentials MyProxy get failed"
categories: wget
date: 2016-03-15 10:55:00
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

Then authentication will be tried without certificates. This easy solution should work if you use Linux.

**Solution 2:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.). The wget script can usually be used without options then.

