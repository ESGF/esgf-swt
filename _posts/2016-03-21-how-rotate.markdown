---
layout: post                     #<-- don't touch
title:  "How can CORDEX data on a grid with rotated poles be rotated back?" #<-- keep the quotes " ... "
categories: data                 #<-- No quotes, comma separated tags
date:   2016-03-21 14:30:00      #<-- current date and time
author: Torsten Rathmann, Bryan Lawrence, Matthias Büchner #<-- Replace with the name
---

Some native CORDEX grids have rotated poles, for example the native European domains EUR-44 and EUR-11. They can easily be regridded (rotated back).

**Solution 1: Use interpolated data** 

Interpolated data are in the domains with "i" at the end, e.g. EUR-44i. These data already have a grid which has been rotated back.

**Solution 2: Use cf-python**

cf-python uses the ESMF regridding library as its regridding engine, and currently provides first-order conservative (by default) or bilinear spherical regridding. CORDEX data are usually NetCDF/CF compliant; so cf-python only needs the following commands:

     import cf
     rotated_fields = cf.read('rotated_pole_file.nc')
     unrotated_field = cf.read('unrotated_latlon_file.nc')
     regridded_fields = rotated_fields.regrids(unrotated_field)

The rotated_fields may have more dimensions thans just rotated latitude (X) and rotated longitude (Y). The above command will regrid each X-Y slice and so regridded_fields will have the same rank as the original.

More details in the [cf-python documentation][cf-python].

**Solution 3: Use CDO**

Climate Data Operator (CDO) offer [different ways of regridding][zmaw discussion], for example cdo rotuvb can perform a backward transformation of velocity components U and V from a rotated spherical system to a geographical system. More details in the [CDO documentation][cdo].

[cf-python]: http://cfpython.bitbucket.org/docs/latest/generated/cf.Field.regrids.html
[zmaw discussion]: https://code.zmaw.de/boards/2/topics/1283
[cdo]: https://code.zmaw.de/projects/cdo/embedded/index.html

