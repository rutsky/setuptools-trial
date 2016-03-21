CHANGES
=======

0.6.0 (2016-XX-XX)
------------------

- Fix working with recent versions of setuptools.

- Python versions < 2.7 support was dropped.
  Currently Python 2.7 and Python 3.4, 3.5 versions are supported
  (should work in other Python 3 releases too, but it is not tested).

- Package "zip-safety" is determined by setuptools.

- New package home page is https://github.com/rutsky/setuptools-trial,
  please report issues there!

Internal changes:

- Getting version from Darcs VCS was removed.

- Remove trash files (prebuild eggs, PKG-INFO).

- Source code is not PEP8 and pyflakes conformant.

- Simple integration tests were added.
