---
layout: post
title:  "md5 fails or file gets downloaded over and over again"
categories: download, wget
date: 2015-06-09 14:45:00
author: Torsten Rathmann, Matthew Harris
---

The md5 checksum does not match.

Example error message:

    md5 failed!
    re-downloading...Downloading

ESGF download scripts ("wget scripts") contain a md5 checksum for each download file. After download, the checksum is again calculated on the user's local machine and compared with that in the script. In case of a mismatch the downloaded file is deleted. This shall prevent unwanted bitstream changes during download. Even though this should not happen, data have sometimes been altered by staff without updating the corresponding metadata, e.g. version number and checksum. In this case deletion of the downloaded file and re-download are useless but the download script cannot automatically know this.

**Solution 1:** Use the option -p to preserve the downloaded files from beeing deleted and to suppress re-download.

     bash wget-################.sh -p 

If the -p option is set, the script does check the md5 and provides the result of that comparison, though it leaves the file as it was downloaded. 

Hint: If you want to verify a proper download anyway, you may download the file twice and compare the two files. Exactly the same bit change during both downloads is very unlikely. The first download file has to be renamed before you can start the second download since ESGF download scripts are able to recognise already downloaded files by their name.

**Solution2:** Contact the ESGF support. The responsible data node administrator will update the checksum then.

