import sys
import os
import shlex
import subprocess

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if read_the_docs_build:
    subprocess.call('doxygen', shell=True)

extensions = ['breathe']
breathe_projects = { "ArduinoDocs": "xml" }
breathe_default_project = "ArduinoDocs"
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ArduinoDocs'
copyright = u'2015, Circuitar'
author = u'Circuitar'
version = '1.0'
release = '1.0'
language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = ['_static']
htmlhelp_basename = 'ArduinoDocsdoc'
latex_elements = {
}
latex_documents = [
  (master_doc, 'ArduinoDocs.tex', u'ArduinoDocs Documentation',
   u'Circuitar', 'manual'),
]
man_pages = [
    (master_doc, 'arduinodocs', u'ArduinoDocs Documentation',
     [author], 1)
]
texinfo_documents = [
  (master_doc, 'ArduinoDocs', u'ArduinoDocs Documentation',
   author, 'ArduinoDocs', 'One line description of project.',
   'Miscellaneous'),
]
