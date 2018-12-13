# -*- coding: utf-8 -*-
#
# GMT Software and Controls documentation build configuration file, created by
# sphinx-quickstart on Wed Jun  5 14:48:12 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
#    'sphinxcontrib.blockdiag',
#    'sphinxcontrib.gnuplot',
#    'sphinxcontrib.googlechart'
]

blockdiag_fontpath = '/Library/Fonts/Tahoma.ttf'

blockdiag_html_image_format = 'SVG'
blockdiag_tex_image_format  = 'PDF'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'GMT Software And Controls'
copyright = u'2015, contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.5'
# The full version, including alpha/beta/rc tags.
release = '1.5.0'

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
exclude_patterns = ['**/*_inc.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
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


# -- Options for HTML output ---------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
  import sphinx_rtd_theme
  html_theme = 'sphinx_rtd_theme'
  html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
  html_style = 'css/additional_style.css'

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

#XXX# # The theme to use for HTML and HTML Help pages.  See the documentation for
#XXX# # a list of builtin themes.
#XXX# html_theme = 'default' # 'default', 'nature'
#XXX# html_theme = 'nature' # 'default', 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'GMT Software And Controls documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
#XXX# html_short_title = 'SWC %s documentation' % version
html_short_title = 'Home'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/logowhite.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }

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
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

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
htmlhelp_basename = 'GMTSoftwareAndControlsdoc'

numfig = True

numfig_secnum_depth = 1

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
  'classoptions': ',openany,oneside',
  'babel':        '\\usepackage[english]{babel}',
  'pointsize':    '9pt',
  'preamble': '\n%Added from template'
              '\n\setcounter{tocdepth}{2}'
              '\n\setcounter{secnumdepth}{3}'
              '\n\usepackage{fancyheadings}'
              '\n\usepackage{tocloft}'
              '\n\setlength{\cftfignumwidth}{2em}'
              '\n\setlength{\cfttabnumwidth}{3em}'
              '\n\\fancypagestyle{wholedocument}{\\fancyhead{}\\fancyfoot{}\\renewcommand{\headrulewidth}{0.4pt}'
              '\n\\renewcommand{\\footrulewidth}{0.4pt}'
              '\n\\fancyhead[R]{\color{black} \\bfseries  \\fontfamily{phv}}'
              '\n\\fancyfoot[L]{\color{black} \\bfseries  \small {\\rightmark}}'
              '\n\\fancyfoot[R]{\color{black} {\\bfseries \\thepage}}}'
              '\n\\renewcommand{\chaptermark}[1]{\markboth{\\thechapter.\#1}{}}'
              '\n\\renewcommand{\sectionmark}[1]{\markright{\\thesection.\ #1}{}}'
              '\n\\renewcommand{\\thepage}{\\roman{page}}'
              '\n\pagestyle{wholedocument}'
              '\n\clearpage'
              '\n\setcounter{page}{1}'
              '\n\pagenumbering{arabic}'
              '\n%Added from template'

# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).

latex_documents = [
#  ('index',                              'swc_all_doc.tex',      u'GMT Software and Controls Documentation',               u'Software and Controls Group', 'manual'),
  ('software_development/installation',  'swc_installation.tex', u'SDK Installation',                        u'Software and Controls Group', 'manual'),
  ('software_development/core_services_user_guide',  'swc_core_services_user_guide.tex', u'Core Services user guide', u'Software and Controls Group', 'manual'),
  ('software_development/gds_guide',  'swc_gds_documentation.tex', u'gds documentation', u'Software and Controls Group', 'manual'),
  ('software_development/modeling_guidelines',  'swc_modeling_guidelines.tex', u'Model specification guide document', u'Software and Controls Group', 'manual'),
  ('software_development/model_language_mapping/mapping_model_to_cpp',  'swc_map_model_cpp.tex', u'Mapping between the Model Definition Files and C++ source code', u'Software and Controls Group', 'manual'),
  ('software_development/isample_example',  'swc_isample_example.tex', u'ISample example', u'Software and Controls Group', 'manual'),
  ('software_development/hdk_example',  'swc_hdk_example.tex', u'HDK example', u'Software and Controls Group', 'manual'),

  #('swc_sys_stds',               'swc_sys_stds.tex',    u'GMT Software and Controls Standards',                   u'Jose M. Filgueira', 'manual'),
  # ('swc_sys_doc',                'swc_sys_doc.tex',      u'GMT Software and Controls Documentation',               u'Jose M. Filgueira', 'manual'),
  # ('swc_sys_glossary',           'swc_sys_glossary.tex',    u'GMT Software and Controls Acronyms and Definitions',  u'Jose M. Filgueira', 'manual'),
  # ('swc_sys_dp_filedef',         'swc_sys_dp_filedef.tex',  u'GMT Software and Controls Data Product Files',        u'Chien Y. Peng',     'manual'),
  # ('swc_sys_dp_kwd_dict',        'swc_sys_dp_kwd_dict.tex', u'GMT Software and Controls FITS Keyword Dictionary',   u'Chien Y. Peng',     'manual'),
  # ('swc_sys_wbs',                'swc_sys_wbs.tex',      u'GMT Software and Controls Work Breakdown Structure',    u'Jose M. Filgueira', 'manual'),
  # ('swc_sys_pbs',                'swc_sys_pbs.tex',      u'GMT Software and Controls Product Breakdown Structure', u'Jose M. Filgueira', 'manual'),
  # ('swc_workflow_rpt',           'swc_workflow_rpt.tex', u'GMT Software and Controls Workflows',                   u'Jose M. Filgueira', 'manual'),
  #('swc_ao_pbs',                 'swc_ao_pbs.tex',      u'GMT Adaptive Optics Software and Controls Packages (DRAFT)',    u'Jose M. Filgueira', 'manual'),
  #('swc_sys_plan',               'swc_sys_plan.tex',    u'GMT Software and Controls Development Plan',            u'Jose M. Filgueira', 'manual'),
  #('swc_sys_process',            'swc_sys_process.tex', u'GMT Software and Controls Development Process',         u'Jose M. Filgueira', 'manual'),
  #('swc_sys_cost',               'swc_sys_cost.tex',    u'GMT Software and Controls Cost Report',                 u'Jose M. Filgueira', 'manual'),
  #('tdcs/m1_cs/m1_cs_drd',       'm1_cs_drd.tex',       u'GMT M1 Control System Requirements',                     u'jmf', 'manual'),
  #('tdcs/m1_cs/m1_cs_icd',       'm1_cs_icd.tex',       u'GMT M1 Control System ICD',                             u'jmf', 'manual'),
  #('tdcs/m1_cs/m1_cs_plan',      'm1_cs_plan.tex',      u'GMT M1 Control System Development Plan',                u'jmf', 'manual')
  #('tdcs/m1_cs/m1_cs_sdd',       'm1_cs_sdd.tex',       u'GMT M1 Control System Design Report',                   u'jmf', 'manual')
  #('tcs/mount_cs/mount_cs_drd',  'mount_cs_drd.tex',    u'GMT Mount Control System Requirements',                 u'jmf', 'manual'),
  # ('tdcs/agws_cs/agws_cs_drd',     'agws_cs_drd.tex',      u'GMT AGWS Control System Requirements',                  u'jmf', 'manual')
  #('tcs/agws_cs/agws_cs_icd',    'agws_cs_icd.tex',     u'GMT AGWS Control System ICD',                           u'jmf', 'manual'),
  #('tcs/agws_cs/agws_cs_plan',   'agws_cs_plan.tex',    u'GMT AGWS Control System Development Plan',              u'jmf', 'manual'),
  #('tcs/agws_cs/agws_cs_sdd,     'agws_cs_sdd.tex',     u'GMT AGWS Control System Design Report',                 u'jmf', 'manual'),
  #('tcs/ngws_cs/ngws_cs_drd',    'ngws_cs_drd.tex',     u'GMT NGWS Control System Requirements',                  u'jmf', 'manual'),
  #('tcs/ngws_cs/ngws_cs_icd',    'ngws_cs_icd.tex',     u'GMT NGWS Control System ICD',                           u'jmf', 'manual'),
  #('tcs/ngws_cs/ngws_cs_plan',   'ngws_cs_plan.tex',    u'GMT NGWS Control System Development Plan',             u'jmf', 'manual'),
  #('tcs/ngws_cs/ngws_cs_sdd,     'ngws_cs_sdd.tex',     u'GMT NGWS Control System Design Report',                u'jmf', 'manual'),
  #('tcs/lsa_cs/lsa_cs_drd',      'lsa_cs_drd.tex',      u'GMT LSA Control System Requirements',                  u'jmf', 'manual'),
  #('tcs/lsa_cs/lsa_cs_icd',      'lsa_cs_icd.tex',      u'GMT LSA Control System ICD',                           u'jmf', 'manual'),
  #('tcs/lsa_cs/lsa_cs_sdd,       'lsa_cs_sdd.tex',      u'GMT LSA Control System Design Report',                 u'jmf', 'manual'),
  #('tcs/lsa_cs/lsa_cs_plan',     'lsa_cs_plan.tex',     u'GMT LSA Control System Development Plan',              u'jmf', 'manual'),
  #('tcs/lsa_cs/lsa_cs_drd',      'lsa_cs_drd.tex',      u'GMT LSA Control System Requirements',                  u'jmf', 'manual'),
  #('tcs/wfc_cs/wfc_cs_icd',      'wfc_cs_icd.tex',      u'GMT WFC Control System ICD',                           u'jmf', 'manual'),
  #('tcs/wfc_cs/wfc_cs_sdd',      'wfc_cs_sdd.tex',      u'GMT WFC Control System Design Report',                 u'jmf', 'manual'),
  #('tcs/wfc_cs/wfc_cs_plan',     'wfc_cs_plan.tex',     u'GMT WFC Control System Development Plan',              u'jmf', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = ['glossary', 'todo']

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'gmtsoftwareandcontrols', u'GMT Software and Controls Documentation',
     [u'jmf'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'GMTSoftwareandControls', u'GMT Software and Controls Documentation',
   u'jmf', 'GMTSoftwareandControls', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'GMT Software and Controls'
epub_author = u'jmf'
epub_publisher = u'jmf'
epub_copyright = u'2013, jmf'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# If 'no', URL addresses will not be shown.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
