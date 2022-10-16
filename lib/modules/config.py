class Config:

    def _add_config_(self, config_name: str, config_value):
        self.__setattr__(config_name, config_value)
