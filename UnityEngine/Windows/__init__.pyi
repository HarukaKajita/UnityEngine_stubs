import typing, clr, abc
from System import Array_1

class CrashReporting(abc.ABC):
    @classmethod
    @property
    def crashReportFolder(cls) -> str: ...


class Crypto(abc.ABC):
    @staticmethod
    def ComputeMD5Hash(buffer: Array_1[int]) -> Array_1[int]: ...
    @staticmethod
    def ComputeSHA1Hash(buffer: Array_1[int]) -> Array_1[int]: ...


class Directory(abc.ABC):
    @classmethod
    @property
    def localFolder(cls) -> str: ...
    @classmethod
    @property
    def roamingFolder(cls) -> str: ...
    @classmethod
    @property
    def temporaryFolder(cls) -> str: ...
    @staticmethod
    def CreateDirectory(path: str) -> None: ...
    @staticmethod
    def Delete(path: str) -> None: ...
    @staticmethod
    def Exists(path: str) -> bool: ...


class File(abc.ABC):
    @staticmethod
    def Delete(path: str) -> None: ...
    @staticmethod
    def Exists(path: str) -> bool: ...
    @staticmethod
    def ReadAllBytes(path: str) -> Array_1[int]: ...
    @staticmethod
    def WriteAllBytes(path: str, bytes: Array_1[int]) -> None: ...


class Input(abc.ABC):
    # Skipped ForwardRawInput due to it being static, abstract and generic.

    ForwardRawInput : ForwardRawInput_MethodGroup
    class ForwardRawInput_MethodGroup:
        @typing.overload
        def __call__(self, rawInputHeaderIndices: int, rawInputDataIndices: int, indicesCount: int, rawInputData: int, rawInputDataSize: int) -> None:...
        @typing.overload
        def __call__(self, rawInputHeaderIndices: clr.Reference[int], rawInputDataIndices: clr.Reference[int], indicesCount: int, rawInputData: clr.Reference[int], rawInputDataSize: int) -> None:...



class LicenseInformation(abc.ABC):
    @classmethod
    @property
    def isOnAppTrial(cls) -> bool: ...
    @staticmethod
    def PurchaseApp() -> str: ...

