#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Give SConscripts access to all SDK python modules.
import sys
from os.path import join as path_join, dirname, realpath, abspath
DIR_PATH = abspath(dirname(realpath(__file__)))
SDK_DIR_PATH = dirname(DIR_PATH)

EXTRA_LIB_PATH = [
    path_join(SDK_DIR_PATH),
    path_join(SDK_DIR_PATH, 'lib'),
    path_join(SDK_DIR_PATH, 'lib', 'appengine'),
]
sys.path = EXTRA_LIB_PATH + sys.path
