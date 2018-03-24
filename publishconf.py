#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
import pelicanconf

SITEURL = 'http://anotherdatum.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "anotherdatum"
GOOGLE_ANALYTICS = "UA-83684090-1"

[item for item in MENUITEMS if item[1] == pelicanconf.SITEURL][0][1] = SITEURL