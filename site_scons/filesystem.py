#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Portions Copyright (C) 2008  HappyChickoo.

import tarfile
import os
import os.path
import fnmatch
import hashlib
import dircache

from os.path import abspath, realpath, join as path_join

def __return(w):
    return w

def __return_true(w):
    return True

def __get_absolute_path(p):
    return os.path.abspath(os.path.realpath(p))

def __sort_wrapper(li):
    li.sort()
    return li


def get_dirs(root):
    for (path, subfolders, files) in os.walk(root):
        subfolders.sort()
        for folder in subfolders:
            yield os.path.join(path, folder)


def __walk_dir(root_directory, recursive=True, absolute_paths=True, file_filter_func=(lambda w: True), dir_filter_func=(lambda w: False)):
    """
    Walk (traverse) a directory tree using a generator.

    root_directory   - root directory.
    recursive        - traverse directories recursive
    file_filter_func - file filter callback function
    dir_filter_func  - directory filter callback function
    """
    #try:
    for item in dircache.listdir(root_directory):
        fullpath = path_join(realpath(abspath(root_directory)), item)
        #print fullpath
        if os.path.isfile(fullpath) and file_filter_func(fullpath):
            if absolute_paths:
                yield fullpath
            else:
                yield path_join(root_directory, item)
        elif os.path.isdir(fullpath) and not os.path.islink(fullpath):
            if dir_filter_func(fullpath):
                if absolute_paths:
                    yield fullpath
                else:
                    yield path_join(root_directory, item)
            if recursive:
                for subitem in walk_dir(fullpath, recursive, absolute_paths, file_filter_func, dir_filter_func):
                    yield subitem
    #except OSError:
    #    pass


def match_patterns(filename, patterns="*", delimiter=";"):
    patterns = set(patterns.split(delimiter))
    result = False
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            result = True
            break
    return result


def walk_dir(root, patterns='*', single_level=False, yield_folders=False, filter_func=None, depth=0, yield_absolute_paths=False, pattern_delimiter=';', sort_files=True):
    """
    Original all_files by
    Robin Parmar, Alex Martelli

    Modifications by Yesudeep Mangalapilly:
    The original function definition:
        - did not allow for filtering using a callback function
        - did not yield directories along with non-* pattern matched files
        - did not allow using a custom delimiter for the patterns
        - did not remove duplicate patterns
        - did not allow a choice between yielding absolute and relative paths
        - did not allow a choice between sorted and unsorted walking
    #todo    - did not allow to choose how deep to go into subfolders
    """
    # Expand patterns from delimiter-separated string to list and remove dups
    # to save processing time.
    patterns = set(patterns.split(pattern_delimiter))
    if not filter_func:
        filter_func = __return_true
    if yield_absolute_paths:
        absolute_path_func = __get_absolute_path
    else:
        absolute_path_func = __return

    if sort_files:
        sort_func = __sort_wrapper
    else:
        sort_func = __return

    #level = 0
    for (path, subfolders, files) in os.walk(root):
        # We store an is_folder boolean flag along with the filename
        # so we won't need to call os.path.isdir() again because
        # we already know which filenames belong to folders and we need only
        # identify them somehow.  So we trade a bit more memory for speed.
        files = zip(files, [False] * len(files))
        if yield_folders:
            subfolders = zip(subfolders, [True] * len(subfolders))
            files.extend(subfolders)
        sort_func(files)
        for (name, is_folder) in files:
            full_path = os.path.join(path, name)
            if filter_func(full_path):
                if is_folder: #os.path.isdir(full_path): # Why FS check again?
                    yield absolute_path_func(full_path)
                else:
                    for pattern in patterns:
                        if fnmatch.fnmatch(name, pattern):
                            yield absolute_path_func(full_path)
                            break
        #level = level + 1
        #if level == depth:
        #    break
        if single_level:
            break


def make_tar(folder_to_backup, dest_folder, compression='bz2'):
    """
    Ed Gordon, Ravi Teja Bhupatiraju
    """
    if compression:
        dest_ext = '.' + compression
    else:
        dest_ext = ''
    arcname = os.path.basename(folder_to_backup)
    dest_name = '%s.tar%s' % (arcname, dest_ext)
    dest_path = os.path.join(dest_folder, dest_name)
    if compression:
        dest_cmp = ':' + compression
    else:
        dest_cmp = ''
    out = tarfile.TarFile.open(dest_path, 'w'+dest_cmp)
    out.add(folder_to_backup, arcname)
    out.close()
    return dest_path


def make_dir(newdir, mode=os.makedirs.func_defaults[0]):
    """works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well

    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/82465

    You can use os.makedirs() instead as well.
    """
    os.makedirs(newdir, mode=mode)
    # Trent Mick's version
    #if os.path.isdir(newdir):
    #    pass
    #elif os.path.isfile(newdir):
    #    raise OSError("a file with the same name as the desired " \
    #                  "dir, '%s', already exists." % newdir)
    #else:
    #    (head, tail) = os.path.split(newdir)
    #    if head and not os.path.isdir(head):
    #        make_dir(head)
    #    #print "make_dir %s" % repr(newdir)
    #    if tail:
    #        os.mkdir(newdir)

def get_file_hash(path, crypto_service=hashlib.sha1):
    return crypto_service(file(path, 'rb').read()).hexdigest()

