#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'LBJ'
SITENAME = u'\u9006\u6d41\u800c\u4e0a'
SITEURL = 'http://www.goingto.top'

PATH = 'content'
PAGE_PATHS = ['pages']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'zh_CN': '%Y-%m-%d %H:%M:%S', }

LOCALE = ('zh_CN.utf8', )
DEFAULT_LANG = u'zh_CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
'''
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
'''

# Social widget
SOCIAL = (('Github', 'https://github.com/hustlbj'),
		('CSDN', 'http://blog.csdn.net/hustsselbj'),)

DEFAULT_PAGINATION = 8

PATH = 'content'
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
		'images/favicon.ico': {'path': 'favicon.ico'}
}
DISPLAY_PAGES_ON_MENU = True
DISQUS_SITENAME = True
#ARTICLE_URL = {'articles/{slug}.html'}
#ARTICLE_SAVE_AS = {'articles/{slug}.html'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/ec2-user/pelican-themes/bootstrap2-dark"

