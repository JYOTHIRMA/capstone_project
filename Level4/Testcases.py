import pytest
from Level1.SystemDriveFinder import SystemDriverFinder
from Level1.FindFile import FileFinder
class Test_Drive:
    def test_DriverCase(self):
        obj=SystemDriverFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','c:\hcl')
        self.expected_filename=d[0]
        self.actual_res='c:\\hcl\\demo.txt'
        assert self.expected_filename==self.actual_res

