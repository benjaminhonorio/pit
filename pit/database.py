import hashlib
import zlib
from pathlib import Path
import string, random


class Database:

    def __init__(self, pathname):
        self.pathname = pathname
    
    def store(self, file_obj):
        file_obj_contents = str(file_obj)
        encoded_content = f'{file_obj.type()} {len(file_obj_contents)}\0{file_obj_contents}'.encode()
        file_obj.oid = hashlib.sha1(encoded_content).hexdigest()
        self.__write_obj(file_obj.oid, encoded_content)

    def __write_obj(self, oid, content):
        obj_path = self.pathname / oid[:2] / oid[2:]
        dirname = Path(obj_path).parent.absolute()
        temp_path = dirname / self.__generate_temp_name()
        try:
            f = open(temp_path, 'rb+')
        except FileNotFoundError:
            try:
                Path.mkdir(dirname)
                f = open(temp_path, 'wb+')
            except FileExistsError:
                f = open(temp_path, 'wb+')
        compressed = zlib.compress(content)
        f.write(compressed)
        f.close()

        try:
            Path(temp_path).rename(obj_path)
            print(oid)
        except FileExistsError:
            print("File name already exists")
            
    def __generate_temp_name(self):
        return f'tmp_obj_{"".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))}'
