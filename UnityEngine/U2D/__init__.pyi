import typing, clr, abc
from System import Array_1
from UnityEngine import MonoBehaviour, Component, GameObject, HideFlags, Transform, Vector3, Object, Sprite, Color32, Quaternion, Matrix4x4, SpriteRenderer, Texture2D, Renderer, Bounds, Color, Vector4, SpriteMaskInteraction, Material, MotionVectorGenerationMode, Vector2, Mesh
from System.Threading import CancellationToken
from Unity.Collections import NativeArray_1, NativeSlice_1
from UnityEngine.Rendering import VertexAttribute, LightProbeUsage, ReflectionProbeUsage, ShadowCastingMode
from UnityEngine.Experimental.Rendering import RayTracingMode
from Unity.Jobs import JobHandle

class AngleRangeInfo:
    end : float
    order : int
    sprites : Array_1[int]
    start : float


class Light2DBase(MonoBehaviour, abc.ABC):
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
    def destroyCancellationToken(self) -> CancellationToken: ...
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
    def renderer(self) -> Component: ...
    @property
    def rigidbody(self) -> Component: ...
    @property
    def rigidbody2D(self) -> Component: ...
    @property
    def runInEditMode(self) -> bool: ...
    @runInEditMode.setter
    def runInEditMode(self, value: bool) -> bool: ...
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: str) -> str: ...
    @property
    def transform(self) -> Transform: ...
    @property
    def useGUILayout(self) -> bool: ...
    @useGUILayout.setter
    def useGUILayout(self, value: bool) -> bool: ...


class PixelPerfectRendering(abc.ABC):
    @classmethod
    @property
    def pixelSnapSpacing(cls) -> float: ...
    @classmethod
    @pixelSnapSpacing.setter
    def pixelSnapSpacing(cls, value: float) -> float: ...


class ShapeControlPoint:
    leftTangent : Vector3
    mode : int
    position : Vector3
    rightTangent : Vector3


class SpriteAtlas(Object):
    def __init__(self) -> None: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def isVariant(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def spriteCount(self) -> int: ...
    @property
    def tag(self) -> str: ...
    def CanBindTo(self, sprite: Sprite) -> bool: ...
    def GetSprite(self, name: str) -> Sprite: ...
    # Skipped GetSprites due to it being static, abstract and generic.

    GetSprites : GetSprites_MethodGroup
    class GetSprites_MethodGroup:
        @typing.overload
        def __call__(self, sprites: Array_1[Sprite]) -> int:...
        @typing.overload
        def __call__(self, sprites: Array_1[Sprite], name: str) -> int:...



class SpriteAtlasManager:
    def __init__(self) -> None: ...


class SpriteBone:
    @property
    def color(self) -> Color32: ...
    @color.setter
    def color(self, value: Color32) -> Color32: ...
    @property
    def guid(self) -> str: ...
    @guid.setter
    def guid(self, value: str) -> str: ...
    @property
    def length(self) -> float: ...
    @length.setter
    def length(self, value: float) -> float: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def parentId(self) -> int: ...
    @parentId.setter
    def parentId(self, value: int) -> int: ...
    @property
    def position(self) -> Vector3: ...
    @position.setter
    def position(self, value: Vector3) -> Vector3: ...
    @property
    def rotation(self) -> Quaternion: ...
    @rotation.setter
    def rotation(self, value: Quaternion) -> Quaternion: ...


class SpriteDataAccessExtensions(abc.ABC):
    @staticmethod
    def GetBindPoses(sprite: Sprite) -> NativeArray_1[Matrix4x4]: ...
    @staticmethod
    def GetBones(sprite: Sprite) -> Array_1[SpriteBone]: ...
    @staticmethod
    def GetIndices(sprite: Sprite) -> NativeArray_1[int]: ...
    @staticmethod
    def GetVertexCount(sprite: Sprite) -> int: ...
    @staticmethod
    def HasVertexAttribute(sprite: Sprite, channel: VertexAttribute) -> bool: ...
    @staticmethod
    def SetBindPoses(sprite: Sprite, src: NativeArray_1[Matrix4x4]) -> None: ...
    @staticmethod
    def SetBones(sprite: Sprite, src: Array_1[SpriteBone]) -> None: ...
    @staticmethod
    def SetIndices(sprite: Sprite, src: NativeArray_1[int]) -> None: ...
    @staticmethod
    def SetVertexCount(sprite: Sprite, count: int) -> None: ...
    # Skipped GetVertexAttribute due to it being static, abstract and generic.

    GetVertexAttribute : GetVertexAttribute_MethodGroup
    class GetVertexAttribute_MethodGroup:
        def __getitem__(self, t:typing.Type[GetVertexAttribute_1_T1]) -> GetVertexAttribute_1[GetVertexAttribute_1_T1]: ...

        GetVertexAttribute_1_T1 = typing.TypeVar('GetVertexAttribute_1_T1')
        class GetVertexAttribute_1(typing.Generic[GetVertexAttribute_1_T1]):
            GetVertexAttribute_1_T = SpriteDataAccessExtensions.GetVertexAttribute_MethodGroup.GetVertexAttribute_1_T1
            def __call__(self, sprite: Sprite, channel: VertexAttribute) -> NativeSlice_1[GetVertexAttribute_1_T]:...


    # Skipped SetVertexAttribute due to it being static, abstract and generic.

    SetVertexAttribute : SetVertexAttribute_MethodGroup
    class SetVertexAttribute_MethodGroup:
        def __getitem__(self, t:typing.Type[SetVertexAttribute_1_T1]) -> SetVertexAttribute_1[SetVertexAttribute_1_T1]: ...

        SetVertexAttribute_1_T1 = typing.TypeVar('SetVertexAttribute_1_T1')
        class SetVertexAttribute_1(typing.Generic[SetVertexAttribute_1_T1]):
            SetVertexAttribute_1_T = SpriteDataAccessExtensions.SetVertexAttribute_MethodGroup.SetVertexAttribute_1_T1
            def __call__(self, sprite: Sprite, channel: VertexAttribute, src: NativeArray_1[SetVertexAttribute_1_T]) -> None:...




class SpriteRendererDataAccessExtensions(abc.ABC):
    @staticmethod
    def DeactivateDeformableBuffer(renderer: SpriteRenderer) -> None: ...


class SpriteShapeMetaData:
    bevelCutoff : float
    bevelSize : float
    corner : bool
    height : float
    spriteIndex : int


class SpriteShapeParameters:
    adaptiveUV : bool
    angleThreshold : float
    bevelCutoff : float
    bevelSize : float
    borderPivot : float
    carpet : bool
    fillScale : int
    fillTexture : Texture2D
    smartSprite : bool
    splineDetail : int
    spriteBorders : bool
    stretchUV : bool
    transform : Matrix4x4


class SpriteShapeRenderer(Renderer):
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
    def GetBounds(self) -> NativeArray_1[Bounds]: ...
    def GetSegments(self, dataSize: int) -> NativeArray_1[SpriteShapeSegment]: ...
    def Prepare(self, handle: JobHandle, shapeParams: SpriteShapeParameters, sprites: Array_1[Sprite]) -> None: ...
    def SetLocalAABB(self, bounds: Bounds) -> None: ...
    # Skipped GetChannels due to it being static, abstract and generic.

    GetChannels : GetChannels_MethodGroup
    class GetChannels_MethodGroup:
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]]) -> None:...
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]], colors: clr.Reference[NativeSlice_1[Color32]]) -> None:...
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]], tangents: clr.Reference[NativeSlice_1[Vector4]]) -> None:...
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]], colors: clr.Reference[NativeSlice_1[Color32]], tangents: clr.Reference[NativeSlice_1[Vector4]]) -> None:...
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]], tangents: clr.Reference[NativeSlice_1[Vector4]], normals: clr.Reference[NativeSlice_1[Vector3]]) -> None:...
        @typing.overload
        def __call__(self, dataSize: int, indices: clr.Reference[NativeArray_1[int]], vertices: clr.Reference[NativeSlice_1[Vector3]], texcoords: clr.Reference[NativeSlice_1[Vector2]], colors: clr.Reference[NativeSlice_1[Color32]], tangents: clr.Reference[NativeSlice_1[Vector4]], normals: clr.Reference[NativeSlice_1[Vector3]]) -> None:...



class SpriteShapeSegment:
    @property
    def geomIndex(self) -> int: ...
    @geomIndex.setter
    def geomIndex(self, value: int) -> int: ...
    @property
    def indexCount(self) -> int: ...
    @indexCount.setter
    def indexCount(self, value: int) -> int: ...
    @property
    def spriteIndex(self) -> int: ...
    @spriteIndex.setter
    def spriteIndex(self, value: int) -> int: ...
    @property
    def vertexCount(self) -> int: ...
    @vertexCount.setter
    def vertexCount(self, value: int) -> int: ...


class SpriteShapeUtility:
    def __init__(self) -> None: ...
    @staticmethod
    def Generate(mesh: Mesh, shapeParams: SpriteShapeParameters, points: Array_1[ShapeControlPoint], metaData: Array_1[SpriteShapeMetaData], angleRange: Array_1[AngleRangeInfo], sprites: Array_1[Sprite], corners: Array_1[Sprite]) -> Array_1[int]: ...
    @staticmethod
    def GenerateSpriteShape(renderer: SpriteShapeRenderer, shapeParams: SpriteShapeParameters, points: Array_1[ShapeControlPoint], metaData: Array_1[SpriteShapeMetaData], angleRange: Array_1[AngleRangeInfo], sprites: Array_1[Sprite], corners: Array_1[Sprite]) -> None: ...

