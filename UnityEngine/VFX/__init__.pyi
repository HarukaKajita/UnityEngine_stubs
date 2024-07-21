import typing, abc
from System import IDisposable, Array_1, Action_1
from UnityEngine import Matrix4x4, Vector2, Vector3, Vector4, AnimationCurve, Gradient, Mesh, Texture, Camera, Bounds, ScriptableObject, HideFlags, Behaviour, Component, GameObject, Transform, SkinnedMeshRenderer, GraphicsBuffer, Object
from System.Collections.Generic import List_1
from UnityEngine.Rendering import CommandBuffer, CullingResults, TextureDimension

class VFXBatchedEffectInfo:
    activeBatchCount : int
    activeInstanceCount : int
    inactiveBatchCount : int
    maxInstancePerBatchCapacity : int
    totalCPUSizeInBytes : int
    totalGPUSizeInBytes : int
    totalInstanceCapacity : int
    unbatchedInstanceCount : int
    vfxAsset : VisualEffectAsset


class VFXCameraBufferTypes(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : VFXCameraBufferTypes # 0
    Depth : VFXCameraBufferTypes # 1
    Color : VFXCameraBufferTypes # 2
    Normal : VFXCameraBufferTypes # 4


class VFXCameraXRSettings:
    viewCount : int
    viewOffset : int
    viewTotal : int


class VFXEventAttribute(IDisposable):
    def __init__(self, original: VFXEventAttribute) -> None: ...
    def CopyValuesFrom(self, eventAttibute: VFXEventAttribute) -> None: ...
    def Dispose(self) -> None: ...
    # Skipped GetBool due to it being static, abstract and generic.

    GetBool : GetBool_MethodGroup
    class GetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped GetFloat due to it being static, abstract and generic.

    GetFloat : GetFloat_MethodGroup
    class GetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> float:...
        @typing.overload
        def __call__(self, name: str) -> float:...

    # Skipped GetInt due to it being static, abstract and generic.

    GetInt : GetInt_MethodGroup
    class GetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetMatrix4x4 due to it being static, abstract and generic.

    GetMatrix4x4 : GetMatrix4x4_MethodGroup
    class GetMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Matrix4x4:...
        @typing.overload
        def __call__(self, name: str) -> Matrix4x4:...

    # Skipped GetUint due to it being static, abstract and generic.

    GetUint : GetUint_MethodGroup
    class GetUint_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetVector2 due to it being static, abstract and generic.

    GetVector2 : GetVector2_MethodGroup
    class GetVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector2:...
        @typing.overload
        def __call__(self, name: str) -> Vector2:...

    # Skipped GetVector3 due to it being static, abstract and generic.

    GetVector3 : GetVector3_MethodGroup
    class GetVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector3:...
        @typing.overload
        def __call__(self, name: str) -> Vector3:...

    # Skipped GetVector4 due to it being static, abstract and generic.

    GetVector4 : GetVector4_MethodGroup
    class GetVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector4:...
        @typing.overload
        def __call__(self, name: str) -> Vector4:...

    # Skipped HasBool due to it being static, abstract and generic.

    HasBool : HasBool_MethodGroup
    class HasBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasFloat due to it being static, abstract and generic.

    HasFloat : HasFloat_MethodGroup
    class HasFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasInt due to it being static, abstract and generic.

    HasInt : HasInt_MethodGroup
    class HasInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasMatrix4x4 due to it being static, abstract and generic.

    HasMatrix4x4 : HasMatrix4x4_MethodGroup
    class HasMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasUint due to it being static, abstract and generic.

    HasUint : HasUint_MethodGroup
    class HasUint_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector2 due to it being static, abstract and generic.

    HasVector2 : HasVector2_MethodGroup
    class HasVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector3 due to it being static, abstract and generic.

    HasVector3 : HasVector3_MethodGroup
    class HasVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector4 due to it being static, abstract and generic.

    HasVector4 : HasVector4_MethodGroup
    class HasVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped SetBool due to it being static, abstract and generic.

    SetBool : SetBool_MethodGroup
    class SetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, b: bool) -> None:...
        @typing.overload
        def __call__(self, name: str, b: bool) -> None:...

    # Skipped SetFloat due to it being static, abstract and generic.

    SetFloat : SetFloat_MethodGroup
    class SetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, f: float) -> None:...
        @typing.overload
        def __call__(self, name: str, f: float) -> None:...

    # Skipped SetInt due to it being static, abstract and generic.

    SetInt : SetInt_MethodGroup
    class SetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, i: int) -> None:...
        @typing.overload
        def __call__(self, name: str, i: int) -> None:...

    # Skipped SetMatrix4x4 due to it being static, abstract and generic.

    SetMatrix4x4 : SetMatrix4x4_MethodGroup
    class SetMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Matrix4x4) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Matrix4x4) -> None:...

    # Skipped SetUint due to it being static, abstract and generic.

    SetUint : SetUint_MethodGroup
    class SetUint_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, i: int) -> None:...
        @typing.overload
        def __call__(self, name: str, i: int) -> None:...

    # Skipped SetVector2 due to it being static, abstract and generic.

    SetVector2 : SetVector2_MethodGroup
    class SetVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector2) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector2) -> None:...

    # Skipped SetVector3 due to it being static, abstract and generic.

    SetVector3 : SetVector3_MethodGroup
    class SetVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector3) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector3) -> None:...

    # Skipped SetVector4 due to it being static, abstract and generic.

    SetVector4 : SetVector4_MethodGroup
    class SetVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector4) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector4) -> None:...



class VFXExposedProperty:
    name : str
    type : typing.Type[typing.Any]


class VFXExpressionValues:
    # Skipped GetAnimationCurve due to it being static, abstract and generic.

    GetAnimationCurve : GetAnimationCurve_MethodGroup
    class GetAnimationCurve_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> AnimationCurve:...
        @typing.overload
        def __call__(self, name: str) -> AnimationCurve:...

    # Skipped GetBool due to it being static, abstract and generic.

    GetBool : GetBool_MethodGroup
    class GetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped GetFloat due to it being static, abstract and generic.

    GetFloat : GetFloat_MethodGroup
    class GetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> float:...
        @typing.overload
        def __call__(self, name: str) -> float:...

    # Skipped GetGradient due to it being static, abstract and generic.

    GetGradient : GetGradient_MethodGroup
    class GetGradient_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Gradient:...
        @typing.overload
        def __call__(self, name: str) -> Gradient:...

    # Skipped GetInt due to it being static, abstract and generic.

    GetInt : GetInt_MethodGroup
    class GetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetMatrix4x4 due to it being static, abstract and generic.

    GetMatrix4x4 : GetMatrix4x4_MethodGroup
    class GetMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Matrix4x4:...
        @typing.overload
        def __call__(self, name: str) -> Matrix4x4:...

    # Skipped GetMesh due to it being static, abstract and generic.

    GetMesh : GetMesh_MethodGroup
    class GetMesh_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Mesh:...
        @typing.overload
        def __call__(self, name: str) -> Mesh:...

    # Skipped GetTexture due to it being static, abstract and generic.

    GetTexture : GetTexture_MethodGroup
    class GetTexture_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Texture:...
        @typing.overload
        def __call__(self, name: str) -> Texture:...

    # Skipped GetUInt due to it being static, abstract and generic.

    GetUInt : GetUInt_MethodGroup
    class GetUInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetVector2 due to it being static, abstract and generic.

    GetVector2 : GetVector2_MethodGroup
    class GetVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector2:...
        @typing.overload
        def __call__(self, name: str) -> Vector2:...

    # Skipped GetVector3 due to it being static, abstract and generic.

    GetVector3 : GetVector3_MethodGroup
    class GetVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector3:...
        @typing.overload
        def __call__(self, name: str) -> Vector3:...

    # Skipped GetVector4 due to it being static, abstract and generic.

    GetVector4 : GetVector4_MethodGroup
    class GetVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector4:...
        @typing.overload
        def __call__(self, name: str) -> Vector4:...



class VFXManager(abc.ABC):
    @classmethod
    @property
    def fixedTimeStep(cls) -> float: ...
    @classmethod
    @fixedTimeStep.setter
    def fixedTimeStep(cls, value: float) -> float: ...
    @classmethod
    @property
    def maxDeltaTime(cls) -> float: ...
    @classmethod
    @maxDeltaTime.setter
    def maxDeltaTime(cls, value: float) -> float: ...
    @staticmethod
    def FlushEmptyBatches() -> None: ...
    @staticmethod
    def GetBatchedEffectInfo(vfx: VisualEffectAsset) -> VFXBatchedEffectInfo: ...
    @staticmethod
    def GetBatchedEffectInfos(infos: List_1[VFXBatchedEffectInfo]) -> None: ...
    @staticmethod
    def GetComponents() -> Array_1[VisualEffect]: ...
    @staticmethod
    def IsCameraBufferNeeded(cam: Camera) -> VFXCameraBufferTypes: ...
    @staticmethod
    def ProcessCamera(cam: Camera) -> None: ...
    @staticmethod
    def SetCameraBuffer(cam: Camera, type: VFXCameraBufferTypes, buffer: Texture, x: int, y: int, width: int, height: int) -> None: ...
    # Skipped PrepareCamera due to it being static, abstract and generic.

    PrepareCamera : PrepareCamera_MethodGroup
    class PrepareCamera_MethodGroup:
        @typing.overload
        def __call__(self, cam: Camera) -> None:...
        @typing.overload
        def __call__(self, cam: Camera, camXRSettings: VFXCameraXRSettings) -> None:...

    # Skipped ProcessCameraCommand due to it being static, abstract and generic.

    ProcessCameraCommand : ProcessCameraCommand_MethodGroup
    class ProcessCameraCommand_MethodGroup:
        @typing.overload
        def __call__(self, cam: Camera, cmd: CommandBuffer) -> None:...
        @typing.overload
        def __call__(self, cam: Camera, cmd: CommandBuffer, camXRSettings: VFXCameraXRSettings) -> None:...
        @typing.overload
        def __call__(self, cam: Camera, cmd: CommandBuffer, camXRSettings: VFXCameraXRSettings, results: CullingResults) -> None:...



class VFXOutputEventArgs:
    def __init__(self, nameId: int, eventAttribute: VFXEventAttribute) -> None: ...
    @property
    def eventAttribute(self) -> VFXEventAttribute: ...
    @property
    def nameId(self) -> int: ...


class VFXParticleSystemInfo:
    def __init__(self, aliveCount: int, capacity: int, sleeping: bool, bounds: Bounds) -> None: ...
    aliveCount : int
    bounds : Bounds
    capacity : int
    sleeping : bool


class VFXSpawnerCallbacks(ScriptableObject, abc.ABC):
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @abc.abstractmethod
    def OnPlay(self, state: VFXSpawnerState, vfxValues: VFXExpressionValues, vfxComponent: VisualEffect) -> None: ...
    @abc.abstractmethod
    def OnStop(self, state: VFXSpawnerState, vfxValues: VFXExpressionValues, vfxComponent: VisualEffect) -> None: ...
    @abc.abstractmethod
    def OnUpdate(self, state: VFXSpawnerState, vfxValues: VFXExpressionValues, vfxComponent: VisualEffect) -> None: ...


class VFXSpawnerLoopState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Finished : VFXSpawnerLoopState # 0
    DelayingBeforeLoop : VFXSpawnerLoopState # 1
    Looping : VFXSpawnerLoopState # 2
    DelayingAfterLoop : VFXSpawnerLoopState # 3


class VFXSpawnerState(IDisposable):
    def __init__(self) -> None: ...
    @property
    def delayAfterLoop(self) -> float: ...
    @delayAfterLoop.setter
    def delayAfterLoop(self, value: float) -> float: ...
    @property
    def delayBeforeLoop(self) -> float: ...
    @delayBeforeLoop.setter
    def delayBeforeLoop(self, value: float) -> float: ...
    @property
    def deltaTime(self) -> float: ...
    @deltaTime.setter
    def deltaTime(self, value: float) -> float: ...
    @property
    def loopCount(self) -> int: ...
    @loopCount.setter
    def loopCount(self, value: int) -> int: ...
    @property
    def loopDuration(self) -> float: ...
    @loopDuration.setter
    def loopDuration(self, value: float) -> float: ...
    @property
    def loopIndex(self) -> int: ...
    @loopIndex.setter
    def loopIndex(self, value: int) -> int: ...
    @property
    def loopState(self) -> VFXSpawnerLoopState: ...
    @loopState.setter
    def loopState(self, value: VFXSpawnerLoopState) -> VFXSpawnerLoopState: ...
    @property
    def newLoop(self) -> bool: ...
    @property
    def playing(self) -> bool: ...
    @playing.setter
    def playing(self, value: bool) -> bool: ...
    @property
    def spawnCount(self) -> float: ...
    @spawnCount.setter
    def spawnCount(self, value: float) -> float: ...
    @property
    def totalTime(self) -> float: ...
    @totalTime.setter
    def totalTime(self, value: float) -> float: ...
    @property
    def vfxEventAttribute(self) -> VFXEventAttribute: ...
    def Dispose(self) -> None: ...


class VisualEffect(Behaviour):
    def __init__(self) -> None: ...
    outputEventReceived : Action_1[VFXOutputEventArgs]
    @property
    def aliveParticleCount(self) -> int: ...
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
    def culled(self) -> bool: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def initialEventID(self) -> int: ...
    @initialEventID.setter
    def initialEventID(self, value: int) -> int: ...
    @property
    def initialEventName(self) -> str: ...
    @initialEventName.setter
    def initialEventName(self, value: str) -> str: ...
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
    def pause(self) -> bool: ...
    @pause.setter
    def pause(self, value: bool) -> bool: ...
    @property
    def playRate(self) -> float: ...
    @playRate.setter
    def playRate(self, value: float) -> float: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def resetSeedOnPlay(self) -> bool: ...
    @resetSeedOnPlay.setter
    def resetSeedOnPlay(self, value: bool) -> bool: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def startSeed(self) -> int: ...
    @startSeed.setter
    def startSeed(self, value: int) -> int: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def visualEffectAsset(self) -> VisualEffectAsset: ...
    @visualEffectAsset.setter
    def visualEffectAsset(self, value: VisualEffectAsset) -> VisualEffectAsset: ...
    def AdvanceOneFrame(self) -> None: ...
    def CreateVFXEventAttribute(self) -> VFXEventAttribute: ...
    def GetOutputEventNames(self, names: List_1[str]) -> None: ...
    def GetParticleSystemNames(self, names: List_1[str]) -> None: ...
    def GetSpawnSystemNames(self, names: List_1[str]) -> None: ...
    def GetSystemNames(self, names: List_1[str]) -> None: ...
    def HasAnySystemAwake(self) -> bool: ...
    def Reinit(self) -> None: ...
    def Simulate(self, stepDeltaTime: float, stepCount: int = ...) -> None: ...
    # Skipped GetAnimationCurve due to it being static, abstract and generic.

    GetAnimationCurve : GetAnimationCurve_MethodGroup
    class GetAnimationCurve_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> AnimationCurve:...
        @typing.overload
        def __call__(self, name: str) -> AnimationCurve:...

    # Skipped GetBool due to it being static, abstract and generic.

    GetBool : GetBool_MethodGroup
    class GetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped GetFloat due to it being static, abstract and generic.

    GetFloat : GetFloat_MethodGroup
    class GetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> float:...
        @typing.overload
        def __call__(self, name: str) -> float:...

    # Skipped GetGradient due to it being static, abstract and generic.

    GetGradient : GetGradient_MethodGroup
    class GetGradient_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Gradient:...
        @typing.overload
        def __call__(self, name: str) -> Gradient:...

    # Skipped GetInt due to it being static, abstract and generic.

    GetInt : GetInt_MethodGroup
    class GetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetMatrix4x4 due to it being static, abstract and generic.

    GetMatrix4x4 : GetMatrix4x4_MethodGroup
    class GetMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Matrix4x4:...
        @typing.overload
        def __call__(self, name: str) -> Matrix4x4:...

    # Skipped GetMesh due to it being static, abstract and generic.

    GetMesh : GetMesh_MethodGroup
    class GetMesh_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Mesh:...
        @typing.overload
        def __call__(self, name: str) -> Mesh:...

    # Skipped GetParticleSystemInfo due to it being static, abstract and generic.

    GetParticleSystemInfo : GetParticleSystemInfo_MethodGroup
    class GetParticleSystemInfo_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> VFXParticleSystemInfo:...
        @typing.overload
        def __call__(self, name: str) -> VFXParticleSystemInfo:...

    # Skipped GetSkinnedMeshRenderer due to it being static, abstract and generic.

    GetSkinnedMeshRenderer : GetSkinnedMeshRenderer_MethodGroup
    class GetSkinnedMeshRenderer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> SkinnedMeshRenderer:...
        @typing.overload
        def __call__(self, name: str) -> SkinnedMeshRenderer:...

    # Skipped GetSpawnSystemInfo due to it being static, abstract and generic.

    GetSpawnSystemInfo : GetSpawnSystemInfo_MethodGroup
    class GetSpawnSystemInfo_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> VFXSpawnerState:...
        @typing.overload
        def __call__(self, name: str) -> VFXSpawnerState:...
        @typing.overload
        def __call__(self, nameID: int, spawnState: VFXSpawnerState) -> None:...

    # Skipped GetTexture due to it being static, abstract and generic.

    GetTexture : GetTexture_MethodGroup
    class GetTexture_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Texture:...
        @typing.overload
        def __call__(self, name: str) -> Texture:...

    # Skipped GetTextureDimension due to it being static, abstract and generic.

    GetTextureDimension : GetTextureDimension_MethodGroup
    class GetTextureDimension_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> TextureDimension:...
        @typing.overload
        def __call__(self, name: str) -> TextureDimension:...

    # Skipped GetUInt due to it being static, abstract and generic.

    GetUInt : GetUInt_MethodGroup
    class GetUInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> int:...
        @typing.overload
        def __call__(self, name: str) -> int:...

    # Skipped GetVector2 due to it being static, abstract and generic.

    GetVector2 : GetVector2_MethodGroup
    class GetVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector2:...
        @typing.overload
        def __call__(self, name: str) -> Vector2:...

    # Skipped GetVector3 due to it being static, abstract and generic.

    GetVector3 : GetVector3_MethodGroup
    class GetVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector3:...
        @typing.overload
        def __call__(self, name: str) -> Vector3:...

    # Skipped GetVector4 due to it being static, abstract and generic.

    GetVector4 : GetVector4_MethodGroup
    class GetVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> Vector4:...
        @typing.overload
        def __call__(self, name: str) -> Vector4:...

    # Skipped HasAnimationCurve due to it being static, abstract and generic.

    HasAnimationCurve : HasAnimationCurve_MethodGroup
    class HasAnimationCurve_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasBool due to it being static, abstract and generic.

    HasBool : HasBool_MethodGroup
    class HasBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasFloat due to it being static, abstract and generic.

    HasFloat : HasFloat_MethodGroup
    class HasFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasGradient due to it being static, abstract and generic.

    HasGradient : HasGradient_MethodGroup
    class HasGradient_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasGraphicsBuffer due to it being static, abstract and generic.

    HasGraphicsBuffer : HasGraphicsBuffer_MethodGroup
    class HasGraphicsBuffer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasInt due to it being static, abstract and generic.

    HasInt : HasInt_MethodGroup
    class HasInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasMatrix4x4 due to it being static, abstract and generic.

    HasMatrix4x4 : HasMatrix4x4_MethodGroup
    class HasMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasMesh due to it being static, abstract and generic.

    HasMesh : HasMesh_MethodGroup
    class HasMesh_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasSkinnedMeshRenderer due to it being static, abstract and generic.

    HasSkinnedMeshRenderer : HasSkinnedMeshRenderer_MethodGroup
    class HasSkinnedMeshRenderer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasSystem due to it being static, abstract and generic.

    HasSystem : HasSystem_MethodGroup
    class HasSystem_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasTexture due to it being static, abstract and generic.

    HasTexture : HasTexture_MethodGroup
    class HasTexture_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasUInt due to it being static, abstract and generic.

    HasUInt : HasUInt_MethodGroup
    class HasUInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector2 due to it being static, abstract and generic.

    HasVector2 : HasVector2_MethodGroup
    class HasVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector3 due to it being static, abstract and generic.

    HasVector3 : HasVector3_MethodGroup
    class HasVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped HasVector4 due to it being static, abstract and generic.

    HasVector4 : HasVector4_MethodGroup
    class HasVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> bool:...
        @typing.overload
        def __call__(self, name: str) -> bool:...

    # Skipped Play due to it being static, abstract and generic.

    Play : Play_MethodGroup
    class Play_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, eventAttribute: VFXEventAttribute) -> None:...

    # Skipped ResetOverride due to it being static, abstract and generic.

    ResetOverride : ResetOverride_MethodGroup
    class ResetOverride_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> None:...
        @typing.overload
        def __call__(self, name: str) -> None:...

    # Skipped SendEvent due to it being static, abstract and generic.

    SendEvent : SendEvent_MethodGroup
    class SendEvent_MethodGroup:
        @typing.overload
        def __call__(self, eventNameID: int) -> None:...
        @typing.overload
        def __call__(self, eventName: str) -> None:...
        @typing.overload
        def __call__(self, eventNameID: int, eventAttribute: VFXEventAttribute) -> None:...
        @typing.overload
        def __call__(self, eventName: str, eventAttribute: VFXEventAttribute) -> None:...

    # Skipped SetAnimationCurve due to it being static, abstract and generic.

    SetAnimationCurve : SetAnimationCurve_MethodGroup
    class SetAnimationCurve_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, c: AnimationCurve) -> None:...
        @typing.overload
        def __call__(self, name: str, c: AnimationCurve) -> None:...

    # Skipped SetBool due to it being static, abstract and generic.

    SetBool : SetBool_MethodGroup
    class SetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, b: bool) -> None:...
        @typing.overload
        def __call__(self, name: str, b: bool) -> None:...

    # Skipped SetFloat due to it being static, abstract and generic.

    SetFloat : SetFloat_MethodGroup
    class SetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, f: float) -> None:...
        @typing.overload
        def __call__(self, name: str, f: float) -> None:...

    # Skipped SetGradient due to it being static, abstract and generic.

    SetGradient : SetGradient_MethodGroup
    class SetGradient_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, g: Gradient) -> None:...
        @typing.overload
        def __call__(self, name: str, g: Gradient) -> None:...

    # Skipped SetGraphicsBuffer due to it being static, abstract and generic.

    SetGraphicsBuffer : SetGraphicsBuffer_MethodGroup
    class SetGraphicsBuffer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, g: GraphicsBuffer) -> None:...
        @typing.overload
        def __call__(self, name: str, g: GraphicsBuffer) -> None:...

    # Skipped SetInt due to it being static, abstract and generic.

    SetInt : SetInt_MethodGroup
    class SetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, i: int) -> None:...
        @typing.overload
        def __call__(self, name: str, i: int) -> None:...

    # Skipped SetMatrix4x4 due to it being static, abstract and generic.

    SetMatrix4x4 : SetMatrix4x4_MethodGroup
    class SetMatrix4x4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Matrix4x4) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Matrix4x4) -> None:...

    # Skipped SetMesh due to it being static, abstract and generic.

    SetMesh : SetMesh_MethodGroup
    class SetMesh_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, m: Mesh) -> None:...
        @typing.overload
        def __call__(self, name: str, m: Mesh) -> None:...

    # Skipped SetSkinnedMeshRenderer due to it being static, abstract and generic.

    SetSkinnedMeshRenderer : SetSkinnedMeshRenderer_MethodGroup
    class SetSkinnedMeshRenderer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, m: SkinnedMeshRenderer) -> None:...
        @typing.overload
        def __call__(self, name: str, m: SkinnedMeshRenderer) -> None:...

    # Skipped SetTexture due to it being static, abstract and generic.

    SetTexture : SetTexture_MethodGroup
    class SetTexture_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, t: Texture) -> None:...
        @typing.overload
        def __call__(self, name: str, t: Texture) -> None:...

    # Skipped SetUInt due to it being static, abstract and generic.

    SetUInt : SetUInt_MethodGroup
    class SetUInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, i: int) -> None:...
        @typing.overload
        def __call__(self, name: str, i: int) -> None:...

    # Skipped SetVector2 due to it being static, abstract and generic.

    SetVector2 : SetVector2_MethodGroup
    class SetVector2_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector2) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector2) -> None:...

    # Skipped SetVector3 due to it being static, abstract and generic.

    SetVector3 : SetVector3_MethodGroup
    class SetVector3_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector3) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector3) -> None:...

    # Skipped SetVector4 due to it being static, abstract and generic.

    SetVector4 : SetVector4_MethodGroup
    class SetVector4_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, v: Vector4) -> None:...
        @typing.overload
        def __call__(self, name: str, v: Vector4) -> None:...

    # Skipped Stop due to it being static, abstract and generic.

    Stop : Stop_MethodGroup
    class Stop_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, eventAttribute: VFXEventAttribute) -> None:...



class VisualEffectAsset(VisualEffectObject):
    def __init__(self) -> None: ...
    PlayEventID : int
    PlayEventName : str
    StopEventID : int
    StopEventName : str
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    def GetEvents(self, names: List_1[str]) -> None: ...
    def GetExposedProperties(self, exposedProperties: List_1[VFXExposedProperty]) -> None: ...
    # Skipped GetTextureDimension due to it being static, abstract and generic.

    GetTextureDimension : GetTextureDimension_MethodGroup
    class GetTextureDimension_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int) -> TextureDimension:...
        @typing.overload
        def __call__(self, name: str) -> TextureDimension:...



class VisualEffectObject(Object, abc.ABC):
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...

