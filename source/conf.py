# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Wax'
copyright = '2024, Jeffrey Barish'
author = 'Jeffrey Barish'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
# html_theme = 'classic'


# Include the following for alabaster:
html_sidebars = {
    '**': [
        'navigation.html',
        'searchbox.html',
    ]
}

