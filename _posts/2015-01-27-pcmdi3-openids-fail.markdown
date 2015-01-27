---
layout: post
title:  "PCMDI3 openid failing"
date:   2015-01-27 09:05:12
categories: jekyll update
---

###Question
I can not log in with my pcmdi3 opedid?  `https://pcmdi3.llnl.gov/esgcet/myopenid/username` I'm getting an error `Error: unable to resolve OpenID identifier.`.

###Anwser
All pcmdi3 openids have been truncated. Unfortunately, they have not yet been
purged from all nodes' databases, which means that if you click `forgot openid` it
may display a pcmdi3 openid that you will be unable to login with it.

###Solution
If you want to stay with pcmdi, create a new account on pcmdi9
[here][pcmdi9]. You may also feel free to create an account on any node in the
federation. A full list can be found [here][nodelist].


[pcmdi9]: https://pcmdi9.llnl.gov/esgf-web-fe/createAccount
[nodelist]: https://github.com/ESGF/esgf.github.io/wiki/Peer-Node-List
