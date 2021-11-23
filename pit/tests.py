import os
import unittest
from pathlib import Path

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_git_folder_exists(self):
        self.assertTrue('.git' in os.listdir(os.getcwd()))

    def test_objects_folder_exists_in_git(self):
        self.assertTrue('.git' in os.listdir(os.getcwd()))
        self.assertTrue('objects' in os.listdir(Path(os.getcwd() + '/.git')))

    def test_refs_folder_exists_in_git(self):
        self.assertTrue('.git' in os.listdir(os.getcwd()))
        self.assertTrue('refs' in os.listdir(Path(os.getcwd() + '/.git')))

if __name__ == '__main__':
    unittest.main()
