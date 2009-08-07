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

Installation:
=============

Requirements
------------
* Linux
* [Java 1.6][java_jre]
* [Ruby 1.8][ruby_lang]
* [Python 2.5 or Python 2.6][python_lang]
* [pyinotify][pyinotify]
* [PyYAML][pyyaml]
* [Compass][compass] and the [Compass 960 plugin][compass_960]
* [Jinja2][jinja2]
* [OptiPNG][optipng]
* [JpegTran][jpegtran]
* [PNGCrush][pngcrush]
* [Cheetah][cheetah]
* [ImageMagick][imagemagick]

Installing on Ubuntu:
---------------------

Install the dependencies first:

    $ sudo easy_install pyinotify pyyaml Jinja2 Cheetah
    $ sudo aptitude install sun-java6-jre optipng pngcrush jpegtran imagemagick

Follow the [installation instructions][compass_installation] for Compass
and the Compass 960 plugin.

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

Installation Notes:
-------------------
Please make sure you have Java 1.6 JRE installed and setup for use.
Some Linux systems come with OpenJDK versions of Java.  YUI Compressor
fails to generate minified files when used with these versions of Java.
To configure Ubuntu to use Java 1.6 you can use the `update-java-alternatives` command.

Please see `update-java-alternatives --help`.

Using Puppy:
============


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

