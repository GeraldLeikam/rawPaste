from time import time
from time import sleep

class Cleaner():

    def __init__(self, config, file_handler):
        expire_time = self.convert_expire_time_to_seconds(config.datastorage.expires)
        self.file_handler = file_handler
        self.handle(expire_time=expire_time)

    def handle(self, expire_time):
        while True:
            if len(self.file_handler.get_file_list()) > 0:
                for file in self.file_handler.get_file_list():
                    if time() > (self.file_handler.get_creation_time(file) + expire_time):
                        self.file_handler.delete_file(file)
            sleep(300)

    def convert_expire_time_to_seconds(self, expire_time):
        if 's' in expire_time.lower():
            return int(expire_time.lower().strip('s'))
        if 'm' in expire_time.lower():
            return int(expire_time.lower().strip('m')) * 60
        if 'h' in expire_time.lower():
            return int(expire_time.lower().strip('h')) * 3600
        if 'd' in expire_time.lower():
            return int(expire_time.lower().strip('d')) * 86400
        if 'w' in expire_time.lower():
            return int(expire_time.lower().strip('w')) * 604800
        return int(expire_time.lower().strip('d')) * 86400