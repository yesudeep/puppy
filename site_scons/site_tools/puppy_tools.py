#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SCons.Builder import Builder
from SCons.Action import Action
from builders import yui_compressor_minify, \
        yui_compressor_minify_emitter, \
        jsmin_minify, \
        jsmin_minify_emitter, \
        concatenate, \
        optimize_png, \
        optimize_jpeg, \
        makeCheetahCommand, \
        pickle_function
import pickle

cheetahBuilder = Builder(generator=makeCheetahCommand, src_suffix='.tmpl', single_source = True)
pickleBuilder = Builder(action = pickle_function, suffix='.pkl')

def generate(env):
    env.Append(BUILDERS = {
        'Concatenate': env.Builder(action=Action(concatenate, "Concatenating into '$TARGET' using '$SOURCE'")),
        'OptimizePNG': env.Builder(action=Action(optimize_png, "Optimizing PNG '$TARGET' from '$SOURCE'")),
        'JsminMinify': env.Builder(action=Action(jsmin_minify, "Minifying (JSMin) '$TARGET' from '$SOURCE'"), emitter=jsmin_minify_emitter),
        'YuiCompressorMinify': env.Builder(action=Action(yui_compressor_minify, "Minifying (YUICompressor) '$TARGET' from '$SOURCE'"), emitter=yui_compressor_minify_emitter),

        'OptimizeJPEG': env.Builder(action=Action(optimize_jpeg, "Optimizing JPEG '$TARGET' from '$SOURCE'")),
        'OptimizeJPG': env.Builder(action=Action(optimize_jpeg, "Optimizing JPEG '$TARGET' from '$SOURCE'")),

        'Cheetah': cheetahBuilder,
        'Pickle': pickleBuilder,
    })

def exists(env):
    return env.Detect('optipng') and env.Detect('jpegtran') and env.Detect('java') and env.Detect('cheetah')

