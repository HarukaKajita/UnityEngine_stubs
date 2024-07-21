import typing, abc
from System.Collections.Generic import IDictionary_2
from UnityEngine import Vector3
from System import Decimal, MulticastDelegate, IAsyncResult, AsyncCallback, IComparable_1, IEquatable_1, Func_1, Array_1
from System.Reflection import MethodInfo

class Analytics(abc.ABC):
    @classmethod
    @property
    def configUrl(cls) -> str: ...
    @classmethod
    @property
    def dashboardUrl(cls) -> str: ...
    @classmethod
    @property
    def deviceStatsEnabled(cls) -> bool: ...
    @classmethod
    @deviceStatsEnabled.setter
    def deviceStatsEnabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @enabled.setter
    def enabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def eventUrl(cls) -> str: ...
    @classmethod
    @property
    def initializeOnStartup(cls) -> bool: ...
    @classmethod
    @initializeOnStartup.setter
    def initializeOnStartup(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def limitUserTracking(cls) -> bool: ...
    @classmethod
    @limitUserTracking.setter
    def limitUserTracking(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def playerOptedOut(cls) -> bool: ...
    @staticmethod
    def EnableCustomEvent(customEventName: str, enabled: bool) -> AnalyticsResult: ...
    @staticmethod
    def EnableEvent(eventName: str, enabled: bool, ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    @staticmethod
    def FlushEvents() -> AnalyticsResult: ...
    @staticmethod
    def IsCustomEventEnabled(customEventName: str) -> AnalyticsResult: ...
    @staticmethod
    def IsEventEnabled(eventName: str, ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    @staticmethod
    def ResumeInitialization() -> AnalyticsResult: ...
    @staticmethod
    def SendEvent(eventName: str, parameters: typing.Any, ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    @staticmethod
    def SetEventEndPoint(eventName: str, endPoint: str, ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    @staticmethod
    def SetEventPriority(eventName: str, eventPriority: AnalyticsEventPriority, ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    @staticmethod
    def SetUserBirthYear(birthYear: int) -> AnalyticsResult: ...
    @staticmethod
    def SetUserGender(gender: Gender) -> AnalyticsResult: ...
    @staticmethod
    def SetUserId(userId: str) -> AnalyticsResult: ...
    # Skipped CustomEvent due to it being static, abstract and generic.

    CustomEvent : CustomEvent_MethodGroup
    class CustomEvent_MethodGroup:
        @typing.overload
        def __call__(self, customEventName: str) -> AnalyticsResult:...
        @typing.overload
        def __call__(self, customEventName: str, eventData: IDictionary_2[str, typing.Any]) -> AnalyticsResult:...
        @typing.overload
        def __call__(self, customEventName: str, position: Vector3) -> AnalyticsResult:...

    # Skipped RegisterEvent due to it being static, abstract and generic.

    RegisterEvent : RegisterEvent_MethodGroup
    class RegisterEvent_MethodGroup:
        @typing.overload
        def __call__(self, eventName: str, maxEventPerHour: int, maxItems: int, vendorKey: str = ..., prefix: str = ...) -> AnalyticsResult:...
        @typing.overload
        def __call__(self, eventName: str, maxEventPerHour: int, maxItems: int, vendorKey: str, ver: int, prefix: str = ...) -> AnalyticsResult:...

    # Skipped Transaction due to it being static, abstract and generic.

    Transaction : Transaction_MethodGroup
    class Transaction_MethodGroup:
        @typing.overload
        def __call__(self, productId: str, amount: Decimal, currency: str) -> AnalyticsResult:...
        @typing.overload
        def __call__(self, productId: str, amount: Decimal, currency: str, receiptPurchaseData: str, signature: str) -> AnalyticsResult:...
        @typing.overload
        def __call__(self, productId: str, amount: Decimal, currency: str, receiptPurchaseData: str, signature: str, usingIAPService: bool) -> AnalyticsResult:...



class AnalyticsCommon(abc.ABC):
    @classmethod
    @property
    def ugsAnalyticsEnabled(cls) -> bool: ...
    @classmethod
    @ugsAnalyticsEnabled.setter
    def ugsAnalyticsEnabled(cls, value: bool) -> bool: ...


class AnalyticsEventPriority(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NormalPriorityEvent : AnalyticsEventPriority # 0
    FlushQueueFlag : AnalyticsEventPriority # 1
    HighPriorityEvent : AnalyticsEventPriority # 1
    NormalPriorityEvent_WithCaching : AnalyticsEventPriority # 2
    CacheImmediatelyFlag : AnalyticsEventPriority # 2
    AllowInStopModeFlag : AnalyticsEventPriority # 4
    HighPriorityEvent_InStopMode : AnalyticsEventPriority # 5
    SendImmediateFlag : AnalyticsEventPriority # 8
    HighestPriorityEvent : AnalyticsEventPriority # 9
    NoCachingFlag : AnalyticsEventPriority # 16
    NoRetryFlag : AnalyticsEventPriority # 32
    NormalPriorityEvent_NoRetryNoCaching : AnalyticsEventPriority # 48
    HighestPriorityEvent_NoRetryNoCaching : AnalyticsEventPriority # 49


class AnalyticsResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Ok : AnalyticsResult # 0
    NotInitialized : AnalyticsResult # 1
    AnalyticsDisabled : AnalyticsResult # 2
    TooManyItems : AnalyticsResult # 3
    SizeLimitReached : AnalyticsResult # 4
    TooManyRequests : AnalyticsResult # 5
    InvalidData : AnalyticsResult # 6
    UnsupportedPlatform : AnalyticsResult # 7


class AnalyticsSessionInfo(abc.ABC):
    @classmethod
    @property
    def customDeviceId(cls) -> str: ...
    @classmethod
    @customDeviceId.setter
    def customDeviceId(cls, value: str) -> str: ...
    @classmethod
    @property
    def customUserId(cls) -> str: ...
    @classmethod
    @customUserId.setter
    def customUserId(cls, value: str) -> str: ...
    @classmethod
    @property
    def identityToken(cls) -> str: ...
    @classmethod
    @property
    def sessionCount(cls) -> int: ...
    @classmethod
    @property
    def sessionElapsedTime(cls) -> int: ...
    @classmethod
    @property
    def sessionFirstRun(cls) -> bool: ...
    @classmethod
    @property
    def sessionId(cls) -> int: ...
    @classmethod
    @property
    def sessionState(cls) -> AnalyticsSessionState: ...
    @classmethod
    @property
    def userId(cls) -> str: ...

    class IdentityTokenChanged(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, token: str, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, token: str) -> None: ...


    class SessionStateChanged(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, sessionState: AnalyticsSessionState, sessionId: int, sessionElapsedTime: int, sessionChanged: bool, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, sessionState: AnalyticsSessionState, sessionId: int, sessionElapsedTime: int, sessionChanged: bool) -> None: ...



class AnalyticsSessionState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    kSessionStopped : AnalyticsSessionState # 0
    kSessionStarted : AnalyticsSessionState # 1
    kSessionPaused : AnalyticsSessionState # 2
    kSessionResumed : AnalyticsSessionState # 3


class ContinuousEvent:
    def __init__(self) -> None: ...
    @staticmethod
    def ConfigureCustomEvent(customEventName: str, metricName: str, interval: float, period: float, enabled: bool = ...) -> AnalyticsResult: ...
    @staticmethod
    def ConfigureEvent(eventName: str, metricName: str, interval: float, period: float, enabled: bool = ..., ver: int = ..., prefix: str = ...) -> AnalyticsResult: ...
    # Skipped RegisterCollector due to it being static, abstract and generic.

    RegisterCollector : RegisterCollector_MethodGroup
    class RegisterCollector_MethodGroup:
        def __getitem__(self, t:typing.Type[RegisterCollector_1_T1]) -> RegisterCollector_1[RegisterCollector_1_T1]: ...

        RegisterCollector_1_T1 = typing.TypeVar('RegisterCollector_1_T1', bound=Union[IComparable_1[RegisterCollector_1_T], IEquatable_1[RegisterCollector_1_T]])
        class RegisterCollector_1(typing.Generic[RegisterCollector_1_T1]):
            RegisterCollector_1_T = ContinuousEvent.RegisterCollector_MethodGroup.RegisterCollector_1_T1
            def __call__(self, metricName: str, del_: Func_1[RegisterCollector_1_T]) -> AnalyticsResult:...


    # Skipped SetCustomEventHistogramThresholds due to it being static, abstract and generic.

    SetCustomEventHistogramThresholds : SetCustomEventHistogramThresholds_MethodGroup
    class SetCustomEventHistogramThresholds_MethodGroup:
        def __getitem__(self, t:typing.Type[SetCustomEventHistogramThresholds_1_T1]) -> SetCustomEventHistogramThresholds_1[SetCustomEventHistogramThresholds_1_T1]: ...

        SetCustomEventHistogramThresholds_1_T1 = typing.TypeVar('SetCustomEventHistogramThresholds_1_T1', bound=Union[IComparable_1[SetCustomEventHistogramThresholds_1_T], IEquatable_1[SetCustomEventHistogramThresholds_1_T]])
        class SetCustomEventHistogramThresholds_1(typing.Generic[SetCustomEventHistogramThresholds_1_T1]):
            SetCustomEventHistogramThresholds_1_T = ContinuousEvent.SetCustomEventHistogramThresholds_MethodGroup.SetCustomEventHistogramThresholds_1_T1
            def __call__(self, eventName: str, count: int, data: Array_1[SetCustomEventHistogramThresholds_1_T]) -> AnalyticsResult:...


    # Skipped SetEventHistogramThresholds due to it being static, abstract and generic.

    SetEventHistogramThresholds : SetEventHistogramThresholds_MethodGroup
    class SetEventHistogramThresholds_MethodGroup:
        def __getitem__(self, t:typing.Type[SetEventHistogramThresholds_1_T1]) -> SetEventHistogramThresholds_1[SetEventHistogramThresholds_1_T1]: ...

        SetEventHistogramThresholds_1_T1 = typing.TypeVar('SetEventHistogramThresholds_1_T1', bound=Union[IComparable_1[SetEventHistogramThresholds_1_T], IEquatable_1[SetEventHistogramThresholds_1_T]])
        class SetEventHistogramThresholds_1(typing.Generic[SetEventHistogramThresholds_1_T1]):
            SetEventHistogramThresholds_1_T = ContinuousEvent.SetEventHistogramThresholds_MethodGroup.SetEventHistogramThresholds_1_T1
            def __call__(self, eventName: str, count: int, data: Array_1[SetEventHistogramThresholds_1_T], ver: int = ..., prefix: str = ...) -> AnalyticsResult:...




class Gender(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Male : Gender # 0
    Female : Gender # 1
    Unknown : Gender # 2


class PerformanceReporting(abc.ABC):
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @enabled.setter
    def enabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def graphicsInitializationFinishTime(cls) -> int: ...


class UGSAnalyticsInternalTools(typing.Protocol):
    @staticmethod
    def SetPrivacyStatus(status: bool) -> None: ...

