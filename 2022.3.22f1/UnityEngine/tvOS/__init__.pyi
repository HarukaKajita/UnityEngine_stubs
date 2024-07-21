import typing

class Device:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def advertisingIdentifier(cls) -> str: ...
    @classmethod
    @property
    def advertisingTrackingEnabled(cls) -> bool: ...
    @classmethod
    @property
    def generation(cls) -> DeviceGeneration: ...
    @classmethod
    @property
    def systemVersion(cls) -> str: ...
    @classmethod
    @property
    def vendorIdentifier(cls) -> str: ...
    @staticmethod
    def ResetNoBackupFlag(path: str) -> None: ...
    @staticmethod
    def SetNoBackupFlag(path: str) -> None: ...


class DeviceGeneration(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unknown : DeviceGeneration # 0
    AppleTV1Gen : DeviceGeneration # 1001
    AppleTVHD : DeviceGeneration # 1001
    AppleTV2Gen : DeviceGeneration # 1002
    AppleTV4K : DeviceGeneration # 1002
    AppleTV4K2Gen : DeviceGeneration # 1003
    AppleTV4K3Gen : DeviceGeneration # 1004


class Remote:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def allowExitToHome(cls) -> bool: ...
    @classmethod
    @allowExitToHome.setter
    def allowExitToHome(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def allowRemoteRotation(cls) -> bool: ...
    @classmethod
    @allowRemoteRotation.setter
    def allowRemoteRotation(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def reportAbsoluteDpadValues(cls) -> bool: ...
    @classmethod
    @reportAbsoluteDpadValues.setter
    def reportAbsoluteDpadValues(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def touchesEnabled(cls) -> bool: ...
    @classmethod
    @touchesEnabled.setter
    def touchesEnabled(cls, value: bool) -> bool: ...

