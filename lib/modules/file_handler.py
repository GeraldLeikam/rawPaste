from time import time
from zlib import crc32
from os.path import join
from os import listdir
from os import stat
from os import remove
from os.path import exists

class FileHandler:

    storages = {}

    def __init__(self, config):
        self.storage_path = config.paths.datastorage

    def check_path(self, path: str) -> bool:
        if exists(path):
            return True
        return False

    def check_file(self, path: str, filename: str) -> bool:
        return self.check_path(join(path, filename))

    def put_file(self, path: str, data: bytes) -> any:
        while True:
            filename = f'{crc32(str(time()).encode("utf-8") + data):x}'
            if filename not in listdir(path):
                with open(join(path, filename), 'wb') as writer:
                    writer.write(data)
                break
        if self.check_file(path=path, filename=filename):
            return filename
        return None

    def get_file(self, path: str, filename: str) -> any:
        if filename in listdir(path):
            with open(join(path, filename), 'rb') as reader:
                return reader.read()
        return None

    def get_file_list(self, path: str) -> list[str]:
        return listdir(path)

    def get_creation_time(self, path: str, filename: str) -> float:
        return stat(join(path, filename)).st_ctime

    def delete_file(self, path: str, filename: str) -> bool:
        try:
            remove(join(path, filename))
            if not self.check_file(path, filename):
                return True
        except:
            return False
