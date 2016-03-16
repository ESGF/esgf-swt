---
layout: post
title:  "Unsupported major.minor version 51.0"
categories: wget
date: 2016-03-16 10:30:00
author: Torsten Rathmann
---

Error message:

     Retrieving Credentials...Exception in thread "main" java.lang.UnsupportedClassVersionError: esg/security/myproxy/MyProxyConsole : Unsupported major.minor version 51.0
	at java.lang.ClassLoader.defineClass1(Native Method)
	at java.lang.ClassLoader.defineClass(ClassLoader.java:643)
	at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
	at java.net.URLClassLoader.defineClass(URLClassLoader.java:277)
	at java.net.URLClassLoader.access$000(URLClassLoader.java:73)
	at java.net.URLClassLoader$1.run(URLClassLoader.java:212)
	at java.security.AccessController.doPrivileged(Native Method)
	at java.net.URLClassLoader.findClass(URLClassLoader.java:205)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:323)
	at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:294)
	at java.lang.ClassLoader.loadClass(ClassLoader.java:268)
     Could not find the main class: esg.security.myproxy.MyProxyConsole. Program will exit.
     Certificate could not be retrieved

Two solutions are possible in case of this Java issue:

**Solution 1:** Run the wget script with the -H option.

     bash wget-################.sh -H

Authentication will be tried without certificates then.

**Solution 2:** Install Oracle Java 1.7 or newer and add it to your environment (define JAVA_HOME etc.). The wget script can usually be used without options then.

