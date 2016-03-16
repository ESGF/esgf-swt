---
layout: post                     #<-- don't touch
title:  "I can not process downloaded data" #<-- keep the quotes " ... "
categories: data                 #<-- No quotes, comma separated tags
date:   2016-03-16 15:30:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

There might be several reasons and solutions for this issue:

**Solution 1:** If you have downloaded the file with your browser's download manager (following a HTTPServer link), compare the checksum of your downloaded file with that in the metadata. In case the checksums are different, repeat the download since the file may have been changed during download. ESGF download scripts perform this check automatically.

**Solution 2:** Many data, especially CORDEX data, are stored in the format [NetCDF4][NetCDF] or compressed NetCDF4. Ensure that your local software can handle this relatively new data format.

[NetCDF]: http://www.unidata.ucar.edu/software/netcdf/


