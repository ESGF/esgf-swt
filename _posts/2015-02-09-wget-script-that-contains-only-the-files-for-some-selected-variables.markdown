---
layout: post
title:  "How can I create a wget script that contains only the files for some selected variables?"
categories: wget
date: 2015-02-09 12:02:21
author: Matthew Harris
---

Please note: the procedure used to generate a wget script that only contains files for a specified variable has changed with the latest ESGF release. Not all ESGF portals have upgraded to the latest version of the software yet. If in doubt, please use the pcmdi9.llnl.gov or esg-datanode.jpl.nasa.gov portals.

Please follow these steps:

1. Use any of the facet constraints on the left to return a set of matching datasets (each dataset containing many files, possibly for more than one variable).
Add the datasets you are interested in, one at a time, to your Data Cart
2. Click on "Data Cart" to view your datasets, and "Show Files" to show the files in each dataset.
3. If the datasets contain more files than you need (for other variables), you can use the text box on top to sub-select the files by a matching string. For example, enter "tas" to only sub-select those files that contain "tas" in their filename. Another option is to restrict to a specific variable by entering for example "variable:tas". In either case, you must click the "Search" button for the constraint to take effect.
4. Click on the radio button "Filter Over Text".
5. Finally, click on each dataset "WGET" link, or on the global "WGET All Selected" link, to generate a wget script containing only those files.
