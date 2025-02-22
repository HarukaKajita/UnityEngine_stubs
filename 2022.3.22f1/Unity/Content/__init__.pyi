from System import Array_1

class ContentNamespace:
    @classmethod
    @property
    def Default(cls) -> ContentNamespace: ...
    @property
    def IsValid(self) -> bool: ...
    def Delete(self) -> None: ...
    @staticmethod
    def GetAll() -> Array_1[ContentNamespace]: ...
    def GetName(self) -> str: ...
    @staticmethod
    def GetOrCreateNamespace(name: str) -> ContentNamespace: ...

