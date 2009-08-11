#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import subprocess
import logging
import jsmin
from fnmatch import fnmatch
import SCons.Builder
import pickle
from functools import partial
from os.path import join as path_join, basename, dirname, abspath, realpath, splitext
from util import is_png, is_jpeg

# TODO:
# Add jslint
# Add jstestdriver

DIR_PATH = abspath(dirname(realpath(__file__)))
SDK_DIR_PATH = dirname(DIR_PATH)

YUI_COMPRESSOR_MINIFIED_SUFFIX = '-min'
JSMIN_MINIFIED_SUFFIX = '-jsmin'
HTML_MINIFIED_SUFFIX = '-min'

YUI_COMPRESSOR_JAR = path_join(SDK_DIR_PATH, 'tools', 'yuicompressor', 'yuicompressor.jar')
YUI_COMPRESSOR_OPTIONS = ' '.join(['--preserve-semi'])

HTML_MINIFIER_EXECUTABLE = path_join(SDK_DIR_PATH, 'tools', 'html_minify', 'html_minify.py')
HTML_MINIFIER = 'python ' + HTML_MINIFIER_EXECUTABLE

jsmin_minifier = jsmin.JavascriptMinify()



def makeCheetahCommand(target, source, env, for_signature):
    base = 'export PYTHONPATH="${TARGET.dir}" &&'
    base += 'cheetah fill --stdout --nobackup '
    sourceAndTarget = '$SOURCE >> $TARGET'

    #in_place_html_compaction('$TARGET')

    if 'PICKLE' in env:
        env.Depends(target, env['PICKLE'])
        return base + '--pickle $PICKLE ' + sourceAndTarget
    else:
        return base + sourceAndTarget

def pickle_function(target, source, env):
    for i in range(len(target)):
        print(target[i])
        pickle.dump(source[i].read(), open(str(target[i]), 'wb'))
    return None

def execute_command(command):
    #logging.info(command)
    subprocess.call(command, shell=True)

def optimize_jpeg(target, source, env):
    s = source[0]
    t = target[0]
    execute_command(' '.join(['jpegtran -optimize -progressive -outfile', str(t), str(s)]))
    return None

def optimize_png(target, source, env):
    s = str(source[0])
    t = str(target[0])
    if not t or t == s:
        logging.warning('Optimizing in-place')
        execute_command(' '.join(['optipng -q -o7', s]))
    else:
        execute_command(' '.join(['optipng -q -o7', s, '-out', t]))
    return None

def stitch_images(target, source, env, orientation='horizontal'):
    t = str(target[0])
    sources = ' '.join([str(s) for s in source])
    if orientation == 'vertical':
        append = '-append'
    else:
        append = '+append'
    execute_command(' '.join(['convert ', sources, append, t]))
    if is_png(t):
        execute_command(' '.join(['optipng -q -o7', t]))
    return None

def h_stitch_images(target, source, env):
    stitch_images(target, source, env, 'horizontal')

def v_stitch_images(target, source, env):
    stitch_images(target, source, env, 'vertical')

def suffix_emitter(target, source, env, suffix=''):
    target.pop()
    for s in source:
        filename, extension = splitext(str(s))
        target_filename = filename + suffix + extension
        target.append(target_filename)
    return target, source

yui_compressor_minify_emitter = partial(suffix_emitter, suffix=YUI_COMPRESSOR_MINIFIED_SUFFIX)
jsmin_minify_emitter = partial(suffix_emitter, suffix=JSMIN_MINIFIED_SUFFIX)

def html_minify(target, source, env):
    s = str(source[0])
    t = str(target[0])
    if env.get('HTML_MINIFY_INLINE', True):
        command = ' '.join([HTML_MINIFIER, '-j', '-o', t, s])
    else:
        command = ' '.join([HTML_MINIFIER, '-o', t, s])
    execute_command(command)
    return None

def yui_compressor_minify(target, source, env):
    for s in source:
        s = str(s)
        filename, extension = splitext(s)
        execute_command(' '.join(['java -jar',
            YUI_COMPRESSOR_JAR,
            YUI_COMPRESSOR_OPTIONS,
            s, '-o',
            filename + YUI_COMPRESSOR_MINIFIED_SUFFIX + extension]))
    return None

def jsmin_minify(target, source, env):
    for s in source:
        s = str(s)
        filename, extension = splitext(s)
        input_file = open(s, 'r')
        target_file = open(filename + JSMIN_MINIFIED_SUFFIX + extension, 'w')
        jsmin_minifier.minify(input_file, target_file)
        input_file.close()
        target_file.close()

def concatenate(target, source, env):
    target_file = open(str(target[0]), 'wb')
    for s in source:
        shutil.copyfileobj(open(str(s), 'rb'), target_file)
    target_file.close()
    return None

