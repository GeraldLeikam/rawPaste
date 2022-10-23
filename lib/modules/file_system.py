from os.path import exists
from os.path import join
from os import remove
from time import time
from zlib import crc32
import random

def path_exists(path: str) -> bool:
    return exists(path)

def file_exists(path: str, filename: str) -> bool:
    if path_exists(path=path):
        return exists(join(path, filename))
    return False

def generate_filename() -> str:
    rand = random
    rand.seed(time())
    filename = f''
    for i in range(0, 64):
        filename = f'{filename}{rand.randint(0, 9)}'
    filename = f'{crc32(str(time()).encode("utf-8") + filename.encode("utf-8")):x}'
    return filename

def read_file(path: str, filename: str) -> bytes:
    file_content = b''
    if file_exists(path=path, filename=filename):
        try:
            with open(join(path, filename), 'rb') as reader:
                file_content = reader.read()
        except:
            file_content = b''
        finally:
            return file_content
    else:
        return file_content

def write_file(path: str, filename: str, content: bytes) -> bool:
    result = False
    if not file_exists(path=path, filename=filename):
        try:
            with open(join(path, filename), 'wb') as writer:
                writer.write(content)
            result = True
        except:
            result = False
        finally:
            return result
    return result

def delete_file(path: str, filename: str) -> bool:
    result = False
    if file_exists(path=path, filename=filename):
        try:
            remove(join(path, filename))
            if not file_exists(path=path, filename=filename):
                result = True
            else:
                result = False
        except:
            result = False
        finally:
            return result
    else:
        return result