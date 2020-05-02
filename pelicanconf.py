#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Configure generation
THEME = 'theme'
PATH = 'content/'
TYPOGRIFY = True
PORT = 8000
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ['.git']
OUTPUT_PATH = 'docs/'

# Configure site
AUTHOR = 'Dan Puttick'
SITENAME = 'Dan Puttick'
SITEURL = 'http://danielputtick.com'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Layout
DIRECT_TEMPLATES = ['index']
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_PAGINATION = False

# Categories
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'journal'
CATEGORY_URL = '{slug}.html'
CATEGORY_SAVE_AS = '{slug}.html'

# Articles
ARTICLE_PATHS = ['journal', 'writing']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'

# Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Turn off things we don't need
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''

# Feed settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social links
GITHUB_ADDRESS = 'https://www.github.com/dputtick'
TWITTER_ADDRESS = 'https://www.twitter.com/dputtick'

# Specifically for local development
RELATIVE_URLS = True
