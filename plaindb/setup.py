__author__ = "Smruti Mohanty"

import setuptools
from sphinx.setup_command import BuildDoc

name = "plaindb"
version = '0.0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author="Animal Logic",
    author_email="2spmohanty@gmail.com",
    description="Plain DB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        name: [
        ]
    },
    packages=setuptools.find_packages(),
    py_modules=['plaindb.core', 'plaindb.render'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.6',
    install_requires=[

    ],
    extras_require={
        'coverage': [
            'coverage',
        ],
        'docs': [

            'sphinx_rtd_theme',
            'sphinx-git',
            'sphinx-markdown-parser',
            'sphinx-markdown-tables',
            'sphinxcontrib-plantuml',
            'sphinxcontrib-confluencebuilder',
            'sphinxcontrib-programoutput',
        ],
        'docs-lint': [
            'rstcheck',
        ],
        'lint': [
            'pylint',
            'prospector',
            'pyflakes',
        ],
        'testing': [
            'pytest',
            'pytest-cov',
            'tox',
        ],
    },
    entry_points={
        'console_scripts': [
            'plaindb = plaindb.app:main',
        ]
    },
    cmdclass={
        'build_sphinx': BuildDoc
    },
    command_options={
        'build_sphinx': {
            'version': ('setup.py', version),
            'source_dir': ('setup.py', 'docs')}
    },
)
