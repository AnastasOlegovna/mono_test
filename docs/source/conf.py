# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# OS path commands should be uncommented in conf.py file
# so that html utility could access the right project files to
# generate documentation.
import pathlib
import sys

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

project = 'Mono_test_webhook'
copyright = '2023, Ponomarova'
author = 'Ponomarova'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # 'myst_parser',
    # 'sphinx_markdown_builder', # побудова документації з markdown
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    # може імпортувати модулі, які ви документуєте, і завантажувати документацію з рядків документації напівавтоматично
    'sphinx.ext.viewcode',  # додає посилання на виділений вихідний код
    'sphinx.ext.duration',  # звіт про тривалість у кінці виводу консолі
    'sphinx.ext.doctest',  # розширення дозволяє тестувати  фрагменти коду в документації природним способом
    'sphinx.ext.autosummary'  # Створення комплексних посилань на API
]

exclude_patterns = []
# exclude_patterns = ['build/*']

templates_path = ['_templates']

# By default, Sphinx only supports 'restructuredtext' file type.
# source_suffix = {
#     '.rst': 'restructuredtext',
#     # '.txt': 'markdown',
#     # '.md': 'markdown',
# }
# HTML block
#
# html_theme = 'alabaster' #standart  scrolls
# html_theme = 'furo'
# html_theme = "classic"
# html_theme = "sphinxdoc"
# html_theme = "scrolls"
html_theme = "agogo"  # best
html_theme_options = {
    "linkcolor": '#204a87',
    'headerlinkcolor': 'white',
    # 'cssfiles': ['_static/custom.css'],
}
# html_theme = "nature"
# html_theme = "pyramid"
# html_theme = "haiku"
# html_theme = "traditional"
# html_theme = "epub"
# html_theme = "bizstyle"

html_static_path = ['_static']
html_title = "Mono_test_webhook's"
html_last_updated_fmt = '%d %b %Y'
html_show_sourcelink = False
html_style = 'custom.css'


# add my own css
def setup(app):
    app.add_css_file('custom.css')
