---
layout: post
title:  "ERROR: Failed to open cert"
categories: wget
date: 2016-01-19 20:30:00
author: Torsten Rathmann
---

Example error message:

     ERROR: Failed to open cert /Users/someone/.esg/certificates/0119347c.signing_policy: (0).

The error message indicates that something is wrong with your local certificate directory. This error is usually not fatal, i.e. the script run is continued. If your script run ended prematurely, also look for messages below.

**Solution:** Remove all contents of the directory ~/.esg and try running the Wget script again. The .esg will automatically be rebuilt when you run the next Wget script.

