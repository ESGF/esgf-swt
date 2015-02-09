---
layout: post
title:  "Java ERROR:"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

     java.security.NoSuchAlgorithmException: algorithm/RSA/ECB/PKCS1Padding is not available from provider Cryptix

* The problem is that the wget script needs Oracle Java 1.7 or newer to work. It wont work with OpenJRE where you'll get cryptographic provider errors. Try running "java -showversion" to check your Java.
