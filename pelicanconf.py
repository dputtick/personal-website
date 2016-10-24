#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic config
AUTHOR = 'Daniel Puttick'
SITENAME = 'Daniel Puttick'
SITEURL = 'https://danielputtick.com'
THEME = 'themes/crowsfoot'
PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'articles'
ARTICLE_PATHS = ['/articles']
TYPOGRIFY = True
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = False

# Turning off feeds
FEED_ALL_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Github', 'http://www.github.com/dputtick'),
          ('Twitter', 'http://www.twitter.com/dputtick'),)

# Crowsfoot specific settings
SHOW_ARTICLE_AUTHOR = False
LICENSE_NAME = 'CC BY-NC'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc/4.0/'
GITHUB_ADDRESS = 'https://www.github.com/dputtick'
TWITTER_ADDRESS = 'https://www.twitter.com/dputtick'

# Uncomment following lines if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
