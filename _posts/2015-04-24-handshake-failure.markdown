---
layout: post
title:  "Received fatal alert: handshake_failure"
categories: wget
date: 2016-03-15 10:31:00
author: Torsten Rathmann
---

Error message:

     Received fatal alert: handshake_failure

Three solutions are possible in case of this Java issue:

**Solution 1:** Run the wget script with the -T option.

     bash wget-################.sh -T

Then another cryptographic protocol will be used for communication: TLS (Transport Layer Security) instead of SSL (Secure Sockets Layer).

**Solution 2:** Run the wget script with the -H option.

     bash wget-################.sh -H

Authentication will be tried without certificates then.

**Solution 3:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.). The wget script can usually be used without options then.

