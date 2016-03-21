#!/usr/bin/env python
# This is a setuptools plugin that adds a 'trial' command which uses the
# trial script from Twisted to run unit tests instead of pyunit.
# The functionality of this plugin was contributed from
# the Elisa project: http://elisa.fluendo.com/.

import os
import re
import sys

from setuptools import find_packages, setup

trove_classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: BSD License",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    "Framework :: Setuptools Plugin",
]

PKG = 'setuptools_trial'
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass  # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print("unable to find version in %s" % (VERSIONFILE,))
        raise RuntimeError(
            "If %s.py exists, it is required to be well-formed." %
            (VERSIONFILE,))

setup_requires = []

data_fnames = ['README.rst', 'COPYING.SPL.txt']

# In case we are building for a .deb with stdeb's sdist_dsc command, we put
# the docs in "share/doc/python-$PKG".
PKG = 'setuptools_trial'
doc_loc = "share/doc/python-" + PKG
data_files = [(doc_loc, data_fnames)]

if {'pytest', 'test'}.intersection(sys.argv):
    setup_requires.append('pytest_runner')

setup(
    name=PKG,
    version=verstr,
    author="Chris Galvan",
    author_email="cgalvan@enthought.com",
    maintainer="Vladimir Rutsky",
    maintainer_email="vladimir@rutsky.org",
    url='https://github.com/rutsky/setuptools-trial',
    description="Setuptools plugin that makes unit tests execute with trial "
                "instead of pyunit.",
    entry_points={
        'distutils.commands': [
            'trial = setuptools_trial.setuptools_trial:TrialTest',
        ],
    },
    install_requires=[
        "Twisted >= 2.4.0",
    ],
    setup_requires=setup_requires,
    test_suite="tests",
    tests_require=[
        "pytest",
        "pytest-virtualenv",
        "virtualenv",
    ],
    keywords="distutils setuptools trial setuptools_plugin",
    license="BSD",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    data_files=data_files,
    classifiers=trove_classifiers,
    extras_require={
        ":python_version == '2.7'": ["pathlib2"],
    },
)
