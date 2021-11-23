import os, sys
from pathlib import Path, PurePath
from colorama import Fore

from workspace import Workspace
from database import Database
from blob import Blob

args = sys.argv
args_len = len(args)

if args_len > 1:
    command = args[1]
    if command == 'init':
        # Initialize .git repo
        path = args[2] if args_len > 2 else os.getcwd()
        root_path = Path(path)
        git_path = root_path / '.git'
        
        folders = ['objects', 'refs']
        for folder in folders:
            try:
                Path.mkdir(Path(git_path / folder), parents=True)
                import platform, subprocess
                if platform.system() == 'Windows':
                    subprocess.call(["attrib", "+H", git_path])  # to hide the .git folder on windows os
            except FileExistsError as e:
                print(Fore.RED + f'Fatal: "Cannot create a file when that file already exists: {PurePath(git_path)}"')
                sys.exit(1)

        print(Fore.GREEN + f'Initialized empty Pit repository in "{PurePath(git_path)}"')
        sys.exit()

    elif command == 'commit':
        # Commit objects to database in .git/objects/
        root_path = Path(os.getcwd())
        git_path = root_path / '.git'
        db_path = git_path / 'objects'
        
        workspace = Workspace(root_path)
        database = Database(db_path)
        # print(workspace.list_files())
        
        for pathname in workspace.list_files():
            print(f'-{pathname}') # Just to print the file been saved # Rework later
            file_content = workspace.read_file(pathname)
            blob = Blob(file_content)
            database.store(blob)

    elif command == 'test':
        # custom: run basic tests to check presence of basic .git structure folders
        import unittest
        import tests
        suite = unittest.TestLoader().loadTestsFromModule(tests)
        unittest.TextTestRunner(verbosity=2).run(suite)
    
    elif command == 'clean':
       # custom:  remove .git directory contents, now disabled for rework
       # hardcoded path for security
        root_path = Path('C:\\Users\\benca\\Documents\\Web\\git_building\\with_python\\pit') # careful if is os.getcwd() since I could delete other folders/files if I'm in the wrong place
        if '.git' in os.listdir(root_path):
            git_path = root_path / '.git'

            for _, dirs, files in os.walk(git_path):
                print(_, dirs, files)
                for name in files:
                    print(name)
                    # os.remove(os.path.join(git_path, name))
                for name in dirs:
                    print(name)
                    # os.rmdir(Path(git_path / name))
            # os.rmdir(git_path)
                    
    else:
        print(Fore.RED + f'pit: "{command}" is not a pit command.')
        sys.exit(1)
else:
    print(Fore.GREEN + f'pit: no command specified. Try with "init".')
    sys.exit(1)
