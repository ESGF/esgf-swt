---
layout: post
title:  "ERROR 403: Forbidden?"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

This denotes lack of proper authorization, either because the user is not properly authorized for CMIP5 Research access, or because the data on the server is not configured to allow access to CMIP5 Research users.

Example error message:

    Connecting to esg-datanode.jpl.nasa.gov|137.78.210.36|:443... connected.
    HTTP request sent, awaiting response... 403 Forbidden 2012-02-03 04:52:26 ERROR 403: Forbidden.

    Solution: please perform an http download of a single file from the web interface before attempting to run a wget script, as described in the [Registration and Download Guide][radg]. This operation will guide you through the process of enrolling with the appropriate data access group. (There is a more robust and streamline group registration process under development, soon to be released.)

[radg]: https://github.com/ESGF/esgf.github.io/wiki/ESGF_Data_Download
