from typing import Type, Dict

resource_registry: Dict[Type, Dict[str, any]] = {}


class LoadPriority:
    HIGH = 1
    NORMAL = 2
    LOW = 3


def GameResource(path: str, load_priority=LoadPriority.NORMAL):
    def decorator(cls):
        resource_registry[cls] = {"path": path, "load_priority": load_priority}
        return cls

    return decorator
