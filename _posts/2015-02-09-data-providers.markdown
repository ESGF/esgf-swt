---
layout: post
title:  "How do I provide data that is not in the MIP tables or Requested Variables list??"
categories: data-providers CMIP5 CMOR
date: 2015-02-09 11:16:16
author: Matthew Harris
---

(Answer status: draft)
You can provide data not requested by CMIP5, though this data will have limited support by the CMIP5 infrastructure. Here is some guidance on how to handle this non-requested data:

Write the data through CMOR (or equivalent). If you elect not to use CMOR then please make the data CF compliant (use http://titania.badc.rl.ac.uk/cgi-bin/cf-checker.pl to check the data). If you variable does not have a CF standard name consider adding it through the CF mailing list.

The CMOR/DRS 'product' should be 'unsolicited' (not 'output').

The unsolicited variable names should not be the same as any of the requested CMIP5 variable names. Possible exceptions are when one might want to provide output of one of the CMIP5 variables, but at a different frequency, or on a different set of levels to those requests (e.g. model levels rather than pressure levels). In this case the variable name should be the same as the requested variable.
You can maintain a set of local MIP tables for use by CMOR. Use the latest versions of the MIP tables as a template.
Choose a suitable name for the CMOR/MIP table. Where variables are based on those requested put them in an equivalent table suffixed with 'Extras' e.g. ' AmonExtras '

Publish using the DRS identifiers as you do for other data, including a version.

If you find exceptions not covered by these recommendations, or see problems with them mail the cmor (cmor AT lists.llnl.gov) or goessp (go-essp-tech AT ucar.edu) mailing lists.
