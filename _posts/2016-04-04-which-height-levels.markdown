---
layout: post                     #<-- don't touch
title:  "Which height levels do the data have?" #<-- keep the quotes " ... "
categories: data                 #<-- No quotes, comma separated tags
date:   2016-04-05 16:40:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

**CORDEX data:** The height level is part of the short variable name. For example, ta500 is  the air temperature at the 500 hPa pressure level.

**Before download with OPeNDAP:** Expand the dataset you need with "Show Files" and click on "OPENDAP". In the OPeNDAP Dataset Access Form look for lev and enable it. Click on "Get ASCII" and login. The lev array with the height levels will be listed.

**After download:** Use local software, for example ncdump, which is a command line tool belonging to [NetCDF software][NetCDF].

      ncdump -c filename.nc

The option -c causes ncdump to output header and coordinate arrays.


[NetCDF]: http://www.unidata.ucar.edu/software/netcdf/

