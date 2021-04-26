# -*- coding: utf-8 -*-

import sphinx_documenter_deploy

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "myst_nb",
]
master_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "myst-nb",
}

# General information about the project.
project = "sphinx documenter deploy"
copyright = "2021 Dan Foreman-Mackey"

version = sphinx_documenter_deploy.__version__
release = sphinx_documenter_deploy.__version__

exclude_patterns = ["_build"]
html_theme = "sphinx_book_theme"
html_title = "sphinx documenter deploy"
html_show_sourcelink = False
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/dfm/sphinx-documenter-deploy",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "jupyterlab",
        "colab_url": "https://colab.research.google.com/",
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
}
html_baseurl = "https://dfm.io/sphinx-documenter-deploy/"
# jupyter_execute_notebooks = "off"
execution_timeout = -1
