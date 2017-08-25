import os
import sys
cwd = os.getcwd()
project_main_path = cwd + "\\src\\main\\python"
sys.path.insert(1, project_main_path)

from pybuilder_noseallure import run_unit_tests, init_nose  # @UnresolvedImport
from pybuilder.core import Author, init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "pybuilder-noseallure"
version = '0.0.1'

authors = [Author('Anukul Singhal','anukul.singhal@gmail.com')]
url = 'https://github.com/anukuls/pybuilder_noseallure'
description = 'Pybuilder plugin to work with Nose and Allure report generation'
license = 'Apache License, Version 2.0'
summary = 'PyBuilder Nose Plugin'

default_task = ['clean', 'install_dependencies', 'publish']

@init
def set_properties(project):
    project.depends_on_requirements('requirements.txt')
    project.set_property('verbose', True)