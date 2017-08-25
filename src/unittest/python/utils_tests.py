import unittest
from pybuilder.core import Project
import os
from pybuilder_noseallure import utils  # @UnresolvedImport

class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.project = Project('/path/to/project')
        self.project.set_property('dir_source_unittest_python', 'src/unittest/python')
        self.project.set_property('dir_target','target')

    def test_importDirs(self):
        cwd = os.getcwd()
        
        dirs = utils.getImportantDirs(self.project)
            
        # test_dir
        self.assertEquals(dirs[0], cwd + "/" + self.project.get_property('dir_source_unittest_python'))
    
        # log_dir
        self.assertEquals(dirs[1], cwd + "/target/allure_report_logs")

