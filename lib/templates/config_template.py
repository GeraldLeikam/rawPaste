class ConfigTemplate:

    def __init__(self, config_dict: dict):
        for key, val in config_dict.items():
            print(key + ': ' + val)