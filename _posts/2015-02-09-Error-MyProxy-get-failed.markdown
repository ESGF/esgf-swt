---
layout: post
title:  "Error: MyProxy get failed"
categories: download, wget
date: 2015-04-01 19:45:00
author: Matthew Harris
---

    [Caused by: Authentication failed [Caused by: Failure unspecified at GSS-API level [Caused by: Unknown CA]]]

Solution: try to remove everything under `~/.esg` and run the wget script or MyProxy command again.
