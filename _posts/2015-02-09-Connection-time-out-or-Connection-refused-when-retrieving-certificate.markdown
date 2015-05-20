---
layout: post
title:  "Connection time out or Connection refused when retrieving certificate"
categories: download, wget
date: 2015-04-28 20:50:00
author: Matthew Harris, Torsten Rathmann
---

through wget script or MyProxyLogon

Example error message:

    Retrieving Credentials...MyProxy get failed. [Caused by: connect timed out]
    Use --help to display help.
    Certificate could not be retrieved
    
**Solution:** please make sure that your wget script can connect to a ESGF MyProxy server, for example on host esgf-data.dkrz.de, and port 7512 do the following:
  
    echo | telnet esgf-data.dkrz.de 7512

This is the output expected if you can connect successfully:

    Trying 136.172.30.96...
    Connected to esgf-data.dkrz.de.
    Escape character is '^]'.
    Connection closed by foreign host.

And this is an example for an output if you cannot make the connection:

    Trying 136.172.30.96...
    telnet: connect to address 136.172.30.96: Connection refused
    telnet: Unable to connect to remote host: Connection refused

If this is the case, you need to contact with your system administrator and tell him you need to access esgf-data.dkrz.de over port 7512 (TCP) (or the server and port you are trying to connect to).

