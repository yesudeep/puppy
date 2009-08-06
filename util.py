#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import logging
import os
import subprocess
import yaml
import sys
import shutil
from fnmatch import fnmatch
from os.path import join as path_join, basename
from QueryDict import QueryDict

def execute_command(program, arguments, echo=True):
    if not arguments:
        arguments = []
    command = program + ' ' + ' '.join(arguments)
    if echo:
        logging.info(command)
    subprocess.call(command, shell=True)

def match_patterns(pathname, patterns):
    retval = False
    for pattern in patterns:
        if fnmatch(pathname, pattern):
            retval = True
            break
    return retval

def remove_dir(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def filter_files(files, ignores=[], allow_patterns=['*'], ignore_patterns=[]):
    files = set(files).difference(set(ignores))
    result = []
    for f in files:
        bf = basename(f)
        if match_patterns(basename(bf), allow_patterns) and not match_patterns(bf, ignore_patterns):
            result.append(f)
    return result

def minifiables(files, ignores=[], allow_patterns=['*.js', '*.css'], ignore_patterns=['*.min.js', '*.min.css', '*-min.js', '*-min.css']):
    return filter_files(files, ignores, allow_patterns, ignore_patterns)


def get_project_config(project_dir=None):
    #if not project_dir:
    #    project_dir = os.getcwd()
    config_path = path_join(project_dir, config.PROJECT_CONFIG_FILE_NAME)
    try:
        project_config = yaml.load(open(config_path, 'r').read())
        if not project_config:
            logging.warning("Using defaults. Project configuration file is empty -- %s" % config_path)
            project_config = {}
        return QueryDict(project_config)
    except IOError:
        if not os.path.exists(config_path):
            logging.error("Project configuration file not found -- %s" % config_path)
        sys.exit(1)


