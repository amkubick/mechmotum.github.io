#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

LABNAME = 'Laboratorium of Marvelous Mechanical Motum'

# TODO : Theme puts the author's name below the logo, should put sitename (i.e.
# it assumes this is a blog).
AUTHOR = LABNAME
SITENAME = LABNAME
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

with open('config.yml', 'r') as config_file:
    config_data = yaml.load(config_file)

THEME = config_data['THEME_PATH']
# svbhack settings
# https://github.com/gfidente/pelican-svbhack/
#GOOGLE_ANALYTICS = ''
USER_LOGO_URL = 'https://objects-us-east-1.dream.io/mechmotum.github.io/bear-bicycle-480x480.png'
#DISQUS_SITENAME = ''
TAGLINE = 'A research group led by<br>Jason K. Moore'