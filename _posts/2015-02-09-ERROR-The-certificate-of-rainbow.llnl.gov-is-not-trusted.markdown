---
layout: post
title:  "ERROR: The certificate of 'rainbow.llnl.gov' is not trusted"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

This error is most commonly seen on MacOS systems, and is caused by wget not finding a standard CA certificate list or bundle. If wget was installed from MacPorts , the easiest solution to this is to install the 'curl-ca-bundle' package, and then edit either /usr/local/etc/wgetrc or ~/.wgetrc to contain the following line:

    CA_CERTIFICATE=/opt/local/share/curl/curl-ca-bundle.crt
