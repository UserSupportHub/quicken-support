# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Download & Activate Quicken Guide'
copyright = '2025, Quicken'
author = 'Quicken Help Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Templates path
templates_path = ['_templates']

# List of patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# HTML theme
# html_theme = 'sphinx_rtd_theme'  # Uncomment to use ReadTheDocs theme

# Title displayed in the browser and documentation
html_title = "Download & Activate Quicken – Official Step-by-Step Guide"

# Optional short title for navbar (if supported by theme)
html_short_title = "Quicken Activation Guide"

# Favicon
html_favicon = 'favicon.ico'  # Place your favicon.ico in _static

# Do not show "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks
html_allow_unsafe = True

# Theme options (customize if needed)
html_theme_options = {
    'show_powered_by': False,
}

# Paths for static files like custom CSS, JS, or images
# Uncomment and create _static folder if needed
# html_static_path = ['_static']
