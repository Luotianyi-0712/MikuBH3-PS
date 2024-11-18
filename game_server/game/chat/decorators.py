from typing import Dict, Type


command_registry: Dict[str, Type] = {}


def Command(prefix: str, usage: str, aliases: list = list()):
    def decorator(func):
        func.usage = usage
        func.prefix = prefix
        func.is_alias = False
        command_registry[prefix] = func

        # Register alias if exist
        for alias in aliases:
            func.is_alias = True
            command_registry[alias] = func

        return func

    return decorator
