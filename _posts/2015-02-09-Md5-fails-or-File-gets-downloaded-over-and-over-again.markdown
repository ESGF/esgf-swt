---
layout: post
title:  "sha256 or md5 fails or file gets downloaded over and over again"
categories: wget
date: 2016-03-16 14:30:00
author: Torsten Rathmann, Matthew Harris
---

The sha256 or md5 checksum does not match.

Example error message:

     sha256 failed!
     re-trying...Downloading

ESGF Wget scripts contain a checksum for each download file. After download, the checksum is again calculated on the user's local machine and compared with that in the script. In case of a mismatch the downloaded file is deleted. This shall prevent unwanted bitstream changes during download. 

This error message is usually thrown if the expected software to calculate the checksum is locally not installed. Seldom, even though this should not happen, data have been altered by staff without updating the corresponding metadata, e.g. version number and checksum. In this case deletion of the downloaded file and re-download are completely useless but the download script cannot automatically know this.

**Solution 1:** If you received the message "command not found", install the missing SHA or MD5 software. This often concerns Mac users since the command line tools sha256sum and md5sum are not standard under Mac OS X. The easiest way to install the missing tools is utilization of Homebrew:

     brew install sha2
     brew install md5sha1sum

Homebrew itself can be installed with the command

     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

**Solution 2:** Use the option -p to preserve the downloaded files from beeing deleted and to suppress re-download.

     bash wget-################.sh -p 

If the -p option is set, the script does check the sha256 or md5 checksum and provides the result of that comparison, though it leaves the file as it was downloaded. 

Hint: If you want to verify a proper download anyway, you may download the file twice and compare the two files. Exactly the same bit change during both downloads is very unlikely. The first download file has to be renamed before you can start the second download since ESGF download scripts are able to recognise already downloaded files by their name.

**Solution 3:** Contact the ESGF support. The responsible data node administrator will update the checksum then.

