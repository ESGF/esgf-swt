---
layout: post
title:  "In which sequence are the data ordered inside a NetCDF file?"
categories: data
date: 2015-12-21 16:30:00
author: Torsten Rathmann
---

The Network Common Data Format (NetCDF) is a binary data format for the exchange of scientific data and consists of a header and a data part. The header contains beside attributes the structure of the data part. The data itself are deposited in arrays in the data part. This enables quick access.

Data variables are defined by means of coordinate variables, for example the near-surface air temperature tas is defined as a function of time, latitude and longitude.

      tas(time, lat, lon)

Inside a data array the data are ordered as follows:

Mathematically, the order inside the array corresponds to the lexical order of its index set. The index set of the data variable is the cartesian product of the index sets of the coordinate variables, for example

I(tas) = I(time) X I(lat) X I(lon)

The definition of the data variable in the file header contains manner and sequence of the coordinate variables.

For the example tas and in easy English: The first value in the tas array is the value for the first time, first lat and first lon. The second value is that for first time, first lat and second lon. Then the tas values for the other longitudes follow. If the number of longitudes is only 2, now the value for first time, second lat and first lon follows. If the number of latitudes is also 2, the first tas value for the second time appears in position 5.

```
| 1 1 1 | 1 1 2 | 1 2 1 | 1 2 2 | 2 1 1 | ...
```

Technically spoken, the values are written to the array in a nested loop. The innermost loop is that for lon, the outermost for time and lat in the middle.
