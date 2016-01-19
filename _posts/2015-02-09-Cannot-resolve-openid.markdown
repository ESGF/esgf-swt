---
layout: post
title:  "Cannot resolve openid"
categories: login
date: 2016-01-19 21:10:00
author: Matthew Harris, Torsten Rathmann
---

This could be either a problem with the user account, or with the server setup where the user registered:

* The user data (openid, first name, last name, etc.) contain non-standard characters, which will make the login fail. The user should change the data him/herself, or contact the server administrator
* Or the account was not overtaken into the overhauled ESGF, see question ["I can not log in with my OpenID created before January 2016"][cannot-login-with-openid-created-before-Jan-2016]
* Or the server was retired (example: pcmdi3)
* Or the server is not setup correctly. The administrator should check for these possible problems:
  * Certificate expired (host certificate or CA certificate)
  * Root CA not in the truststore or not in the federation certificate repository
  * Server OpenID provider URL not in the whitelist of OpenID relying party
  * Server clock sync issue
  * Firewall side effects
  * The file esg-trustore.ts does NOT match the file jssecacerts in the JAVA installation directory

[cannot-login-with-openid-created-before-Jan-2016]: http://esgf.github.io/esgf-swt/login/2016/01/18/cannot-login-with-openid-created-before-Jan-2016.html

