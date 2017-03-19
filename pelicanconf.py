#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic config
AUTHOR = 'Dan Puttick'
SITENAME = 'Daniel Puttick'
SITEURL = 'http://danielputtick.com'
THEME = 'themes/crowsfoot'
PATH = 'content/'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['writing']
DIRECT_TEMPLATES = ['index']
TYPOGRIFY = True
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = False

# Turning off feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'https://www.github.com/dputtick'),
          ('Twitter', 'https://www.twitter.com/dputtick'),)

# Crowsfoot specific settings
SHOW_ARTICLE_AUTHOR = False
LICENSE_NAME = 'CC BY-NC'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc/4.0/'
GITHUB_ADDRESS = 'https://www.github.com/dputtick'
TWITTER_ADDRESS = 'https://www.twitter.com/dputtick'
MENUITEMS = []

# Uncomment following lines if you want document-relative URLs when developing
RELATIVE_URLS = True
