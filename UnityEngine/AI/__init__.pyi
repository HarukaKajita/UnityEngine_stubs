import typing, clr, abc
from System import Array_1, MulticastDelegate, IAsyncResult, AsyncCallback
from UnityEngine import Vector3, Quaternion, Behaviour, Component, GameObject, HideFlags, Object, Transform, Bounds, AsyncOperation, Matrix4x4
from System.Reflection import MethodInfo
from System.Collections.Generic import List_1

class NavMesh(abc.ABC):
    AllAreas : int
    onPreUpdate : NavMesh.OnNavMeshPreUpdate
    @classmethod
    @property
    def avoidancePredictionTime(cls) -> float: ...
    @classmethod
    @avoidancePredictionTime.setter
    def avoidancePredictionTime(cls, value: float) -> float: ...
    @classmethod
    @property
    def pathfindingIterationsPerFrame(cls) -> int: ...
    @classmethod
    @pathfindingIterationsPerFrame.setter
    def pathfindingIterationsPerFrame(cls, value: int) -> int: ...
    @staticmethod
    def AddOffMeshLinks() -> None: ...
    @staticmethod
    def CalculateTriangulation() -> NavMeshTriangulation: ...
    @staticmethod
    def CreateSettings() -> NavMeshBuildSettings: ...
    @staticmethod
    def GetAreaCost(areaIndex: int) -> float: ...
    @staticmethod
    def GetAreaFromName(areaName: str) -> int: ...
    @staticmethod
    def GetLayerCost(layer: int) -> float: ...
    @staticmethod
    def GetNavMeshLayerFromName(layerName: str) -> int: ...
    @staticmethod
    def GetSettingsByID(agentTypeID: int) -> NavMeshBuildSettings: ...
    @staticmethod
    def GetSettingsByIndex(index: int) -> NavMeshBuildSettings: ...
    @staticmethod
    def GetSettingsCount() -> int: ...
    @staticmethod
    def GetSettingsNameFromID(agentTypeID: int) -> str: ...
    @staticmethod
    def RemoveAllNavMeshData() -> None: ...
    @staticmethod
    def RemoveLink(handle: NavMeshLinkInstance) -> None: ...
    @staticmethod
    def RemoveNavMeshData(handle: NavMeshDataInstance) -> None: ...
    @staticmethod
    def RemoveSettings(agentTypeID: int) -> None: ...
    @staticmethod
    def RestoreNavMesh() -> None: ...
    @staticmethod
    def SetAreaCost(areaIndex: int, cost: float) -> None: ...
    @staticmethod
    def SetLayerCost(layer: int, cost: float) -> None: ...
    @staticmethod
    def Triangulate(vertices: clr.Reference[Array_1[Vector3]], indices: clr.Reference[Array_1[int]]) -> None: ...
    # Skipped AddLink due to it being static, abstract and generic.

    AddLink : AddLink_MethodGroup
    class AddLink_MethodGroup:
        @typing.overload
        def __call__(self, link: NavMeshLinkData) -> NavMeshLinkInstance:...
        @typing.overload
        def __call__(self, link: NavMeshLinkData, position: Vector3, rotation: Quaternion) -> NavMeshLinkInstance:...

    # Skipped AddNavMeshData due to it being static, abstract and generic.

    AddNavMeshData : AddNavMeshData_MethodGroup
    class AddNavMeshData_MethodGroup:
        @typing.overload
        def __call__(self, navMeshData: NavMeshData) -> NavMeshDataInstance:...
        @typing.overload
        def __call__(self, navMeshData: NavMeshData, position: Vector3, rotation: Quaternion) -> NavMeshDataInstance:...

    # Skipped CalculatePath due to it being static, abstract and generic.

    CalculatePath : CalculatePath_MethodGroup
    class CalculatePath_MethodGroup:
        @typing.overload
        def __call__(self, sourcePosition: Vector3, targetPosition: Vector3, areaMask: int, path: NavMeshPath) -> bool:...
        @typing.overload
        def __call__(self, sourcePosition: Vector3, targetPosition: Vector3, filter: NavMeshQueryFilter, path: NavMeshPath) -> bool:...

    # Skipped FindClosestEdge due to it being static, abstract and generic.

    FindClosestEdge : FindClosestEdge_MethodGroup
    class FindClosestEdge_MethodGroup:
        @typing.overload
        def __call__(self, sourcePosition: Vector3, hit: clr.Reference[NavMeshHit], areaMask: int) -> bool:...
        @typing.overload
        def __call__(self, sourcePosition: Vector3, hit: clr.Reference[NavMeshHit], filter: NavMeshQueryFilter) -> bool:...

    # Skipped Raycast due to it being static, abstract and generic.

    Raycast : Raycast_MethodGroup
    class Raycast_MethodGroup:
        @typing.overload
        def __call__(self, sourcePosition: Vector3, targetPosition: Vector3, hit: clr.Reference[NavMeshHit], areaMask: int) -> bool:...
        @typing.overload
        def __call__(self, sourcePosition: Vector3, targetPosition: Vector3, hit: clr.Reference[NavMeshHit], filter: NavMeshQueryFilter) -> bool:...

    # Skipped SamplePosition due to it being static, abstract and generic.

    SamplePosition : SamplePosition_MethodGroup
    class SamplePosition_MethodGroup:
        @typing.overload
        def __call__(self, sourcePosition: Vector3, hit: clr.Reference[NavMeshHit], maxDistance: float, areaMask: int) -> bool:...
        @typing.overload
        def __call__(self, sourcePosition: Vector3, hit: clr.Reference[NavMeshHit], maxDistance: float, filter: NavMeshQueryFilter) -> bool:...


    class OnNavMeshPreUpdate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self) -> None: ...



class NavMeshAgent(Behaviour):
    def __init__(self) -> None: ...
    @property
    def acceleration(self) -> float: ...
    @acceleration.setter
    def acceleration(self, value: float) -> float: ...
    @property
    def agentTypeID(self) -> int: ...
    @agentTypeID.setter
    def agentTypeID(self, value: int) -> int: ...
    @property
    def angularSpeed(self) -> float: ...
    @angularSpeed.setter
    def angularSpeed(self, value: float) -> float: ...
    @property
    def animation(self) -> Component: ...
    @property
    def areaMask(self) -> int: ...
    @areaMask.setter
    def areaMask(self, value: int) -> int: ...
    @property
    def audio(self) -> Component: ...
    @property
    def autoBraking(self) -> bool: ...
    @autoBraking.setter
    def autoBraking(self, value: bool) -> bool: ...
    @property
    def autoRepath(self) -> bool: ...
    @autoRepath.setter
    def autoRepath(self, value: bool) -> bool: ...
    @property
    def autoTraverseOffMeshLink(self) -> bool: ...
    @autoTraverseOffMeshLink.setter
    def autoTraverseOffMeshLink(self, value: bool) -> bool: ...
    @property
    def avoidancePriority(self) -> int: ...
    @avoidancePriority.setter
    def avoidancePriority(self, value: int) -> int: ...
    @property
    def baseOffset(self) -> float: ...
    @baseOffset.setter
    def baseOffset(self, value: float) -> float: ...
    @property
    def camera(self) -> Component: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def currentOffMeshLinkData(self) -> OffMeshLinkData: ...
    @property
    def desiredVelocity(self) -> Vector3: ...
    @property
    def destination(self) -> Vector3: ...
    @destination.setter
    def destination(self, value: Vector3) -> Vector3: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hasPath(self) -> bool: ...
    @property
    def height(self) -> float: ...
    @height.setter
    def height(self, value: float) -> float: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def isActiveAndEnabled(self) -> bool: ...
    @property
    def isOnNavMesh(self) -> bool: ...
    @property
    def isOnOffMeshLink(self) -> bool: ...
    @property
    def isPathStale(self) -> bool: ...
    @property
    def isStopped(self) -> bool: ...
    @isStopped.setter
    def isStopped(self, value: bool) -> bool: ...
    @property
    def light(self) -> Component: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def navMeshOwner(self) -> Object: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def nextOffMeshLinkData(self) -> OffMeshLinkData: ...
    @property
    def nextPosition(self) -> Vector3: ...
    @nextPosition.setter
    def nextPosition(self, value: Vector3) -> Vector3: ...
    @property
    def obstacleAvoidanceType(self) -> ObstacleAvoidanceType: ...
    @obstacleAvoidanceType.setter
    def obstacleAvoidanceType(self, value: ObstacleAvoidanceType) -> ObstacleAvoidanceType: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def path(self) -> NavMeshPath: ...
    @path.setter
    def path(self, value: NavMeshPath) -> NavMeshPath: ...
    @property
    def pathEndPosition(self) -> Vector3: ...
    @property
    def pathPending(self) -> bool: ...
    @property
    def pathStatus(self) -> NavMeshPathStatus: ...
    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> float: ...
    @property
    def remainingDistance(self) -> float: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def speed(self) -> float: ...
    @speed.setter
    def speed(self, value: float) -> float: ...
    @property
    def steeringTarget(self) -> Vector3: ...
    @property
    def stoppingDistance(self) -> float: ...
    @stoppingDistance.setter
    def stoppingDistance(self, value: float) -> float: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def updatePosition(self) -> bool: ...
    @updatePosition.setter
    def updatePosition(self, value: bool) -> bool: ...
    @property
    def updateRotation(self) -> bool: ...
    @updateRotation.setter
    def updateRotation(self, value: bool) -> bool: ...
    @property
    def updateUpAxis(self) -> bool: ...
    @updateUpAxis.setter
    def updateUpAxis(self, value: bool) -> bool: ...
    @property
    def velocity(self) -> Vector3: ...
    @velocity.setter
    def velocity(self, value: Vector3) -> Vector3: ...
    @property
    def walkableMask(self) -> int: ...
    @walkableMask.setter
    def walkableMask(self, value: int) -> int: ...
    def ActivateCurrentOffMeshLink(self, activated: bool) -> None: ...
    def CalculatePath(self, targetPosition: Vector3, path: NavMeshPath) -> bool: ...
    def CompleteOffMeshLink(self) -> None: ...
    def FindClosestEdge(self, hit: clr.Reference[NavMeshHit]) -> bool: ...
    def GetAreaCost(self, areaIndex: int) -> float: ...
    def GetLayerCost(self, layer: int) -> float: ...
    def Move(self, offset: Vector3) -> None: ...
    def Raycast(self, targetPosition: Vector3, hit: clr.Reference[NavMeshHit]) -> bool: ...
    def ResetPath(self) -> None: ...
    def Resume(self) -> None: ...
    def SamplePathPosition(self, areaMask: int, maxDistance: float, hit: clr.Reference[NavMeshHit]) -> bool: ...
    def SetAreaCost(self, areaIndex: int, areaCost: float) -> None: ...
    def SetDestination(self, target: Vector3) -> bool: ...
    def SetLayerCost(self, layer: int, cost: float) -> None: ...
    def SetPath(self, path: NavMeshPath) -> bool: ...
    def Warp(self, newPosition: Vector3) -> bool: ...
    # Skipped Stop due to it being static, abstract and generic.

    Stop : Stop_MethodGroup
    class Stop_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, stopUpdates: bool) -> None:...



class NavMeshBuildDebugFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : NavMeshBuildDebugFlags # 0
    InputGeometry : NavMeshBuildDebugFlags # 1
    Voxels : NavMeshBuildDebugFlags # 2
    Regions : NavMeshBuildDebugFlags # 4
    RawContours : NavMeshBuildDebugFlags # 8
    SimplifiedContours : NavMeshBuildDebugFlags # 16
    PolygonMeshes : NavMeshBuildDebugFlags # 32
    PolygonMeshesDetail : NavMeshBuildDebugFlags # 64
    All : NavMeshBuildDebugFlags # 127


class NavMeshBuildDebugSettings:
    @property
    def flags(self) -> NavMeshBuildDebugFlags: ...
    @flags.setter
    def flags(self, value: NavMeshBuildDebugFlags) -> NavMeshBuildDebugFlags: ...


class NavMeshBuilder(abc.ABC):
    @staticmethod
    def BuildNavMeshData(buildSettings: NavMeshBuildSettings, sources: List_1[NavMeshBuildSource], localBounds: Bounds, position: Vector3, rotation: Quaternion) -> NavMeshData: ...
    @staticmethod
    def Cancel(data: NavMeshData) -> None: ...
    @staticmethod
    def UpdateNavMeshData(data: NavMeshData, buildSettings: NavMeshBuildSettings, sources: List_1[NavMeshBuildSource], localBounds: Bounds) -> bool: ...
    @staticmethod
    def UpdateNavMeshDataAsync(data: NavMeshData, buildSettings: NavMeshBuildSettings, sources: List_1[NavMeshBuildSource], localBounds: Bounds) -> AsyncOperation: ...
    # Skipped CollectSources due to it being static, abstract and generic.

    CollectSources : CollectSources_MethodGroup
    class CollectSources_MethodGroup:
        @typing.overload
        def __call__(self, root: Transform, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, markups: List_1[NavMeshBuildMarkup], results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, includedWorldBounds: Bounds, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, markups: List_1[NavMeshBuildMarkup], results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, root: Transform, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, generateLinksByDefault: bool, markups: List_1[NavMeshBuildMarkup], includeOnlyMarkedObjects: bool, results: List_1[NavMeshBuildSource]) -> None:...
        @typing.overload
        def __call__(self, includedWorldBounds: Bounds, includedLayerMask: int, geometry: NavMeshCollectGeometry, defaultArea: int, generateLinksByDefault: bool, markups: List_1[NavMeshBuildMarkup], includeOnlyMarkedObjects: bool, results: List_1[NavMeshBuildSource]) -> None:...



class NavMeshBuildMarkup:
    @property
    def applyToChildren(self) -> bool: ...
    @applyToChildren.setter
    def applyToChildren(self, value: bool) -> bool: ...
    @property
    def area(self) -> int: ...
    @area.setter
    def area(self, value: int) -> int: ...
    @property
    def generateLinks(self) -> bool: ...
    @generateLinks.setter
    def generateLinks(self, value: bool) -> bool: ...
    @property
    def ignoreFromBuild(self) -> bool: ...
    @ignoreFromBuild.setter
    def ignoreFromBuild(self, value: bool) -> bool: ...
    @property
    def overrideArea(self) -> bool: ...
    @overrideArea.setter
    def overrideArea(self, value: bool) -> bool: ...
    @property
    def overrideGenerateLinks(self) -> bool: ...
    @overrideGenerateLinks.setter
    def overrideGenerateLinks(self, value: bool) -> bool: ...
    @property
    def overrideIgnore(self) -> bool: ...
    @overrideIgnore.setter
    def overrideIgnore(self, value: bool) -> bool: ...
    @property
    def root(self) -> Transform: ...
    @root.setter
    def root(self, value: Transform) -> Transform: ...


class NavMeshBuildSettings:
    @property
    def agentClimb(self) -> float: ...
    @agentClimb.setter
    def agentClimb(self, value: float) -> float: ...
    @property
    def agentHeight(self) -> float: ...
    @agentHeight.setter
    def agentHeight(self, value: float) -> float: ...
    @property
    def agentRadius(self) -> float: ...
    @agentRadius.setter
    def agentRadius(self, value: float) -> float: ...
    @property
    def agentSlope(self) -> float: ...
    @agentSlope.setter
    def agentSlope(self, value: float) -> float: ...
    @property
    def agentTypeID(self) -> int: ...
    @agentTypeID.setter
    def agentTypeID(self, value: int) -> int: ...
    @property
    def buildHeightMesh(self) -> bool: ...
    @buildHeightMesh.setter
    def buildHeightMesh(self, value: bool) -> bool: ...
    @property
    def debug(self) -> NavMeshBuildDebugSettings: ...
    @debug.setter
    def debug(self, value: NavMeshBuildDebugSettings) -> NavMeshBuildDebugSettings: ...
    @property
    def ledgeDropHeight(self) -> float: ...
    @ledgeDropHeight.setter
    def ledgeDropHeight(self, value: float) -> float: ...
    @property
    def maxJobWorkers(self) -> int: ...
    @maxJobWorkers.setter
    def maxJobWorkers(self, value: int) -> int: ...
    @property
    def maxJumpAcrossDistance(self) -> float: ...
    @maxJumpAcrossDistance.setter
    def maxJumpAcrossDistance(self, value: float) -> float: ...
    @property
    def minRegionArea(self) -> float: ...
    @minRegionArea.setter
    def minRegionArea(self, value: float) -> float: ...
    @property
    def overrideTileSize(self) -> bool: ...
    @overrideTileSize.setter
    def overrideTileSize(self, value: bool) -> bool: ...
    @property
    def overrideVoxelSize(self) -> bool: ...
    @overrideVoxelSize.setter
    def overrideVoxelSize(self, value: bool) -> bool: ...
    @property
    def preserveTilesOutsideBounds(self) -> bool: ...
    @preserveTilesOutsideBounds.setter
    def preserveTilesOutsideBounds(self, value: bool) -> bool: ...
    @property
    def tileSize(self) -> int: ...
    @tileSize.setter
    def tileSize(self, value: int) -> int: ...
    @property
    def voxelSize(self) -> float: ...
    @voxelSize.setter
    def voxelSize(self, value: float) -> float: ...
    def ValidationReport(self, buildBounds: Bounds) -> Array_1[str]: ...


class NavMeshBuildSource:
    @property
    def area(self) -> int: ...
    @area.setter
    def area(self, value: int) -> int: ...
    @property
    def component(self) -> Component: ...
    @component.setter
    def component(self, value: Component) -> Component: ...
    @property
    def generateLinks(self) -> bool: ...
    @generateLinks.setter
    def generateLinks(self, value: bool) -> bool: ...
    @property
    def shape(self) -> NavMeshBuildSourceShape: ...
    @shape.setter
    def shape(self, value: NavMeshBuildSourceShape) -> NavMeshBuildSourceShape: ...
    @property
    def size(self) -> Vector3: ...
    @size.setter
    def size(self, value: Vector3) -> Vector3: ...
    @property
    def sourceObject(self) -> Object: ...
    @sourceObject.setter
    def sourceObject(self, value: Object) -> Object: ...
    @property
    def transform(self) -> Matrix4x4: ...
    @transform.setter
    def transform(self, value: Matrix4x4) -> Matrix4x4: ...


class NavMeshBuildSourceShape(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Mesh : NavMeshBuildSourceShape # 0
    Terrain : NavMeshBuildSourceShape # 1
    Box : NavMeshBuildSourceShape # 2
    Sphere : NavMeshBuildSourceShape # 3
    Capsule : NavMeshBuildSourceShape # 4
    ModifierBox : NavMeshBuildSourceShape # 5


class NavMeshCollectGeometry(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RenderMeshes : NavMeshCollectGeometry # 0
    PhysicsColliders : NavMeshCollectGeometry # 1


class NavMeshData(Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, agentTypeID: int) -> None: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def position(self) -> Vector3: ...
    @position.setter
    def position(self, value: Vector3) -> Vector3: ...
    @property
    def rotation(self) -> Quaternion: ...
    @rotation.setter
    def rotation(self, value: Quaternion) -> Quaternion: ...
    @property
    def sourceBounds(self) -> Bounds: ...


class NavMeshDataInstance:
    @property
    def owner(self) -> Object: ...
    @owner.setter
    def owner(self, value: Object) -> Object: ...
    @property
    def valid(self) -> bool: ...
    def Remove(self) -> None: ...


class NavMeshHit:
    @property
    def distance(self) -> float: ...
    @distance.setter
    def distance(self, value: float) -> float: ...
    @property
    def hit(self) -> bool: ...
    @hit.setter
    def hit(self, value: bool) -> bool: ...
    @property
    def mask(self) -> int: ...
    @mask.setter
    def mask(self, value: int) -> int: ...
    @property
    def normal(self) -> Vector3: ...
    @normal.setter
    def normal(self, value: Vector3) -> Vector3: ...
    @property
    def position(self) -> Vector3: ...
    @position.setter
    def position(self, value: Vector3) -> Vector3: ...


class NavMeshLinkData:
    @property
    def agentTypeID(self) -> int: ...
    @agentTypeID.setter
    def agentTypeID(self, value: int) -> int: ...
    @property
    def area(self) -> int: ...
    @area.setter
    def area(self, value: int) -> int: ...
    @property
    def bidirectional(self) -> bool: ...
    @bidirectional.setter
    def bidirectional(self, value: bool) -> bool: ...
    @property
    def costModifier(self) -> float: ...
    @costModifier.setter
    def costModifier(self, value: float) -> float: ...
    @property
    def endPosition(self) -> Vector3: ...
    @endPosition.setter
    def endPosition(self, value: Vector3) -> Vector3: ...
    @property
    def startPosition(self) -> Vector3: ...
    @startPosition.setter
    def startPosition(self, value: Vector3) -> Vector3: ...
    @property
    def width(self) -> float: ...
    @width.setter
    def width(self, value: float) -> float: ...


class NavMeshLinkInstance:
    @property
    def owner(self) -> Object: ...
    @owner.setter
    def owner(self, value: Object) -> Object: ...
    @property
    def valid(self) -> bool: ...
    def Remove(self) -> None: ...


class NavMeshObstacle(Behaviour):
    def __init__(self) -> None: ...
    @property
    def animation(self) -> Component: ...
    @property
    def audio(self) -> Component: ...
    @property
    def camera(self) -> Component: ...
    @property
    def carveOnlyStationary(self) -> bool: ...
    @carveOnlyStationary.setter
    def carveOnlyStationary(self, value: bool) -> bool: ...
    @property
    def carving(self) -> bool: ...
    @carving.setter
    def carving(self, value: bool) -> bool: ...
    @property
    def carvingMoveThreshold(self) -> float: ...
    @carvingMoveThreshold.setter
    def carvingMoveThreshold(self, value: float) -> float: ...
    @property
    def carvingTimeToStationary(self) -> float: ...
    @carvingTimeToStationary.setter
    def carvingTimeToStationary(self, value: float) -> float: ...
    @property
    def center(self) -> Vector3: ...
    @center.setter
    def center(self, value: Vector3) -> Vector3: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def height(self) -> float: ...
    @height.setter
    def height(self, value: float) -> float: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
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
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> float: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def shape(self) -> NavMeshObstacleShape: ...
    @shape.setter
    def shape(self, value: NavMeshObstacleShape) -> NavMeshObstacleShape: ...
    @property
    def size(self) -> Vector3: ...
    @size.setter
    def size(self, value: Vector3) -> Vector3: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def velocity(self) -> Vector3: ...
    @velocity.setter
    def velocity(self, value: Vector3) -> Vector3: ...


class NavMeshObstacleShape(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Capsule : NavMeshObstacleShape # 0
    Box : NavMeshObstacleShape # 1


class NavMeshPath:
    def __init__(self) -> None: ...
    @property
    def corners(self) -> Array_1[Vector3]: ...
    @property
    def status(self) -> NavMeshPathStatus: ...
    def ClearCorners(self) -> None: ...
    def GetCornersNonAlloc(self, results: Array_1[Vector3]) -> int: ...


class NavMeshPathStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    PathComplete : NavMeshPathStatus # 0
    PathPartial : NavMeshPathStatus # 1
    PathInvalid : NavMeshPathStatus # 2


class NavMeshQueryFilter:
    @property
    def agentTypeID(self) -> int: ...
    @agentTypeID.setter
    def agentTypeID(self, value: int) -> int: ...
    @property
    def areaMask(self) -> int: ...
    @areaMask.setter
    def areaMask(self, value: int) -> int: ...
    def GetAreaCost(self, areaIndex: int) -> float: ...
    def SetAreaCost(self, areaIndex: int, cost: float) -> None: ...


class NavMeshTriangulation:
    areas : Array_1[int]
    indices : Array_1[int]
    vertices : Array_1[Vector3]
    @property
    def layers(self) -> Array_1[int]: ...


class ObstacleAvoidanceType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NoObstacleAvoidance : ObstacleAvoidanceType # 0
    LowQualityObstacleAvoidance : ObstacleAvoidanceType # 1
    MedQualityObstacleAvoidance : ObstacleAvoidanceType # 2
    GoodQualityObstacleAvoidance : ObstacleAvoidanceType # 3
    HighQualityObstacleAvoidance : ObstacleAvoidanceType # 4


class OffMeshLink(Behaviour):
    def __init__(self) -> None: ...
    @property
    def activated(self) -> bool: ...
    @activated.setter
    def activated(self, value: bool) -> bool: ...
    @property
    def animation(self) -> Component: ...
    @property
    def area(self) -> int: ...
    @area.setter
    def area(self, value: int) -> int: ...
    @property
    def audio(self) -> Component: ...
    @property
    def autoUpdatePositions(self) -> bool: ...
    @autoUpdatePositions.setter
    def autoUpdatePositions(self, value: bool) -> bool: ...
    @property
    def biDirectional(self) -> bool: ...
    @biDirectional.setter
    def biDirectional(self, value: bool) -> bool: ...
    @property
    def camera(self) -> Component: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def costOverride(self) -> float: ...
    @costOverride.setter
    def costOverride(self, value: float) -> float: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def endTransform(self) -> Transform: ...
    @endTransform.setter
    def endTransform(self, value: Transform) -> Transform: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def isActiveAndEnabled(self) -> bool: ...
    @property
    def light(self) -> Component: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def navMeshLayer(self) -> int: ...
    @navMeshLayer.setter
    def navMeshLayer(self, value: int) -> int: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def occupied(self) -> bool: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def startTransform(self) -> Transform: ...
    @startTransform.setter
    def startTransform(self, value: Transform) -> Transform: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    def UpdatePositions(self) -> None: ...


class OffMeshLinkData:
    @property
    def activated(self) -> bool: ...
    @property
    def endPos(self) -> Vector3: ...
    @property
    def linkType(self) -> OffMeshLinkType: ...
    @property
    def offMeshLink(self) -> OffMeshLink: ...
    @property
    def startPos(self) -> Vector3: ...
    @property
    def valid(self) -> bool: ...


class OffMeshLinkType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    LinkTypeManual : OffMeshLinkType # 0
    LinkTypeDropDown : OffMeshLinkType # 1
    LinkTypeJumpAcross : OffMeshLinkType # 2

