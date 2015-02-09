---
layout: post
title:  "Md5 fails or File gets downloaded over and over again"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

The md5 checksum does not match

Example error message:

    md5 failed!
    re-downloading...Downloading

Solution: use -p to preserve the file even if the md5 checksum doesn't match. Some institutions are known to alter the files after publication without updating their metadata, e.g. the checksum. In those cases it's impossible to know if the file was downloaded correctly. The -p flag does check the md5 and provides the result of that comparison, though it leaves the file as it was downloaded. We can't do anything else, you'll have to contact the author and ask for the checksum or blindly trust what you've downloaded.
