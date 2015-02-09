---
layout: post
title:  "The wget script does not trust the certificate of the server."
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

Solution: the script needs to be run with the -i option
certificate unknown : signals that the server does not trust the certificate issued by the MyProxy CA

Example error message:

    Connecting to test-datanode.jpl.nasa.gov|137.78.210.101|:443... connected.
    OpenSSL: error:14094416:SSL routines:SSL3_READ_BYTES:sslv3 alert certificate unknown Unable to establish SSL connection. download failed

* Solution: you might need to re-install the set of trusted ESGF certificates:
  * remove everything in the directory `~/.esg/*`
  * run the wget script to download a new set of trusted certificates
  * Solution: contact the ESGF users mailing list to notify the ESGF administrators there might be a problem with the server certificate

In a less common scenario it is possible that you might not have access to the VeriSign CA and therefore you cannot download the required files from rainbow.

To turn off the security checking create (or edit) the file `$HOME/.wgetrc` and add this line to the bottom of it: please note this is a security problem, since you will be sending your data to untrusted servers! Ask your Sysadmin about this procedure, you could have problems depending on your institutions security regulations

    check_certificate = off

This causes wget to send your personal ESGF certificate to pretty much anyone who asks for it.
