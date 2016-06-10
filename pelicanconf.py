#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ray Alez'
SITENAME = 'orangemind'
SITEURL = '' #

LOCALE = ('en_US.UTF-8')

LANG=('en_US')

PATH = 'content'

STATIC_PATHS = [
    'images',
    ]

IGNORE_FILES = ['.#*', '*draft*']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://orangemind.io'
FEED_ALL_ATOM = 'feeds/all.atom.xml' #None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

# FEED_RSS = 'feeds/all.rss.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Menu should be fiction, articles, 
MENUITEMS = [
    # ('Videos', 'http://lumiverse.io/series/orangemind'),
    # ('Fiction', 'http://fictionhub.io/user/rayalez'),
    ('About', '/about'),
    # ('Store', '/store'),
    # ('Essays', '/category/articles'),    

    # ('Browse Articles', '/browse'),    
]
#('Essays', '/essays'), ('Home', '/')
# ('Stories', '/stories'),

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 12

# ARTICLE_ORDER_BY = 'date'

SUMMARY_MAX_LENGTH = 128

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'post/{slug}'
ARTICLE_SAVE_AS = 'post/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

TAG_URL = 'tag/{slug}/'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# TAGS_URL = 'tags/'
# TAGS_SAVE_AS = 'tags/index.html'

# PAGINATION_PATTERNS = (
#     (1, '{base_name}/posts/', '{base_name}/index.html'),
#     (2, '{base_name}/posts/{number}/', '{base_name}/posts/{number}/index.html'),
#)

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'store','about','browse','browse-cards','projects') #'about',



THEME = "/home/ray/orangemind/themes/orangemind"

# Plugins
PLUGIN_PATHS = ['/home/ray/orangemind/pelican-plugins']
# PLUGINS = ['pdf']

# PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.include_code', 'liquid_tags.notebook', 'summary']

# EXTRA_HEADER = open('_nb_header.html').read() #.encode('utf-8')


