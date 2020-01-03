# -*- coding: utf-8 -*-
#
# Pythran documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 19 20:57:04 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import re

from pythran import __version__

with open("../README.rst") as readme:
    readme_body = readme.read()
    toc = '''

.. toctree::
    :maxdepth: 1


    MANUAL
    EXAMPLES
    CLI
    SUPPORT
    DEVGUIDE
    TUTORIAL
    INTERNAL
    LICENSE
    AUTHORS
    Changelog
'''

    readme_body = readme_body.replace('http://pythran.readthedocs.io', toc)

    with open("index.rst", "w") as index:
        index.write(readme_body)
    del readme_body

with open("../LICENSE") as license:
    with open('LICENSE.rst', 'w') as license_rst:
        license_rst.write("=======\nLICENSE\n=======\n\n")
        license_rst.write(license.read())

with open("../Changelog") as changelog:
    with open('Changelog.rst', 'w') as changelog_rst:
        changelog_rst.write('=========\nChangelog\n=========\n\n')
        changelog_rst.write(changelog.read())

with open("../AUTHORS") as authors:
    with open('AUTHORS.rst', 'w') as authors_rst:
        authors_rst.write(authors.read())

def make_support():
    from pythran import tables

    TITLE = "Supported Modules and Functions"

    DEPTHS = '=*-+:~#.^"`'

    body = []

    body.append(DEPTHS[0]*len(TITLE))
    body.append(TITLE)
    body.append(DEPTHS[0]*len(TITLE))
    body.append("")


    def format_name(name):
        if name.endswith('_') and not name.startswith('_'):
            name = name[:-1]
        return name


    def isiterable(obj):
        return hasattr(obj, '__iter__')


    def dump_entry(entry_name, entry_value, depth):
        if isiterable(entry_value):
            body.append(entry_name)
            body.append(DEPTHS[depth] * len(entry_name))
            body.append("")
            sym_entries, sub_entries = [], []
            for sym in entry_value:
                w = sub_entries if isiterable(entry_value[sym]) else sym_entries
                w.append(sym)
            for k in sorted(sym_entries):
                dump_entry(format_name(k), entry_value[k], depth + 1)
            body.append("")
            for k in sorted(sub_entries):
                dump_entry(format_name(k), entry_value[k], depth + 1)
                body.append("")
        else:
            body.append(entry_name)

    for MODULE in sorted(tables.MODULES):
        if MODULE != '__dispatch__':
            dump_entry(format_name(MODULE), tables.MODULES[MODULE], 1)

    return "\n".join(body)

with open('SUPPORT.rst', 'w') as support:
    support.write(make_support())


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['nbsphinx',]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Pythran'
copyright = u'2014, Serge Guelton, Pierrick Brunet et al.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['**.ipynb_checkpoints']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import guzzle_sphinx_theme

html_theme_path = guzzle_sphinx_theme.html_theme_path()
html_theme = 'guzzle_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "Project Name",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'pythran.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pythrandoc'

