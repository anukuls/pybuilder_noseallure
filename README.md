# pybuilder_noseallure
Pybuilder plugin for using Nose to run unit tests and integration with allure reports

# Usage

Add plugin dependency to your build.py

    use_plugin('pypi:pybuilder_noseallure')

If you are also using the plugin python.unittest, you should remove it.

In theory, this is all you need to do to start using Nose for unit testing and generating allure reports. However, if you want to tweak it, all nose command line parameters are available for configuration through the project properties. Simply append "nose_" for the property key.

For example, if you want to replace the allure log directory:

    @init
    def init(project):
      project.set_property('nose_logdir', '/path/to/logdir')

This is equivalent to running

    $ nosetests --logdir=/path/to/logdir
    
# Task

In your build.py, add run_unit_tests task to the list of default_task.  This task will trigger nosetests with-allure and logdir option

For example,

    default_task = ['clean','install_dependencies','run_unit_tests','publish']
    
run_unit_tests task defined in build.py will run the equivalent command:

    $ nosetests tests/sample_tests.py --with-allure --logdir=/path/to/logdir

# Example build.py

    from pybuilder.core import use_plugin, init

    use_plugin("python.core")
    use_plugin('pypi:pybuilder_noseallure') 
    use_plugin("python.install_dependencies")
    use_plugin("python.distutils")

    name = "Name_of_Your_Project"
    default_task = ['clean','install_dependencies','run_unit_tests','publish']

    @init
    def initialize(project):
      pass
      
# Execution

## Linux

    $ pyb
   
## Windows

    > pyb_.exe
