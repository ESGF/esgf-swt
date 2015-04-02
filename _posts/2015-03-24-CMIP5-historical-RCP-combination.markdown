---
layout: post                     #<-- don't touch
title:  "May CMIP5 historical and RCP data be combined to one long time series?" #<-- keep the quotes " ... "
categories: data, CMIP5          #<-- No quotes, comma separated tags
date:   2015-03-24 17:50:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Yes, if you select matching ensemble members. Look into the header of the RCP data file: The attributes *parent_experiment_id* and *parent_experiment_rip* name the right ensemble member for combination. [Background information][IS-ENES CMIP5 data structure] 

[IS-ENES CMIP5 data structure]: https://verc.enes.org/community/projects-and-partnerships/projects/cmip5/datastructure
