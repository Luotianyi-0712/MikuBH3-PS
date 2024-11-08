import json
import traceback
from typing import Dict, Type, TypeVar, Optional, Any, List

from utils.logger import Error, Info
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import resource_registry
import game_server.resource.configdb  # noqa: F401

T = TypeVar("T", bound=BaseResource)


def filter_data(cls: Type, data):
    valid_fields = cls.__annotations__.keys()
    return {field: data.get(field, None) for field in valid_fields}


class ResourceManager:
    def __init__(self):
        self.data: Dict[Type[T], Dict[Any, T]] = {}

    def load_resources(self) -> None:
        Info("[BOOT] [ResourceManager] Loading Resourcses...")
        sorted_load_priority = dict(
            sorted(resource_registry.items(), key=lambda item: item[1]["load_priority"])
        ).items()
        for cls, metadata in sorted_load_priority:
            path = metadata["path"]
            try:
                with open(path, "r", encoding="utf-8") as file:
                    raw_data = json.load(file)
            except Exception:
                Error(f"Error when loading resource {path}")
                traceback.print_exc()
                continue

            self.data[cls] = {}
            i = 0
            for data in raw_data:
                data = filter_data(cls, data)
                item: T = cls(**data)
                if not item.on_load():
                    continue
                i += 1
                index_value = item.get_index()
                self.data[cls][index_value] = item
            Info(f"[BOOT] [ResourceManager] Loaded {i} config(s) for {cls.__name__}")

    def find_by_index(self, cls: Type[T], value: Any) -> Optional[T]:
        return self.data.get(cls, {}).get(str(value))

    def has_index(self, cls: Type[T], value: Any) -> bool:
        return value in self.data.get(cls, {})

    def values(self, cls: Type[T]) -> List[T]:
        return list(self.data.get(cls, {}).values())

    @staticmethod
    def instance():
        return resource_manager


resource_manager = ResourceManager()
