---
layout: post
title:  "I can not log in with my pcmdi3 OpenID"
categories: login
date:   2015-04-29 17:40:00
author: Matthew Harris, Torsten Rathmann
---

I'm getting an error `Error: unable to resolve OpenID identifier.`

All pcmdi3 OpenID's `https://pcmdi3.llnl.gov/esgcet/myopenid/username` have been truncated. Unfortunately, they have not yet been purged from all nodes' databases, which means that if you click "Forgot Openid", it may display a pcmdi3 OpenID that you will be unable to login with it.

If you want to stay with PCMDI, create a new account on pcmdi9
[here][pcmdi9]. You may also feel free to create an account on any node in the
federation. A full list can be found [here][nodelist].

[pcmdi9]: https://pcmdi9.llnl.gov/esgf-web-fe/createAccount
[nodelist]: https://github.com/ESGF/esgf.github.io/wiki/Peer-Node-List
