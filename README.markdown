Introduction
============
Puppy is a (driver) meta-framework for Python Web developers.

Bugs or enhancements?
---------------------
Please file them at the [issue tracker][issue_tracker].

Bundled Software:
-----------------
* [subcommand][subcommand]
* [YUI Compressor][yui_compressor]
* [JSLint][jslint]
* [JSMin][jsmin]
* [Mozilla Rhino JavaScript Engine][rhino]

Installation Requirements
-------------------------
* Linux
* [Java 1.6][java_jre]
* [Ruby 1.8][ruby_lang]
* [Python 2.5 or Python 2.6][python_lang]
* [pyinotify][pyinotify]
* [PyYAML][pyyaml]
* [Compass][compass] and the [Compass 960 plugin][compass_960]
* [Jinja2][jinja2]

Installing on Ubuntu:
=====================

Install the dependencies first:

    $ sudo easy_install pyinotify pyyaml Jinja2
    $ sudo aptitude install sun-java6-jre

Follow the [installation instructions][compass_installation] for Compass
and the Compass 960 plugin.


Notes:
======
Please make sure you have Java 1.6 JRE installed and setup for use.
Some Linux systems come with OpenJDK versions of Java.  YUI Compressor
fails to generate minified files when used with these versions of Java.
To configure Ubuntu to use Java 1.6 you can use the `update-java-alternatives` command.

Please see `update-java-alternatives --help`.

[jinja2]: http://jinja.pocoo.org/2/
[compass]: http://compass-style.org/
[compass_installation]: http://wiki.github.com/chriseppstein/compass
[compass_960]: http://github.com/chriseppstein/compass-960-plugin/
[lighthouse_issue_tracker]: http://happychickoo.lighthouseapp.com/projects/34621-puppy
[issue_tracker]: http://github.com/yesudeep/puppy/issues
[rhino]: http://www.mozilla.org/rhino/
[jsmin]: http://crockford.com/javascript/jsmin
[jslint]: http://jslint.com
[yui_compressor]: http://developer.yahoo.com/yui/compressor/
[python_lang]: http://www.python.org/
[ruby_lang]: http://www.ruby-lang.org/
[java_jre]: http://java.sun.com/
[pyinotify]: http://trac.dbzteam.org/pyinotify
[pyyaml]: http://pyyaml.org/
[subcommand]: http://github.com/anandology/subcommand/

