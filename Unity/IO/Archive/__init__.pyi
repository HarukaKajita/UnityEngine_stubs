import typing, abc
from System import Array_1
from Unity.Content import ContentNamespace
from UnityEngine import CompressionType
from Unity.Jobs import JobHandle

class ArchiveFileInfo:
    Filename : str
    FileSize : int


class ArchiveFileInterface(abc.ABC):
    @staticmethod
    def GetMountedArchives(namespaceId: ContentNamespace) -> Array_1[ArchiveHandle]: ...
    @staticmethod
    def MountAsync(namespaceId: ContentNamespace, filePath: str, prefix: str) -> ArchiveHandle: ...


class ArchiveHandle:
    @property
    def Compression(self) -> CompressionType: ...
    @property
    def IsStreamed(self) -> bool: ...
    @property
    def JobHandle(self) -> JobHandle: ...
    @property
    def Status(self) -> ArchiveStatus: ...
    def GetFileInfo(self) -> Array_1[ArchiveFileInfo]: ...
    def GetMountPath(self) -> str: ...
    def Unmount(self) -> JobHandle: ...


class ArchiveStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    InProgress : ArchiveStatus # 0
    Complete : ArchiveStatus # 1
    Failed : ArchiveStatus # 2

