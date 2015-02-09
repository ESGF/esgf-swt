---
layout: post
title:  "I am having trouble downloading CNRM-CM5 data?"
categories: data access data-access 
date: 2015-02-09 11:30:21
author: Matthew Harris
---

The problem was that CNRM had republished some datasets after having modified the THREDDS dataset root entries, without unpublishing the datasets first. Specifically, it appears that they replaced the single dataset root esg_dataroot with four dataset roots esg_dataroot1, ..., esg_dataroot4. Then the gateway has duplicate URLs for many files. When a download is requested, the gateway picks one of the URLs arbitrarily by some mysterious mechanism. If the URL is invalid the download fails. The solution, report this to a pcmdi9 administrator who must look into the issue. It may be resolved by identifying and removing those duplicates.
