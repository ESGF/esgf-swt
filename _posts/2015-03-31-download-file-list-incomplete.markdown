---
layout: post                     #<-- don't touch
title:  "The download file list in wget script is incomplete" #<-- keep the quotes " ... "
categories: download, wget       #<-- No quotes, comma separated tags
date:   2015-03-31 17:40:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Downloads with ESGF wget scripts are usually limited to 1000 files per run. Therefore the download file list is truncated if the number of files exceeds 1000. Two ways are possible to overcome this issue:

**1. Select the variables you need with "Filter over text"** 

Unless you need all variables, you should filter them. Unfortunately simple selection via the Search Categories "Variable", "Variable Long Name" and "CF Standard Name" only affects the dataset list. A selection of files inside a dataset is not be done in this way. Instead use "Filter over text". The following steps lead to a wget script for one variable only, in the example tas:

* Type-in *variable:tas* in the text field left to the light blue "Search" button
* Press the light blue "Search" button. A *query:variable:tas* should appear in the "Current Selections"
* In case this has not be done before, add the data sets you are interested in to the Data Cart
* Under tab "Data Cart" enable the radio button "Filter over text"
* Click on "WGET", download the wget script and run it

In case you need more than one variable, you may use the OR keyword in the text field in the first step, for example:

    variable:tas OR variable:tasmax OR variable:tasmin


**2. Use URL-based script generation**

Sometimes the number of download files still exceeds 1000. Scripts for huge downloads can efficiently be created by using ESGF Search RESTful URLs. The example below shows the URL for creation of a wget script for several variables and all CMIP5 RCP Amon scenarios:

    http://esgf-data.dkrz.de/esg-search/wget/?project=CMIP5&experiment_family=RCP&cmor_table=Amon&variable=tas&variable=tasmax&variable=tasmin&limit=8000

* With the command "limit=8000" the file number limit is enlarged to 8000. The maximum file number limit allowed in ESGF is 10000
* Search categories are delimited by "&"
* Equal search categories are processed in the sense of logical OR. Since the URL contains three "variable" statements for the three variables tas, tasmax and tasmin, the search will provide a file list for these three variables.
* Different search categories are processed in the sense of AND
* Blanks in the category name are replaces by "_"

A comprehensive description of ESGF Search RESTful URLs can be found [here][ESGF Search RESTful API].

[ESGF Search RESTful API]: https://github.com/ESGF/esgf.github.io/wiki/ESGF_Search_REST_API

