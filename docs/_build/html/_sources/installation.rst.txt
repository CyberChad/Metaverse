..
    structure based on https://raw.githubusercontent.com/pyqtgraph/pyqtgraph/master/doc/source/installation.rst

Installation
============

Metaverse depends on:

* Python 3.7+
* OpenAI Gym

The easiest way to meet these dependencies is with ``pip`` or with a scientific
python distribution like Anaconda.

There are many different ways to install metaverse, depending on your needs:

pip
---

The most common way to install metaverse is with pip::

    $ pip install metaverse

Some users may need to call ``pip3`` instead. This method should work on all
platforms.

..
    conda
    -----

    metaverse is on the default Anaconda channel::

        $ conda install metaverse

    It is also available in the conda-forge channel::

        $ conda install -c conda-forge metaverse

From Source
-----------

To get access to the very latest features and bugfixes you have three choices:

1. Clone metaverse from github::

    $ git clone https://github.com/cyberchad/metaverse
    $ cd metaverse

   Now you can install metaverse from the source::

    $ pip install .

2. Directly install from GitHub repo::

    $ pip install git+git://github.com/cyberchad/metaverse.git@master

   You can change ``master`` of the above command to the branch name or the
   commit you prefer.

3. You can simply place the metaverse folder someplace importable, such as
   inside the root of another project. Metaverse does not need to be "built" or
   compiled in any way.

..
    Other Packages
    --------------

    Packages for metaverse are also available in a few other forms:

    * **Debian, Ubuntu, and similar Linux:** Use ``apt install python-pyqtgraph`` or
      download the .deb file linked at the top of the pyqtgraph web page.
    * **Arch Linux:** https://www.archlinux.org/packages/community/any/python-pyqtgraph/
    * **Windows:** Download and run the .exe installer file linked at the top of the
      pyqtgraph web page: http://pyqtgraph.org