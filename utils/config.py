from dataclasses import asdict, dataclass
import os
import json
from dacite import from_dict


@dataclass
class ServerConfig:
    IP: str
    Port: int


@dataclass
class ConfigData:
    LogLevel: str
    GameServer: ServerConfig
    SDKServer: ServerConfig
    VerboseLevel: int
    RegionName: str
    UseLocalCache: bool
    AESKeys: dict[str, str]
    EnableDispatchEncryption: bool
    HotpatchConfig: dict[str, dict]

    def write_default_config():
        config = ConfigData(
            LogLevel="INFO",
            GameServer=ServerConfig(IP="127.0.0.1", Port=16100),
            SDKServer=ServerConfig(IP="127.0.0.1", Port=80),
            VerboseLevel=1,
            RegionName="MikuBH3",
            UseLocalCache=False,
            EnableDispatchEncryption=True,
            AESKeys={
                "7.9.0": "36 31 65 37 64 33 65 66 33 32 30 63 31 35 66 66 61 64 37 61 66 32 31 34 61 64 65 64 32 34 33 38",
                "7.8.0": "64 34 32 33 30 30 31 62 32 36 38 34 62 33 62 30 61 33 30 38 66 37 65 35 63 30 61 38 66 33 65 32"
            },
            HotpatchConfig=dict(),
        )
        with open("Config.json", "w") as f:
            f.write(json.dumps(asdict(config), indent=2))

        return config

    def load():
        if not os.path.exists("Config.json"):
            return ConfigData.write_default_config()

        with open("Config.json", "r", encoding="utf-8") as f:
            try:
                return from_dict(ConfigData, json.load(f))
            except Exception:
                return ConfigData.write_default_config()

    def get_aes_key(self, version: str):
        return self.AESKeys[version.split("_")[0]]

    def get_hotpatch_manifest(self, version: str):
        return self.HotpatchConfig.get(version, dict()).get("manifest", dict())

    def get_hotpatch_ext(self, version: str):
        return self.HotpatchConfig.get(version, dict()).get("ext", dict())


Config = ConfigData.load()
