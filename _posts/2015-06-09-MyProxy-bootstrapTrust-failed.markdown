---
layout: post
title:  "MyProxy bootstrapTrust failed"
categories: wget
date: 2016-03-16 10:20:00
author: Torsten Rathmann
---

Error message:

    Connecting to pcmdi9.llnl.gov...
    Error: MyProxy bootstrapTrust failed. [Caused by: No appropriate protocol (protocol is disabled or cipher suites are inappropriate)]

Three solutions are possible in case of this Java issue:

**Solution 1:** Run the wget script with the -H option.

     bash wget-################.sh -H

Then authentication will be tried without certificates.

**Solution 2:** Run the wget script with the -T option.

     bash wget-################.sh -T

Then another cryptographic protocol will be used for communication: TLS (Transport Layer Security) instead of SSL (Secure Sockets Layer).

**Solution 3:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.). The wget script can usually be used without options then.

