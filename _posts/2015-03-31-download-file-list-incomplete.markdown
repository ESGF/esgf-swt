---
layout: post                     #<-- don't touch
title:  "The download file list in wget script is incomplete" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2016-01-18 21:00:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Downloads with ESGF wget scripts are usually limited to 1000 files per run. Therefore the download file list is truncated if the number of files exceeds 1000. Two ways are possible to overcome this issue:

**Solution 1: Select the variables you need with help of text field** 

Unless you need all variables, you should filter them. Unfortunately simple selection via the Search Categories "Variable", "Variable Long Name" and "CF Standard Name" only affects the dataset list. A selection of files inside a dataset can not be done in this way. Instead use the text field of the data cart. The following steps lead to a Wget script only for the variables you want:

* Login
* Add the datasets you need to your data cart
* Type-in the names of the variables you need in the text field right of "When 'Show Files' is clicked, or when using WGET or Globus, you may use an optional string to sub-select the filenames"
* Press the "Apply" button
* Create your WGET script, download and run it

If you need more than one variable, type-in the variable names with a blank as delimiter, for example:

    tas tasmin tasmax


**Solution 2: Use URL-based script generation**

Sometimes the number of download files still exceeds 1000. Scripts for huge downloads can efficiently be created by using ESGF Search RESTful URLs. The example below shows the URL for creation of a wget script for several variables and all CMIP5 RCP Amon scenarios:

    http://esgf-data.dkrz.de/esg-search/wget/?project=CMIP5&experiment_family=RCP&cmor_table=Amon&variable=tas&variable=tasmax&variable=tasmin&limit=8000

* With the command `limit=8000` the file number limit is enlarged to 8000. The maximum file number limit allowed in ESGF is 10000
* Search categories are delimited by `&`
* Equal search categories will be processed in the sense of logical OR. Since the URL contains three "variable" statements for the three variables tas, tasmax and tasmin, the search will provide a file list for these three variables.
* Different search categories will be processed in the sense of AND
* Blanks in the category name are to be replaced by `_`

A comprehensive description of ESGF Search RESTful URLs can be found [here][ESGF Search RESTful API].

[ESGF Search RESTful API]: https://github.com/ESGF/esgf.github.io/wiki/ESGF_Search_REST_API

