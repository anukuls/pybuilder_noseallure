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

   $ nodetests --html-coverage-dir=/path/to/html
