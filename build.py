import os
import sys
cwd = os.getcwd()
project_main_path = cwd + "\\src\\main\\python"
sys.path.insert(1, project_main_path)

from pybuilder_noseallure import run_unit_tests, init_nose  # @UnresolvedImport
from pybuilder_noseallure.utils import getImportantDirs  # @UnresolvedImport
from pybuilder.core import Author, init, use_plugin, task, description
import subprocess, os.path

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "pybuilder-noseallure"
version = '0.0.2'

authors = [Author('Anukul Singhal','anukul.singhal@gmail.com')]
url = 'https://github.com/anukuls/pybuilder_noseallure'
description = 'Pybuilder plugin to work with Nose and Allure report generation'
license = 'Apache License, Version 2.0'
summary = 'PyBuilder Nose Allure Plugin'

default_task = ['clean', 'install_dependencies', 'publish', 'upload']
# default_task = ['clean', 'install_dependencies', 'run_unit_tests', 'generate_report', 'publish']

@init
def set_properties(project):
    project.depends_on_requirements('requirements.txt')
    project.set_property('verbose', True)
#    project.set_property('distutils_upload_repository', 'https://upload.pypi.org/legacy/')

@task
def generate_report(project, logger):
    # set cwd to project root
    test_dir,log_dir = getImportantDirs(project)

    logger.debug("Log dir: %s" % log_dir) 
    
    allureEnv = os.environ.copy()
    cwd = os.getcwd()
    project_main_path = cwd
    allureEnv["PYTHONPATH"] = project_main_path
    
    #Generate Allure Report folder
    args = ['allure', 'generate', log_dir, '--clean']
  
    allureProc = subprocess.Popen(args, stdout=subprocess.PIPE, env=allureEnv, shell=True)
  
    while allureProc.poll() is None:
        l = allureProc.stdout.readline()
        logger.debug(l)
  
    if allureProc.returncode != 0:
        logger.warn('Allure report generation failed with exit code %s' % allureProc.returncode)