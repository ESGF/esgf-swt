---
layout: post
title:  "Connection time out or Connection refused when retrieving certificate?"
categories: wget
date: 2015-02-09 14:28:21
author: Matthew Harris
---

through wget script or MyProxyLogon

Example error message:

    Retrieving Credentials...MyProxy get failed. [Caused by: connect timed out]
    Use --help to display help.
    Certificate could not be retrieved
    
Solution: please make sure that your wget script can connect to the ESGF MyProxy server, for example on host "ipcc-ar5.dkrz.de" and port "7512" do the following:
  
    echo | telnet ipcc-ar5.dkrz.de 7512

This is the output expected if you can connect successfully:

    Trying 136.172.30.10... 
    Connected to bd110.dkrz.de (136.172.30.10). 
    Escape character is '^]'. Connection closed by foreign host.

And this is the output expected if you cannot make the connection:

    Trying 136.172.30.10... 
    telnet: connect to address 136.172.30.10: Connection refused
    telnet: Unable to connect to remote host: Connection refused
    
If this is the case, you need to contact with your system administrator and tell him you need to access ipcc-ar5.dkrz.de over port 7512 (TCP) (or the server and port you are trying to connect to). (see node port matrix )
