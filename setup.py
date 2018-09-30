# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re
import ast
import codecs
import setuptools
import setuptools.command.test

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('grpc_proto_validator/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


# -*- Requirements -*-

def _strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            _strip_comments(l) for l in open(
                os.path.join(os.getcwd(), 'requirements', *f)).readlines()
        ) if r]


def reqs(*f):
    """Parse requirement file.
    Example:
        reqs('default.txt')          # requirements/default.txt
        reqs('extras', 'redis.txt')  # requirements/extras/redis.txt
    Returns:
        List[str]: list of requirements specified in the file.
    """
    return [req for subreq in _reqs(*f) for req in subreq]


def install_requires():
    """Get list of requirements required for installation."""
    return reqs('default.txt')


# -*- Long Description -*-

def long_description():
    try:
        return codecs.open('README.RST', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.rst file'


# -*- Command: setup.py test -*-

class pytest(setuptools.command.test.test):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        setuptools.command.test.test.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest as _pytest
        sys.exit(_pytest.main(self.pytest_args))


setuptools.setup(
    name='grpc-proto-validator',
    version=version,
    url='https://github.com/v1c77/py_grpc_validator',
    license='MIT',
    author='v1c77',
    author_email='heyuhuade@gmail.com',
    description='grpc proto validator.',
    long_description=long_description(),
    install_requires=install_requires(),
    tests_require=reqs('test.txt'),
    include_package_data=True,
    packages=['grpc_proto_validator'],
    zip_safe=False,
    platforms='any',
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Quality Assurance',
    ]
)
