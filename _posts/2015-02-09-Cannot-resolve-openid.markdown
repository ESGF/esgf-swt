---
layout: post
title:  "Cannot resolve openid?"
categories: openid
date: 2015-02-09 11:59:21
author: Matthew Harris
---

This could be either a problem with the user account, or with the server setup where the user registered:

* Possibly, the user data (openid, first name, last name, etc.) contain non-standard characters, which will make the login fail. The user should change the data him/herself, or contact the server administrator
* Or, the server is not setup correctly. The administrator should check for these possible problems:
  * Certificate expired (host certificate or CA certificate)
  * Root CA not in the truststore or not in the federation certificate repository
  * Server OpenID provider URL not in the whitelist of OpenID relying party
  * Server clock sync issue
  * Firewall side effects
  * The file esg-trustore.ts does NOT match the file jssecacerts in the JAVA installation directory
