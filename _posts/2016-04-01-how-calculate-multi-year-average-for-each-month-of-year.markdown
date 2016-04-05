---
layout: post                     #<-- don't touch
title:  "How can I calculate a multi-year average for each month of year?" #<-- keep the quotes " ... "
categories: data                 #<-- No quotes, comma separated tags
date:   2016-04-01 19:20:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

A multi-year average for each month of year can easily be calculated with CDO ymonavg. Example:

      cdo splityear OH_Amon_ULAQ_rcp45_r1i1p1_196001-210012.nc OH_   # split into years
      cdo cat OH_1995.nc OH_1996.nc OH_1997.nc OH_1998.nc OH_1999.nc OH_2000.nc OH_2001.nc OH_2002.nc OH_2003.nc OH_2004.nc  OH_Amon_ULAQ_rcp45_r1i1p1_1995-2004.nc  # concatenate to a file containing 10 years
      cdo ymonavg OH_Amon_ULAQ_rcp45_r1i1p1_1995-2004.nc OH_average_over_1195-2004_ULAQ_rcp45_r1i1p1_Jan-Dec.nc  # calculate multi-year average for each month

More details are in the [CDO documentation][cdo].

[cdo]: https://code.zmaw.de/projects/cdo/embedded/index.html

