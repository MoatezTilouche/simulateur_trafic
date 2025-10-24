import os
import sys
from datetime import datetime

# Add project root to sys.path so autodoc can import the package modules
sys.path.insert(0, os.path.abspath('..'))

project = 'simulateur_trafic'
author = 'Project'
year = datetime.now().year
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
html_static_path = ['_static']

# Autodoc settings
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
}
