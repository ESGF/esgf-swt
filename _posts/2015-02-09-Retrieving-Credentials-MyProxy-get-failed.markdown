---
layout: post
title:  "Retrieving Credentials MyProxy get failed"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

    [Caused by: Authentication failed [Caused by: org.ietf.jgss.GSSException, major code: 11, minor code: 0]]

Example error message:

    The certificate expires in less than 8 hour(s). Renewing...

    Please give your OpenID (hit ENTER to accept default) 
    [https://myserver/example/username]? https://pcmdi9.llnl.gov/esgf-idp/openid/....... 
    MyProxy Password? 
    Retrieving Credentials...
    MyProxy get failed. [Caused by: Authentication failed 
    [Caused by: org.ietf.jgss.GSSException, major code: 11, minor code: 0 major string: General failure, unspecified at GSSAPI level minor string: None 
    [Caused by: Bad certificate (java.security.SignatureException: SHA-1/RSA/PKCS#1: Not initialized)]]] Use --help to display help. Certificate could not be retrieved

Solution: make sure that you have installed Oracle Java 1.7 or above, try running `java -version` and `java -showversion`.
