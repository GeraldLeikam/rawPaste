from lib.modules.config import Config
from lib.modules.config_sub_object import ConfigSubObject
import yaml

class ConfigReader:

    def __init__(self, config_file):
        config_file_input = self.__read_file__(config_file)
        self.config_dict = self.parse_config_file_input(config_file_input)


    def __read_file__(self, config_file: str) -> bytes:
        with open(config_file, 'rb') as reader:
            return reader.read()

    def parse_config_file_input(self, config_file_input: bytes) -> dict:
        return yaml.safe_load(config_file_input)

    def create_config_object(self, config_dict: dict) -> Config:
        temp_object = Config()
        for key in config_dict:
            temp_object._add_config_(config_name=key.lower(), config_value=ConfigSubObject(config_dict=config_dict[key]))
        return temp_object

    @property
    def config(self) -> Config:
        return self.create_config_object(config_dict=self.config_dict)
