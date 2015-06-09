---
layout: post
title:  "MyProxy bootstrapTrust failed"
categories: download, wget
date: 2015-06-09 16:35:00
author: Torsten Rathmann
---

Error message:

    Connecting to pcmdi9.llnl.gov...
    Error: MyProxy bootstrapTrust failed. [Caused by: No appropriate protocol (protocol is disabled or cipher suites are inappropriate)]

Three solutions are possible in case of this Java issue:

**Solution 1:** Run the wget script with the -H option.

     bash wget-################.sh -H

Then authentication will be tried without certificates. This easy solution should work, if

* The ESGF portal you use for script generation runs version 1.8 of ESGF software (The version is shown in the brown rectangle at the bottom of the Home page)
* The data you need are not from NCAR data node tds.ucar.edu (error message: "http request to OpenID Relying Party service failed.")

**Solution 2:** Run the wget script with the -T option.

     bash wget-################.sh -T

Then another cryptographic protocol will be used for communication: TLS (Transport Layer Security) instead of SSL (Secure Sockets Layer).

**Solution 3:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.). The wget script can usually be used without options then.

