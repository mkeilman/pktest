import os
import sys

sys.path.insert(0, os.path.abspath("../pktest/"))

extensions = [
    "sphinx.ext.autodoc",
]
html_theme = "sphinx_rtd_theme"
source_suffix = [
    ".md",
    ".rst",
]
