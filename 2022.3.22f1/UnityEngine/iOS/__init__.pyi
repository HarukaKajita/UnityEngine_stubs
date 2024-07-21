import typing, abc
from UnityEngine import Vector2, AsyncOperation
from System import MulticastDelegate, IAsyncResult, AsyncCallback, Array_1, IDisposable
from System.Reflection import MethodInfo

class ActivityIndicatorStyle(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    WhiteLarge : ActivityIndicatorStyle # 0
    White : ActivityIndicatorStyle # 1
    Gray : ActivityIndicatorStyle # 2
    DontShow : ActivityIndicatorStyle # -1


class ADBannerView:
    def __init__(self, type: ADBannerView.Type, layout: ADBannerView.Layout) -> None: ...
    @property
    def layout(self) -> ADBannerView.Layout: ...
    @layout.setter
    def layout(self, value: ADBannerView.Layout) -> ADBannerView.Layout: ...
    @property
    def loaded(self) -> bool: ...
    @property
    def position(self) -> Vector2: ...
    @position.setter
    def position(self, value: Vector2) -> Vector2: ...
    @property
    def size(self) -> Vector2: ...
    @property
    def visible(self) -> bool: ...
    @visible.setter
    def visible(self, value: bool) -> bool: ...
    @staticmethod
    def IsAvailable(type: ADBannerView.Type) -> bool: ...

    class BannerFailedToLoadDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...


    class BannerWasClickedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...


    class BannerWasLoadedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...


    class Layout(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Top : ADBannerView.Layout # 0
        TopLeft : ADBannerView.Layout # 0
        BottomLeft : ADBannerView.Layout # 1
        Bottom : ADBannerView.Layout # 1
        CenterLeft : ADBannerView.Layout # 2
        TopRight : ADBannerView.Layout # 4
        BottomRight : ADBannerView.Layout # 5
        CenterRight : ADBannerView.Layout # 6
        TopCenter : ADBannerView.Layout # 8
        BottomCenter : ADBannerView.Layout # 9
        Center : ADBannerView.Layout # 10
        Manual : ADBannerView.Layout # -1


    class Type(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Banner : ADBannerView.Type # 0
        MediumRect : ADBannerView.Type # 1



class ADInterstitialAd:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, autoReload: bool) -> None: ...
    @classmethod
    @property
    def isAvailable(cls) -> bool: ...
    @property
    def loaded(self) -> bool: ...
    def ReloadAd(self) -> None: ...
    def Show(self) -> None: ...

    class InterstitialWasLoadedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...


    class InterstitialWasViewedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...



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
    def deferSystemGesturesMode(cls) -> SystemGestureDeferMode: ...
    @classmethod
    @deferSystemGesturesMode.setter
    def deferSystemGesturesMode(cls, value: SystemGestureDeferMode) -> SystemGestureDeferMode: ...
    @classmethod
    @property
    def generation(cls) -> DeviceGeneration: ...
    @classmethod
    @property
    def hideHomeButton(cls) -> bool: ...
    @classmethod
    @hideHomeButton.setter
    def hideHomeButton(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def iosAppOnMac(cls) -> bool: ...
    @classmethod
    @property
    def lowPowerModeEnabled(cls) -> bool: ...
    @classmethod
    @property
    def systemVersion(cls) -> str: ...
    @classmethod
    @property
    def vendorIdentifier(cls) -> str: ...
    @classmethod
    @property
    def wantsSoftwareDimming(cls) -> bool: ...
    @classmethod
    @wantsSoftwareDimming.setter
    def wantsSoftwareDimming(cls, value: bool) -> bool: ...
    @staticmethod
    def RequestStoreReview() -> bool: ...
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
    iPhone : DeviceGeneration # 1
    iPhone3G : DeviceGeneration # 2
    iPhone3GS : DeviceGeneration # 3
    iPodTouch1Gen : DeviceGeneration # 4
    iPodTouch2Gen : DeviceGeneration # 5
    iPodTouch3Gen : DeviceGeneration # 6
    iPad1Gen : DeviceGeneration # 7
    iPhone4 : DeviceGeneration # 8
    iPodTouch4Gen : DeviceGeneration # 9
    iPad2Gen : DeviceGeneration # 10
    iPhone4S : DeviceGeneration # 11
    iPad3Gen : DeviceGeneration # 12
    iPhone5 : DeviceGeneration # 13
    iPodTouch5Gen : DeviceGeneration # 14
    iPadMini1Gen : DeviceGeneration # 15
    iPad4Gen : DeviceGeneration # 16
    iPhone5C : DeviceGeneration # 17
    iPhone5S : DeviceGeneration # 18
    iPadAir1 : DeviceGeneration # 19
    iPadMini2Gen : DeviceGeneration # 20
    iPhone6 : DeviceGeneration # 21
    iPhone6Plus : DeviceGeneration # 22
    iPadMini3Gen : DeviceGeneration # 23
    iPadAir2 : DeviceGeneration # 24
    iPhone6S : DeviceGeneration # 25
    iPhone6SPlus : DeviceGeneration # 26
    iPadPro1Gen : DeviceGeneration # 27
    iPadMini4Gen : DeviceGeneration # 28
    iPhoneSE1Gen : DeviceGeneration # 29
    iPadPro10Inch1Gen : DeviceGeneration # 30
    iPhone7 : DeviceGeneration # 31
    iPhone7Plus : DeviceGeneration # 32
    iPodTouch6Gen : DeviceGeneration # 33
    iPad5Gen : DeviceGeneration # 34
    iPadPro2Gen : DeviceGeneration # 35
    iPadPro10Inch2Gen : DeviceGeneration # 36
    iPhone8 : DeviceGeneration # 37
    iPhone8Plus : DeviceGeneration # 38
    iPhoneX : DeviceGeneration # 39
    iPhoneXS : DeviceGeneration # 40
    iPhoneXSMax : DeviceGeneration # 41
    iPhoneXR : DeviceGeneration # 42
    iPadPro11Inch : DeviceGeneration # 43
    iPadPro3Gen : DeviceGeneration # 44
    iPad6Gen : DeviceGeneration # 45
    iPadAir3Gen : DeviceGeneration # 46
    iPadMini5Gen : DeviceGeneration # 47
    iPhone11 : DeviceGeneration # 48
    iPhone11Pro : DeviceGeneration # 49
    iPhone11ProMax : DeviceGeneration # 50
    iPodTouch7Gen : DeviceGeneration # 51
    iPad7Gen : DeviceGeneration # 52
    iPhoneSE2Gen : DeviceGeneration # 53
    iPadPro11Inch2Gen : DeviceGeneration # 54
    iPadPro4Gen : DeviceGeneration # 55
    iPhone12Mini : DeviceGeneration # 56
    iPhone12 : DeviceGeneration # 57
    iPhone12Pro : DeviceGeneration # 58
    iPhone12ProMax : DeviceGeneration # 59
    iPad8Gen : DeviceGeneration # 60
    iPadAir4Gen : DeviceGeneration # 61
    iPad9Gen : DeviceGeneration # 62
    iPadMini6Gen : DeviceGeneration # 63
    iPhone13 : DeviceGeneration # 64
    iPhone13Mini : DeviceGeneration # 65
    iPhone13Pro : DeviceGeneration # 66
    iPhone13ProMax : DeviceGeneration # 67
    iPadPro5Gen : DeviceGeneration # 68
    iPadPro11Inch3Gen : DeviceGeneration # 69
    iPhoneSE3Gen : DeviceGeneration # 70
    iPadAir5Gen : DeviceGeneration # 71
    iPhone14 : DeviceGeneration # 72
    iPhone14Plus : DeviceGeneration # 73
    iPhone14Pro : DeviceGeneration # 74
    iPhone14ProMax : DeviceGeneration # 75
    iPadPro6Gen : DeviceGeneration # 76
    iPadPro11Inch4Gen : DeviceGeneration # 77
    iPad10Gen : DeviceGeneration # 78
    iPhone15 : DeviceGeneration # 79
    iPhone15Plus : DeviceGeneration # 80
    iPhone15Pro : DeviceGeneration # 81
    iPhone15ProMax : DeviceGeneration # 82
    iPhoneUnknown : DeviceGeneration # 10001
    iPadUnknown : DeviceGeneration # 10002
    iPodTouchUnknown : DeviceGeneration # 10003


class OnDemandResources(abc.ABC):
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @staticmethod
    def PreloadAsync(tags: Array_1[str]) -> OnDemandResourcesRequest: ...


class OnDemandResourcesRequest(AsyncOperation, IDisposable):
    @property
    def allowSceneActivation(self) -> bool: ...
    @allowSceneActivation.setter
    def allowSceneActivation(self, value: bool) -> bool: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def loadingPriority(self) -> float: ...
    @loadingPriority.setter
    def loadingPriority(self, value: float) -> float: ...
    @property
    def priority(self) -> int: ...
    @priority.setter
    def priority(self, value: int) -> int: ...
    @property
    def progress(self) -> float: ...
    def Dispose(self) -> None: ...
    def GetResourcePath(self, resourceName: str) -> str: ...


class SystemGestureDeferMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SystemGestureDeferMode # 0
    TopEdge : SystemGestureDeferMode # 1
    LeftEdge : SystemGestureDeferMode # 2
    BottomEdge : SystemGestureDeferMode # 4
    RightEdge : SystemGestureDeferMode # 8
    All : SystemGestureDeferMode # 15

