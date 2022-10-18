from time import time
from time import sleep

class Cleaner():

    def __init__(self, config, file_handler):
        expire_time = self.convert_time_to_seconds(config.datastorage.expiretime)
        cleaner_execution_time = self.convert_time_to_seconds(config.datastorage.cleanerexecutiontime)
        data_storage = config.paths.datastorage
        self.file_handler = file_handler
        if config.datastorage.filesexpires:
            self.handle(data_storage=data_storage, expire_time=expire_time, execution_time=cleaner_execution_time)

    def handle(self, data_storage, expire_time, execution_time):
        while True:
            if len(self.file_handler.get_file_list(path=data_storage)) > 0:
                for file in self.file_handler.get_file_list(path=data_storage):
                    if time() > (self.file_handler.get_creation_time(path=data_storage, filename=file) + expire_time):
                        self.file_handler.delete_file(file)
            sleep(execution_time)

    def convert_time_to_seconds(self, expire_time):
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