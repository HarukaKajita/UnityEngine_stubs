import typing, clr, abc
from UnityEngine import BoundsInt, Bounds, Vector3Int, Color, Sprite, Matrix4x4, GameObject, HideFlags, ScriptableObject, GridLayout, Component, Vector3, Grid, Transform, Object, Collider2D, Rigidbody2D, LayerMask, CompositeCollider2D, ColliderErrorState2D, Vector2, PhysicsMaterial2D, Renderer, Vector4, SpriteMaskInteraction, Material, MotionVectorGenerationMode
from System import Array_1
from UnityEngine.Rendering import LightProbeUsage, ReflectionProbeUsage, ShadowCastingMode
from UnityEngine.Experimental.Rendering import RayTracingMode

class ITilemap:
    def __init__(self, tilemap: Tilemap) -> None: ...
    @property
    def cellBounds(self) -> BoundsInt: ...
    @property
    def localBounds(self) -> Bounds: ...
    @property
    def origin(self) -> Vector3Int: ...
    @property
    def size(self) -> Vector3Int: ...
    def GetColor(self, position: Vector3Int) -> Color: ...
    def GetSprite(self, position: Vector3Int) -> Sprite: ...
    def GetTileFlags(self, position: Vector3Int) -> TileFlags: ...
    def GetTransformMatrix(self, position: Vector3Int) -> Matrix4x4: ...
    # Operator not supported op_Implicit(tilemap: Tilemap)
    def RefreshTile(self, position: Vector3Int) -> None: ...
    # Skipped GetComponent due to it being static, abstract and generic.

    GetComponent : GetComponent_MethodGroup
    class GetComponent_MethodGroup:
        def __getitem__(self, t:typing.Type[GetComponent_1_T1]) -> GetComponent_1[GetComponent_1_T1]: ...

        GetComponent_1_T1 = typing.TypeVar('GetComponent_1_T1')
        class GetComponent_1(typing.Generic[GetComponent_1_T1]):
            GetComponent_1_T = ITilemap.GetComponent_MethodGroup.GetComponent_1_T1
            def __call__(self) -> GetComponent_1_T:...


    # Skipped GetTile due to it being static, abstract and generic.

    GetTile : GetTile_MethodGroup
    class GetTile_MethodGroup:
        def __getitem__(self, t:typing.Type[GetTile_1_T1]) -> GetTile_1[GetTile_1_T1]: ...

        GetTile_1_T1 = typing.TypeVar('GetTile_1_T1')
        class GetTile_1(typing.Generic[GetTile_1_T1]):
            GetTile_1_T = ITilemap.GetTile_MethodGroup.GetTile_1_T1
            def __call__(self, position: Vector3Int) -> GetTile_1_T:...

        def __call__(self, position: Vector3Int) -> TileBase:...



class Tile(TileBase):
    def __init__(self) -> None: ...
    @property
    def colliderType(self) -> Tile.ColliderType: ...
    @colliderType.setter
    def colliderType(self, value: Tile.ColliderType) -> Tile.ColliderType: ...
    @property
    def color(self) -> Color: ...
    @color.setter
    def color(self, value: Color) -> Color: ...
    @property
    def flags(self) -> TileFlags: ...
    @flags.setter
    def flags(self, value: TileFlags) -> TileFlags: ...
    @property
    def gameObject(self) -> GameObject: ...
    @gameObject.setter
    def gameObject(self, value: GameObject) -> GameObject: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def sprite(self) -> Sprite: ...
    @sprite.setter
    def sprite(self, value: Sprite) -> Sprite: ...
    @property
    def transform(self) -> Matrix4x4: ...
    @transform.setter
    def transform(self, value: Matrix4x4) -> Matrix4x4: ...
    def GetTileData(self, position: Vector3Int, tilemap: ITilemap, tileData: clr.Reference[TileData]) -> None: ...

    class ColliderType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : Tile.ColliderType # 0
        Sprite : Tile.ColliderType # 1
        Grid : Tile.ColliderType # 2



class TileAnimationData:
    @property
    def animatedSprites(self) -> Array_1[Sprite]: ...
    @animatedSprites.setter
    def animatedSprites(self, value: Array_1[Sprite]) -> Array_1[Sprite]: ...
    @property
    def animationSpeed(self) -> float: ...
    @animationSpeed.setter
    def animationSpeed(self, value: float) -> float: ...
    @property
    def animationStartTime(self) -> float: ...
    @animationStartTime.setter
    def animationStartTime(self, value: float) -> float: ...
    @property
    def flags(self) -> TileAnimationFlags: ...
    @flags.setter
    def flags(self, value: TileAnimationFlags) -> TileAnimationFlags: ...


class TileAnimationFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : TileAnimationFlags # 0
    LoopOnce : TileAnimationFlags # 1
    PauseAnimation : TileAnimationFlags # 2
    UpdatePhysics : TileAnimationFlags # 4


class TileBase(ScriptableObject, abc.ABC):
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    def GetTileAnimationData(self, position: Vector3Int, tilemap: ITilemap, tileAnimationData: clr.Reference[TileAnimationData]) -> bool: ...
    def GetTileData(self, position: Vector3Int, tilemap: ITilemap, tileData: clr.Reference[TileData]) -> None: ...
    def RefreshTile(self, position: Vector3Int, tilemap: ITilemap) -> None: ...
    def StartUp(self, position: Vector3Int, tilemap: ITilemap, go: GameObject) -> bool: ...


class TileChangeData:
    def __init__(self, position: Vector3Int, tile: TileBase, color: Color, transform: Matrix4x4) -> None: ...
    @property
    def color(self) -> Color: ...
    @color.setter
    def color(self, value: Color) -> Color: ...
    @property
    def position(self) -> Vector3Int: ...
    @position.setter
    def position(self, value: Vector3Int) -> Vector3Int: ...
    @property
    def tile(self) -> TileBase: ...
    @tile.setter
    def tile(self, value: TileBase) -> TileBase: ...
    @property
    def transform(self) -> Matrix4x4: ...
    @transform.setter
    def transform(self, value: Matrix4x4) -> Matrix4x4: ...


class TileData:
    @property
    def colliderType(self) -> Tile.ColliderType: ...
    @colliderType.setter
    def colliderType(self, value: Tile.ColliderType) -> Tile.ColliderType: ...
    @property
    def color(self) -> Color: ...
    @color.setter
    def color(self, value: Color) -> Color: ...
    @property
    def flags(self) -> TileFlags: ...
    @flags.setter
    def flags(self, value: TileFlags) -> TileFlags: ...
    @property
    def gameObject(self) -> GameObject: ...
    @gameObject.setter
    def gameObject(self, value: GameObject) -> GameObject: ...
    @property
    def sprite(self) -> Sprite: ...
    @sprite.setter
    def sprite(self, value: Sprite) -> Sprite: ...
    @property
    def transform(self) -> Matrix4x4: ...
    @transform.setter
    def transform(self, value: Matrix4x4) -> Matrix4x4: ...


class TileFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : TileFlags # 0
    LockColor : TileFlags # 1
    LockTransform : TileFlags # 2
    LockAll : TileFlags # 3
    InstantiateGameObjectRuntimeOnly : TileFlags # 4
    KeepGameObjectRuntimeOnly : TileFlags # 8


class Tilemap(GridLayout):
    def __init__(self) -> None: ...
    @property
    def animation(self) -> Component: ...
    @property
    def animationFrameRate(self) -> float: ...
    @animationFrameRate.setter
    def animationFrameRate(self, value: float) -> float: ...
    @property
    def audio(self) -> Component: ...
    @property
    def camera(self) -> Component: ...
    @property
    def cellBounds(self) -> BoundsInt: ...
    @property
    def cellGap(self) -> Vector3: ...
    @property
    def cellLayout(self) -> GridLayout.CellLayout: ...
    @property
    def cellSize(self) -> Vector3: ...
    @property
    def cellSwizzle(self) -> GridLayout.CellSwizzle: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def color(self) -> Color: ...
    @color.setter
    def color(self, value: Color) -> Color: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def editorPreviewOrigin(self) -> Vector3Int: ...
    @property
    def editorPreviewSize(self) -> Vector3Int: ...
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
    def isActiveAndEnabled(self) -> bool: ...
    @property
    def layoutGrid(self) -> Grid: ...
    @property
    def light(self) -> Component: ...
    @property
    def localBounds(self) -> Bounds: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def orientation(self) -> Tilemap.Orientation: ...
    @orientation.setter
    def orientation(self, value: Tilemap.Orientation) -> Tilemap.Orientation: ...
    @property
    def orientationMatrix(self) -> Matrix4x4: ...
    @orientationMatrix.setter
    def orientationMatrix(self, value: Matrix4x4) -> Matrix4x4: ...
    @property
    def origin(self) -> Vector3Int: ...
    @origin.setter
    def origin(self, value: Vector3Int) -> Vector3Int: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def size(self) -> Vector3Int: ...
    @size.setter
    def size(self, value: Vector3Int) -> Vector3Int: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def tileAnchor(self) -> Vector3: ...
    @tileAnchor.setter
    def tileAnchor(self, value: Vector3) -> Vector3: ...
    @property
    def transform(self) -> Transform: ...
    def AddTileAnimationFlags(self, position: Vector3Int, flags: TileAnimationFlags) -> None: ...
    def AddTileFlags(self, position: Vector3Int, flags: TileFlags) -> None: ...
    def BoxFill(self, position: Vector3Int, tile: TileBase, startX: int, startY: int, endX: int, endY: int) -> None: ...
    def ClearAllEditorPreviewTiles(self) -> None: ...
    def ClearAllTiles(self) -> None: ...
    def CompressBounds(self) -> None: ...
    def ContainsTile(self, tileAsset: TileBase) -> bool: ...
    def EditorPreviewBoxFill(self, position: Vector3Int, tile: Object, startX: int, startY: int, endX: int, endY: int) -> None: ...
    def EditorPreviewFloodFill(self, position: Vector3Int, tile: TileBase) -> None: ...
    def FloodFill(self, position: Vector3Int, tile: TileBase) -> None: ...
    def GetAnimationFrame(self, position: Vector3Int) -> int: ...
    def GetAnimationFrameCount(self, position: Vector3Int) -> int: ...
    def GetAnimationTime(self, position: Vector3Int) -> float: ...
    def GetCellCenterLocal(self, position: Vector3Int) -> Vector3: ...
    def GetCellCenterWorld(self, position: Vector3Int) -> Vector3: ...
    def GetColliderType(self, position: Vector3Int) -> Tile.ColliderType: ...
    def GetColor(self, position: Vector3Int) -> Color: ...
    def GetEditorPreviewColor(self, position: Vector3Int) -> Color: ...
    def GetEditorPreviewSprite(self, position: Vector3Int) -> Sprite: ...
    def GetEditorPreviewTileFlags(self, position: Vector3Int) -> TileFlags: ...
    def GetEditorPreviewTransformMatrix(self, position: Vector3Int) -> Matrix4x4: ...
    def GetInstantiatedObject(self, position: Vector3Int) -> GameObject: ...
    def GetObjectToInstantiate(self, position: Vector3Int) -> GameObject: ...
    def GetSprite(self, position: Vector3Int) -> Sprite: ...
    def GetTileAnimationFlags(self, position: Vector3Int) -> TileAnimationFlags: ...
    def GetTileFlags(self, position: Vector3Int) -> TileFlags: ...
    def GetTilesBlock(self, bounds: BoundsInt) -> Array_1[TileBase]: ...
    def GetTilesBlockNonAlloc(self, bounds: BoundsInt, tiles: Array_1[TileBase]) -> int: ...
    def GetTilesRangeCount(self, startPosition: Vector3Int, endPosition: Vector3Int) -> int: ...
    def GetTilesRangeNonAlloc(self, startPosition: Vector3Int, endPosition: Vector3Int, positions: Array_1[Vector3Int], tiles: Array_1[TileBase]) -> int: ...
    def GetTransformMatrix(self, position: Vector3Int) -> Matrix4x4: ...
    def GetUsedSpritesCount(self) -> int: ...
    def GetUsedSpritesNonAlloc(self, usedSprites: Array_1[Sprite]) -> int: ...
    def GetUsedTilesCount(self) -> int: ...
    def GetUsedTilesNonAlloc(self, usedTiles: Array_1[TileBase]) -> int: ...
    def HasEditorPreviewTile(self, position: Vector3Int) -> bool: ...
    def HasTile(self, position: Vector3Int) -> bool: ...
    def RefreshAllTiles(self) -> None: ...
    def RefreshTile(self, position: Vector3Int) -> None: ...
    def RemoveTileAnimationFlags(self, position: Vector3Int, flags: TileAnimationFlags) -> None: ...
    def RemoveTileFlags(self, position: Vector3Int, flags: TileFlags) -> None: ...
    def ResizeBounds(self) -> None: ...
    def SetAnimationFrame(self, position: Vector3Int, frame: int) -> None: ...
    def SetAnimationTime(self, position: Vector3Int, time: float) -> None: ...
    def SetColliderType(self, position: Vector3Int, colliderType: Tile.ColliderType) -> None: ...
    def SetColor(self, position: Vector3Int, color: Color) -> None: ...
    def SetEditorPreviewColor(self, position: Vector3Int, color: Color) -> None: ...
    def SetEditorPreviewTile(self, position: Vector3Int, tile: TileBase) -> None: ...
    def SetEditorPreviewTransformMatrix(self, position: Vector3Int, transform: Matrix4x4) -> None: ...
    def SetTileAnimationFlags(self, position: Vector3Int, flags: TileAnimationFlags) -> None: ...
    def SetTileFlags(self, position: Vector3Int, flags: TileFlags) -> None: ...
    def SetTilesBlock(self, position: BoundsInt, tileArray: Array_1[TileBase]) -> None: ...
    def SetTransformMatrix(self, position: Vector3Int, transform: Matrix4x4) -> None: ...
    def SwapTile(self, changeTile: TileBase, newTile: TileBase) -> None: ...
    # Skipped DeleteCells due to it being static, abstract and generic.

    DeleteCells : DeleteCells_MethodGroup
    class DeleteCells_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector3Int, deleteCells: Vector3Int) -> None:...
        @typing.overload
        def __call__(self, position: Vector3Int, numColumns: int, numRows: int, numLayers: int) -> None:...

    # Skipped GetEditorPreviewTile due to it being static, abstract and generic.

    GetEditorPreviewTile : GetEditorPreviewTile_MethodGroup
    class GetEditorPreviewTile_MethodGroup:
        def __getitem__(self, t:typing.Type[GetEditorPreviewTile_1_T1]) -> GetEditorPreviewTile_1[GetEditorPreviewTile_1_T1]: ...

        GetEditorPreviewTile_1_T1 = typing.TypeVar('GetEditorPreviewTile_1_T1')
        class GetEditorPreviewTile_1(typing.Generic[GetEditorPreviewTile_1_T1]):
            GetEditorPreviewTile_1_T = Tilemap.GetEditorPreviewTile_MethodGroup.GetEditorPreviewTile_1_T1
            def __call__(self, position: Vector3Int) -> GetEditorPreviewTile_1_T:...

        def __call__(self, position: Vector3Int) -> TileBase:...

    # Skipped GetTile due to it being static, abstract and generic.

    GetTile : GetTile_MethodGroup
    class GetTile_MethodGroup:
        def __getitem__(self, t:typing.Type[GetTile_1_T1]) -> GetTile_1[GetTile_1_T1]: ...

        GetTile_1_T1 = typing.TypeVar('GetTile_1_T1')
        class GetTile_1(typing.Generic[GetTile_1_T1]):
            GetTile_1_T = Tilemap.GetTile_MethodGroup.GetTile_1_T1
            def __call__(self, position: Vector3Int) -> GetTile_1_T:...

        def __call__(self, position: Vector3Int) -> TileBase:...

    # Skipped InsertCells due to it being static, abstract and generic.

    InsertCells : InsertCells_MethodGroup
    class InsertCells_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector3Int, insertCells: Vector3Int) -> None:...
        @typing.overload
        def __call__(self, position: Vector3Int, numColumns: int, numRows: int, numLayers: int) -> None:...

    # Skipped SetTile due to it being static, abstract and generic.

    SetTile : SetTile_MethodGroup
    class SetTile_MethodGroup:
        @typing.overload
        def __call__(self, position: Vector3Int, tile: TileBase) -> None:...
        @typing.overload
        def __call__(self, tileChangeData: TileChangeData, ignoreLockFlags: bool) -> None:...

    # Skipped SetTiles due to it being static, abstract and generic.

    SetTiles : SetTiles_MethodGroup
    class SetTiles_MethodGroup:
        @typing.overload
        def __call__(self, positionArray: Array_1[Vector3Int], tileArray: Array_1[TileBase]) -> None:...
        @typing.overload
        def __call__(self, tileChangeDataArray: Array_1[TileChangeData], ignoreLockFlags: bool) -> None:...


    class Orientation(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        XY : Tilemap.Orientation # 0
        XZ : Tilemap.Orientation # 1
        YX : Tilemap.Orientation # 2
        YZ : Tilemap.Orientation # 3
        ZX : Tilemap.Orientation # 4
        ZY : Tilemap.Orientation # 5
        Custom : Tilemap.Orientation # 6


    class SyncTile:
        @property
        def position(self) -> Vector3Int: ...
        @property
        def tile(self) -> TileBase: ...
        @property
        def tileData(self) -> TileData: ...



class TilemapCollider2D(Collider2D):
    def __init__(self) -> None: ...
    @property
    def animation(self) -> Component: ...
    @property
    def attachedRigidbody(self) -> Rigidbody2D: ...
    @property
    def audio(self) -> Component: ...
    @property
    def bounciness(self) -> float: ...
    @property
    def bounds(self) -> Bounds: ...
    @property
    def callbackLayers(self) -> LayerMask: ...
    @callbackLayers.setter
    def callbackLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def camera(self) -> Component: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def composite(self) -> CompositeCollider2D: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def contactCaptureLayers(self) -> LayerMask: ...
    @contactCaptureLayers.setter
    def contactCaptureLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def density(self) -> float: ...
    @density.setter
    def density(self, value: float) -> float: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def errorState(self) -> ColliderErrorState2D: ...
    @property
    def excludeLayers(self) -> LayerMask: ...
    @excludeLayers.setter
    def excludeLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def extrusionFactor(self) -> float: ...
    @extrusionFactor.setter
    def extrusionFactor(self, value: float) -> float: ...
    @property
    def forceReceiveLayers(self) -> LayerMask: ...
    @forceReceiveLayers.setter
    def forceReceiveLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def forceSendLayers(self) -> LayerMask: ...
    @forceSendLayers.setter
    def forceSendLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def friction(self) -> float: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hasTilemapChanges(self) -> bool: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def includeLayers(self) -> LayerMask: ...
    @includeLayers.setter
    def includeLayers(self, value: LayerMask) -> LayerMask: ...
    @property
    def isActiveAndEnabled(self) -> bool: ...
    @property
    def isTrigger(self) -> bool: ...
    @isTrigger.setter
    def isTrigger(self, value: bool) -> bool: ...
    @property
    def layerOverridePriority(self) -> int: ...
    @layerOverridePriority.setter
    def layerOverridePriority(self, value: int) -> int: ...
    @property
    def light(self) -> Component: ...
    @property
    def maximumTileChangeCount(self) -> int: ...
    @maximumTileChangeCount.setter
    def maximumTileChangeCount(self, value: int) -> int: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def offset(self) -> Vector2: ...
    @offset.setter
    def offset(self, value: Vector2) -> Vector2: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def shapeCount(self) -> int: ...
    @property
    def sharedMaterial(self) -> PhysicsMaterial2D: ...
    @sharedMaterial.setter
    def sharedMaterial(self, value: PhysicsMaterial2D) -> PhysicsMaterial2D: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def usedByComposite(self) -> bool: ...
    @usedByComposite.setter
    def usedByComposite(self, value: bool) -> bool: ...
    @property
    def usedByEffector(self) -> bool: ...
    @usedByEffector.setter
    def usedByEffector(self, value: bool) -> bool: ...
    @property
    def useDelaunayMesh(self) -> bool: ...
    @useDelaunayMesh.setter
    def useDelaunayMesh(self, value: bool) -> bool: ...
    def ProcessTilemapChanges(self) -> None: ...


class TilemapRenderer(Renderer):
    def __init__(self) -> None: ...
    @property
    def allowOcclusionWhenDynamic(self) -> bool: ...
    @allowOcclusionWhenDynamic.setter
    def allowOcclusionWhenDynamic(self, value: bool) -> bool: ...
    @property
    def animation(self) -> Component: ...
    @property
    def audio(self) -> Component: ...
    @property
    def bounds(self) -> Bounds: ...
    @bounds.setter
    def bounds(self, value: Bounds) -> Bounds: ...
    @property
    def camera(self) -> Component: ...
    @property
    def castShadows(self) -> bool: ...
    @castShadows.setter
    def castShadows(self, value: bool) -> bool: ...
    @property
    def chunkCullingBounds(self) -> Vector3: ...
    @chunkCullingBounds.setter
    def chunkCullingBounds(self, value: Vector3) -> Vector3: ...
    @property
    def chunkSize(self) -> Vector3Int: ...
    @chunkSize.setter
    def chunkSize(self, value: Vector3Int) -> Vector3Int: ...
    @property
    def collider(self) -> Component: ...
    @property
    def collider2D(self) -> Component: ...
    @property
    def constantForce(self) -> Component: ...
    @property
    def detectChunkCullingBounds(self) -> TilemapRenderer.DetectChunkCullingBounds: ...
    @detectChunkCullingBounds.setter
    def detectChunkCullingBounds(self, value: TilemapRenderer.DetectChunkCullingBounds) -> TilemapRenderer.DetectChunkCullingBounds: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> bool: ...
    @property
    def forceRenderingOff(self) -> bool: ...
    @forceRenderingOff.setter
    def forceRenderingOff(self, value: bool) -> bool: ...
    @property
    def gameObject(self) -> GameObject: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def hingeJoint(self) -> Component: ...
    @property
    def isPartOfStaticBatch(self) -> bool: ...
    @property
    def isVisible(self) -> bool: ...
    @property
    def light(self) -> Component: ...
    @property
    def lightmapIndex(self) -> int: ...
    @lightmapIndex.setter
    def lightmapIndex(self, value: int) -> int: ...
    @property
    def lightmapScaleOffset(self) -> Vector4: ...
    @lightmapScaleOffset.setter
    def lightmapScaleOffset(self, value: Vector4) -> Vector4: ...
    @property
    def lightmapTilingOffset(self) -> Vector4: ...
    @lightmapTilingOffset.setter
    def lightmapTilingOffset(self, value: Vector4) -> Vector4: ...
    @property
    def lightProbeAnchor(self) -> Transform: ...
    @lightProbeAnchor.setter
    def lightProbeAnchor(self, value: Transform) -> Transform: ...
    @property
    def lightProbeProxyVolumeOverride(self) -> GameObject: ...
    @lightProbeProxyVolumeOverride.setter
    def lightProbeProxyVolumeOverride(self, value: GameObject) -> GameObject: ...
    @property
    def lightProbeUsage(self) -> LightProbeUsage: ...
    @lightProbeUsage.setter
    def lightProbeUsage(self, value: LightProbeUsage) -> LightProbeUsage: ...
    @property
    def localBounds(self) -> Bounds: ...
    @localBounds.setter
    def localBounds(self, value: Bounds) -> Bounds: ...
    @property
    def localToWorldMatrix(self) -> Matrix4x4: ...
    @property
    def maskInteraction(self) -> SpriteMaskInteraction: ...
    @maskInteraction.setter
    def maskInteraction(self, value: SpriteMaskInteraction) -> SpriteMaskInteraction: ...
    @property
    def material(self) -> Material: ...
    @material.setter
    def material(self, value: Material) -> Material: ...
    @property
    def materials(self) -> Array_1[Material]: ...
    @materials.setter
    def materials(self, value: Array_1[Material]) -> Array_1[Material]: ...
    @property
    def maxChunkCount(self) -> int: ...
    @maxChunkCount.setter
    def maxChunkCount(self, value: int) -> int: ...
    @property
    def maxFrameAge(self) -> int: ...
    @maxFrameAge.setter
    def maxFrameAge(self, value: int) -> int: ...
    @property
    def mode(self) -> TilemapRenderer.Mode: ...
    @mode.setter
    def mode(self, value: TilemapRenderer.Mode) -> TilemapRenderer.Mode: ...
    @property
    def motionVectorGenerationMode(self) -> MotionVectorGenerationMode: ...
    @motionVectorGenerationMode.setter
    def motionVectorGenerationMode(self, value: MotionVectorGenerationMode) -> MotionVectorGenerationMode: ...
    @property
    def motionVectors(self) -> bool: ...
    @motionVectors.setter
    def motionVectors(self, value: bool) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def networkView(self) -> Component: ...
    @property
    def particleSystem(self) -> Component: ...
    @property
    def probeAnchor(self) -> Transform: ...
    @probeAnchor.setter
    def probeAnchor(self, value: Transform) -> Transform: ...
    @property
    def rayTracingMode(self) -> RayTracingMode: ...
    @rayTracingMode.setter
    def rayTracingMode(self, value: RayTracingMode) -> RayTracingMode: ...
    @property
    def realtimeLightmapIndex(self) -> int: ...
    @realtimeLightmapIndex.setter
    def realtimeLightmapIndex(self, value: int) -> int: ...
    @property
    def realtimeLightmapScaleOffset(self) -> Vector4: ...
    @realtimeLightmapScaleOffset.setter
    def realtimeLightmapScaleOffset(self, value: Vector4) -> Vector4: ...
    @property
    def receiveShadows(self) -> bool: ...
    @receiveShadows.setter
    def receiveShadows(self, value: bool) -> bool: ...
    @property
    def reflectionProbeUsage(self) -> ReflectionProbeUsage: ...
    @reflectionProbeUsage.setter
    def reflectionProbeUsage(self, value: ReflectionProbeUsage) -> ReflectionProbeUsage: ...
    @property
    def renderer(self) -> Component: ...
    @property
    def rendererPriority(self) -> int: ...
    @rendererPriority.setter
    def rendererPriority(self, value: int) -> int: ...
    @property
    def renderingLayerMask(self) -> int: ...
    @renderingLayerMask.setter
    def renderingLayerMask(self, value: int) -> int: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def shadowCastingMode(self) -> ShadowCastingMode: ...
    @shadowCastingMode.setter
    def shadowCastingMode(self, value: ShadowCastingMode) -> ShadowCastingMode: ...
    @property
    def sharedMaterial(self) -> Material: ...
    @sharedMaterial.setter
    def sharedMaterial(self, value: Material) -> Material: ...
    @property
    def sharedMaterials(self) -> Array_1[Material]: ...
    @sharedMaterials.setter
    def sharedMaterials(self, value: Array_1[Material]) -> Array_1[Material]: ...
    @property
    def sortingLayerID(self) -> int: ...
    @sortingLayerID.setter
    def sortingLayerID(self, value: int) -> int: ...
    @property
    def sortingLayerName(self) -> str: ...
    @sortingLayerName.setter
    def sortingLayerName(self, value: str) -> str: ...
    @property
    def sortingOrder(self) -> int: ...
    @sortingOrder.setter
    def sortingOrder(self, value: int) -> int: ...
    @property
    def sortOrder(self) -> TilemapRenderer.SortOrder: ...
    @sortOrder.setter
    def sortOrder(self, value: TilemapRenderer.SortOrder) -> TilemapRenderer.SortOrder: ...
    @property
    def staticShadowCaster(self) -> bool: ...
    @staticShadowCaster.setter
    def staticShadowCaster(self, value: bool) -> bool: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def useLightProbes(self) -> bool: ...
    @useLightProbes.setter
    def useLightProbes(self, value: bool) -> bool: ...
    @property
    def worldToLocalMatrix(self) -> Matrix4x4: ...

    class DetectChunkCullingBounds(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Auto : TilemapRenderer.DetectChunkCullingBounds # 0
        Manual : TilemapRenderer.DetectChunkCullingBounds # 1


    class Mode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Chunk : TilemapRenderer.Mode # 0
        Individual : TilemapRenderer.Mode # 1


    class SortOrder(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        BottomLeft : TilemapRenderer.SortOrder # 0
        BottomRight : TilemapRenderer.SortOrder # 1
        TopLeft : TilemapRenderer.SortOrder # 2
        TopRight : TilemapRenderer.SortOrder # 3


