import typing, abc
from UnityEngine import Object, ScriptableObject, Texture2D, HideFlags
from UnityEngine.SceneManagement import Scene
from UnityEditor import SceneAsset, MonoScript
from System import Array_1, MulticastDelegate, IAsyncResult, AsyncCallback
from System.Reflection import MethodInfo

class DependencyInfo:
    def __init__(self) -> None: ...
    dependency : Object
    instantiationMode : TemplateInstantiationMode


class InstantiationResult:
    @property
    def scene(self) -> Scene: ...
    @scene.setter
    def scene(self, value: Scene) -> Scene: ...
    @property
    def sceneAsset(self) -> SceneAsset: ...
    @sceneAsset.setter
    def sceneAsset(self, value: SceneAsset) -> SceneAsset: ...


class ISceneTemplatePipeline(typing.Protocol):
    @abc.abstractmethod
    def AfterTemplateInstantiation(self, sceneTemplateAsset: SceneTemplateAsset, scene: Scene, isAdditive: bool, sceneName: str) -> None: ...
    @abc.abstractmethod
    def BeforeTemplateInstantiation(self, sceneTemplateAsset: SceneTemplateAsset, isAdditive: bool, sceneName: str) -> None: ...
    @abc.abstractmethod
    def IsValidTemplateForInstantiation(self, sceneTemplateAsset: SceneTemplateAsset) -> bool: ...


class SceneTemplateAsset(ScriptableObject):
    def __init__(self) -> None: ...
    addToDefaults : bool
    badge : Texture2D
    dependencies : Array_1[DependencyInfo]
    description : str
    preview : Texture2D
    templateName : str
    templatePipeline : MonoScript
    templateScene : SceneAsset
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def isValid(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...


class SceneTemplatePipelineAdapter(ISceneTemplatePipeline):
    def __init__(self) -> None: ...
    def AfterTemplateInstantiation(self, sceneTemplateAsset: SceneTemplateAsset, scene: Scene, isAdditive: bool, sceneName: str) -> None: ...
    def BeforeTemplateInstantiation(self, sceneTemplateAsset: SceneTemplateAsset, isAdditive: bool, sceneName: str) -> None: ...
    def IsValidTemplateForInstantiation(self, sceneTemplateAsset: SceneTemplateAsset) -> bool: ...


class SceneTemplateService(abc.ABC):
    @staticmethod
    def CreateSceneTemplate(sceneTemplatePath: str) -> SceneTemplateAsset: ...
    @staticmethod
    def CreateTemplateFromScene(sourceSceneAsset: SceneAsset, sceneTemplatePath: str) -> SceneTemplateAsset: ...
    @staticmethod
    def Instantiate(sceneTemplate: SceneTemplateAsset, loadAdditively: bool, newSceneOutputPath: str = ...) -> InstantiationResult: ...

    class NewTemplateInstantiated(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, sceneTemplateAsset: SceneTemplateAsset, scene: Scene, sceneAsset: SceneAsset, additiveLoad: bool, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, sceneTemplateAsset: SceneTemplateAsset, scene: Scene, sceneAsset: SceneAsset, additiveLoad: bool) -> None: ...


    class NewTemplateInstantiating(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, sceneTemplateAsset: SceneTemplateAsset, newSceneOutputPath: str, additiveLoad: bool, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, sceneTemplateAsset: SceneTemplateAsset, newSceneOutputPath: str, additiveLoad: bool) -> None: ...



class TemplateInstantiationMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Clone : TemplateInstantiationMode # 0
    Reference : TemplateInstantiationMode # 1

