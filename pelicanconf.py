#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

SITE_AUTHOR = 'Svyatoslav Kubakh'
SITENAME = SITE_AUTHOR
BIO_TEXT = 'Web developer'
INDEX_DESCRIPTION = 'A backend software developer.'

TWITTER_USERNAME = 'realksar'

DOMAIN = 'kubakh.name'
SITEURL ='http://%s' % DOMAIN

PELICAN_URL = 'https://getpelican.com'

FOOTER_TEXT = '<h6 class="text-center copyright">© %d, %s. Powered by <a href="%s">Pelican</a>.</h6>'\
              % (datetime.now().year, SITE_AUTHOR, PELICAN_URL)

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/contacts/">Contacts</a>',
]

PATH = 'content'

TEMPLATE_PAGES = {page: page for page in ['404.html']}

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# LOCALE = ('en_US', 'en-US')

DIRECT_TEMPLATES = ['index', 'archives']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

CATEGORY_SAVE_AS = ''

FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ICONS_PATH = 'images/icons'

GOOGLE_FONTS = [
    'Nunito Sans:300,700',
    'Source Code Pro',
]

SOCIAL_ICONS = [
    ('https://github.com/svyatoslav-kubakh', 'My GitHub projects', 'fa-github'),
    ('https://linkedin.com/in/svyatoslav-kubakh', 'My Linkedin Profile', 'fa-linkedin'),
    ('https://facebook.com/svyatoslav.kubakh', 'My facebook page', 'fa-facebook'),
    ('https://twitter.com/%s/' % TWITTER_USERNAME, 'Twitter', 'fa-twitter'),
    ('/atom.xml', 'Atom Feed', 'fa-rss'),
]

THEME = 'themes/pneumatic'
THEME_COLOR = '#000000'

PLUGINS = ['pelican_webassets', 'neighbors', 'sitemap']


DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extra', 'images', 'cv']
EXTRA_PATH_METADATA = {
    'extra/%s' % file: {'path': file} for file in ['favicon.ico', 'robots.txt']
}


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
    },
    'exclude': {
        '404.html'
    }
}

GOOGLE_ANALYTICS = 'UA-59913034-1'
