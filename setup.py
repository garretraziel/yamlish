# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
from distutils.core import setup, Command
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os.path
import yamlish

class RunTests(Command):
    """New setup.py command to run all tests for the package.
    """
    description = "run all tests for the package"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = unittest.TestLoader()
        loader.discover('.')
        suite = loader.suiteClass()
        result = unittest.TestResult()
        suite.run(result)

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as inf:
        return "\n" + inf.read().replace("\r\n", "\n")
    # private

def get_long_description():
    return read("README.txt") \
        + "\nChangelog:\n" + "=" * 10 + "\n" \
        + read("NEWS.txt")

setup(
    name='yamlish',
    version=yamlish.__version__,
    description='Python implementation of YAMLish',
    author='Matej Cepl',
    author_email='mcepl@redhat.com',
    url='https://gitorious.org/yamlish',
    py_modules=['yamlish'],
    long_description=get_long_description(),
    keywords=['TAP', 'YAML', 'yamlish'],
    cmdclass={'test': RunTests},
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
        ]
)

