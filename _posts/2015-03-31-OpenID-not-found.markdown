---
layout: post                     #<-- don't touch
title:  "wget script stopped after inquiring the OpenID" #<-- keep the quotes " ... "
categories: wget                 #<-- No quotes, comma separated tags
date:   2015-03-31 15:30:00      #<-- current date and time
author: Torsten Rathmann         #<-- Replace with the name
---
 
    $ bash wget-20150331153950.sh &
    ...
    Please give your OpenID (Example: https://myserver/example/username) ? https://esgf-data.dkrz.de/esgf-idp/openid/myname

    [1]+  Stopped                 ./wget-20150331153950.sh

Don't send the script to the background with the ampersand at the end of the command. Instead run the script in the foreground (without "&" at the end).


