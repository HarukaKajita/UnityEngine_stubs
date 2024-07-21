import typing, abc
from System import Array_1, Action_1, Action_2
from UnityEngine import CustomYieldInstruction, AndroidJavaProxy, AndroidJavaClass

class AndroidAssetPackError(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NoError : AndroidAssetPackError # 0
    InternalError : AndroidAssetPackError # -100
    AppNotOwned : AndroidAssetPackError # -13
    NetworkUnrestricted : AndroidAssetPackError # -12
    PlayStoreNotFound : AndroidAssetPackError # -11
    InsufficientStorage : AndroidAssetPackError # -10
    AccessDenied : AndroidAssetPackError # -7
    NetworkError : AndroidAssetPackError # -6
    ApiNotAvailable : AndroidAssetPackError # -5
    DownloadNotFound : AndroidAssetPackError # -4
    InvalidRequest : AndroidAssetPackError # -3
    PackUnavailable : AndroidAssetPackError # -2
    AppUnavailable : AndroidAssetPackError # -1


class AndroidAssetPackInfo:
    @property
    def bytesDownloaded(self) -> int: ...
    @property
    def error(self) -> AndroidAssetPackError: ...
    @property
    def name(self) -> str: ...
    @property
    def size(self) -> int: ...
    @property
    def status(self) -> AndroidAssetPackStatus: ...
    @property
    def transferProgress(self) -> float: ...


class AndroidAssetPacks(abc.ABC):
    @classmethod
    @property
    def coreUnityAssetPacksDownloaded(cls) -> bool: ...
    @staticmethod
    def CancelAssetPackDownload(assetPackNames: Array_1[str]) -> None: ...
    @staticmethod
    def GetAssetPackPath(assetPackName: str) -> str: ...
    @staticmethod
    def GetCoreUnityAssetPackNames() -> Array_1[str]: ...
    @staticmethod
    def RemoveAssetPack(assetPackName: str) -> None: ...
    # Skipped DownloadAssetPackAsync due to it being static, abstract and generic.

    DownloadAssetPackAsync : DownloadAssetPackAsync_MethodGroup
    class DownloadAssetPackAsync_MethodGroup:
        @typing.overload
        def __call__(self, assetPackNames: Array_1[str]) -> DownloadAssetPackAsyncOperation:...
        @typing.overload
        def __call__(self, assetPackNames: Array_1[str], callback: Action_1[AndroidAssetPackInfo]) -> None:...

    # Skipped GetAssetPackStateAsync due to it being static, abstract and generic.

    GetAssetPackStateAsync : GetAssetPackStateAsync_MethodGroup
    class GetAssetPackStateAsync_MethodGroup:
        @typing.overload
        def __call__(self, assetPackNames: Array_1[str]) -> GetAssetPackStateAsyncOperation:...
        @typing.overload
        def __call__(self, assetPackNames: Array_1[str], callback: Action_2[int, Array_1[AndroidAssetPackState]]) -> None:...

    # Skipped RequestToUseMobileDataAsync due to it being static, abstract and generic.

    RequestToUseMobileDataAsync : RequestToUseMobileDataAsync_MethodGroup
    class RequestToUseMobileDataAsync_MethodGroup:
        @typing.overload
        def __call__(self) -> RequestToUseMobileDataAsyncOperation:...
        @typing.overload
        def __call__(self, callback: Action_1[AndroidAssetPackUseMobileDataRequestResult]) -> None:...



class AndroidAssetPackState:
    @property
    def error(self) -> AndroidAssetPackError: ...
    @property
    def name(self) -> str: ...
    @property
    def status(self) -> AndroidAssetPackStatus: ...


class AndroidAssetPackStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unknown : AndroidAssetPackStatus # 0
    Pending : AndroidAssetPackStatus # 1
    Downloading : AndroidAssetPackStatus # 2
    Transferring : AndroidAssetPackStatus # 3
    Completed : AndroidAssetPackStatus # 4
    Failed : AndroidAssetPackStatus # 5
    Canceled : AndroidAssetPackStatus # 6
    WaitingForWifi : AndroidAssetPackStatus # 7
    NotInstalled : AndroidAssetPackStatus # 8


class AndroidAssetPackUseMobileDataRequestResult:
    @property
    def allowed(self) -> bool: ...


class AndroidDevice:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def hardwareType(cls) -> AndroidHardwareType: ...
    @staticmethod
    def SetSustainedPerformanceMode(enabled: bool) -> None: ...


class AndroidHardwareType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Generic : AndroidHardwareType # 0
    ChromeOS : AndroidHardwareType # 1


class DiagnosticsReporting(abc.ABC):
    @staticmethod
    def CallReportFullyDrawn() -> None: ...


class DownloadAssetPackAsyncOperation(CustomYieldInstruction):
    @property
    def Current(self) -> typing.Any: ...
    @property
    def downloadedAssetPacks(self) -> Array_1[str]: ...
    @property
    def downloadFailedAssetPacks(self) -> Array_1[str]: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def keepWaiting(self) -> bool: ...
    @property
    def progress(self) -> float: ...


class GetAssetPackStateAsyncOperation(CustomYieldInstruction):
    @property
    def Current(self) -> typing.Any: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def keepWaiting(self) -> bool: ...
    @property
    def size(self) -> int: ...
    @property
    def states(self) -> Array_1[AndroidAssetPackState]: ...


class Permission:
    Camera : str
    CoarseLocation : str
    ExternalStorageRead : str
    ExternalStorageWrite : str
    FineLocation : str
    Microphone : str
    @staticmethod
    def HasUserAuthorizedPermission(permission: str) -> bool: ...
    # Skipped RequestUserPermission due to it being static, abstract and generic.

    RequestUserPermission : RequestUserPermission_MethodGroup
    class RequestUserPermission_MethodGroup:
        @typing.overload
        def __call__(self, permission: str) -> None:...
        @typing.overload
        def __call__(self, permission: str, callbacks: PermissionCallbacks) -> None:...

    # Skipped RequestUserPermissions due to it being static, abstract and generic.

    RequestUserPermissions : RequestUserPermissions_MethodGroup
    class RequestUserPermissions_MethodGroup:
        @typing.overload
        def __call__(self, permissions: Array_1[str]) -> None:...
        @typing.overload
        def __call__(self, permissions: Array_1[str], callbacks: PermissionCallbacks) -> None:...



class PermissionCallbacks(AndroidJavaProxy):
    def __init__(self) -> None: ...
    javaInterface : AndroidJavaClass


class RequestToUseMobileDataAsyncOperation(CustomYieldInstruction):
    @property
    def Current(self) -> typing.Any: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def keepWaiting(self) -> bool: ...
    @property
    def result(self) -> AndroidAssetPackUseMobileDataRequestResult: ...

