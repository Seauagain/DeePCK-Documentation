# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sys
import os
## Add code absolute path
main_path = os.path.join('..', '..')
sys.path.insert(0, os.path.abspath(main_path))
sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('../../Data/'))
# -- Project information -----------------------------------------------------

project = 'CKODE'
copyright = '2022, Yuxiao Yi'
author = 'Yuxiao Yi'

# The full version, including alpha/beta/rc tags
release = 'v1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', 
        'sphinx.ext.autodoc', 
        'sphinx.ext.doctest',
        'sphinx.ext.napoleon',
        'sphinx.ext.mathjax',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.intersphinx']

autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
    'undoc-members': True,
}
# latex_engine = 'xelatex'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The suffix of source filenames.
source_suffix = '.rst'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'github_user': 'Seauagain',
    'github_repo': 'CKODE-Documentation',
    'github_banner': True,
    'github_button': True,
    'show_powered_by': True,
    'travis_button': True,
}




## module preivew style setup 
autodoc_default_options = {'members': True}
autoclass_content = 'class'
napoleon_numpy_docstring = True
napoleon_google_docstring = False


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

#
# html_extra_path = ['../build/API']


## type in your comment
intersphinx_mapping = {
  'python': ('https://docs.python.org/3.10', None),
  'numpy': ('https://docs.scipy.org/doc/numpy/', None),
#   'cantera': ('https://cantera.org/documentation/docs-2.6/sphinx/html/?', None),
#   'torch': ('https://pytorch.org/docs/', None),
  #'pytables': ('http://www.pytables.org/usersguide/libref/', None)
}

# Make the module index more useful by sorting on the module name
# instead of the package name
# modindex_common_prefix = ['CKODE.']

## show class/fucntion by the order in the source code
autodoc_member_order = 'bysource'

def setup(app):
    app.add_css_file('custom.css')