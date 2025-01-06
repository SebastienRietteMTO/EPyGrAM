EPyGrAM
=======

__*Enhanced Python for Graphics and Analysis of Meteorological fields*__

---

The epygram library package is a set of Python classes and functions designed to handle meteorological fields in Python, as well as interfacing their storage in various usual (or not) data formats.

Dependencies
------------

EPyGrAM dependencies are available from Pypi (pip install ...), and listed in `pyproject.toml`.
Some packages are mandatory, others are optional, only necessary for the use of specific functionalities or formats.
Formats for which the import of the according underlying package fails are deactivated at runtime.

Installation
------------

`pip install epygram`

or

`pip3 install epygram`

To use specific functionalities which dependencies are not covered by default,
you may need to manually pip install the according package(s).

Tests
-----

To run tests, cf. [`tests/README.md`](tests/README.md).

Documentation
-------------

To generate Sphinx doc: `make doc`. It will be generated in `docs/build/html`.
Online doc of the latest release on `master` branch is available at https://umr-cnrm.github.io/EPyGrAM-doc

License
-------

This software is governed by the open-source [CeCILL-C](http://www.cecill.info) license under French law, cf. LICENSE.txt.
Downloading and using this code means that you have had knowledge of the CeCILL-C license and that you accept its terms.

