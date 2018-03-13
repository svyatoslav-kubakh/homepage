#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Svyatoslav Kubakh'
DOMAIN = 'http://localhost:8000'
BIO_TEXT = 'Web developer'

SITE_AUTHOR = 'Svyatoslav Kubakh'
INDEX_DESCRIPTION = 'A fullstack software developer with core expertise in Python and related technologies.'

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/contact/">Contact</a>',
]

PATH = 'content'

TEMPLATE_PAGES = {page: page for page in ['404.html']}

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

DIRECT_TEMPLATES = ['index', 'archives']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARCHIVES_SAVE_AS = 'archive/index.html'

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ICONS_PATH = 'images'

GOOGLE_FONTS = [
    'Nunito Sans:300,700',
    'Source Code Pro',
]

SOCIAL_ICONS = [
    ('http://github.com/amitness', 'Browse my projects', 'fa-github'),
    ('https://np.linkedin.com/in/amitness', 'View Linkedin Profile', 'fa-linkedin'),
    ('/atom.xml', 'Atom Feed', 'fa-rss'),
]

THEME = "themes/pneumatic"

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets', 'neighbors', 'sitemap']


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra', 'images']
EXTRA_PATH_METADATA = {
    'extra/%s' % file: {'path': file} for file in ['favicon.ico', 'robots.txt']
}


# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
