import typing, abc
from UnityEngine import Object, Transform, Bounds, Rect
from System import Array_1
from UnityEngine.AI import NavMeshCollectGeometry, NavMeshBuildMarkup, NavMeshBuildSource, NavMeshData, NavMeshBuildDebugFlags
from System.Collections.Generic import List_1
from UnityEngine.SceneManagement import Scene

class NavMeshBuilder:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def isRunning(cls) -> bool: ...
    @classmethod
    @property
    def navMeshSettingsObject(cls) -> Object: ...
    @staticmethod
    def BuildNavMesh() -> None: ...
    @staticmethod
    def BuildNavMeshAsync() -> None: ...
    @staticmethod
    def BuildNavMeshForMultipleScenes(paths: Array_1[str]) -> None: ...
    @staticmethod
    def Cancel() -> None: ...
    @staticmethod
    def ClearAllNavMeshes() -> None: ...
    # Skipped CollectSourcesInStage due to it being static, abstract and generic.

    CollectSourcesInStage : CollectSourcesInStage_MethodGroup
    class CollectSourcesInStage_MethodGroup:
        @typing.overload
        def __call__(self, root: Transform, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, markups: List_1[NavMeshBuildMarkup], stageProxy: Scene, results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, includedWorldBounds: Bounds, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, markups: List_1[NavMeshBuildMarkup], stageProxy: Scene, results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, root: Transform, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, generateLinksByDefault: bool, markups: List_1[NavMeshBuildMarkup], includeOnlyMarkedObjects: bool, stageProxy: Scene, results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, includedWorldBounds: Bounds, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, generateLinksByDefault: bool, markups: List_1[NavMeshBuildMarkup], includeOnlyMarkedObjects: bool, stageProxy: Scene, results: List_1[NavMeshBuildSource]) -> None:...



class NavMeshEditorHelpers(abc.ABC):
    @staticmethod
    def DrawAgentDiagram(rect: Rect, agentRadius: float, agentHeight: float, agentClimb: float, agentSlope: float) -> None: ...
    @staticmethod
    def OpenAgentSettings(agentTypeID: int) -> None: ...
    @staticmethod
    def OpenAreaSettings() -> None: ...
    # Skipped DrawBuildDebug due to it being static, abstract and generic.

    DrawBuildDebug : DrawBuildDebug_MethodGroup
    class DrawBuildDebug_MethodGroup:
        @typing.overload
        def __call__(self, navMeshData: NavMeshData) -> None:...
        @typing.overload
        def __call__(self, navMeshData: NavMeshData, flags: NavMeshBuildDebugFlags) -> None:...



class NavMeshVisualizationSettings:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def showNavigation(cls) -> int: ...
    @classmethod
    @showNavigation.setter
    def showNavigation(cls, value: int) -> int: ...

