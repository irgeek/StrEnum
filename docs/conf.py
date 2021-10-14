# Configuration file for the Sphinx documentation builder.
# pylint: disable=invalid-name,redefined-builtin,wrong-import-position,import-error,unused-import
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import myst_parser

# from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath(".."))


import strenum

# -- Project information -----------------------------------------------------

project = "StrEnum"
copyright = "2021, James Sinclair"
author = "James Sinclair"

# The full version, including alpha/beta/rc tags
release = strenum.__version__
github_doc_root = "https://github.com/irgeek/strenum/tree/master/docs/"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    # "sphinx.ext.viewcode",
    # "sphinx.ext.autosummary",
    "myst_parser",
]

source_suffix = [".rst", ".md"]
master_doc = "index"
templates_path = []

html_theme = "sphinx_rtd_theme"
html_static_path = []

exclude_patterns = [".venv"]

pygments_style = "sphinx"

autodoc_member_order = "bysource"
autodoc_class_signature = "separated"
autosummary_generate = True
