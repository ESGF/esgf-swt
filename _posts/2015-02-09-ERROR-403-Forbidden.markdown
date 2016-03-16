---
layout: post
title:  "ERROR 403: Forbidden"
categories: wget
date: 2016-03-16 11:30:00
author: Torsten Rathmann, Matthew Harris
---

Access to ESGF data is usually restricted. Before you can download data, you have to join a data access group. In case of the most important projects, condition for being accepted is the acknowledgement of a policy. If you lack a group membership and try to get data from ESGF with a download script, you will get an error message like this:

    Connecting to esg-datanode.jpl.nasa.gov|137.78.210.36|:443... connected.
    HTTP request sent, awaiting response... 403 Forbidden 
    2012-02-03 04:52:26 ERROR 403: Forbidden.

The error "403 Forbidden" may also be caused by a server issue. A typical behaviour of a server, which has difficulties in handling group memberships, is an endless loop of registration requests without accepting you. 

**Solution in case of a missing group membership:**

Please join a proper data access group. Most ESGF portals have links to a page where you can accept the terms.

An alternative way to join a data access group is a data download with the browser's download manager. Simply expand a project's dataset with "Show Files" and follow a HTTPServer link. This operation will also guide you through the process of enrolling with the appropriate data access group. After registration, download scripts should work for you.

For download of CMIP5 data you need to be member of either *CMIP5 Research* (for non-commercial research and education only) or *CMIP5 Commercial*. Which data are available for unrestricted use and which may only be used for non-commercial research and education is listed in the CMIP5 document [Modeling Groups and their Terms of Use][CMIP5 Terms of Use]. 

For download of CORDEX data you need to be member of either *CORDEX Research* (for non-commercial research and education only) or *CORDEX Commercial*.

**Solution in case of a server issue:**

Try downloading a replica. Most CMIP5 data are also available as a replica. Enable the checkbox “Show All Replicas” in ESGF Search to see replicas in the search results.

[CMIP5 Terms of Use]: http://cmip-pcmdi.llnl.gov/cmip5/docs/CMIP5_modeling_groups.pdf

