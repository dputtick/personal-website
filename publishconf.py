#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Reconfigure for production
SITEURL = 'https://danielputtick.com'
RELATIVE_URLS = False

# Feed settings
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'  # Can maybe use category feeds to have a separate writing and journal feed
