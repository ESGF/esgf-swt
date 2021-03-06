---
layout: post
title:  "How can I preserve the directory structure?"
categories: wget
date: 2016-02-03 14:40:00
author: Torsten Rathmann, Katharina Berger
---

If you want to create a directory structure on your local computer and to copy your downloaded files into this structure, create your Wget script via URL (more precisely ESGF Search RESTful API) and use the download_structure command. For example, a CMIP5 directory structure can be created with

    http://esgf-data.dkrz.de/esg-search/wget?download_structure=project,product,institute,model,experiment,time_frequency,realm,cmor_table,ensemble,variable&project=CMIP5&experiment=historical&cmor_table=Amon&variable=tas&variable=pr

The other commands, delimited by `&`, are search categories.

* Equal search categories will be processed in the sense of logical OR. Since the URL contains two "variable" statements, one for near surface temperature tas and one for precipitation pr, the search will provide a file list for these two variables.
* Different search categories will be processed in the sense of AND
* Blanks in the category name are to be replaced by `_`

For preservation of the CORDEX data structure you may use

    http://esgf-data.dkrz.de/esg-search/wget?download_structure=project,product,domain,institute,driving_model,experiment,ensemble,rcm_model,rcm_version,time_frequency,variable&project=CORDEX 

followed by the search categories you need.

A comprehensive description of ESGF Search RESTful URLs can be found [here][ESGF Search RESTful API].

[ESGF Search RESTful API]: https://github.com/ESGF/esgf.github.io/wiki/ESGF_Search_REST_API
