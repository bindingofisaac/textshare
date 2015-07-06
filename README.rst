=========
textshare
=========

*A simple command line utility to share code and texts*

Download python package here `pypi <https://pypi.python.org/pypi/textshare/>`_

Submit issues here `github <https://github.com/bindingofisaac/textshare>`_

============
installation
============

.. code-block:: bash

    $ pip install textshare

=====
usage
=====

textshare [OPTIONS] [FILEPATHS]...

Options:
-i, --input  uses stdin as input

--help       Show this message and exit.

========
examples
========

.. code-block:: bash 

    $ textshare filename1 filename2

    $ cat file | textshare -i
