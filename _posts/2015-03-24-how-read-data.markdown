---
layout: post                     #<-- don't touch
title:  "How can I read or process downloaded data?" #<-- keep the quotes " ... "
categories: data, CMIP5          #<-- No quotes, comma separated tags
date:   2015-03-24 17:40:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Data downloaded from ESGF are usually in NetCDF format. [NetCDF][NetCDF] is a header based binary format and can be read/processed by
* ncdump (conversion to ASCII) and ncview (simple graphics), i.e. command line tools belonging to [NetCDF software][NetCDF]
* Command line tools, e.g. [Climate Data Operators (CDO)][CDO] and [netCDF Operator (NCO)][NCO]: show, convert, add, subtract, split, merge, write NetCDF
* Command line graphics, e.g. [NCAR Command Language (NCL)][NCL]
* Some applications, e.g. Matlab and Ferret

An exception is NetCDF OPENDAP download. Here you can get ASCII CSV, i.e. readable text (Comma Separated Values), or dodc (binary OPENDAP data format). ASCII CSV can directly imported, for example, into Microsoft Excel.

[NetCDF]: http://www.unidata.ucar.edu/software/netcdf/
[CDO]: https://code.zmaw.de/projects/cdo/wiki/Cdo#Documentation
[NCO]: http://nco.sourceforge.net/
[NCL]: http://ncl.ucar.edu/

