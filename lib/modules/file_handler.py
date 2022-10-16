from time import time
from zlib import crc32
from os.path import join
from os import listdir
from os import stat
from os import remove

class FileHandler:

    def __init__(self, config):
        self.storage_path = config.datastorage.path

    def put_file(self, data: bytes) -> str:
        while True:
            filename = f'{crc32(str(time()).encode("utf-8") + data):x}'
            if filename not in listdir(self.storage_path):
                break
        with open(join(self.storage_path, filename), 'wb') as writer:
            writer.write(data)
        return filename

    def get_file(self, filename):
        if filename in listdir(self.storage_path):
            with open(join(self.storage_path, filename), 'rb') as reader:
                return reader.read()
        return None

    def get_file_list(self):
        return listdir(self.storage_path)

    def get_creation_time(self, file):
        return stat(join(self.storage_path, file)).st_ctime

    def delete_file(self, file):
        try:
            remove(join(self.storage_path, file))
        except:
            pass
