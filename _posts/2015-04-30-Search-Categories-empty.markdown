---
layout: post                     #<-- don't touch
title:  "I don't get search results regardless what I do" #<-- keep the quotes " ... "
categories: search               #<-- No quotes, comma separated tags
date:   2015-04-30 21:30:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---

Outside China this issue is hardly known. ESGF Search via portal uses Google routines. The Chinese government has these routines blocked, thus "search" toolbar in all ESGF portals (index nodes) can not work normally. 

**Solution 1: Circumvent the Big Firewall**

Google has many IP addresses. Not all of these IP addresses have been blocked but its domain name has been linked to a wrong IP address. As a consequence, users inside China can't touch the "real" Google. Conversely, if the users can touch one unblocked "real IP address" of Google, they add this unblocked "real IP address" to their hosts file, and then they can normally use the ESGF Search toolbar.

These little tricks have been discussed in certain Chinese blogs. Ask your Chinese colleagues.

**Solution 2: Query the search index using facets in the URL**

Instead of the Search form you may use [ESGF URL-based search][ESGF_Search_REST_API]. The basic URL for this search service is e.g. `http://esgf-data.dkrz.de/esg-search/search?`. To select some specific data please add facets to the search URL, e.g.:

     http://esgf-data.dkrz.de/esg-search/search?project=CMIP5&institute=MPI-M&variable=tas&experiment=historical

You can also generate a wget script using this search service:

     http://esgf-data.dkrz.de/esg-search/wget?project=CMIP5&institute=MPI-M&variable=tas&experiment=historical

**Solution 3: Search ESGF data nodes directly**

ESGF data nodes have a catalog, the THREDDS catalog. You can visit the corresponding web pages, e.g. http://pcmdi9.llnl.gov/thredds/, and perform even data downloads. Links to the THREDDS catalogs of the European data nodes can be found [here][IS-ENES data nodes].

[ESGF_Search_REST_API]:https://github.com/ESGF/esgf.github.io/wiki/ESGF_Search_REST_API
[IS-ENES data nodes]: https://verc.enes.org/data/is-enes-data-infrastructure/enes-data-nodes


