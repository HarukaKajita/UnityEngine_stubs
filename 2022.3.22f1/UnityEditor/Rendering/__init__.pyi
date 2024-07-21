import typing, abc
from UnityEngine import Color, Camera, Texture, RenderingPath
from UnityEditor import StaticEditorFlags, BuildTargetGroup, BuildTarget
from System import Array_1, Attribute
from UnityEngine.Rendering import ShaderHardwareTier, GraphicsTier, PlatformKeywordSet, ShaderKeywordSet, PassIdentifier, PassType, CameraHDRMode, RealtimeGICPUUsage
from UnityEditor.Build import NamedBuildTarget

class AlbedoSwatchInfo:
    color : Color
    maxLuminance : float
    minLuminance : float
    name : str


class EditorCameraUtils(abc.ABC):
    @staticmethod
    def RenderToCubemap(camera: Camera, target: Texture, faceMask: int, culledFlags: StaticEditorFlags) -> bool: ...


class EditorGraphicsSettings:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def albedoSwatches(cls) -> Array_1[AlbedoSwatchInfo]: ...
    @classmethod
    @albedoSwatches.setter
    def albedoSwatches(cls, value: Array_1[AlbedoSwatchInfo]) -> Array_1[AlbedoSwatchInfo]: ...
    @staticmethod
    def GetShaderSettingsForPlatform(target: BuildTargetGroup, tier: ShaderHardwareTier) -> PlatformShaderSettings: ...
    @staticmethod
    def SetShaderSettingsForPlatform(target: BuildTargetGroup, tier: ShaderHardwareTier, settings: PlatformShaderSettings) -> None: ...
    # Skipped GetTierSettings due to it being static, abstract and generic.

    GetTierSettings : GetTierSettings_MethodGroup
    class GetTierSettings_MethodGroup:
        @typing.overload
        def __call__(self, target: BuildTargetGroup, tier: GraphicsTier) -> TierSettings:...
        @typing.overload
        def __call__(self, target: BuildTargetGroup, tier: ShaderHardwareTier) -> TierSettings:...
        @typing.overload
        def __call__(self, target: NamedBuildTarget, tier: GraphicsTier) -> TierSettings:...

    # Skipped SetTierSettings due to it being static, abstract and generic.

    SetTierSettings : SetTierSettings_MethodGroup
    class SetTierSettings_MethodGroup:
        @typing.overload
        def __call__(self, target: BuildTargetGroup, tier: GraphicsTier, settings: TierSettings) -> None:...
        @typing.overload
        def __call__(self, target: BuildTargetGroup, tier: ShaderHardwareTier, settings: TierSettings) -> None:...
        @typing.overload
        def __call__(self, target: NamedBuildTarget, tier: GraphicsTier, settings: TierSettings) -> None:...



class PlatformShaderSettings:
    cascadedShadowMaps : bool
    reflectionProbeBlending : bool
    reflectionProbeBoxProjection : bool
    standardShaderQuality : ShaderQuality


class RenderPipelineEditorUtility(abc.ABC):
    # Skipped FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension due to it being static, abstract and generic.

    FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension : FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_MethodGroup
    class FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_MethodGroup:
        def __getitem__(self, t:typing.Type[FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1]) -> FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1[FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1]: ...

        FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1 = typing.TypeVar('FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1')
        class FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1(typing.Generic[FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1]):
            FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_TBaseClass = RenderPipelineEditorUtility.FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_MethodGroup.FetchFirstCompatibleTypeUsingScriptableRenderPipelineExtension_1_T1
            def __call__(self) -> typing.Type[typing.Any]:...




class ScriptableRenderPipelineExtensionAttribute(Attribute):
    def __init__(self, renderPipelineAsset: typing.Type[typing.Any]) -> None: ...
    @property
    def inUse(self) -> bool: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ShaderCompilerData:
    platformKeywordSet : PlatformKeywordSet
    shaderKeywordSet : ShaderKeywordSet
    @property
    def buildTarget(self) -> BuildTarget: ...
    @property
    def graphicsTier(self) -> GraphicsTier: ...
    @property
    def shaderCompilerPlatform(self) -> ShaderCompilerPlatform: ...
    @property
    def shaderRequirements(self) -> ShaderRequirements: ...


class ShaderCompilerMessageSeverity(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Error : ShaderCompilerMessageSeverity # 0
    Warning : ShaderCompilerMessageSeverity # 1


class ShaderCompilerPlatform(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ShaderCompilerPlatform # 0
    D3D : ShaderCompilerPlatform # 4
    GLES20 : ShaderCompilerPlatform # 5
    GLES3x : ShaderCompilerPlatform # 9
    PS4 : ShaderCompilerPlatform # 11
    XboxOneD3D11 : ShaderCompilerPlatform # 12
    Metal : ShaderCompilerPlatform # 14
    OpenGLCore : ShaderCompilerPlatform # 15
    Vulkan : ShaderCompilerPlatform # 18
    Switch : ShaderCompilerPlatform # 19
    XboxOneD3D12 : ShaderCompilerPlatform # 20
    GameCoreXboxOne : ShaderCompilerPlatform # 21
    GameCoreXboxSeries : ShaderCompilerPlatform # 22
    PS5 : ShaderCompilerPlatform # 23
    PS5NGGC : ShaderCompilerPlatform # 24
    GameCore : ShaderCompilerPlatform # 25


class ShaderQuality(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Low : ShaderQuality # 0
    Medium : ShaderQuality # 1
    High : ShaderQuality # 2


class ShaderRequirements(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ShaderRequirements # 0
    BaseShaders : ShaderRequirements # 1
    Interpolators10 : ShaderRequirements # 2
    Interpolators32 : ShaderRequirements # 4
    MRT4 : ShaderRequirements # 8
    MRT8 : ShaderRequirements # 16
    Derivatives : ShaderRequirements # 32
    SampleLOD : ShaderRequirements # 64
    FragCoord : ShaderRequirements # 128
    FragClipDepth : ShaderRequirements # 256
    Interpolators15Integers : ShaderRequirements # 512
    Texture2DArray : ShaderRequirements # 1024
    Instancing : ShaderRequirements # 2048
    Geometry : ShaderRequirements # 4096
    CubeArray : ShaderRequirements # 8192
    Compute : ShaderRequirements # 16384
    RandomWrite : ShaderRequirements # 32768
    TessellationCompute : ShaderRequirements # 65536
    TessellationShaders : ShaderRequirements # 131072
    SparseTexelResident : ShaderRequirements # 262144
    FramebufferFetch : ShaderRequirements # 524288
    MSAATextureSamples : ShaderRequirements # 1048576
    SetRTArrayIndexFromAnyShader : ShaderRequirements # 2097152


class ShaderSnippetData:
    @property
    def pass(self) -> PassIdentifier: ...
    @property
    def passName(self) -> str: ...
    @property
    def passType(self) -> PassType: ...
    @property
    def shaderType(self) -> ShaderType: ...


class ShaderType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Vertex : ShaderType # 1
    Fragment : ShaderType # 2
    Geometry : ShaderType # 3
    Hull : ShaderType # 4
    Domain : ShaderType # 5
    Surface : ShaderType # 6
    RayTracing : ShaderType # 7
    Count : ShaderType # 7


class TierSettings:
    cascadedShadowMaps : bool
    detailNormalMap : bool
    enableLPPV : bool
    hdr : bool
    hdrMode : CameraHDRMode
    prefer32BitShadowMaps : bool
    realtimeGICPUUsage : RealtimeGICPUUsage
    reflectionProbeBlending : bool
    reflectionProbeBoxProjection : bool
    renderingPath : RenderingPath
    semitransparentShadows : bool
    standardShaderQuality : ShaderQuality

