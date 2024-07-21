import abc

class PurchasingSettings(abc.ABC):
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @enabled.setter
    def enabled(cls, value: bool) -> bool: ...

