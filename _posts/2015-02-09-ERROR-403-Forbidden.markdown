---
layout: post
title:  "ERROR 403: Forbidden"
categories: download, wget, CMIP5, CORDEX
date: 2015-04-01 18:50:00
author: Matthew Harris, Torsten Rathmann
---

Access to ESGF data is usually restricted. Before you can download data, you have to join a group. In case of the most important projects, condition for being accepted is the acknowledgement of a policy. If you lack a group membership and you try to download data from ESGF, you will get an error message like this:

    Connecting to esg-datanode.jpl.nasa.gov|137.78.210.36|:443... connected.
    HTTP request sent, awaiting response... 403 Forbidden 2012-02-03 04:52:26 ERROR 403: Forbidden.

The error "403 Forbidden" may also be caused by a server issue.

Solution: 

1. **Group membership missing**: Please perform an HTTP download of a single file from the web interface before attempting to run a wget script. This operation will guide you through the process of enrolling with the appropriate data access group. After registration, wget scripting should work for you.

For download of CMIP5 data you need to be member of either *CMIP5 Research* (for non-commercial research and education only) or *CMIP5 Commercial*. Which data are available for unrestricted use and which may only be used for non-commercial research and education is listed in the CMIP5 document [Modeling Groups and their Terms of Use][CMIP5 Terms of Use]. 

For download of CORDEX data you need to be member of either *CORDEX Research* (for non-commercial research and education only) or *CORDEX Commercial*.

2. **Server issue**: Please also try an HTTP download. A typical behaviour of a server which has difficulties in handling group memberships is an endless loop of registration requests without accepting you. Try finding a replica in this case (enable the checkbox "Show All Replicas" in ESGF Search). 

[CMIP5 Terms of Use]: http://cmip-pcmdi.llnl.gov/cmip5/docs/CMIP5_modeling_groups.pdf

