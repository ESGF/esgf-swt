---
layout: post
title:  "How can I create a wget script that contains only the files for some selected variables?"
categories: wget
date: 2015-10-29 17:30:00
author: Matthew Harris, Torsten Rathmann
---

Please follow these steps:

* Use any of the facet constraints on the left to return a set of matching datasets (each dataset containing many files, possibly for more than one variable).
* Login
* Add the datasets you need to your data cart
* Type-in the names of the variables you need in the text field right of "When 'Show Files' is clicked, or when using WGET or Globus, you may use an optional string to sub-select the filenames"
* Press the "Apply" button
* Create your WGET script, download and run it

In case you need more than one variable, you may use the OR keyword in the text field, for example:

    variable:tas OR variable:tasmin OR variable:tasmax

or simply search the variable names with a blank as delimiter:

    tas tasmin tasmax


