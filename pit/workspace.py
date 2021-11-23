import os

class Workspace:
    IGNORE = ['.', '..', '.git', '__pycache__'] # remove __pycache__ later
    
    def __init__(self, root_pathname):
        self.root_pathname = root_pathname

    def list_files(self):
        return [file for file in os.listdir(self.root_pathname) if file not in self.IGNORE]

    def read_file(self, file_pathname):
        return open(self.root_pathname / file_pathname).read()
