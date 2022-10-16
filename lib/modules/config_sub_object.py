from ..templates.config_template import ConfigTemplate

class ConfigSubObject():
    def __init__(self, config_dict: dict):
        for key, value in config_dict.items():
            self.__setattr__(key.lower(), value)
