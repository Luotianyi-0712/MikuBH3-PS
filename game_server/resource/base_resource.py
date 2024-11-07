from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T", bound="BaseResource")

@dataclass
class BaseResource(ABC):
    def on_load(self: T) -> bool:
        """returns True by default if item loaded, otherwise will be skipped"""
        return True

    @abstractmethod
    def get_index(self) -> str:
        pass
