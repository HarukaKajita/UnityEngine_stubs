import typing, abc
from System import IDisposable, Array_1, IEquatable_1
from UnityEngine import Hash128

class IScriptableBakedReflectionSystem(IDisposable, typing.Protocol):
    @property
    def stageCount(self) -> int: ...
    @property
    def stateHashes(self) -> Array_1[Hash128]: ...
    @abc.abstractmethod
    def BakeAllReflectionProbes(self) -> bool: ...
    @abc.abstractmethod
    def Cancel(self) -> None: ...
    @abc.abstractmethod
    def Clear(self) -> None: ...
    @abc.abstractmethod
    def SynchronizeReflectionProbes(self) -> None: ...
    @abc.abstractmethod
    def Tick(self, sceneStateHash: SceneStateHash, handle: IScriptableBakedReflectionSystemStageNotifier) -> None: ...


class IScriptableBakedReflectionSystemStageNotifier(typing.Protocol):
    @abc.abstractmethod
    def EnterStage(self, stage: int, progressMessage: str, progress: float) -> None: ...
    @abc.abstractmethod
    def ExitStage(self, stage: int) -> None: ...
    @abc.abstractmethod
    def SetIsDone(self, isDone: bool) -> None: ...


class SceneStateHash(IEquatable_1[SceneStateHash]):
    def __init__(self, sceneObjectsHash: Hash128, skySettingsHash: Hash128, ambientProbeHash: Hash128) -> None: ...
    @property
    def ambientProbeHash(self) -> Hash128: ...
    @property
    def sceneObjectsHash(self) -> Hash128: ...
    @property
    def skySettingsHash(self) -> Hash128: ...
    def GetHashCode(self) -> int: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: SceneStateHash) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class ScriptableBakedReflectionSystem(IScriptableBakedReflectionSystem, abc.ABC):
    @property
    def stageCount(self) -> int: ...
    @property
    def stateHashes(self) -> Array_1[Hash128]: ...
    @stateHashes.setter
    def stateHashes(self, value: Array_1[Hash128]) -> Array_1[Hash128]: ...
    def BakeAllReflectionProbes(self) -> bool: ...
    def Cancel(self) -> None: ...
    def Clear(self) -> None: ...
    def SynchronizeReflectionProbes(self) -> None: ...
    def Tick(self, sceneStateHash: SceneStateHash, handle: IScriptableBakedReflectionSystemStageNotifier) -> None: ...


class ScriptableBakedReflectionSystemSettings(abc.ABC):
    @classmethod
    @property
    def system(cls) -> IScriptableBakedReflectionSystem: ...
    @classmethod
    @system.setter
    def system(cls, value: IScriptableBakedReflectionSystem) -> IScriptableBakedReflectionSystem: ...

