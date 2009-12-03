Introduction
============
Puppy is a (driver) meta-framework for Python Web developers.

You've manually run minification tools, image optimizers,
css generators, JavaScript unit testing tools, and other tools
when deploying your Website, haven't you?

Puppy automates all this for you.

It uses many tools to make it easier for you to develop a production
quality Website. For example, if you modify a CSS file in your code, Puppy
detects the change and builds a minified version alongside your
untouched CSS **as you work**.  And this happens transparently in
the background, so there is really no reason to issue build commands
repeatedly.

Sit back and let Puppy take over all that for you.

What can Puppy do for you?
--------------------------
1. Minify CSS/JavaScript files.
2. Optimize PNG/JPEG images.
3. Convert SASS to optimized CSS.
4. Run JavaScript unit tests in the background.
5. Run your framework development server.
6. Create project templates for your favorite framework.
7. Build-time templates that compile into Web templates that will be rendered at runtime.
   (e.g., you can prefill your Web templates at *build-time* using Cheetah, compact markup, etc.).
8. Stitching multiple images together to create one image to reduce the number of requests.

And, of course, *wag*.

Do I have a dog?
---------------
Yep, I've got two lovely dogs.  One's a brown mongrel.
The other one's a black Labbie.

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

* Linux/Mac OS X
* [Java 1.6][java_jre]
* [Ruby 1.8][ruby_lang]
* [Python 2.5 or Python 2.6][python_lang]
* [pyinotify][pyinotify] (Linux only)
* [PyYAML][pyyaml]
* [Compass][compass] and the [Compass 960 plugin][compass_960]
* [SCons][scons]
* [Jinja2][jinja2]
* [OptiPNG][optipng]
* [JpegTran][jpegtran]
* [PNGCrush][pngcrush]
* [Cheetah][cheetah]
* [ImageMagick][imagemagick]
* [JpegOptim][jpegoptim]

Installing on Ubuntu:
=====================

You will need the python development packages for your system 
version of Python so please also install the python-dev package:

    $ sudo aptitude install python-setuptools python-dev build-essential automake autoconf libtool intltool


Install the dependencies first:

    $ sudo easy_install pyinotify pyyaml Jinja2 Cheetah
    $ sudo aptitude install git-core git-email git-load-dirs git-doc \
        sun-java6-jre optipng pngcrush libjpeg-progs imagemagick scons

Python 2.5 Notes:
-----------------

If you're using a fairly recent version of Ubuntu Linux, Python 2.5 might
not be installed already.  You can install it using:

    $ sudo aptitude install python2.5 python2.5-dev python2.5-setuptools

When you're using a web framework that works only with Python 2.5
you might need to install one or more of the easy_install packages in addition
to the above like so:

    $ sudo easy_install-2.5 Jinja2

Java Installation Notes:
------------------------
Please make sure you have Java 1.6 JRE installed and setup for use.
Some Linux systems come with OpenJDK versions of Java.  YUI Compressor
fails to generate minified files when used with these versions of Java.
To configure Ubuntu to use Java 1.6 you can use the `update-java-alternatives` command.

Please see `update-java-alternatives --help`.

Typing the following command should not show you "OpenJDK" in the output:

    $ java -version
    java version "1.6.0_14"
    Java(TM) SE Runtime Environment (build 1.6.0_14-b08)
    Java HotSpot(TM) 64-Bit Server VM (build 14.0-b16, mixed mode)

    $ java -version 
    java version "1.6.0_15"
    Java(TM) SE Runtime Environment (build 1.6.0_15-b03)
    Java HotSpot(TM) 64-Bit Server VM (build 14.1-b02, mixed mode)


Generally, you would want to do something along the lines of:

    $ update-java-alternatives --list
    java-6-openjdk 1061 /usr/lib/jvm/java-6-openjdk
    java-6-sun 63 /usr/lib/jvm/java-6-sun
    $ sudo update-java-alternatives --set java-6-sun

Installing on Mac OS X:
=======================

Please check the version of Java installed on your machine before proceeding.
You need at least Java Runtime Environment 1.5.  Here's how to check for
the version on OS X 10.5 or higher.  Open Terminal.app and then type:

    $ java -version
    java version "1.5.0_19"
    Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_19-b02-304)
    Java HotSpot(TM) Client VM (build 1.5.0_19-137, mixed mode, sharing)

Snow Leopard should show something similar to:

    $ java -version
    java version "1.6.0_15"
    Java(TM) SE Runtime Environment (build 1.6.0_15-b03-219)
    Java HotSpot(TM) 64-Bit Server VM (build 14.1-b02-90, mixed mode)

Also make sure you have python2.5 installed if you are using google_appengine.
As of today, the Google AppEngine SDK does not work with Python 2.6 or higher.

You will also need [git][git_macosx], [MacPorts][macports], and [XCode][xcode] installed to proceed.

Install all the dependencies:
-----------------------------
    $ sudo easy_install pyyaml Jinja2 SCons Cheetah
    $ sudo port install pngcrush optipng

Do NOT install ImageMagick yet.  Installing ImageMagick installs jpeg v6 
with the current MacPorts.  You want jpeg v7 installed as well.  

Troubleshooting the Cheetah installation:
-----------------------------------------
If you had trouble installing Cheetah on Mac OS X for example, you can [download
the gzipped source tarball][cheetah], and installing using the instructions given in that file.

Troubleshooting SCons installation:
-----------------------------------
If installing SCons succeeded, but you are unable to run SCons and get
an error along the lines of `ImportError: No module name SCons.Script`,
you may need to add lines similar to the following to your `~/.profile`
in Mac OS X 10.6 (Snow Leopard):

    # Python 2.5
    export SCONS_LIB_DIR=/Library/Python/2.5/site-packages/scons-1.2.0-py2.5.egg/scons-1.2.0

    # Python 2.6
    export SCONS_LIB_DIR=/Library/Python/2.6/site-packages/scons-1.2.0-py2.6.egg/scons-1.2.0

If you're using Mac OS X 10.5:

    # Python 2.5
    export SCONS_LIB_DIR=/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/scons-1.2.0-py2.5.egg/scons-1.2.0

    # Python 2.6
    export SCONS_LIB_DIR=/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/scons-1.2.0-py2.6.egg/scons-1.2.0

SCons should now work.  You can check by issuing `scons --version` which
will show you something like:

    SCons by Steven Knight et al.:
	script: v1.2.0.r3842, 2008/12/20 22:59:52, by scons on scons-dev
	engine: v1.2.0.r3842, 2008/12/20 22:59:52, by scons on scons-dev
    Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 The SCons Foundation

Installing jpegtran:
--------------------
    $ curl http://ijg.org/files/jpegsrc.v7.tar.gz > /tmp/libjpeg.tar.gz    
    $ tar zxvf /tmp/libjpeg.tar.gz
    $ cd /tmp/jpeg-7
    $ ./configure --enable-static --enable-shared
    $ make
    $ sudo make install

Installing jpegoptim:
---------------------
Download it from [here][jpegoptim].

    $ cd jpegoptim-1.2.3
    $ ./configure 
    $ make
    $ sudo make install

Checking whether jpegtran has been correctly installed:

    $ jpegtran -v
    Independent JPEG Group's JPEGTRAN, version 7  27-Jun-2009
    Copyright (C) 2009, Thomas G. Lane, Guido Vollbeding

Google App Engine, Snow Leopard, Python2.5 and PIL:
---------------------------------------------------
Google App Engine currently works only with Python 2.5 and
the Apple build for Python 2.5 on Snow Leopard is a 32-bit
build, which causes a lot problems when you want PIL working
correctly.  We recommend installing the MacPorts version of
Python2.5, which is a 64-bit version.

Apple's version:
    
    $ file /usr/bin/python2.5
    /usr/bin/python2.5: Mach-O universal binary with 2 architectures
    /usr/bin/python2.5 (for architecture i386): Mach-O executable i386
    /usr/bin/python2.5 (for architecture ppc7400):  Mach-O executable ppc

MacPorts' version:

    $ sudo port install python25
    
    $ which python2.5
    /opt/local/bin/python2.5

    $ file `which python2.5`
    /opt/local/bin/python2.5: Mach-O 64-bit executable x86_64

Installing Python Imaging (PIL):
--------------------------------
Installing PIL for Python 2.6 on Snow Leopard should not be a problem,
but here is the procedure for Python 2.5 (from MacPorts):

    $ tar zxvf Imaging-1.1.6.tar.gz
    $ cd Imaging-1.1.6

    $ which python2.5
    /opt/local/bin/python2.5
    # Make sure python2.5 is the macports version for the next step.
    
    $ python2.5 setup.py build
    # Everything should be OK here.

    $ sudo python2.5 setup.py install

Now, install ImageMagick using MacPorts:
----------------------------------------
Here's how you do it:

    $ sudo port install ImageMagick

All set.

File monitoring on Mac OS X:
----------------------------
On Linux, Puppy uses inotify (pyinotify) to monitor the file system for
changes so it will perform a build only when a watched file changes.  While
Mac OS X has a similar API called FSEvents available, it has not yet been
integrated.  On platforms other than Linux, Puppy polls your project
directory for changes.  This may change in the future.


Common to UNIX platforms:
=========================
Follow the [installation instructions][compass_installation] for Compass
and the Compass 960 plugin.  Please also install the compass plugins:

    chrisppestein-compass-960-plugin
    compass-colors
    fancy-buttons
    compass-slickmap

or more plugins based on what is used in your project.

Clone the repository to a location on your disk and update submodules:

    $ git clone git://github.com/yesudeep/puppy.git ~/puppy
    $ cd ~/puppy
    $ git submodule init
    $ git submodule update

We will refer to the installation directory as `PUPPY_SDK_DIR` henceforth.
Add the `PUPPY_SDK_DIR` path to your `PATH` environment variable:

    $ PUPPY_SDK_DIR=/home/Google/puppy
    $ export PATH=${PUPPY_SDK_DIR}:${PATH}

Alternatively, you can update your `~/.bashrc` or `~/.profile` as well.
If you are a bash user and want bash-completion enabled for puppy,
you can include this line in your bash profile.

    source ${PUPPY_SDK_DIR}/tools/bash_completion/puppy

Setting up Google App Engine SDK:
=================================
These instructions apply while the SDK supports only Python 2.5.

    $ cd <google_appengine_installation_dir>
    
    $ chmod u+w dev_appserver.py

Edit the first line of the dev_appserver.py script to look like:

    #!/usr/bin/env python2.5

    $ chmod u-w dev_appserver.py

Now edit your .profile or .bashrc file to include these lines:

    GOOGLE_APP_ENGINE_SDK_DIR=/wherever/you/installed/google_appengine
    export PATH=$GOOGLE_APP_ENGINE_SDK_DIR:$PATH

Now you should be able to get the console version of the SDK working.

Using Puppy:
============
Yet to be written.

[pngcrush]: http://pmt.sourceforge.net/pngcrush/
[jpegtran]: http://jpegclub.org/
[optipng]: http://optipng.sourceforge.net/
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
[cheetah]: http://www.cheetahtemplate.org/
[imagemagick]: http://www.imagemagick.org/
[scons]: http://www.scons.org
[git_macosx]: http://code.google.com/p/git-osx-installer/
[macports]: http://www.macports.org/
[xcode]: http://developer.apple.com/TOOLS/Xcode/
[jpegoptim]: http://freshmeat.net/projects/jpegoptim/

