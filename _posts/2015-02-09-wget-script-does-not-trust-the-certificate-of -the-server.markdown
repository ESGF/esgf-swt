---
layout: post
title:  "The wget script does not trust the certificate of the server"
categories: wget
date: 2015-04-01 21:20:00
author: Matthew Harris, Torsten Rathmann
---

Example error message:

    Self-signed certificate encountered.

Further example error message:

    Connecting to test-datanode.jpl.nasa.gov|137.78.210.101|:443... connected.
    OpenSSL: error:14094416:SSL routines:SSL3_READ_BYTES:sslv3 alert certificate unknown 
    Unable to establish SSL connection. download failed

"Certificate unknown" signals that the server does not trust the certificate issued by the MyProxy CA (Certification Authority)

* Solution: the script needs to be run with the -i option. 

    bash wget-###############.sh -i

* Solution: you might need to re-install the set of trusted ESGF certificates:
  * remove everything in the directory `~/.esg/*`
  * run the wget script to download a new set of trusted certificates

* Solution: contact the ESGF users mailing list to notify the ESGF administrators there might be a problem with the server certificate

