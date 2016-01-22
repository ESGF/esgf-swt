---
layout: post
title:  "How can I preserve the directory structure?"
categories: wget
date: 2016-01-21 11:30:00
author: Torsten Rathmann, Katharina Berger
---

If you want to create a directory structure on your local computer and to copy your downloaded files into this structure, create your Wget script via URL (more precisely ESGF Search RESTful API) and use the download_structure command. For example, a CMIP5 directory structure can be created with

    http://esgf-data.dkrz.de/esg-search/wget?download_structure=project,product,institute,model,experiment,time_frequency,realm,cmor_table,ensemble,version,variable&project=CMIP5&experiment=historical&cmor_table=Amon&variable=tas&variable=pr

