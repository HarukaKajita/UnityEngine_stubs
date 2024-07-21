import typing, clr, abc
from UnityEngine import Animator, RuntimeAnimatorController, AnimationClip, PropertyName, GameObject, ScriptableObject, HideFlags, Object, Behaviour, IExposedPropertyTable, Component, Transform
from UnityEngine.Animations import AnimatorControllerPlayable, AnimationClipPlayable, AnimationLayerMixerPlayable, AnimationMixerPlayable
from System.Collections.Generic import IEnumerable_1
from System import IEquatable_1, ICloneable, Array_1

class AnimationPlayableUtilities(abc.ABC):
    @staticmethod
    def Play(animator: Animator, playable: Playable, graph: PlayableGraph) -> None: ...
    @staticmethod
    def PlayAnimatorController(animator: Animator, controller: RuntimeAnimatorController, graph: clr.Reference[PlayableGraph]) -> AnimatorControllerPlayable: ...
    @staticmethod
    def PlayClip(animator: Animator, clip: AnimationClip, graph: clr.Reference[PlayableGraph]) -> AnimationClipPlayable: ...
    @staticmethod
    def PlayLayerMixer(animator: Animator, inputCount: int, graph: clr.Reference[PlayableGraph]) -> AnimationLayerMixerPlayable: ...
    @staticmethod
    def PlayMixer(animator: Animator, inputCount: int, graph: clr.Reference[PlayableGraph]) -> AnimationMixerPlayable: ...


class DataStreamType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Animation : DataStreamType # 0
    Audio : DataStreamType # 1
    Texture : DataStreamType # 2
    None_ : DataStreamType # 3


class DirectorUpdateMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    DSPClock : DirectorUpdateMode # 0
    GameTime : DirectorUpdateMode # 1
    UnscaledGameTime : DirectorUpdateMode # 2
    Manual : DirectorUpdateMode # 3


class DirectorWrapMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Hold : DirectorWrapMode # 0
    Loop : DirectorWrapMode # 1
    None_ : DirectorWrapMode # 2


class FrameData:
    @property
    def deltaTime(self) -> float: ...
    @property
    def effectiveParentDelay(self) -> float: ...
    @property
    def effectiveParentSpeed(self) -> float: ...
    @property
    def effectivePlayState(self) -> PlayState: ...
    @property
    def effectiveSpeed(self) -> float: ...
    @property
    def effectiveWeight(self) -> float: ...
    @property
    def evaluationType(self) -> FrameData.EvaluationType: ...
    @property
    def frameId(self) -> int: ...
    @property
    def output(self) -> PlayableOutput: ...
    @property
    def seekOccurred(self) -> bool: ...
    @property
    def timeHeld(self) -> bool: ...
    @property
    def timeLooped(self) -> bool: ...
    @property
    def weight(self) -> float: ...

    class EvaluationType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Evaluate : FrameData.EvaluationType # 0
        Playback : FrameData.EvaluationType # 1



class INotification(typing.Protocol):
    @property
    def id(self) -> PropertyName: ...


class INotificationReceiver(typing.Protocol):
    @abc.abstractmethod
    def OnNotify(self, origin: Playable, notification: INotification, context: typing.Any) -> None: ...


class IPlayable(typing.Protocol):
    @abc.abstractmethod
    def GetHandle(self) -> PlayableHandle: ...


class IPlayableAsset(typing.Protocol):
    @property
    def duration(self) -> float: ...
    @property
    def outputs(self) -> IEnumerable_1[PlayableBinding]: ...
    @abc.abstractmethod
    def CreatePlayable(self, graph: PlayableGraph, owner: GameObject) -> Playable: ...


class IPlayableBehaviour(typing.Protocol):
    @abc.abstractmethod
    def OnBehaviourPause(self, playable: Playable, info: FrameData) -> None: ...
    @abc.abstractmethod
    def OnBehaviourPlay(self, playable: Playable, info: FrameData) -> None: ...
    @abc.abstractmethod
    def OnGraphStart(self, playable: Playable) -> None: ...
    @abc.abstractmethod
    def OnGraphStop(self, playable: Playable) -> None: ...
    @abc.abstractmethod
    def OnPlayableCreate(self, playable: Playable) -> None: ...
    @abc.abstractmethod
    def OnPlayableDestroy(self, playable: Playable) -> None: ...
    @abc.abstractmethod
    def PrepareFrame(self, playable: Playable, info: FrameData) -> None: ...
    @abc.abstractmethod
    def ProcessFrame(self, playable: Playable, info: FrameData, playerData: typing.Any) -> None: ...


class IPlayableOutput(typing.Protocol):
    @abc.abstractmethod
    def GetHandle(self) -> PlayableOutputHandle: ...


class Notification(INotification):
    def __init__(self, name: str) -> None: ...
    @property
    def id(self) -> PropertyName: ...


class Playable(IEquatable_1[Playable], IPlayable):
    @classmethod
    @property
    def Null(cls) -> Playable: ...
    @staticmethod
    def Create(graph: PlayableGraph, inputCount: int = ...) -> Playable: ...
    def Equals(self, other: Playable) -> bool: ...
    def GetHandle(self) -> PlayableHandle: ...
    def GetPlayableType(self) -> typing.Type[typing.Any]: ...
    # Skipped IsPlayableOfType due to it being static, abstract and generic.

    IsPlayableOfType : IsPlayableOfType_MethodGroup
    class IsPlayableOfType_MethodGroup:
        def __getitem__(self, t:typing.Type[IsPlayableOfType_1_T1]) -> IsPlayableOfType_1[IsPlayableOfType_1_T1]: ...

        IsPlayableOfType_1_T1 = typing.TypeVar('IsPlayableOfType_1_T1')
        class IsPlayableOfType_1(typing.Generic[IsPlayableOfType_1_T1]):
            IsPlayableOfType_1_T = Playable.IsPlayableOfType_MethodGroup.IsPlayableOfType_1_T1
            def __call__(self) -> bool:...




class PlayableAsset(ScriptableObject, IPlayableAsset, abc.ABC):
    @property
    def duration(self) -> float: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def outputs(self) -> IEnumerable_1[PlayableBinding]: ...
    @abc.abstractmethod
    def CreatePlayable(self, graph: PlayableGraph, owner: GameObject) -> Playable: ...


class PlayableBehaviour(ICloneable, IPlayableBehaviour, abc.ABC):
    def __init__(self) -> None: ...
    def Clone(self) -> typing.Any: ...
    def OnBehaviourDelay(self, playable: Playable, info: FrameData) -> None: ...
    def OnBehaviourPause(self, playable: Playable, info: FrameData) -> None: ...
    def OnBehaviourPlay(self, playable: Playable, info: FrameData) -> None: ...
    def OnGraphStart(self, playable: Playable) -> None: ...
    def OnGraphStop(self, playable: Playable) -> None: ...
    def OnPlayableCreate(self, playable: Playable) -> None: ...
    def OnPlayableDestroy(self, playable: Playable) -> None: ...
    def PrepareData(self, playable: Playable, info: FrameData) -> None: ...
    def PrepareFrame(self, playable: Playable, info: FrameData) -> None: ...
    def ProcessFrame(self, playable: Playable, info: FrameData, playerData: typing.Any) -> None: ...


class PlayableBinding:
    DefaultDuration : float
    None : Array_1[PlayableBinding]
    @property
    def outputTargetType(self) -> typing.Type[typing.Any]: ...
    @property
    def sourceBindingType(self) -> typing.Type[typing.Any]: ...
    @sourceBindingType.setter
    def sourceBindingType(self, value: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    @property
    def sourceObject(self) -> Object: ...
    @sourceObject.setter
    def sourceObject(self, value: Object) -> Object: ...
    @property
    def streamName(self) -> str: ...
    @streamName.setter
    def streamName(self, value: str) -> str: ...
    @property
    def streamType(self) -> DataStreamType: ...
    @streamType.setter
    def streamType(self, value: DataStreamType) -> DataStreamType: ...


class PlayableDirector(Behaviour, IExposedPropertyTable):
    def __init__(self) -> None: ...
    @property
    def animation(self) -> Component: ...
    @property
    def audio(self) -> Component: ...
    @property
    def camera(self) -> Component: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def duration(self) -> float: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def extrapolationMode(self) -> DirectorWrapMode: ...
    @extrapolationMode.setter
    def extrapolationMode(self, value: DirectorWrapMode) -> DirectorWrapMode: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def initialTime(self) -> float: ...
    @initialTime.setter
    def initialTime(self, value: float) -> float: ...
    @property
    def isActiveAndEnabled(self) -> bool: ...
    @property
    def light(self) -> Component: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def playableAsset(self) -> PlayableAsset: ...
    @playableAsset.setter
    def playableAsset(self, value: PlayableAsset) -> PlayableAsset: ...
    @property
    def playableGraph(self) -> PlayableGraph: ...
    @property
    def playOnAwake(self) -> bool: ...
    @playOnAwake.setter
    def playOnAwake(self, value: bool) -> bool: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def state(self) -> PlayState: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def time(self) -> float: ...
    @time.setter
    def time(self, value: float) -> float: ...
    @property
    def timeUpdateMode(self) -> DirectorUpdateMode: ...
    @timeUpdateMode.setter
    def timeUpdateMode(self, value: DirectorUpdateMode) -> DirectorUpdateMode: ...
    @property
    def transform(self) -> Transform: ...
    def ClearGenericBinding(self, key: Object) -> None: ...
    def ClearReferenceValue(self, id: PropertyName) -> None: ...
    def DeferredEvaluate(self) -> None: ...
    def Evaluate(self) -> None: ...
    def GetGenericBinding(self, key: Object) -> Object: ...
    def GetReferenceValue(self, id: PropertyName, idValid: clr.Reference[bool]) -> Object: ...
    def Pause(self) -> None: ...
    def RebindPlayableGraphOutputs(self) -> None: ...
    def RebuildGraph(self) -> None: ...
    def Resume(self) -> None: ...
    def SetGenericBinding(self, key: Object, value: Object) -> None: ...
    def SetReferenceValue(self, id: PropertyName, value: Object) -> None: ...
    def Stop(self) -> None: ...
    # Skipped Play due to it being static, abstract and generic.

    Play : Play_MethodGroup
    class Play_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, asset: PlayableAsset) -> None:...
        @typing.overload
        def __call__(self, asset: PlayableAsset, mode: DirectorWrapMode) -> None:...



class PlayableExtensions(abc.ABC):
    # Skipped AddInput due to it being static, abstract and generic.

    AddInput : AddInput_MethodGroup
    class AddInput_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[AddInput_2_T1], typing.Type[AddInput_2_T2]]) -> AddInput_2[AddInput_2_T1, AddInput_2_T2]: ...

        AddInput_2_T1 = typing.TypeVar('AddInput_2_T1')
        AddInput_2_T2 = typing.TypeVar('AddInput_2_T2')
        class AddInput_2(typing.Generic[AddInput_2_T1, AddInput_2_T2]):
            AddInput_2_U = PlayableExtensions.AddInput_MethodGroup.AddInput_2_T1
            AddInput_2_V = PlayableExtensions.AddInput_MethodGroup.AddInput_2_T2
            def __call__(self, playable: AddInput_2_U, sourcePlayable: AddInput_2_V, sourceOutputIndex: int, weight: float = ...) -> int:...


    # Skipped CanChangeInputs due to it being static, abstract and generic.

    CanChangeInputs : CanChangeInputs_MethodGroup
    class CanChangeInputs_MethodGroup:
        def __getitem__(self, t:typing.Type[CanChangeInputs_1_T1]) -> CanChangeInputs_1[CanChangeInputs_1_T1]: ...

        CanChangeInputs_1_T1 = typing.TypeVar('CanChangeInputs_1_T1')
        class CanChangeInputs_1(typing.Generic[CanChangeInputs_1_T1]):
            CanChangeInputs_1_U = PlayableExtensions.CanChangeInputs_MethodGroup.CanChangeInputs_1_T1
            def __call__(self, playable: CanChangeInputs_1_U) -> bool:...


    # Skipped CanDestroy due to it being static, abstract and generic.

    CanDestroy : CanDestroy_MethodGroup
    class CanDestroy_MethodGroup:
        def __getitem__(self, t:typing.Type[CanDestroy_1_T1]) -> CanDestroy_1[CanDestroy_1_T1]: ...

        CanDestroy_1_T1 = typing.TypeVar('CanDestroy_1_T1')
        class CanDestroy_1(typing.Generic[CanDestroy_1_T1]):
            CanDestroy_1_U = PlayableExtensions.CanDestroy_MethodGroup.CanDestroy_1_T1
            def __call__(self, playable: CanDestroy_1_U) -> bool:...


    # Skipped CanSetWeights due to it being static, abstract and generic.

    CanSetWeights : CanSetWeights_MethodGroup
    class CanSetWeights_MethodGroup:
        def __getitem__(self, t:typing.Type[CanSetWeights_1_T1]) -> CanSetWeights_1[CanSetWeights_1_T1]: ...

        CanSetWeights_1_T1 = typing.TypeVar('CanSetWeights_1_T1')
        class CanSetWeights_1(typing.Generic[CanSetWeights_1_T1]):
            CanSetWeights_1_U = PlayableExtensions.CanSetWeights_MethodGroup.CanSetWeights_1_T1
            def __call__(self, playable: CanSetWeights_1_U) -> bool:...


    # Skipped ConnectInput due to it being static, abstract and generic.

    ConnectInput : ConnectInput_MethodGroup
    class ConnectInput_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ConnectInput_2_T1], typing.Type[ConnectInput_2_T2]]) -> ConnectInput_2[ConnectInput_2_T1, ConnectInput_2_T2]: ...

        ConnectInput_2_T1 = typing.TypeVar('ConnectInput_2_T1')
        ConnectInput_2_T2 = typing.TypeVar('ConnectInput_2_T2')
        class ConnectInput_2(typing.Generic[ConnectInput_2_T1, ConnectInput_2_T2]):
            ConnectInput_2_U = PlayableExtensions.ConnectInput_MethodGroup.ConnectInput_2_T1
            ConnectInput_2_V = PlayableExtensions.ConnectInput_MethodGroup.ConnectInput_2_T2
            @typing.overload
            def __call__(self, playable: ConnectInput_2_U, inputIndex: int, sourcePlayable: ConnectInput_2_V, sourceOutputIndex: int) -> None:...
            @typing.overload
            def __call__(self, playable: ConnectInput_2_U, inputIndex: int, sourcePlayable: ConnectInput_2_V, sourceOutputIndex: int, weight: float) -> None:...


    # Skipped Destroy due to it being static, abstract and generic.

    Destroy : Destroy_MethodGroup
    class Destroy_MethodGroup:
        def __getitem__(self, t:typing.Type[Destroy_1_T1]) -> Destroy_1[Destroy_1_T1]: ...

        Destroy_1_T1 = typing.TypeVar('Destroy_1_T1')
        class Destroy_1(typing.Generic[Destroy_1_T1]):
            Destroy_1_U = PlayableExtensions.Destroy_MethodGroup.Destroy_1_T1
            def __call__(self, playable: Destroy_1_U) -> None:...


    # Skipped DisconnectInput due to it being static, abstract and generic.

    DisconnectInput : DisconnectInput_MethodGroup
    class DisconnectInput_MethodGroup:
        def __getitem__(self, t:typing.Type[DisconnectInput_1_T1]) -> DisconnectInput_1[DisconnectInput_1_T1]: ...

        DisconnectInput_1_T1 = typing.TypeVar('DisconnectInput_1_T1')
        class DisconnectInput_1(typing.Generic[DisconnectInput_1_T1]):
            DisconnectInput_1_U = PlayableExtensions.DisconnectInput_MethodGroup.DisconnectInput_1_T1
            def __call__(self, playable: DisconnectInput_1_U, inputPort: int) -> None:...


    # Skipped GetDelay due to it being static, abstract and generic.

    GetDelay : GetDelay_MethodGroup
    class GetDelay_MethodGroup:
        def __getitem__(self, t:typing.Type[GetDelay_1_T1]) -> GetDelay_1[GetDelay_1_T1]: ...

        GetDelay_1_T1 = typing.TypeVar('GetDelay_1_T1')
        class GetDelay_1(typing.Generic[GetDelay_1_T1]):
            GetDelay_1_U = PlayableExtensions.GetDelay_MethodGroup.GetDelay_1_T1
            def __call__(self, playable: GetDelay_1_U) -> float:...


    # Skipped GetDuration due to it being static, abstract and generic.

    GetDuration : GetDuration_MethodGroup
    class GetDuration_MethodGroup:
        def __getitem__(self, t:typing.Type[GetDuration_1_T1]) -> GetDuration_1[GetDuration_1_T1]: ...

        GetDuration_1_T1 = typing.TypeVar('GetDuration_1_T1')
        class GetDuration_1(typing.Generic[GetDuration_1_T1]):
            GetDuration_1_U = PlayableExtensions.GetDuration_MethodGroup.GetDuration_1_T1
            def __call__(self, playable: GetDuration_1_U) -> float:...


    # Skipped GetGraph due to it being static, abstract and generic.

    GetGraph : GetGraph_MethodGroup
    class GetGraph_MethodGroup:
        def __getitem__(self, t:typing.Type[GetGraph_1_T1]) -> GetGraph_1[GetGraph_1_T1]: ...

        GetGraph_1_T1 = typing.TypeVar('GetGraph_1_T1')
        class GetGraph_1(typing.Generic[GetGraph_1_T1]):
            GetGraph_1_U = PlayableExtensions.GetGraph_MethodGroup.GetGraph_1_T1
            def __call__(self, playable: GetGraph_1_U) -> PlayableGraph:...


    # Skipped GetInput due to it being static, abstract and generic.

    GetInput : GetInput_MethodGroup
    class GetInput_MethodGroup:
        def __getitem__(self, t:typing.Type[GetInput_1_T1]) -> GetInput_1[GetInput_1_T1]: ...

        GetInput_1_T1 = typing.TypeVar('GetInput_1_T1')
        class GetInput_1(typing.Generic[GetInput_1_T1]):
            GetInput_1_U = PlayableExtensions.GetInput_MethodGroup.GetInput_1_T1
            def __call__(self, playable: GetInput_1_U, inputPort: int) -> Playable:...


    # Skipped GetInputCount due to it being static, abstract and generic.

    GetInputCount : GetInputCount_MethodGroup
    class GetInputCount_MethodGroup:
        def __getitem__(self, t:typing.Type[GetInputCount_1_T1]) -> GetInputCount_1[GetInputCount_1_T1]: ...

        GetInputCount_1_T1 = typing.TypeVar('GetInputCount_1_T1')
        class GetInputCount_1(typing.Generic[GetInputCount_1_T1]):
            GetInputCount_1_U = PlayableExtensions.GetInputCount_MethodGroup.GetInputCount_1_T1
            def __call__(self, playable: GetInputCount_1_U) -> int:...


    # Skipped GetInputWeight due to it being static, abstract and generic.

    GetInputWeight : GetInputWeight_MethodGroup
    class GetInputWeight_MethodGroup:
        def __getitem__(self, t:typing.Type[GetInputWeight_1_T1]) -> GetInputWeight_1[GetInputWeight_1_T1]: ...

        GetInputWeight_1_T1 = typing.TypeVar('GetInputWeight_1_T1')
        class GetInputWeight_1(typing.Generic[GetInputWeight_1_T1]):
            GetInputWeight_1_U = PlayableExtensions.GetInputWeight_MethodGroup.GetInputWeight_1_T1
            def __call__(self, playable: GetInputWeight_1_U, inputIndex: int) -> float:...


    # Skipped GetLeadTime due to it being static, abstract and generic.

    GetLeadTime : GetLeadTime_MethodGroup
    class GetLeadTime_MethodGroup:
        def __getitem__(self, t:typing.Type[GetLeadTime_1_T1]) -> GetLeadTime_1[GetLeadTime_1_T1]: ...

        GetLeadTime_1_T1 = typing.TypeVar('GetLeadTime_1_T1')
        class GetLeadTime_1(typing.Generic[GetLeadTime_1_T1]):
            GetLeadTime_1_U = PlayableExtensions.GetLeadTime_MethodGroup.GetLeadTime_1_T1
            def __call__(self, playable: GetLeadTime_1_U) -> float:...


    # Skipped GetOutput due to it being static, abstract and generic.

    GetOutput : GetOutput_MethodGroup
    class GetOutput_MethodGroup:
        def __getitem__(self, t:typing.Type[GetOutput_1_T1]) -> GetOutput_1[GetOutput_1_T1]: ...

        GetOutput_1_T1 = typing.TypeVar('GetOutput_1_T1')
        class GetOutput_1(typing.Generic[GetOutput_1_T1]):
            GetOutput_1_U = PlayableExtensions.GetOutput_MethodGroup.GetOutput_1_T1
            def __call__(self, playable: GetOutput_1_U, outputPort: int) -> Playable:...


    # Skipped GetOutputCount due to it being static, abstract and generic.

    GetOutputCount : GetOutputCount_MethodGroup
    class GetOutputCount_MethodGroup:
        def __getitem__(self, t:typing.Type[GetOutputCount_1_T1]) -> GetOutputCount_1[GetOutputCount_1_T1]: ...

        GetOutputCount_1_T1 = typing.TypeVar('GetOutputCount_1_T1')
        class GetOutputCount_1(typing.Generic[GetOutputCount_1_T1]):
            GetOutputCount_1_U = PlayableExtensions.GetOutputCount_MethodGroup.GetOutputCount_1_T1
            def __call__(self, playable: GetOutputCount_1_U) -> int:...


    # Skipped GetPlayState due to it being static, abstract and generic.

    GetPlayState : GetPlayState_MethodGroup
    class GetPlayState_MethodGroup:
        def __getitem__(self, t:typing.Type[GetPlayState_1_T1]) -> GetPlayState_1[GetPlayState_1_T1]: ...

        GetPlayState_1_T1 = typing.TypeVar('GetPlayState_1_T1')
        class GetPlayState_1(typing.Generic[GetPlayState_1_T1]):
            GetPlayState_1_U = PlayableExtensions.GetPlayState_MethodGroup.GetPlayState_1_T1
            def __call__(self, playable: GetPlayState_1_U) -> PlayState:...


    # Skipped GetPreviousTime due to it being static, abstract and generic.

    GetPreviousTime : GetPreviousTime_MethodGroup
    class GetPreviousTime_MethodGroup:
        def __getitem__(self, t:typing.Type[GetPreviousTime_1_T1]) -> GetPreviousTime_1[GetPreviousTime_1_T1]: ...

        GetPreviousTime_1_T1 = typing.TypeVar('GetPreviousTime_1_T1')
        class GetPreviousTime_1(typing.Generic[GetPreviousTime_1_T1]):
            GetPreviousTime_1_U = PlayableExtensions.GetPreviousTime_MethodGroup.GetPreviousTime_1_T1
            def __call__(self, playable: GetPreviousTime_1_U) -> float:...


    # Skipped GetPropagateSetTime due to it being static, abstract and generic.

    GetPropagateSetTime : GetPropagateSetTime_MethodGroup
    class GetPropagateSetTime_MethodGroup:
        def __getitem__(self, t:typing.Type[GetPropagateSetTime_1_T1]) -> GetPropagateSetTime_1[GetPropagateSetTime_1_T1]: ...

        GetPropagateSetTime_1_T1 = typing.TypeVar('GetPropagateSetTime_1_T1')
        class GetPropagateSetTime_1(typing.Generic[GetPropagateSetTime_1_T1]):
            GetPropagateSetTime_1_U = PlayableExtensions.GetPropagateSetTime_MethodGroup.GetPropagateSetTime_1_T1
            def __call__(self, playable: GetPropagateSetTime_1_U) -> bool:...


    # Skipped GetSpeed due to it being static, abstract and generic.

    GetSpeed : GetSpeed_MethodGroup
    class GetSpeed_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSpeed_1_T1]) -> GetSpeed_1[GetSpeed_1_T1]: ...

        GetSpeed_1_T1 = typing.TypeVar('GetSpeed_1_T1')
        class GetSpeed_1(typing.Generic[GetSpeed_1_T1]):
            GetSpeed_1_U = PlayableExtensions.GetSpeed_MethodGroup.GetSpeed_1_T1
            def __call__(self, playable: GetSpeed_1_U) -> float:...


    # Skipped GetTime due to it being static, abstract and generic.

    GetTime : GetTime_MethodGroup
    class GetTime_MethodGroup:
        def __getitem__(self, t:typing.Type[GetTime_1_T1]) -> GetTime_1[GetTime_1_T1]: ...

        GetTime_1_T1 = typing.TypeVar('GetTime_1_T1')
        class GetTime_1(typing.Generic[GetTime_1_T1]):
            GetTime_1_U = PlayableExtensions.GetTime_MethodGroup.GetTime_1_T1
            def __call__(self, playable: GetTime_1_U) -> float:...


    # Skipped GetTraversalMode due to it being static, abstract and generic.

    GetTraversalMode : GetTraversalMode_MethodGroup
    class GetTraversalMode_MethodGroup:
        def __getitem__(self, t:typing.Type[GetTraversalMode_1_T1]) -> GetTraversalMode_1[GetTraversalMode_1_T1]: ...

        GetTraversalMode_1_T1 = typing.TypeVar('GetTraversalMode_1_T1')
        class GetTraversalMode_1(typing.Generic[GetTraversalMode_1_T1]):
            GetTraversalMode_1_U = PlayableExtensions.GetTraversalMode_MethodGroup.GetTraversalMode_1_T1
            def __call__(self, playable: GetTraversalMode_1_U) -> PlayableTraversalMode:...


    # Skipped IsDelayed due to it being static, abstract and generic.

    IsDelayed : IsDelayed_MethodGroup
    class IsDelayed_MethodGroup:
        def __getitem__(self, t:typing.Type[IsDelayed_1_T1]) -> IsDelayed_1[IsDelayed_1_T1]: ...

        IsDelayed_1_T1 = typing.TypeVar('IsDelayed_1_T1')
        class IsDelayed_1(typing.Generic[IsDelayed_1_T1]):
            IsDelayed_1_U = PlayableExtensions.IsDelayed_MethodGroup.IsDelayed_1_T1
            def __call__(self, playable: IsDelayed_1_U) -> bool:...


    # Skipped IsDone due to it being static, abstract and generic.

    IsDone : IsDone_MethodGroup
    class IsDone_MethodGroup:
        def __getitem__(self, t:typing.Type[IsDone_1_T1]) -> IsDone_1[IsDone_1_T1]: ...

        IsDone_1_T1 = typing.TypeVar('IsDone_1_T1')
        class IsDone_1(typing.Generic[IsDone_1_T1]):
            IsDone_1_U = PlayableExtensions.IsDone_MethodGroup.IsDone_1_T1
            def __call__(self, playable: IsDone_1_U) -> bool:...


    # Skipped IsNull due to it being static, abstract and generic.

    IsNull : IsNull_MethodGroup
    class IsNull_MethodGroup:
        def __getitem__(self, t:typing.Type[IsNull_1_T1]) -> IsNull_1[IsNull_1_T1]: ...

        IsNull_1_T1 = typing.TypeVar('IsNull_1_T1')
        class IsNull_1(typing.Generic[IsNull_1_T1]):
            IsNull_1_U = PlayableExtensions.IsNull_MethodGroup.IsNull_1_T1
            def __call__(self, playable: IsNull_1_U) -> bool:...


    # Skipped IsValid due to it being static, abstract and generic.

    IsValid : IsValid_MethodGroup
    class IsValid_MethodGroup:
        def __getitem__(self, t:typing.Type[IsValid_1_T1]) -> IsValid_1[IsValid_1_T1]: ...

        IsValid_1_T1 = typing.TypeVar('IsValid_1_T1')
        class IsValid_1(typing.Generic[IsValid_1_T1]):
            IsValid_1_U = PlayableExtensions.IsValid_MethodGroup.IsValid_1_T1
            def __call__(self, playable: IsValid_1_U) -> bool:...


    # Skipped Pause due to it being static, abstract and generic.

    Pause : Pause_MethodGroup
    class Pause_MethodGroup:
        def __getitem__(self, t:typing.Type[Pause_1_T1]) -> Pause_1[Pause_1_T1]: ...

        Pause_1_T1 = typing.TypeVar('Pause_1_T1')
        class Pause_1(typing.Generic[Pause_1_T1]):
            Pause_1_U = PlayableExtensions.Pause_MethodGroup.Pause_1_T1
            def __call__(self, playable: Pause_1_U) -> None:...


    # Skipped Play due to it being static, abstract and generic.

    Play : Play_MethodGroup
    class Play_MethodGroup:
        def __getitem__(self, t:typing.Type[Play_1_T1]) -> Play_1[Play_1_T1]: ...

        Play_1_T1 = typing.TypeVar('Play_1_T1')
        class Play_1(typing.Generic[Play_1_T1]):
            Play_1_U = PlayableExtensions.Play_MethodGroup.Play_1_T1
            def __call__(self, playable: Play_1_U) -> None:...


    # Skipped SetDelay due to it being static, abstract and generic.

    SetDelay : SetDelay_MethodGroup
    class SetDelay_MethodGroup:
        def __getitem__(self, t:typing.Type[SetDelay_1_T1]) -> SetDelay_1[SetDelay_1_T1]: ...

        SetDelay_1_T1 = typing.TypeVar('SetDelay_1_T1')
        class SetDelay_1(typing.Generic[SetDelay_1_T1]):
            SetDelay_1_U = PlayableExtensions.SetDelay_MethodGroup.SetDelay_1_T1
            def __call__(self, playable: SetDelay_1_U, delay: float) -> None:...


    # Skipped SetDone due to it being static, abstract and generic.

    SetDone : SetDone_MethodGroup
    class SetDone_MethodGroup:
        def __getitem__(self, t:typing.Type[SetDone_1_T1]) -> SetDone_1[SetDone_1_T1]: ...

        SetDone_1_T1 = typing.TypeVar('SetDone_1_T1')
        class SetDone_1(typing.Generic[SetDone_1_T1]):
            SetDone_1_U = PlayableExtensions.SetDone_MethodGroup.SetDone_1_T1
            def __call__(self, playable: SetDone_1_U, value: bool) -> None:...


    # Skipped SetDuration due to it being static, abstract and generic.

    SetDuration : SetDuration_MethodGroup
    class SetDuration_MethodGroup:
        def __getitem__(self, t:typing.Type[SetDuration_1_T1]) -> SetDuration_1[SetDuration_1_T1]: ...

        SetDuration_1_T1 = typing.TypeVar('SetDuration_1_T1')
        class SetDuration_1(typing.Generic[SetDuration_1_T1]):
            SetDuration_1_U = PlayableExtensions.SetDuration_MethodGroup.SetDuration_1_T1
            def __call__(self, playable: SetDuration_1_U, value: float) -> None:...


    # Skipped SetInputCount due to it being static, abstract and generic.

    SetInputCount : SetInputCount_MethodGroup
    class SetInputCount_MethodGroup:
        def __getitem__(self, t:typing.Type[SetInputCount_1_T1]) -> SetInputCount_1[SetInputCount_1_T1]: ...

        SetInputCount_1_T1 = typing.TypeVar('SetInputCount_1_T1')
        class SetInputCount_1(typing.Generic[SetInputCount_1_T1]):
            SetInputCount_1_U = PlayableExtensions.SetInputCount_MethodGroup.SetInputCount_1_T1
            def __call__(self, playable: SetInputCount_1_U, value: int) -> None:...


    # Skipped SetInputWeight due to it being static, abstract and generic.

    SetInputWeight : SetInputWeight_MethodGroup
    class SetInputWeight_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[SetInputWeight_1_T1]) -> SetInputWeight_1[SetInputWeight_1_T1]: ...

        SetInputWeight_1_T1 = typing.TypeVar('SetInputWeight_1_T1')
        class SetInputWeight_1(typing.Generic[SetInputWeight_1_T1]):
            SetInputWeight_1_U = PlayableExtensions.SetInputWeight_MethodGroup.SetInputWeight_1_T1
            def __call__(self, playable: SetInputWeight_1_U, inputIndex: int, weight: float) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[SetInputWeight_2_T1], typing.Type[SetInputWeight_2_T2]]) -> SetInputWeight_2[SetInputWeight_2_T1, SetInputWeight_2_T2]: ...

        SetInputWeight_2_T1 = typing.TypeVar('SetInputWeight_2_T1')
        SetInputWeight_2_T2 = typing.TypeVar('SetInputWeight_2_T2')
        class SetInputWeight_2(typing.Generic[SetInputWeight_2_T1, SetInputWeight_2_T2]):
            SetInputWeight_2_U = PlayableExtensions.SetInputWeight_MethodGroup.SetInputWeight_2_T1
            SetInputWeight_2_V = PlayableExtensions.SetInputWeight_MethodGroup.SetInputWeight_2_T2
            def __call__(self, playable: SetInputWeight_2_U, input: SetInputWeight_2_V, weight: float) -> None:...


    # Skipped SetLeadTime due to it being static, abstract and generic.

    SetLeadTime : SetLeadTime_MethodGroup
    class SetLeadTime_MethodGroup:
        def __getitem__(self, t:typing.Type[SetLeadTime_1_T1]) -> SetLeadTime_1[SetLeadTime_1_T1]: ...

        SetLeadTime_1_T1 = typing.TypeVar('SetLeadTime_1_T1')
        class SetLeadTime_1(typing.Generic[SetLeadTime_1_T1]):
            SetLeadTime_1_U = PlayableExtensions.SetLeadTime_MethodGroup.SetLeadTime_1_T1
            def __call__(self, playable: SetLeadTime_1_U, value: float) -> None:...


    # Skipped SetOutputCount due to it being static, abstract and generic.

    SetOutputCount : SetOutputCount_MethodGroup
    class SetOutputCount_MethodGroup:
        def __getitem__(self, t:typing.Type[SetOutputCount_1_T1]) -> SetOutputCount_1[SetOutputCount_1_T1]: ...

        SetOutputCount_1_T1 = typing.TypeVar('SetOutputCount_1_T1')
        class SetOutputCount_1(typing.Generic[SetOutputCount_1_T1]):
            SetOutputCount_1_U = PlayableExtensions.SetOutputCount_MethodGroup.SetOutputCount_1_T1
            def __call__(self, playable: SetOutputCount_1_U, value: int) -> None:...


    # Skipped SetPlayState due to it being static, abstract and generic.

    SetPlayState : SetPlayState_MethodGroup
    class SetPlayState_MethodGroup:
        def __getitem__(self, t:typing.Type[SetPlayState_1_T1]) -> SetPlayState_1[SetPlayState_1_T1]: ...

        SetPlayState_1_T1 = typing.TypeVar('SetPlayState_1_T1')
        class SetPlayState_1(typing.Generic[SetPlayState_1_T1]):
            SetPlayState_1_U = PlayableExtensions.SetPlayState_MethodGroup.SetPlayState_1_T1
            def __call__(self, playable: SetPlayState_1_U, value: PlayState) -> None:...


    # Skipped SetPropagateSetTime due to it being static, abstract and generic.

    SetPropagateSetTime : SetPropagateSetTime_MethodGroup
    class SetPropagateSetTime_MethodGroup:
        def __getitem__(self, t:typing.Type[SetPropagateSetTime_1_T1]) -> SetPropagateSetTime_1[SetPropagateSetTime_1_T1]: ...

        SetPropagateSetTime_1_T1 = typing.TypeVar('SetPropagateSetTime_1_T1')
        class SetPropagateSetTime_1(typing.Generic[SetPropagateSetTime_1_T1]):
            SetPropagateSetTime_1_U = PlayableExtensions.SetPropagateSetTime_MethodGroup.SetPropagateSetTime_1_T1
            def __call__(self, playable: SetPropagateSetTime_1_U, value: bool) -> None:...


    # Skipped SetSpeed due to it being static, abstract and generic.

    SetSpeed : SetSpeed_MethodGroup
    class SetSpeed_MethodGroup:
        def __getitem__(self, t:typing.Type[SetSpeed_1_T1]) -> SetSpeed_1[SetSpeed_1_T1]: ...

        SetSpeed_1_T1 = typing.TypeVar('SetSpeed_1_T1')
        class SetSpeed_1(typing.Generic[SetSpeed_1_T1]):
            SetSpeed_1_U = PlayableExtensions.SetSpeed_MethodGroup.SetSpeed_1_T1
            def __call__(self, playable: SetSpeed_1_U, value: float) -> None:...


    # Skipped SetTime due to it being static, abstract and generic.

    SetTime : SetTime_MethodGroup
    class SetTime_MethodGroup:
        def __getitem__(self, t:typing.Type[SetTime_1_T1]) -> SetTime_1[SetTime_1_T1]: ...

        SetTime_1_T1 = typing.TypeVar('SetTime_1_T1')
        class SetTime_1(typing.Generic[SetTime_1_T1]):
            SetTime_1_U = PlayableExtensions.SetTime_MethodGroup.SetTime_1_T1
            def __call__(self, playable: SetTime_1_U, value: float) -> None:...


    # Skipped SetTraversalMode due to it being static, abstract and generic.

    SetTraversalMode : SetTraversalMode_MethodGroup
    class SetTraversalMode_MethodGroup:
        def __getitem__(self, t:typing.Type[SetTraversalMode_1_T1]) -> SetTraversalMode_1[SetTraversalMode_1_T1]: ...

        SetTraversalMode_1_T1 = typing.TypeVar('SetTraversalMode_1_T1')
        class SetTraversalMode_1(typing.Generic[SetTraversalMode_1_T1]):
            SetTraversalMode_1_U = PlayableExtensions.SetTraversalMode_MethodGroup.SetTraversalMode_1_T1
            def __call__(self, playable: SetTraversalMode_1_U, mode: PlayableTraversalMode) -> None:...




class PlayableGraph:
    def Destroy(self) -> None: ...
    def GetEditorName(self) -> str: ...
    def GetOutput(self, index: int) -> PlayableOutput: ...
    def GetOutputCount(self) -> int: ...
    def GetPlayableCount(self) -> int: ...
    def GetResolver(self) -> IExposedPropertyTable: ...
    def GetRootPlayable(self, index: int) -> Playable: ...
    def GetRootPlayableCount(self) -> int: ...
    def GetTimeUpdateMode(self) -> DirectorUpdateMode: ...
    def IsDone(self) -> bool: ...
    def IsPlaying(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def Play(self) -> None: ...
    def SetResolver(self, value: IExposedPropertyTable) -> None: ...
    def SetTimeUpdateMode(self, value: DirectorUpdateMode) -> None: ...
    def Stop(self) -> None: ...
    # Skipped Connect due to it being static, abstract and generic.

    Connect : Connect_MethodGroup
    class Connect_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Connect_2_T1], typing.Type[Connect_2_T2]]) -> Connect_2[Connect_2_T1, Connect_2_T2]: ...

        Connect_2_T1 = typing.TypeVar('Connect_2_T1')
        Connect_2_T2 = typing.TypeVar('Connect_2_T2')
        class Connect_2(typing.Generic[Connect_2_T1, Connect_2_T2]):
            Connect_2_U = PlayableGraph.Connect_MethodGroup.Connect_2_T1
            Connect_2_V = PlayableGraph.Connect_MethodGroup.Connect_2_T2
            def __call__(self, source: Connect_2_U, sourceOutputPort: int, destination: Connect_2_V, destinationInputPort: int) -> bool:...


    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup
    class Create_MethodGroup:
        @typing.overload
        def __call__(self) -> PlayableGraph:...
        @typing.overload
        def __call__(self, name: str) -> PlayableGraph:...

    # Skipped DestroyOutput due to it being static, abstract and generic.

    DestroyOutput : DestroyOutput_MethodGroup
    class DestroyOutput_MethodGroup:
        def __getitem__(self, t:typing.Type[DestroyOutput_1_T1]) -> DestroyOutput_1[DestroyOutput_1_T1]: ...

        DestroyOutput_1_T1 = typing.TypeVar('DestroyOutput_1_T1')
        class DestroyOutput_1(typing.Generic[DestroyOutput_1_T1]):
            DestroyOutput_1_U = PlayableGraph.DestroyOutput_MethodGroup.DestroyOutput_1_T1
            def __call__(self, output: DestroyOutput_1_U) -> None:...


    # Skipped DestroyPlayable due to it being static, abstract and generic.

    DestroyPlayable : DestroyPlayable_MethodGroup
    class DestroyPlayable_MethodGroup:
        def __getitem__(self, t:typing.Type[DestroyPlayable_1_T1]) -> DestroyPlayable_1[DestroyPlayable_1_T1]: ...

        DestroyPlayable_1_T1 = typing.TypeVar('DestroyPlayable_1_T1')
        class DestroyPlayable_1(typing.Generic[DestroyPlayable_1_T1]):
            DestroyPlayable_1_U = PlayableGraph.DestroyPlayable_MethodGroup.DestroyPlayable_1_T1
            def __call__(self, playable: DestroyPlayable_1_U) -> None:...


    # Skipped DestroySubgraph due to it being static, abstract and generic.

    DestroySubgraph : DestroySubgraph_MethodGroup
    class DestroySubgraph_MethodGroup:
        def __getitem__(self, t:typing.Type[DestroySubgraph_1_T1]) -> DestroySubgraph_1[DestroySubgraph_1_T1]: ...

        DestroySubgraph_1_T1 = typing.TypeVar('DestroySubgraph_1_T1')
        class DestroySubgraph_1(typing.Generic[DestroySubgraph_1_T1]):
            DestroySubgraph_1_U = PlayableGraph.DestroySubgraph_MethodGroup.DestroySubgraph_1_T1
            def __call__(self, playable: DestroySubgraph_1_U) -> None:...


    # Skipped Disconnect due to it being static, abstract and generic.

    Disconnect : Disconnect_MethodGroup
    class Disconnect_MethodGroup:
        def __getitem__(self, t:typing.Type[Disconnect_1_T1]) -> Disconnect_1[Disconnect_1_T1]: ...

        Disconnect_1_T1 = typing.TypeVar('Disconnect_1_T1')
        class Disconnect_1(typing.Generic[Disconnect_1_T1]):
            Disconnect_1_U = PlayableGraph.Disconnect_MethodGroup.Disconnect_1_T1
            def __call__(self, input: Disconnect_1_U, inputPort: int) -> None:...


    # Skipped Evaluate due to it being static, abstract and generic.

    Evaluate : Evaluate_MethodGroup
    class Evaluate_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, deltaTime: float) -> None:...

    # Skipped GetOutputByType due to it being static, abstract and generic.

    GetOutputByType : GetOutputByType_MethodGroup
    class GetOutputByType_MethodGroup:
        def __getitem__(self, t:typing.Type[GetOutputByType_1_T1]) -> GetOutputByType_1[GetOutputByType_1_T1]: ...

        GetOutputByType_1_T1 = typing.TypeVar('GetOutputByType_1_T1')
        class GetOutputByType_1(typing.Generic[GetOutputByType_1_T1]):
            GetOutputByType_1_T = PlayableGraph.GetOutputByType_MethodGroup.GetOutputByType_1_T1
            def __call__(self, index: int) -> PlayableOutput:...


    # Skipped GetOutputCountByType due to it being static, abstract and generic.

    GetOutputCountByType : GetOutputCountByType_MethodGroup
    class GetOutputCountByType_MethodGroup:
        def __getitem__(self, t:typing.Type[GetOutputCountByType_1_T1]) -> GetOutputCountByType_1[GetOutputCountByType_1_T1]: ...

        GetOutputCountByType_1_T1 = typing.TypeVar('GetOutputCountByType_1_T1')
        class GetOutputCountByType_1(typing.Generic[GetOutputCountByType_1_T1]):
            GetOutputCountByType_1_T = PlayableGraph.GetOutputCountByType_MethodGroup.GetOutputCountByType_1_T1
            def __call__(self) -> int:...




class PlayableHandle(IEquatable_1[PlayableHandle]):
    @classmethod
    @property
    def Null(cls) -> PlayableHandle: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, x: PlayableHandle, y: PlayableHandle) -> bool: ...
    def __ne__(self, x: PlayableHandle, y: PlayableHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: PlayableHandle) -> bool:...
        @typing.overload
        def __call__(self, p: typing.Any) -> bool:...



class PlayableOutput(IEquatable_1[PlayableOutput], IPlayableOutput):
    @classmethod
    @property
    def Null(cls) -> PlayableOutput: ...
    def Equals(self, other: PlayableOutput) -> bool: ...
    def GetHandle(self) -> PlayableOutputHandle: ...
    def GetPlayableOutputType(self) -> typing.Type[typing.Any]: ...
    # Skipped IsPlayableOutputOfType due to it being static, abstract and generic.

    IsPlayableOutputOfType : IsPlayableOutputOfType_MethodGroup
    class IsPlayableOutputOfType_MethodGroup:
        def __getitem__(self, t:typing.Type[IsPlayableOutputOfType_1_T1]) -> IsPlayableOutputOfType_1[IsPlayableOutputOfType_1_T1]: ...

        IsPlayableOutputOfType_1_T1 = typing.TypeVar('IsPlayableOutputOfType_1_T1')
        class IsPlayableOutputOfType_1(typing.Generic[IsPlayableOutputOfType_1_T1]):
            IsPlayableOutputOfType_1_T = PlayableOutput.IsPlayableOutputOfType_MethodGroup.IsPlayableOutputOfType_1_T1
            def __call__(self) -> bool:...




class PlayableOutputExtensions(abc.ABC):
    # Skipped AddNotificationReceiver due to it being static, abstract and generic.

    AddNotificationReceiver : AddNotificationReceiver_MethodGroup
    class AddNotificationReceiver_MethodGroup:
        def __getitem__(self, t:typing.Type[AddNotificationReceiver_1_T1]) -> AddNotificationReceiver_1[AddNotificationReceiver_1_T1]: ...

        AddNotificationReceiver_1_T1 = typing.TypeVar('AddNotificationReceiver_1_T1')
        class AddNotificationReceiver_1(typing.Generic[AddNotificationReceiver_1_T1]):
            AddNotificationReceiver_1_U = PlayableOutputExtensions.AddNotificationReceiver_MethodGroup.AddNotificationReceiver_1_T1
            def __call__(self, output: AddNotificationReceiver_1_U, receiver: INotificationReceiver) -> None:...


    # Skipped GetNotificationReceivers due to it being static, abstract and generic.

    GetNotificationReceivers : GetNotificationReceivers_MethodGroup
    class GetNotificationReceivers_MethodGroup:
        def __getitem__(self, t:typing.Type[GetNotificationReceivers_1_T1]) -> GetNotificationReceivers_1[GetNotificationReceivers_1_T1]: ...

        GetNotificationReceivers_1_T1 = typing.TypeVar('GetNotificationReceivers_1_T1')
        class GetNotificationReceivers_1(typing.Generic[GetNotificationReceivers_1_T1]):
            GetNotificationReceivers_1_U = PlayableOutputExtensions.GetNotificationReceivers_MethodGroup.GetNotificationReceivers_1_T1
            def __call__(self, output: GetNotificationReceivers_1_U) -> Array_1[INotificationReceiver]:...


    # Skipped GetReferenceObject due to it being static, abstract and generic.

    GetReferenceObject : GetReferenceObject_MethodGroup
    class GetReferenceObject_MethodGroup:
        def __getitem__(self, t:typing.Type[GetReferenceObject_1_T1]) -> GetReferenceObject_1[GetReferenceObject_1_T1]: ...

        GetReferenceObject_1_T1 = typing.TypeVar('GetReferenceObject_1_T1')
        class GetReferenceObject_1(typing.Generic[GetReferenceObject_1_T1]):
            GetReferenceObject_1_U = PlayableOutputExtensions.GetReferenceObject_MethodGroup.GetReferenceObject_1_T1
            def __call__(self, output: GetReferenceObject_1_U) -> Object:...


    # Skipped GetSourceInputPort due to it being static, abstract and generic.

    GetSourceInputPort : GetSourceInputPort_MethodGroup
    class GetSourceInputPort_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSourceInputPort_1_T1]) -> GetSourceInputPort_1[GetSourceInputPort_1_T1]: ...

        GetSourceInputPort_1_T1 = typing.TypeVar('GetSourceInputPort_1_T1')
        class GetSourceInputPort_1(typing.Generic[GetSourceInputPort_1_T1]):
            GetSourceInputPort_1_U = PlayableOutputExtensions.GetSourceInputPort_MethodGroup.GetSourceInputPort_1_T1
            def __call__(self, output: GetSourceInputPort_1_U) -> int:...


    # Skipped GetSourceOutputPort due to it being static, abstract and generic.

    GetSourceOutputPort : GetSourceOutputPort_MethodGroup
    class GetSourceOutputPort_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSourceOutputPort_1_T1]) -> GetSourceOutputPort_1[GetSourceOutputPort_1_T1]: ...

        GetSourceOutputPort_1_T1 = typing.TypeVar('GetSourceOutputPort_1_T1')
        class GetSourceOutputPort_1(typing.Generic[GetSourceOutputPort_1_T1]):
            GetSourceOutputPort_1_U = PlayableOutputExtensions.GetSourceOutputPort_MethodGroup.GetSourceOutputPort_1_T1
            def __call__(self, output: GetSourceOutputPort_1_U) -> int:...


    # Skipped GetSourcePlayable due to it being static, abstract and generic.

    GetSourcePlayable : GetSourcePlayable_MethodGroup
    class GetSourcePlayable_MethodGroup:
        def __getitem__(self, t:typing.Type[GetSourcePlayable_1_T1]) -> GetSourcePlayable_1[GetSourcePlayable_1_T1]: ...

        GetSourcePlayable_1_T1 = typing.TypeVar('GetSourcePlayable_1_T1')
        class GetSourcePlayable_1(typing.Generic[GetSourcePlayable_1_T1]):
            GetSourcePlayable_1_U = PlayableOutputExtensions.GetSourcePlayable_MethodGroup.GetSourcePlayable_1_T1
            def __call__(self, output: GetSourcePlayable_1_U) -> Playable:...


    # Skipped GetUserData due to it being static, abstract and generic.

    GetUserData : GetUserData_MethodGroup
    class GetUserData_MethodGroup:
        def __getitem__(self, t:typing.Type[GetUserData_1_T1]) -> GetUserData_1[GetUserData_1_T1]: ...

        GetUserData_1_T1 = typing.TypeVar('GetUserData_1_T1')
        class GetUserData_1(typing.Generic[GetUserData_1_T1]):
            GetUserData_1_U = PlayableOutputExtensions.GetUserData_MethodGroup.GetUserData_1_T1
            def __call__(self, output: GetUserData_1_U) -> Object:...


    # Skipped GetWeight due to it being static, abstract and generic.

    GetWeight : GetWeight_MethodGroup
    class GetWeight_MethodGroup:
        def __getitem__(self, t:typing.Type[GetWeight_1_T1]) -> GetWeight_1[GetWeight_1_T1]: ...

        GetWeight_1_T1 = typing.TypeVar('GetWeight_1_T1')
        class GetWeight_1(typing.Generic[GetWeight_1_T1]):
            GetWeight_1_U = PlayableOutputExtensions.GetWeight_MethodGroup.GetWeight_1_T1
            def __call__(self, output: GetWeight_1_U) -> float:...


    # Skipped IsOutputNull due to it being static, abstract and generic.

    IsOutputNull : IsOutputNull_MethodGroup
    class IsOutputNull_MethodGroup:
        def __getitem__(self, t:typing.Type[IsOutputNull_1_T1]) -> IsOutputNull_1[IsOutputNull_1_T1]: ...

        IsOutputNull_1_T1 = typing.TypeVar('IsOutputNull_1_T1')
        class IsOutputNull_1(typing.Generic[IsOutputNull_1_T1]):
            IsOutputNull_1_U = PlayableOutputExtensions.IsOutputNull_MethodGroup.IsOutputNull_1_T1
            def __call__(self, output: IsOutputNull_1_U) -> bool:...


    # Skipped IsOutputValid due to it being static, abstract and generic.

    IsOutputValid : IsOutputValid_MethodGroup
    class IsOutputValid_MethodGroup:
        def __getitem__(self, t:typing.Type[IsOutputValid_1_T1]) -> IsOutputValid_1[IsOutputValid_1_T1]: ...

        IsOutputValid_1_T1 = typing.TypeVar('IsOutputValid_1_T1')
        class IsOutputValid_1(typing.Generic[IsOutputValid_1_T1]):
            IsOutputValid_1_U = PlayableOutputExtensions.IsOutputValid_MethodGroup.IsOutputValid_1_T1
            def __call__(self, output: IsOutputValid_1_U) -> bool:...


    # Skipped PushNotification due to it being static, abstract and generic.

    PushNotification : PushNotification_MethodGroup
    class PushNotification_MethodGroup:
        def __getitem__(self, t:typing.Type[PushNotification_1_T1]) -> PushNotification_1[PushNotification_1_T1]: ...

        PushNotification_1_T1 = typing.TypeVar('PushNotification_1_T1')
        class PushNotification_1(typing.Generic[PushNotification_1_T1]):
            PushNotification_1_U = PlayableOutputExtensions.PushNotification_MethodGroup.PushNotification_1_T1
            def __call__(self, output: PushNotification_1_U, origin: Playable, notification: INotification, context: typing.Any = ...) -> None:...


    # Skipped RemoveNotificationReceiver due to it being static, abstract and generic.

    RemoveNotificationReceiver : RemoveNotificationReceiver_MethodGroup
    class RemoveNotificationReceiver_MethodGroup:
        def __getitem__(self, t:typing.Type[RemoveNotificationReceiver_1_T1]) -> RemoveNotificationReceiver_1[RemoveNotificationReceiver_1_T1]: ...

        RemoveNotificationReceiver_1_T1 = typing.TypeVar('RemoveNotificationReceiver_1_T1')
        class RemoveNotificationReceiver_1(typing.Generic[RemoveNotificationReceiver_1_T1]):
            RemoveNotificationReceiver_1_U = PlayableOutputExtensions.RemoveNotificationReceiver_MethodGroup.RemoveNotificationReceiver_1_T1
            def __call__(self, output: RemoveNotificationReceiver_1_U, receiver: INotificationReceiver) -> None:...


    # Skipped SetReferenceObject due to it being static, abstract and generic.

    SetReferenceObject : SetReferenceObject_MethodGroup
    class SetReferenceObject_MethodGroup:
        def __getitem__(self, t:typing.Type[SetReferenceObject_1_T1]) -> SetReferenceObject_1[SetReferenceObject_1_T1]: ...

        SetReferenceObject_1_T1 = typing.TypeVar('SetReferenceObject_1_T1')
        class SetReferenceObject_1(typing.Generic[SetReferenceObject_1_T1]):
            SetReferenceObject_1_U = PlayableOutputExtensions.SetReferenceObject_MethodGroup.SetReferenceObject_1_T1
            def __call__(self, output: SetReferenceObject_1_U, value: Object) -> None:...


    # Skipped SetSourceInputPort due to it being static, abstract and generic.

    SetSourceInputPort : SetSourceInputPort_MethodGroup
    class SetSourceInputPort_MethodGroup:
        def __getitem__(self, t:typing.Type[SetSourceInputPort_1_T1]) -> SetSourceInputPort_1[SetSourceInputPort_1_T1]: ...

        SetSourceInputPort_1_T1 = typing.TypeVar('SetSourceInputPort_1_T1')
        class SetSourceInputPort_1(typing.Generic[SetSourceInputPort_1_T1]):
            SetSourceInputPort_1_U = PlayableOutputExtensions.SetSourceInputPort_MethodGroup.SetSourceInputPort_1_T1
            def __call__(self, output: SetSourceInputPort_1_U, value: int) -> None:...


    # Skipped SetSourceOutputPort due to it being static, abstract and generic.

    SetSourceOutputPort : SetSourceOutputPort_MethodGroup
    class SetSourceOutputPort_MethodGroup:
        def __getitem__(self, t:typing.Type[SetSourceOutputPort_1_T1]) -> SetSourceOutputPort_1[SetSourceOutputPort_1_T1]: ...

        SetSourceOutputPort_1_T1 = typing.TypeVar('SetSourceOutputPort_1_T1')
        class SetSourceOutputPort_1(typing.Generic[SetSourceOutputPort_1_T1]):
            SetSourceOutputPort_1_U = PlayableOutputExtensions.SetSourceOutputPort_MethodGroup.SetSourceOutputPort_1_T1
            def __call__(self, output: SetSourceOutputPort_1_U, value: int) -> None:...


    # Skipped SetSourcePlayable due to it being static, abstract and generic.

    SetSourcePlayable : SetSourcePlayable_MethodGroup
    class SetSourcePlayable_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[SetSourcePlayable_2_T1], typing.Type[SetSourcePlayable_2_T2]]) -> SetSourcePlayable_2[SetSourcePlayable_2_T1, SetSourcePlayable_2_T2]: ...

        SetSourcePlayable_2_T1 = typing.TypeVar('SetSourcePlayable_2_T1')
        SetSourcePlayable_2_T2 = typing.TypeVar('SetSourcePlayable_2_T2')
        class SetSourcePlayable_2(typing.Generic[SetSourcePlayable_2_T1, SetSourcePlayable_2_T2]):
            SetSourcePlayable_2_U = PlayableOutputExtensions.SetSourcePlayable_MethodGroup.SetSourcePlayable_2_T1
            SetSourcePlayable_2_V = PlayableOutputExtensions.SetSourcePlayable_MethodGroup.SetSourcePlayable_2_T2
            @typing.overload
            def __call__(self, output: SetSourcePlayable_2_U, value: SetSourcePlayable_2_V) -> None:...
            @typing.overload
            def __call__(self, output: SetSourcePlayable_2_U, value: SetSourcePlayable_2_V, port: int) -> None:...


    # Skipped SetUserData due to it being static, abstract and generic.

    SetUserData : SetUserData_MethodGroup
    class SetUserData_MethodGroup:
        def __getitem__(self, t:typing.Type[SetUserData_1_T1]) -> SetUserData_1[SetUserData_1_T1]: ...

        SetUserData_1_T1 = typing.TypeVar('SetUserData_1_T1')
        class SetUserData_1(typing.Generic[SetUserData_1_T1]):
            SetUserData_1_U = PlayableOutputExtensions.SetUserData_MethodGroup.SetUserData_1_T1
            def __call__(self, output: SetUserData_1_U, value: Object) -> None:...


    # Skipped SetWeight due to it being static, abstract and generic.

    SetWeight : SetWeight_MethodGroup
    class SetWeight_MethodGroup:
        def __getitem__(self, t:typing.Type[SetWeight_1_T1]) -> SetWeight_1[SetWeight_1_T1]: ...

        SetWeight_1_T1 = typing.TypeVar('SetWeight_1_T1')
        class SetWeight_1(typing.Generic[SetWeight_1_T1]):
            SetWeight_1_U = PlayableOutputExtensions.SetWeight_MethodGroup.SetWeight_1_T1
            def __call__(self, output: SetWeight_1_U, value: float) -> None:...




class PlayableOutputHandle(IEquatable_1[PlayableOutputHandle]):
    @classmethod
    @property
    def Null(cls) -> PlayableOutputHandle: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, lhs: PlayableOutputHandle, rhs: PlayableOutputHandle) -> bool: ...
    def __ne__(self, lhs: PlayableOutputHandle, rhs: PlayableOutputHandle) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: PlayableOutputHandle) -> bool:...
        @typing.overload
        def __call__(self, p: typing.Any) -> bool:...



class PlayableTraversalMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Mix : PlayableTraversalMode # 0
    Passthrough : PlayableTraversalMode # 1


class PlayState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Paused : PlayState # 0
    Playing : PlayState # 1
    Delayed : PlayState # 2


class ScriptPlayable_GenericClasses(abc.ABCMeta):
    Generic_ScriptPlayable_GenericClasses_ScriptPlayable_1_T = typing.TypeVar('Generic_ScriptPlayable_GenericClasses_ScriptPlayable_1_T')
    def __getitem__(self, types : typing.Type[Generic_ScriptPlayable_GenericClasses_ScriptPlayable_1_T]) -> typing.Type[ScriptPlayable_1[Generic_ScriptPlayable_GenericClasses_ScriptPlayable_1_T]]: ...

ScriptPlayable : ScriptPlayable_GenericClasses

ScriptPlayable_1_T = typing.TypeVar('ScriptPlayable_1_T')
class ScriptPlayable_1(typing.Generic[ScriptPlayable_1_T], IEquatable_1[ScriptPlayable_1[ScriptPlayable_1_T]], IPlayable):
    @classmethod
    @property
    def Null(cls) -> ScriptPlayable_1[ScriptPlayable_1_T]: ...
    def Equals(self, other: ScriptPlayable_1[ScriptPlayable_1_T]) -> bool: ...
    def GetBehaviour(self) -> ScriptPlayable_1_T: ...
    def GetHandle(self) -> PlayableHandle: ...
    # Operator not supported op_Explicit(playable: Playable)
    # Operator not supported op_Implicit(playable: ScriptPlayable`1)
    # Skipped Create due to it being static, abstract and generic.

    Create : Create_MethodGroup[ScriptPlayable_1_T]
    Create_MethodGroup_ScriptPlayable_1_T = typing.TypeVar('Create_MethodGroup_ScriptPlayable_1_T')
    class Create_MethodGroup(typing.Generic[Create_MethodGroup_ScriptPlayable_1_T]):
        Create_MethodGroup_ScriptPlayable_1_T = ScriptPlayable_1.Create_MethodGroup_ScriptPlayable_1_T
        @typing.overload
        def __call__(self, graph: PlayableGraph, inputCount: int = ...) -> ScriptPlayable_1[Create_MethodGroup_ScriptPlayable_1_T]:...
        @typing.overload
        def __call__(self, graph: PlayableGraph, template: Create_MethodGroup_ScriptPlayable_1_T, inputCount: int = ...) -> ScriptPlayable_1[Create_MethodGroup_ScriptPlayable_1_T]:...



class ScriptPlayableBinding(abc.ABC):
    @staticmethod
    def Create(name: str, key: Object, type: typing.Type[typing.Any]) -> PlayableBinding: ...


class ScriptPlayableOutput(IPlayableOutput):
    @classmethod
    @property
    def Null(cls) -> ScriptPlayableOutput: ...
    @staticmethod
    def Create(graph: PlayableGraph, name: str) -> ScriptPlayableOutput: ...
    def GetHandle(self) -> PlayableOutputHandle: ...
    # Operator not supported op_Explicit(output: PlayableOutput)
    # Operator not supported op_Implicit(output: ScriptPlayableOutput)

