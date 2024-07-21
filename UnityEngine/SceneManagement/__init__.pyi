import typing, abc
from System import Array_1
from UnityEngine import GameObject, AsyncOperation
from System.Collections.Generic import List_1
from Unity.Collections import NativeArray_1

class CreateSceneParameters:
    def __init__(self, physicsMode: LocalPhysicsMode) -> None: ...
    @property
    def localPhysicsMode(self) -> LocalPhysicsMode: ...
    @localPhysicsMode.setter
    def localPhysicsMode(self, value: LocalPhysicsMode) -> LocalPhysicsMode: ...


class LoadSceneMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Single : LoadSceneMode # 0
    Additive : LoadSceneMode # 1


class LoadSceneParameters:
    @typing.overload
    def __init__(self, mode: LoadSceneMode) -> None: ...
    @typing.overload
    def __init__(self, mode: LoadSceneMode, physicsMode: LocalPhysicsMode) -> None: ...
    @property
    def loadSceneMode(self) -> LoadSceneMode: ...
    @loadSceneMode.setter
    def loadSceneMode(self, value: LoadSceneMode) -> LoadSceneMode: ...
    @property
    def localPhysicsMode(self) -> LocalPhysicsMode: ...
    @localPhysicsMode.setter
    def localPhysicsMode(self, value: LocalPhysicsMode) -> LocalPhysicsMode: ...


class LocalPhysicsMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : LocalPhysicsMode # 0
    Physics2D : LocalPhysicsMode # 1
    Physics3D : LocalPhysicsMode # 2


class Scene:
    @property
    def buildIndex(self) -> int: ...
    @property
    def handle(self) -> int: ...
    @property
    def isDirty(self) -> bool: ...
    @property
    def isLoaded(self) -> bool: ...
    @property
    def isSubScene(self) -> bool: ...
    @isSubScene.setter
    def isSubScene(self, value: bool) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def rootCount(self) -> int: ...
    def Equals(self, other: typing.Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def IsValid(self) -> bool: ...
    def __eq__(self, lhs: Scene, rhs: Scene) -> bool: ...
    def __ne__(self, lhs: Scene, rhs: Scene) -> bool: ...
    # Skipped GetRootGameObjects due to it being static, abstract and generic.

    GetRootGameObjects : GetRootGameObjects_MethodGroup
    class GetRootGameObjects_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[GameObject]:...
        @typing.overload
        def __call__(self, rootGameObjects: List_1[GameObject]) -> None:...



class SceneManager:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def loadedSceneCount(cls) -> int: ...
    @classmethod
    @property
    def sceneCount(cls) -> int: ...
    @classmethod
    @property
    def sceneCountInBuildSettings(cls) -> int: ...
    @staticmethod
    def GetActiveScene() -> Scene: ...
    @staticmethod
    def GetAllScenes() -> Array_1[Scene]: ...
    @staticmethod
    def GetSceneAt(index: int) -> Scene: ...
    @staticmethod
    def GetSceneByBuildIndex(buildIndex: int) -> Scene: ...
    @staticmethod
    def GetSceneByName(name: str) -> Scene: ...
    @staticmethod
    def GetSceneByPath(scenePath: str) -> Scene: ...
    @staticmethod
    def MergeScenes(sourceScene: Scene, destinationScene: Scene) -> None: ...
    @staticmethod
    def MoveGameObjectsToScene(instanceIDs: NativeArray_1[int], scene: Scene) -> None: ...
    @staticmethod
    def MoveGameObjectToScene(go: GameObject, scene: Scene) -> None: ...
    @staticmethod
    def SetActiveScene(scene: Scene) -> bool: ...
    # Skipped CreateScene due to it being static, abstract and generic.

    CreateScene : CreateScene_MethodGroup
    class CreateScene_MethodGroup:
        @typing.overload
        def __call__(self, sceneName: str) -> Scene:...
        @typing.overload
        def __call__(self, sceneName: str, parameters: CreateSceneParameters) -> Scene:...

    # Skipped LoadScene due to it being static, abstract and generic.

    LoadScene : LoadScene_MethodGroup
    class LoadScene_MethodGroup:
        @typing.overload
        def __call__(self, sceneBuildIndex: int) -> None:...
        @typing.overload
        def __call__(self, sceneName: str) -> None:...
        @typing.overload
        def __call__(self, sceneBuildIndex: int, mode: LoadSceneMode) -> None:...
        @typing.overload
        def __call__(self, sceneBuildIndex: int, parameters: LoadSceneParameters) -> Scene:...
        @typing.overload
        def __call__(self, sceneName: str, mode: LoadSceneMode) -> None:...
        @typing.overload
        def __call__(self, sceneName: str, parameters: LoadSceneParameters) -> Scene:...

    # Skipped LoadSceneAsync due to it being static, abstract and generic.

    LoadSceneAsync : LoadSceneAsync_MethodGroup
    class LoadSceneAsync_MethodGroup:
        @typing.overload
        def __call__(self, sceneBuildIndex: int) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneName: str) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneBuildIndex: int, mode: LoadSceneMode) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneBuildIndex: int, parameters: LoadSceneParameters) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneName: str, mode: LoadSceneMode) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneName: str, parameters: LoadSceneParameters) -> AsyncOperation:...

    # Skipped UnloadScene due to it being static, abstract and generic.

    UnloadScene : UnloadScene_MethodGroup
    class UnloadScene_MethodGroup:
        @typing.overload
        def __call__(self, sceneBuildIndex: int) -> bool:...
        @typing.overload
        def __call__(self, scene: Scene) -> bool:...
        @typing.overload
        def __call__(self, sceneName: str) -> bool:...

    # Skipped UnloadSceneAsync due to it being static, abstract and generic.

    UnloadSceneAsync : UnloadSceneAsync_MethodGroup
    class UnloadSceneAsync_MethodGroup:
        @typing.overload
        def __call__(self, sceneBuildIndex: int) -> AsyncOperation:...
        @typing.overload
        def __call__(self, scene: Scene) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneName: str) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneBuildIndex: int, options: UnloadSceneOptions) -> AsyncOperation:...
        @typing.overload
        def __call__(self, sceneName: str, options: UnloadSceneOptions) -> AsyncOperation:...
        @typing.overload
        def __call__(self, scene: Scene, options: UnloadSceneOptions) -> AsyncOperation:...



class SceneManagerAPI:
    @classmethod
    @property
    def overrideAPI(cls) -> SceneManagerAPI: ...
    @classmethod
    @overrideAPI.setter
    def overrideAPI(cls, value: SceneManagerAPI) -> SceneManagerAPI: ...


class SceneUtility(abc.ABC):
    @staticmethod
    def GetBuildIndexByScenePath(scenePath: str) -> int: ...
    @staticmethod
    def GetScenePathByBuildIndex(buildIndex: int) -> str: ...


class UnloadSceneOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : UnloadSceneOptions # 0
    UnloadAllEmbeddedSceneObjects : UnloadSceneOptions # 1

