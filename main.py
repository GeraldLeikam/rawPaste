from lib.modules.config_reader import ConfigReader
from lib.modules.webserver import Webserver
from lib.modules.netcat_server import NetcatServer
from lib.modules.file_handler import FileHandler
from lib.modules.cleaner import Cleaner
from threading import Thread

config_file = './config/config.yaml'

def main(config_file):
    config = ConfigReader(config_file=config_file).config
    file_handler = FileHandler(config=config)
    Thread(target=NetcatServer, args=(config, file_handler)).start()
    Thread(target=Webserver, args=(config, file_handler)).start()
    Thread(target=Cleaner, args=(config, file_handler)).start()

if __name__ == '__main__':
    main(config_file=config_file)
