import typing, abc
from System import MulticastDelegate, IAsyncResult, AsyncCallback, Array_1
from System.Reflection import MethodInfo
from UnityEngine import Color32, Rect, Vector2

class AppCallbackItem(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class Application:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def advertisingIdentifier(cls) -> str: ...
    @classmethod
    @property
    def arguments(cls) -> str: ...
    @staticmethod
    def InvokeOnAppThread(item: AppCallbackItem, waitUntilDone: bool) -> None: ...
    @staticmethod
    def InvokeOnUIThread(item: AppCallbackItem, waitUntilDone: bool) -> None: ...
    @staticmethod
    def RunningOnAppThread() -> bool: ...
    @staticmethod
    def RunningOnUIThread() -> bool: ...


class Cursor(abc.ABC):
    @staticmethod
    def SetCustomCursor(id: int) -> None: ...


class Folder(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Installation : Folder # 0
    Temporary : Folder # 1
    Local : Folder # 2
    Roaming : Folder # 3
    CameraRoll : Folder # 4
    DocumentsLibrary : Folder # 5
    HomeGroup : Folder # 6
    MediaServerDevices : Folder # 7
    MusicLibrary : Folder # 8
    PicturesLibrary : Folder # 9
    Playlists : Folder # 10
    RemovableDevices : Folder # 11
    SavedPictures : Folder # 12
    VideosLibrary : Folder # 13


class Launcher:
    def __init__(self) -> None: ...
    @staticmethod
    def LaunchFile(folder: Folder, relativeFilePath: str, showWarning: bool) -> None: ...
    @staticmethod
    def LaunchFileWithPicker(fileExtension: str) -> None: ...
    @staticmethod
    def LaunchUri(uri: str, showWarning: bool) -> None: ...


class SecondaryTileData:
    def __init__(self, id: str, displayName: str) -> None: ...
    arguments : str
    backgroundColorSet : bool
    displayName : str
    foregroundText : TileForegroundText
    lockScreenBadgeLogo : str
    lockScreenDisplayBadgeAndTileText : bool
    phoneticName : str
    roamingEnabled : bool
    showNameOnSquare150x150Logo : bool
    showNameOnSquare310x310Logo : bool
    showNameOnWide310x150Logo : bool
    square150x150Logo : str
    square30x30Logo : str
    square310x310Logo : str
    square70x70Logo : str
    tileId : str
    wide310x150Logo : str
    @property
    def backgroundColor(self) -> Color32: ...
    @backgroundColor.setter
    def backgroundColor(self, value: Color32) -> Color32: ...


class Tile:
    @property
    def exists(self) -> bool: ...
    @property
    def hasUserConsent(self) -> bool: ...
    @property
    def id(self) -> str: ...
    @classmethod
    @property
    def main(cls) -> Tile: ...
    @staticmethod
    def Exists(tileId: str) -> bool: ...
    @staticmethod
    def GetSecondaries() -> Array_1[Tile]: ...
    @staticmethod
    def GetSecondary(tileId: str) -> Tile: ...
    @staticmethod
    def GetTemplate(templ: TileTemplate) -> str: ...
    def PeriodicBadgeUpdate(self, uri: str, interval: float) -> None: ...
    def PeriodicUpdate(self, uri: str, interval: float) -> None: ...
    def RemoveBadge(self) -> None: ...
    def StopPeriodicBadgeUpdate(self) -> None: ...
    def StopPeriodicUpdate(self) -> None: ...
    def UpdateBadgeImage(self, image: str) -> None: ...
    def UpdateBadgeNumber(self, number: float) -> None: ...
    # Skipped CreateOrUpdateSecondary due to it being static, abstract and generic.

    CreateOrUpdateSecondary : CreateOrUpdateSecondary_MethodGroup
    class CreateOrUpdateSecondary_MethodGroup:
        @typing.overload
        def __call__(self, data: SecondaryTileData) -> Tile:...
        @typing.overload
        def __call__(self, data: SecondaryTileData, area: Rect) -> Tile:...
        @typing.overload
        def __call__(self, data: SecondaryTileData, pos: Vector2) -> Tile:...

    # Skipped Delete due to it being static, abstract and generic.

    Delete : Delete_MethodGroup
    class Delete_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, area: Rect) -> None:...
        @typing.overload
        def __call__(self, pos: Vector2) -> None:...

    # Skipped DeleteSecondary due to it being static, abstract and generic.

    DeleteSecondary : DeleteSecondary_MethodGroup
    class DeleteSecondary_MethodGroup:
        @typing.overload
        def __call__(self, tileId: str) -> None:...
        @typing.overload
        def __call__(self, tileId: str, area: Rect) -> None:...
        @typing.overload
        def __call__(self, tileId: str, pos: Vector2) -> None:...

    # Skipped Update due to it being static, abstract and generic.

    Update : Update_MethodGroup
    class Update_MethodGroup:
        @typing.overload
        def __call__(self, xml: str) -> None:...
        @typing.overload
        def __call__(self, medium: str, wide: str, large: str, text: str) -> None:...



class TileForegroundText(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Dark : TileForegroundText # 0
    Light : TileForegroundText # 1
    Default : TileForegroundText # -1


class TileTemplate(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TileSquare150x150Image : TileTemplate # 0
    TileSquare150x150Block : TileTemplate # 1
    TileSquare150x150Text01 : TileTemplate # 2
    TileSquare150x150Text02 : TileTemplate # 3
    TileSquare150x150Text03 : TileTemplate # 4
    TileSquare150x150Text04 : TileTemplate # 5
    TileSquare150x150PeekImageAndText01 : TileTemplate # 6
    TileSquare150x150PeekImageAndText02 : TileTemplate # 7
    TileSquare150x150PeekImageAndText03 : TileTemplate # 8
    TileSquare150x150PeekImageAndText04 : TileTemplate # 9
    TileWide310x150Image : TileTemplate # 10
    TileWide310x150ImageCollection : TileTemplate # 11
    TileWide310x150ImageAndText01 : TileTemplate # 12
    TileWide310x150ImageAndText02 : TileTemplate # 13
    TileWide310x150BlockAndText01 : TileTemplate # 14
    TileWide310x150BlockAndText02 : TileTemplate # 15
    TileWide310x150PeekImageCollection01 : TileTemplate # 16
    TileWide310x150PeekImageCollection02 : TileTemplate # 17
    TileWide310x150PeekImageCollection03 : TileTemplate # 18
    TileWide310x150PeekImageCollection04 : TileTemplate # 19
    TileWide310x150PeekImageCollection05 : TileTemplate # 20
    TileWide310x150PeekImageCollection06 : TileTemplate # 21
    TileWide310x150PeekImageAndText01 : TileTemplate # 22
    TileWide310x150PeekImageAndText02 : TileTemplate # 23
    TileWide310x150PeekImage01 : TileTemplate # 24
    TileWide310x150PeekImage02 : TileTemplate # 25
    TileWide310x150PeekImage03 : TileTemplate # 26
    TileWide310x150PeekImage04 : TileTemplate # 27
    TileWide310x150PeekImage05 : TileTemplate # 28
    TileWide310x150PeekImage06 : TileTemplate # 29
    TileWide310x150SmallImageAndText01 : TileTemplate # 30
    TileWide310x150SmallImageAndText02 : TileTemplate # 31
    TileWide310x150SmallImageAndText03 : TileTemplate # 32
    TileWide310x150SmallImageAndText04 : TileTemplate # 33
    TileWide310x150SmallImageAndText05 : TileTemplate # 34
    TileWide310x150Text01 : TileTemplate # 35
    TileWide310x150Text02 : TileTemplate # 36
    TileWide310x150Text03 : TileTemplate # 37
    TileWide310x150Text04 : TileTemplate # 38
    TileWide310x150Text05 : TileTemplate # 39
    TileWide310x150Text06 : TileTemplate # 40
    TileWide310x150Text07 : TileTemplate # 41
    TileWide310x150Text08 : TileTemplate # 42
    TileWide310x150Text09 : TileTemplate # 43
    TileWide310x150Text10 : TileTemplate # 44
    TileWide310x150Text11 : TileTemplate # 45
    TileSquare310x310BlockAndText01 : TileTemplate # 46
    TileSquare310x310BlockAndText02 : TileTemplate # 47
    TileSquare310x310Image : TileTemplate # 48
    TileSquare310x310ImageAndText01 : TileTemplate # 49
    TileSquare310x310ImageAndText02 : TileTemplate # 50
    TileSquare310x310ImageAndTextOverlay01 : TileTemplate # 51
    TileSquare310x310ImageAndTextOverlay02 : TileTemplate # 52
    TileSquare310x310ImageAndTextOverlay03 : TileTemplate # 53
    TileSquare310x310ImageCollectionAndText01 : TileTemplate # 54
    TileSquare310x310ImageCollectionAndText02 : TileTemplate # 55
    TileSquare310x310ImageCollection : TileTemplate # 56
    TileSquare310x310SmallImagesAndTextList01 : TileTemplate # 57
    TileSquare310x310SmallImagesAndTextList02 : TileTemplate # 58
    TileSquare310x310SmallImagesAndTextList03 : TileTemplate # 59
    TileSquare310x310SmallImagesAndTextList04 : TileTemplate # 60
    TileSquare310x310Text01 : TileTemplate # 61
    TileSquare310x310Text02 : TileTemplate # 62
    TileSquare310x310Text03 : TileTemplate # 63
    TileSquare310x310Text04 : TileTemplate # 64
    TileSquare310x310Text05 : TileTemplate # 65
    TileSquare310x310Text06 : TileTemplate # 66
    TileSquare310x310Text07 : TileTemplate # 67
    TileSquare310x310Text08 : TileTemplate # 68
    TileSquare310x310TextList01 : TileTemplate # 69
    TileSquare310x310TextList02 : TileTemplate # 70
    TileSquare310x310TextList03 : TileTemplate # 71
    TileSquare310x310SmallImageAndText01 : TileTemplate # 72
    TileSquare310x310SmallImagesAndTextList05 : TileTemplate # 73
    TileSquare310x310Text09 : TileTemplate # 74
    TileSquare71x71IconWithBadge : TileTemplate # 75
    TileSquare150x150IconWithBadge : TileTemplate # 76
    TileWide310x150IconWithBadgeAndText : TileTemplate # 77
    TileSquare71x71Image : TileTemplate # 78
    TileTall150x310Image : TileTemplate # 79
    TileSquare99x99IconWithBadge : TileTemplate # 1000
    TileSquare210x210IconWithBadge : TileTemplate # 1001
    TileWide432x210IconWithBadgeAndText : TileTemplate # 1002


class Toast:
    @property
    def activated(self) -> bool: ...
    @property
    def arguments(self) -> str: ...
    @arguments.setter
    def arguments(self, value: str) -> str: ...
    @property
    def dismissed(self) -> bool: ...
    @property
    def dismissedByUser(self) -> bool: ...
    @staticmethod
    def GetTemplate(templ: ToastTemplate) -> str: ...
    def Hide(self) -> None: ...
    def Show(self) -> None: ...
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self, xml: str) -> Toast:...
        @typing.overload
        def __call__(self, image: str, text: str) -> Toast:...



class ToastTemplate(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ToastImageAndText01 : ToastTemplate # 0
    ToastImageAndText02 : ToastTemplate # 1
    ToastImageAndText03 : ToastTemplate # 2
    ToastImageAndText04 : ToastTemplate # 3
    ToastText01 : ToastTemplate # 4
    ToastText02 : ToastTemplate # 5
    ToastText03 : ToastTemplate # 6
    ToastText04 : ToastTemplate # 7


class WindowActivated(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, state: WindowActivationState, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, state: WindowActivationState) -> None: ...


class WindowActivationState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    CodeActivated : WindowActivationState # 0
    Deactivated : WindowActivationState # 1
    PointerActivated : WindowActivationState # 2


class WindowSizeChanged(MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, width: int, height: int, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, width: int, height: int) -> None: ...

