import typing, abc
from System import IDisposable, MulticastDelegate, IAsyncResult, AsyncCallback, Array_1, TimeSpan, DateTime
from System.Reflection import MethodInfo
from System.Collections.Generic import IEnumerable_1

class ConfidenceLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    High : ConfidenceLevel # 0
    Medium : ConfidenceLevel # 1
    Low : ConfidenceLevel # 2
    Rejected : ConfidenceLevel # 3


class DictationCompletionCause(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Complete : DictationCompletionCause # 0
    AudioQualityFailure : DictationCompletionCause # 1
    Canceled : DictationCompletionCause # 2
    TimeoutExceeded : DictationCompletionCause # 3
    PauseLimitExceeded : DictationCompletionCause # 4
    NetworkFailure : DictationCompletionCause # 5
    MicrophoneUnavailable : DictationCompletionCause # 6
    UnknownError : DictationCompletionCause # 7


class DictationRecognizer(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, confidenceLevel: ConfidenceLevel) -> None: ...
    @typing.overload
    def __init__(self, minimumConfidence: ConfidenceLevel, topic: DictationTopicConstraint) -> None: ...
    @typing.overload
    def __init__(self, topic: DictationTopicConstraint) -> None: ...
    @property
    def AutoSilenceTimeoutSeconds(self) -> float: ...
    @AutoSilenceTimeoutSeconds.setter
    def AutoSilenceTimeoutSeconds(self, value: float) -> float: ...
    @property
    def InitialSilenceTimeoutSeconds(self) -> float: ...
    @InitialSilenceTimeoutSeconds.setter
    def InitialSilenceTimeoutSeconds(self, value: float) -> float: ...
    @property
    def Status(self) -> SpeechSystemStatus: ...
    def Dispose(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...

    class DictationCompletedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, cause: DictationCompletionCause, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, cause: DictationCompletionCause) -> None: ...


    class DictationErrorHandler(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, error: str, hresult: int, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, error: str, hresult: int) -> None: ...


    class DictationHypothesisDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, text: str, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, text: str) -> None: ...


    class DictationResultDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, text: str, confidence: ConfidenceLevel, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, text: str, confidence: ConfidenceLevel) -> None: ...



class DictationTopicConstraint(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    WebSearch : DictationTopicConstraint # 0
    Form : DictationTopicConstraint # 1
    Dictation : DictationTopicConstraint # 2


class GrammarRecognizer(PhraseRecognizer):
    @typing.overload
    def __init__(self, grammarFilePath: str) -> None: ...
    @typing.overload
    def __init__(self, grammarFilePath: str, minimumConfidence: ConfidenceLevel) -> None: ...
    @property
    def GrammarFilePath(self) -> str: ...
    @GrammarFilePath.setter
    def GrammarFilePath(self, value: str) -> str: ...
    @property
    def IsRunning(self) -> bool: ...


class KeywordRecognizer(PhraseRecognizer):
    @typing.overload
    def __init__(self, keywords: Array_1[str]) -> None: ...
    @typing.overload
    def __init__(self, keywords: Array_1[str], minimumConfidence: ConfidenceLevel) -> None: ...
    @property
    def IsRunning(self) -> bool: ...
    @property
    def Keywords(self) -> IEnumerable_1[str]: ...
    @Keywords.setter
    def Keywords(self, value: IEnumerable_1[str]) -> IEnumerable_1[str]: ...


class PhraseRecognitionSystem(abc.ABC):
    @classmethod
    @property
    def isSupported(cls) -> bool: ...
    @classmethod
    @property
    def Status(cls) -> SpeechSystemStatus: ...
    @staticmethod
    def Restart() -> None: ...
    @staticmethod
    def Shutdown() -> None: ...

    class ErrorDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, errorCode: SpeechError, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, errorCode: SpeechError) -> None: ...


    class StatusDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, status: SpeechSystemStatus, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, status: SpeechSystemStatus) -> None: ...



class PhraseRecognizedEventArgs:
    confidence : ConfidenceLevel
    phraseDuration : TimeSpan
    phraseStartTime : DateTime
    semanticMeanings : Array_1[SemanticMeaning]
    text : str


class PhraseRecognizer(IDisposable, abc.ABC):
    @property
    def IsRunning(self) -> bool: ...
    def Dispose(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...

    class PhraseRecognizedDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, args: PhraseRecognizedEventArgs, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, args: PhraseRecognizedEventArgs) -> None: ...



class SemanticMeaning:
    key : str
    values : Array_1[str]


class SpeechError(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NoError : SpeechError # 0
    TopicLanguageNotSupported : SpeechError # 1
    GrammarLanguageMismatch : SpeechError # 2
    GrammarCompilationFailure : SpeechError # 3
    AudioQualityFailure : SpeechError # 4
    PauseLimitExceeded : SpeechError # 5
    TimeoutExceeded : SpeechError # 6
    NetworkFailure : SpeechError # 7
    MicrophoneUnavailable : SpeechError # 8
    UnknownError : SpeechError # 9


class SpeechSystemStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Stopped : SpeechSystemStatus # 0
    Running : SpeechSystemStatus # 1
    Failed : SpeechSystemStatus # 2

