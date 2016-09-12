import json


class ConfigOptionNotExist(Exception):
    def __init__(self, option):
        self.option = option

    def __repr__(self):
        return "Config option {} not exist".format(self.option)


class ConfigLoader:
    def __init__(self, auto_reload=False):
        self.auto_reload = auto_reload
        self._set_config()

    def _set_config(self, config_file='./config.json'):
        self.config_file = config_file
        with open(config_file) as cf:
            config = json.loads(cf.read())

        self.config = config

    def __getattr__(self, item):
        if self.auto_reload:
            self._set_config()

        return self.config.get(item)

    def update_config(self, **kwargs):
        # for key in kwargs.keys():
        #     if key not in self.config:
        #         raise ConfigOptionNotExist(key)
        self.config.update(kwargs)

    def __repr__(self):
        return '<ConfigLoader: {}>'.format(self.config_file)

config = ConfigLoader()