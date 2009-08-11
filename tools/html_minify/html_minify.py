#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Basic HTML Minifier
# Also minifies inline scripts using jsmin.

import re
import sys
import optparse
from jsmin import jsmin

SCRIPT_TAG = re.compile(r'(<[\s]*script[^>]*>[\s\S]*?<\/[\s]*script[\s]*>)', re.IGNORECASE | re.MULTILINE)
SCRIPT_TAG_PARTS = re.compile(r'<[\s]*script(?P<attributes>[^>]*)>[\s]*(?P<data>[\s\S]*?)<\/[\s]*script[\s]*>', re.IGNORECASE | re.MULTILINE)

def lstrip_script_content(content):
    lines = content.splitlines()
    return '\n'.join([line.lstrip() for line in lines])

def html_minify(html, minify_inline_javascript=False):
    content = SCRIPT_TAG.split(html, re.IGNORECASE | re.MULTILINE)
    func = lstrip_script_content
    if minify_inline_javascript:
        func = jsmin
    new_content = []
    for c in content:
        if SCRIPT_TAG.match(c):
            d = SCRIPT_TAG_PARTS.match(c).groupdict()
            attr = d['attributes'].strip()
            if attr:
                attr = ' ' + attr
            new_content.append('<script' + attr + '>' + func(d['data']) + '</script>')
        else:
            new_content.append(''.join([line.strip() for line in c.splitlines()]))
    content = ''.join(new_content)
    return content

def minify_file(in_name, out_name=None, minify_inline_javascript=False):
    # Don't handle exceptions.  Let Python bomb with the right messages on failure.
    in_file = open(in_name, 'r')
    content = html_minify(in_file.read(), minify_inline_javascript)
    in_file.close()
    if out_name:
        out_file = open(out_name, 'w')
    else:
        out_file = sys.stdout
    out_file.write(content)
    out_file.write('\n')
    out_file.close()

def main():
    parser = optparse.OptionParser(usage='%prog [options] files...')
    parser.add_option('-j', '--jsmin', dest='minify_inline_javascript', help='minify inline javascript as well', action='store_true')
    parser.add_option('-i', '--in-place', dest='in_place', help='replace the source files with minified files', action='store_true')
    parser.add_option('-o', '--output', dest='output_file', help='output file', metavar="FILE")
    (options, args) = parser.parse_args()

    options.minify_inline_javascript = bool(options.minify_inline_javascript)
    if options.in_place:
        if len(args):
            for arg in args:
                minify_file(arg, arg, options.minify_inline_javascript)
        else:
            parser.print_help()
            sys.exit(1)
    elif options.output_file:
        if len(args):
            minify_file(args[0], options.output_file, options.minify_inline_javascript)
        else:
            parser.print_help()
            sys.exit(1)
    else:
        if len(args):
            minify_file(args[0], None, options.minify_inline_javascript)
        else:
            parser.print_help()
            sys.exit(1)


if __name__ == '__main__':
    main()

