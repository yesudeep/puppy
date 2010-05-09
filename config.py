#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join as path_join, realpath, abspath, dirname
import os
import sys
import yaml
import logging

logging.basicConfig(level=logging.DEBUG)

SDK_DIR_PATH = abspath(dirname(realpath(__file__)))
LIB_DIR_PATH = path_join(SDK_DIR_PATH, 'lib')

EXTRA_LIB_PATH = [
    LIB_DIR_PATH,
    path_join(LIB_DIR_PATH, 'subcommand'),
    path_join(LIB_DIR_PATH, 'appengine'),
]
sys.path = EXTRA_LIB_PATH + sys.path

CONFIG_FILE_NAME = 'config.yaml'
CONFIG_FILE_PATH = path_join(SDK_DIR_PATH, CONFIG_FILE_NAME)

CONFIG = yaml.load(open(CONFIG_FILE_PATH, 'r').read())

PROJECT_CONFIG_FILE_NAME = 'puppy.yaml'

IGNORE_PATTERNS = ['*~', '*.swp', '*.bak', '.DS_Store', '__MACOSX', '__MACOSX__', 'Thumbs.db', 'Desktop.ini']
WATCH_IGNORE_PATTERNS = IGNORE_PATTERNS + ['.*']
WATCH_PATHS = ['media']
REPOSITORY_IGNORE_PATTERNS = IGNORE_PATTERNS

FRAMEWORK_GAE_PYTHON = 'google-app-engine-python'
FRAMEWORK_TORNADO = 'tornado'

DEFAULT_APP_DIR = 'app'
DEFAULT_MEDIA_DIR = 'media'
DEFAULT_FRAMEWORK = FRAMEWORK_GAE_PYTHON
DEFAULT_SERVER_PORT = '8000'
DEFAULT_SERVER_HOST = '0.0.0.0'

DEFAULT_TEMPLATES_DEST_DIR = 'templates'
DEFAULT_MEDIA_DEST_DIR = 'public'
DEFAULT_MEDIA_SRC_DIR = 'media'

SCHEDULED_BUILD_DELAY = 2   # seconds

# Compass arguments
COMPASS = 'compass'
COMPASS_CONFIG = 'compass_config.rb'
COMPASS_ARGS = []
SASS_PATTERNS = ['.sass', '.css']

# Scons arguments.
SCONS = 'scons'
SITE_SCONS_DIR_PATH = path_join(SDK_DIR_PATH, 'site_scons')
SCONS_ARGS = ['-Q', '--site-dir=' + SITE_SCONS_DIR_PATH]
SCONS_BUILD_ARGS = SCONS_ARGS + ['-j', '4']
SCONS_CLEAN_ARGS = SCONS_ARGS + ['-c']

SERVER_SCRIPTS = {
    'google-app-engine': 'dev_appserver.py'
}

