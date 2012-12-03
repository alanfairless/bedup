#!/usr/bin/env python

from setuptools import setup
from sys import version_info

import bedup.btrfs
import bedup.chattr
import bedup.fiemap
import bedup.futimens
import bedup.ioprio
import bedup.openat
import bedup.syncfs
import bedup.time

install_requires = [
    'alembic',  # XXX I need Alembic, but not Mako or MarkupSafe.
    'cffi >= 0.4.2',
    'pyxdg',
    'SQLAlchemy',
    'contextlib2',
]

if version_info < (2, 7):
    install_requires.append('argparse')

setup(
    name='bedup',
    version='0.0.7',
    author='Gabriel de Perthuis',
    author_email='g2p.code+bedup@gmail.com',
    url='https://github.com/g2p/bedup',
    license='GNU GPL',
    keywords='btrfs deduplication filesystem dedup',
    description='Deduplication for Btrfs filesystems',
    install_requires=install_requires,
    extras_require={
        'interactive': ['ipdb']},
    entry_points={
        'console_scripts': [
            'bedup = bedup.__main__:script_main']},
    ext_modules=[
        bedup.btrfs.ffi.verifier.get_extension(),
        bedup.chattr.ffi.verifier.get_extension(),
        bedup.fiemap.ffi.verifier.get_extension(),
        bedup.futimens.ffi.verifier.get_extension(),
        bedup.ioprio.ffi.verifier.get_extension(),
        bedup.openat.ffi.verifier.get_extension(),
        bedup.syncfs.ffi.verifier.get_extension(),
        bedup.time.ffi.verifier.get_extension(),
    ],
    ext_package='bedup',
    packages=[
        'bedup',
    ],
    use_2to3=True,
    zip_safe=False,  # cargo-culted from the CFFI docs
    classifiers='''
        Programming Language :: Python :: 2
        Programming Language :: Python :: 3
        Programming Language :: Python :: Implementation :: CPython
        Programming Language :: Python :: Implementation :: PyPy
        License :: OSI Approved :: GNU General Public License (GPL)
        Operating System :: POSIX :: Linux
        Intended Audience :: System Administrators
        Intended Audience :: End Users/Desktop
        Topic :: System :: Filesystems
        Topic :: Utilities
        Environment :: Console
    '''.strip().splitlines(),
    long_description='''
    Deduplication for Btrfs.

    bedup looks for new and changed files, making sure that multiple copies of
    identical files share space on disk. It integrates deeply with btrfs so that
    scans are incremental and low-impact.

    See `github.com/g2p/bedup <https://github.com/g2p/bedup#readme>`_
    for usage instructions.''')

