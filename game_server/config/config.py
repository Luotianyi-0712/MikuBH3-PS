import os
import json
from dynaconf import Dynaconf

# 此处设置默认值
Root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ConfigData = {
    "LogLevel": "INFO",
    "MaxSessions": 10,
    "GameServer": {
        "Ip": "127.0.0.1",
        "Port": 16100
    },
    "SdkServer": {
        "Ip": "127.0.0.1",
        "Port": 80
    },
    "VerboseLevel":1,
    "RegionName":"MikuBH3",
    "UseLocalCache":False
}

class ConfigInit:
    def __init__(self):
        self.ConfigPath = f"{Root}/../Config.json"
        self.ConfigData = self.Load()

        if not os.path.exists(self.ConfigPath):
            with open(self.ConfigPath, 'w') as f:
                json.dump(ConfigData, f, indent=4)

    def Load(self):
        Settings = Dynaconf(
            settings_files = [self.ConfigPath],
            default_settings = ConfigData
        )
        return Settings

    def Get(self):
        return self.ConfigData

Config = ConfigInit().Load()