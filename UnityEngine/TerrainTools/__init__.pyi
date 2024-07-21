import typing, clr, abc
from UnityEngine import Vector2, Rect, Terrain, RectInt, RenderTexture, RenderTextureFormat, Texture, Color, Material, TerrainLayer, Vector4, Texture2D
from System import Func_2, Action_1

class BrushTransform:
    def __init__(self, brushOrigin: Vector2, brushU: Vector2, brushV: Vector2) -> None: ...
    @property
    def brushOrigin(self) -> Vector2: ...
    @property
    def brushU(self) -> Vector2: ...
    @property
    def brushV(self) -> Vector2: ...
    @property
    def targetOrigin(self) -> Vector2: ...
    @property
    def targetX(self) -> Vector2: ...
    @property
    def targetY(self) -> Vector2: ...
    def FromBrushUV(self, brushUV: Vector2) -> Vector2: ...
    @staticmethod
    def FromRect(brushRect: Rect) -> BrushTransform: ...
    def GetBrushXYBounds(self) -> Rect: ...
    def ToBrushUV(self, targetXY: Vector2) -> Vector2: ...


class PaintContext:
    def __init__(self, terrain: Terrain, pixelRect: RectInt, targetTextureWidth: int, targetTextureHeight: int, sharedBoundaryTexel: bool = ..., fillOutsideTerrain: bool = ...) -> None: ...
    @property
    def destinationRenderTexture(self) -> RenderTexture: ...
    @destinationRenderTexture.setter
    def destinationRenderTexture(self, value: RenderTexture) -> RenderTexture: ...
    @property
    def heightWorldSpaceMin(self) -> float: ...
    @property
    def heightWorldSpaceSize(self) -> float: ...
    @classmethod
    @property
    def kNormalizedHeightScale(cls) -> float: ...
    @property
    def oldRenderTexture(self) -> RenderTexture: ...
    @oldRenderTexture.setter
    def oldRenderTexture(self, value: RenderTexture) -> RenderTexture: ...
    @property
    def originTerrain(self) -> Terrain: ...
    @property
    def pixelRect(self) -> RectInt: ...
    @property
    def pixelSize(self) -> Vector2: ...
    @property
    def sourceRenderTexture(self) -> RenderTexture: ...
    @sourceRenderTexture.setter
    def sourceRenderTexture(self, value: RenderTexture) -> RenderTexture: ...
    @property
    def targetTextureHeight(self) -> int: ...
    @property
    def targetTextureWidth(self) -> int: ...
    @property
    def terrainCount(self) -> int: ...
    @staticmethod
    def ApplyDelayedActions() -> None: ...
    def Cleanup(self, restoreRenderTexture: bool = ...) -> None: ...
    @staticmethod
    def CreateFromBounds(terrain: Terrain, boundsInTerrainSpace: Rect, inputTextureWidth: int, inputTextureHeight: int, extraBorderPixels: int = ..., sharedBoundaryTexel: bool = ..., fillOutsideTerrain: bool = ...) -> PaintContext: ...
    def CreateRenderTargets(self, colorFormat: RenderTextureFormat) -> None: ...
    def Gather(self, terrainSource: Func_2[PaintContext.ITerrainInfo, Texture], defaultColor: Color, blitMaterial: Material = ..., blitPass: int = ..., beforeBlit: Action_1[PaintContext.ITerrainInfo] = ..., afterBlit: Action_1[PaintContext.ITerrainInfo] = ...) -> None: ...
    def GatherAlphamap(self, inputLayer: TerrainLayer, addLayerIfDoesntExist: bool = ...) -> None: ...
    def GatherHeightmap(self) -> None: ...
    def GatherHoles(self) -> None: ...
    def GatherNormals(self) -> None: ...
    def GetClippedPixelRectInRenderTexturePixels(self, terrainIndex: int) -> RectInt: ...
    def GetClippedPixelRectInTerrainPixels(self, terrainIndex: int) -> RectInt: ...
    def GetTerrain(self, terrainIndex: int) -> Terrain: ...
    def Scatter(self, terrainDest: Func_2[PaintContext.ITerrainInfo, RenderTexture], blitMaterial: Material = ..., blitPass: int = ..., beforeBlit: Action_1[PaintContext.ITerrainInfo] = ..., afterBlit: Action_1[PaintContext.ITerrainInfo] = ...) -> None: ...
    def ScatterAlphamap(self, editorUndoName: str) -> None: ...
    def ScatterHeightmap(self, editorUndoName: str) -> None: ...
    def ScatterHoles(self, editorUndoName: str) -> None: ...

    class ITerrainInfo(typing.Protocol):
        @property
        def clippedPCPixels(self) -> RectInt: ...
        @property
        def clippedTerrainPixels(self) -> RectInt: ...
        @property
        def gatherEnable(self) -> bool: ...
        @gatherEnable.setter
        def gatherEnable(self, value: bool) -> bool: ...
        @property
        def paddedPCPixels(self) -> RectInt: ...
        @property
        def paddedTerrainPixels(self) -> RectInt: ...
        @property
        def scatterEnable(self) -> bool: ...
        @scatterEnable.setter
        def scatterEnable(self, value: bool) -> bool: ...
        @property
        def terrain(self) -> Terrain: ...
        @property
        def userData(self) -> typing.Any: ...
        @userData.setter
        def userData(self, value: typing.Any) -> typing.Any: ...



class TerrainBuiltinPaintMaterialPasses(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RaiseLowerHeight : TerrainBuiltinPaintMaterialPasses # 0
    StampHeight : TerrainBuiltinPaintMaterialPasses # 1
    SetHeights : TerrainBuiltinPaintMaterialPasses # 2
    SmoothHeights : TerrainBuiltinPaintMaterialPasses # 3
    PaintTexture : TerrainBuiltinPaintMaterialPasses # 4
    PaintHoles : TerrainBuiltinPaintMaterialPasses # 5


class TerrainPaintUtility(abc.ABC):
    @staticmethod
    def BeginPaintHeightmap(terrain: Terrain, boundsInTerrainSpace: Rect, extraBorderPixels: int = ..., fillOutsideTerrain: bool = ...) -> PaintContext: ...
    @staticmethod
    def BeginPaintHoles(terrain: Terrain, boundsInTerrainSpace: Rect, extraBorderPixels: int = ..., fillOutsideTerrain: bool = ...) -> PaintContext: ...
    @staticmethod
    def BeginPaintTexture(terrain: Terrain, boundsInTerrainSpace: Rect, inputLayer: TerrainLayer, extraBorderPixels: int = ..., fillOutsideTerrain: bool = ...) -> PaintContext: ...
    @staticmethod
    def BuildTransformPaintContextUVToPaintContextUV(src: PaintContext, dst: PaintContext, scaleOffset: clr.Reference[Vector4]) -> None: ...
    @staticmethod
    def CalculateBrushTransform(terrain: Terrain, brushCenterTerrainUV: Vector2, brushSize: float, brushRotationDegrees: float) -> BrushTransform: ...
    @staticmethod
    def CollectNormals(terrain: Terrain, boundsInTerrainSpace: Rect, extraBorderPixels: int = ..., fillOutsideTerrain: bool = ...) -> PaintContext: ...
    @staticmethod
    def EndPaintHeightmap(ctx: PaintContext, editorUndoName: str) -> None: ...
    @staticmethod
    def EndPaintHoles(ctx: PaintContext, editorUndoName: str) -> None: ...
    @staticmethod
    def EndPaintTexture(ctx: PaintContext, editorUndoName: str) -> None: ...
    @staticmethod
    def FindTerrainLayerIndex(terrain: Terrain, inputLayer: TerrainLayer) -> int: ...
    @staticmethod
    def GetBlitMaterial() -> Material: ...
    @staticmethod
    def GetBrushWorldSizeLimits(minBrushWorldSize: clr.Reference[float], maxBrushWorldSize: clr.Reference[float], terrainTileWorldSize: float, terrainTileTextureResolutionPixels: int, minBrushResolutionPixels: int = ..., maxBrushResolutionPixels: int = ...) -> None: ...
    @staticmethod
    def GetBuiltinPaintMaterial() -> Material: ...
    @staticmethod
    def GetCopyTerrainLayerMaterial() -> Material: ...
    @staticmethod
    def GetHeightBlitMaterial() -> Material: ...
    @staticmethod
    def GetTerrainAlphaMapChecked(terrain: Terrain, mapIndex: int) -> Texture2D: ...
    @staticmethod
    def ReleaseContextResources(ctx: PaintContext) -> None: ...
    @staticmethod
    def SetupTerrainToolMaterialProperties(paintContext: PaintContext, brushXform: clr.Reference[BrushTransform], material: Material) -> None: ...

