import typing, clr, abc
from UnityEngine import RenderTextureFormat, TextureFormat, RenderTextureReadWrite, Renderer, MaterialPropertyBlock, GraphicsBuffer, Material, Matrix4x4, Vector3, Plane, Object, HideFlags, Camera, ComputeBuffer, Texture, Vector4, Shader, ShaderVariantCollection
from UnityEngine.Rendering import FormatSwizzle, LODParameters, ShaderTagId, VertexAttributeDescriptor
from System import IDisposable, Array_1

class DefaultFormat(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    LDR : DefaultFormat # 0
    HDR : DefaultFormat # 1
    DepthStencil : DefaultFormat # 2
    Shadow : DefaultFormat # 3
    Video : DefaultFormat # 4


class ExternalGPUProfiler(abc.ABC):
    @staticmethod
    def BeginGPUCapture() -> None: ...
    @staticmethod
    def EndGPUCapture() -> None: ...
    @staticmethod
    def IsAttached() -> bool: ...


class FormatUsage(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Sample : FormatUsage # 0
    Linear : FormatUsage # 1
    Sparse : FormatUsage # 2
    Render : FormatUsage # 4
    Blend : FormatUsage # 5
    GetPixels : FormatUsage # 6
    SetPixels : FormatUsage # 7
    SetPixels32 : FormatUsage # 8
    ReadPixels : FormatUsage # 9
    LoadStore : FormatUsage # 10
    MSAA2x : FormatUsage # 11
    MSAA4x : FormatUsage # 12
    MSAA8x : FormatUsage # 13
    StencilSampling : FormatUsage # 16


class GraphicsDeviceSettings(abc.ABC):
    @classmethod
    @property
    def graphicsJobsSyncPoint(cls) -> GraphicsJobsSyncPoint: ...
    @classmethod
    @graphicsJobsSyncPoint.setter
    def graphicsJobsSyncPoint(cls, value: GraphicsJobsSyncPoint) -> GraphicsJobsSyncPoint: ...
    @classmethod
    @property
    def waitForPresentSyncPoint(cls) -> WaitForPresentSyncPoint: ...
    @classmethod
    @waitForPresentSyncPoint.setter
    def waitForPresentSyncPoint(cls, value: WaitForPresentSyncPoint) -> WaitForPresentSyncPoint: ...


class GraphicsFormat(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : GraphicsFormat # 0
    R8_SRGB : GraphicsFormat # 1
    R8G8_SRGB : GraphicsFormat # 2
    R8G8B8_SRGB : GraphicsFormat # 3
    R8G8B8A8_SRGB : GraphicsFormat # 4
    R8_UNorm : GraphicsFormat # 5
    R8G8_UNorm : GraphicsFormat # 6
    R8G8B8_UNorm : GraphicsFormat # 7
    R8G8B8A8_UNorm : GraphicsFormat # 8
    R8_SNorm : GraphicsFormat # 9
    R8G8_SNorm : GraphicsFormat # 10
    R8G8B8_SNorm : GraphicsFormat # 11
    R8G8B8A8_SNorm : GraphicsFormat # 12
    R8_UInt : GraphicsFormat # 13
    R8G8_UInt : GraphicsFormat # 14
    R8G8B8_UInt : GraphicsFormat # 15
    R8G8B8A8_UInt : GraphicsFormat # 16
    R8_SInt : GraphicsFormat # 17
    R8G8_SInt : GraphicsFormat # 18
    R8G8B8_SInt : GraphicsFormat # 19
    R8G8B8A8_SInt : GraphicsFormat # 20
    R16_UNorm : GraphicsFormat # 21
    R16G16_UNorm : GraphicsFormat # 22
    R16G16B16_UNorm : GraphicsFormat # 23
    R16G16B16A16_UNorm : GraphicsFormat # 24
    R16_SNorm : GraphicsFormat # 25
    R16G16_SNorm : GraphicsFormat # 26
    R16G16B16_SNorm : GraphicsFormat # 27
    R16G16B16A16_SNorm : GraphicsFormat # 28
    R16_UInt : GraphicsFormat # 29
    R16G16_UInt : GraphicsFormat # 30
    R16G16B16_UInt : GraphicsFormat # 31
    R16G16B16A16_UInt : GraphicsFormat # 32
    R16_SInt : GraphicsFormat # 33
    R16G16_SInt : GraphicsFormat # 34
    R16G16B16_SInt : GraphicsFormat # 35
    R16G16B16A16_SInt : GraphicsFormat # 36
    R32_UInt : GraphicsFormat # 37
    R32G32_UInt : GraphicsFormat # 38
    R32G32B32_UInt : GraphicsFormat # 39
    R32G32B32A32_UInt : GraphicsFormat # 40
    R32_SInt : GraphicsFormat # 41
    R32G32_SInt : GraphicsFormat # 42
    R32G32B32_SInt : GraphicsFormat # 43
    R32G32B32A32_SInt : GraphicsFormat # 44
    R16_SFloat : GraphicsFormat # 45
    R16G16_SFloat : GraphicsFormat # 46
    R16G16B16_SFloat : GraphicsFormat # 47
    R16G16B16A16_SFloat : GraphicsFormat # 48
    R32_SFloat : GraphicsFormat # 49
    R32G32_SFloat : GraphicsFormat # 50
    R32G32B32_SFloat : GraphicsFormat # 51
    R32G32B32A32_SFloat : GraphicsFormat # 52
    B8G8R8_SRGB : GraphicsFormat # 56
    B8G8R8A8_SRGB : GraphicsFormat # 57
    B8G8R8_UNorm : GraphicsFormat # 58
    B8G8R8A8_UNorm : GraphicsFormat # 59
    B8G8R8_SNorm : GraphicsFormat # 60
    B8G8R8A8_SNorm : GraphicsFormat # 61
    B8G8R8_UInt : GraphicsFormat # 62
    B8G8R8A8_UInt : GraphicsFormat # 63
    B8G8R8_SInt : GraphicsFormat # 64
    B8G8R8A8_SInt : GraphicsFormat # 65
    R4G4B4A4_UNormPack16 : GraphicsFormat # 66
    B4G4R4A4_UNormPack16 : GraphicsFormat # 67
    R5G6B5_UNormPack16 : GraphicsFormat # 68
    B5G6R5_UNormPack16 : GraphicsFormat # 69
    R5G5B5A1_UNormPack16 : GraphicsFormat # 70
    B5G5R5A1_UNormPack16 : GraphicsFormat # 71
    A1R5G5B5_UNormPack16 : GraphicsFormat # 72
    E5B9G9R9_UFloatPack32 : GraphicsFormat # 73
    B10G11R11_UFloatPack32 : GraphicsFormat # 74
    A2B10G10R10_UNormPack32 : GraphicsFormat # 75
    A2B10G10R10_UIntPack32 : GraphicsFormat # 76
    A2B10G10R10_SIntPack32 : GraphicsFormat # 77
    A2R10G10B10_UNormPack32 : GraphicsFormat # 78
    A2R10G10B10_UIntPack32 : GraphicsFormat # 79
    A2R10G10B10_SIntPack32 : GraphicsFormat # 80
    A2R10G10B10_XRSRGBPack32 : GraphicsFormat # 81
    A2R10G10B10_XRUNormPack32 : GraphicsFormat # 82
    R10G10B10_XRSRGBPack32 : GraphicsFormat # 83
    R10G10B10_XRUNormPack32 : GraphicsFormat # 84
    A10R10G10B10_XRSRGBPack32 : GraphicsFormat # 85
    A10R10G10B10_XRUNormPack32 : GraphicsFormat # 86
    D16_UNorm : GraphicsFormat # 90
    D24_UNorm : GraphicsFormat # 91
    D24_UNorm_S8_UInt : GraphicsFormat # 92
    D32_SFloat : GraphicsFormat # 93
    D32_SFloat_S8_UInt : GraphicsFormat # 94
    S8_UInt : GraphicsFormat # 95
    RGB_DXT1_SRGB : GraphicsFormat # 96
    RGBA_DXT1_SRGB : GraphicsFormat # 96
    RGB_DXT1_UNorm : GraphicsFormat # 97
    RGBA_DXT1_UNorm : GraphicsFormat # 97
    RGBA_DXT3_SRGB : GraphicsFormat # 98
    RGBA_DXT3_UNorm : GraphicsFormat # 99
    RGBA_DXT5_SRGB : GraphicsFormat # 100
    RGBA_DXT5_UNorm : GraphicsFormat # 101
    R_BC4_UNorm : GraphicsFormat # 102
    R_BC4_SNorm : GraphicsFormat # 103
    RG_BC5_UNorm : GraphicsFormat # 104
    RG_BC5_SNorm : GraphicsFormat # 105
    RGB_BC6H_UFloat : GraphicsFormat # 106
    RGB_BC6H_SFloat : GraphicsFormat # 107
    RGBA_BC7_SRGB : GraphicsFormat # 108
    RGBA_BC7_UNorm : GraphicsFormat # 109
    RGB_PVRTC_2Bpp_SRGB : GraphicsFormat # 110
    RGB_PVRTC_2Bpp_UNorm : GraphicsFormat # 111
    RGB_PVRTC_4Bpp_SRGB : GraphicsFormat # 112
    RGB_PVRTC_4Bpp_UNorm : GraphicsFormat # 113
    RGBA_PVRTC_2Bpp_SRGB : GraphicsFormat # 114
    RGBA_PVRTC_2Bpp_UNorm : GraphicsFormat # 115
    RGBA_PVRTC_4Bpp_SRGB : GraphicsFormat # 116
    RGBA_PVRTC_4Bpp_UNorm : GraphicsFormat # 117
    RGB_ETC_UNorm : GraphicsFormat # 118
    RGB_ETC2_SRGB : GraphicsFormat # 119
    RGB_ETC2_UNorm : GraphicsFormat # 120
    RGB_A1_ETC2_SRGB : GraphicsFormat # 121
    RGB_A1_ETC2_UNorm : GraphicsFormat # 122
    RGBA_ETC2_SRGB : GraphicsFormat # 123
    RGBA_ETC2_UNorm : GraphicsFormat # 124
    R_EAC_UNorm : GraphicsFormat # 125
    R_EAC_SNorm : GraphicsFormat # 126
    RG_EAC_UNorm : GraphicsFormat # 127
    RG_EAC_SNorm : GraphicsFormat # 128
    RGBA_ASTC4X4_SRGB : GraphicsFormat # 129
    RGBA_ASTC4X4_UNorm : GraphicsFormat # 130
    RGBA_ASTC5X5_SRGB : GraphicsFormat # 131
    RGBA_ASTC5X5_UNorm : GraphicsFormat # 132
    RGBA_ASTC6X6_SRGB : GraphicsFormat # 133
    RGBA_ASTC6X6_UNorm : GraphicsFormat # 134
    RGBA_ASTC8X8_SRGB : GraphicsFormat # 135
    RGBA_ASTC8X8_UNorm : GraphicsFormat # 136
    RGBA_ASTC10X10_SRGB : GraphicsFormat # 137
    RGBA_ASTC10X10_UNorm : GraphicsFormat # 138
    RGBA_ASTC12X12_SRGB : GraphicsFormat # 139
    RGBA_ASTC12X12_UNorm : GraphicsFormat # 140
    YUV2 : GraphicsFormat # 141
    DepthAuto : GraphicsFormat # 142
    ShadowAuto : GraphicsFormat # 143
    VideoAuto : GraphicsFormat # 144
    RGBA_ASTC4X4_UFloat : GraphicsFormat # 145
    RGBA_ASTC5X5_UFloat : GraphicsFormat # 146
    RGBA_ASTC6X6_UFloat : GraphicsFormat # 147
    RGBA_ASTC8X8_UFloat : GraphicsFormat # 148
    RGBA_ASTC10X10_UFloat : GraphicsFormat # 149
    RGBA_ASTC12X12_UFloat : GraphicsFormat # 150
    D16_UNorm_S8_UInt : GraphicsFormat # 151


class GraphicsFormatUtility:
    def __init__(self) -> None: ...
    @staticmethod
    def GetDepthBits(format: GraphicsFormat) -> int: ...
    @staticmethod
    def GetDepthStencilFormat(minimumDepthBits: int, minimumStencilBits: int) -> GraphicsFormat: ...
    @staticmethod
    def GetLinearFormat(format: GraphicsFormat) -> GraphicsFormat: ...
    @staticmethod
    def GetRenderTextureFormat(format: GraphicsFormat) -> RenderTextureFormat: ...
    @staticmethod
    def GetSRGBFormat(format: GraphicsFormat) -> GraphicsFormat: ...
    @staticmethod
    def GetTextureFormat(format: GraphicsFormat) -> TextureFormat: ...
    @staticmethod
    def IsCrunchFormat(format: TextureFormat) -> bool: ...
    @staticmethod
    def IsDepthFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsDepthStencilFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsFloatFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsHalfFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsIEEE754Format(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsIntegerFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsNormFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsSIntFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsSNormFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsSRGBFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsStencilFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsUIntFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsUNormFormat(format: GraphicsFormat) -> bool: ...
    @staticmethod
    def IsXRFormat(format: GraphicsFormat) -> bool: ...
    # Skipped ComputeMipChainSize due to it being static, abstract and generic.

    ComputeMipChainSize : ComputeMipChainSize_MethodGroup
    class ComputeMipChainSize_MethodGroup:
        @typing.overload
        def __call__(self, width: int, height: int, format: GraphicsFormat, mipCount: int = ...) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, format: TextureFormat, mipCount: int = ...) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, depth: int, format: GraphicsFormat, mipCount: int = ...) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, depth: int, format: TextureFormat, mipCount: int = ...) -> int:...

    # Skipped ComputeMipmapSize due to it being static, abstract and generic.

    ComputeMipmapSize : ComputeMipmapSize_MethodGroup
    class ComputeMipmapSize_MethodGroup:
        @typing.overload
        def __call__(self, width: int, height: int, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, format: TextureFormat) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, depth: int, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, width: int, height: int, depth: int, format: TextureFormat) -> int:...

    # Skipped ConvertToAlphaFormat due to it being static, abstract and generic.

    ConvertToAlphaFormat : ConvertToAlphaFormat_MethodGroup
    class ConvertToAlphaFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> GraphicsFormat:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> TextureFormat:...

    # Skipped GetAlphaComponentCount due to it being static, abstract and generic.

    GetAlphaComponentCount : GetAlphaComponentCount_MethodGroup
    class GetAlphaComponentCount_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetBlockHeight due to it being static, abstract and generic.

    GetBlockHeight : GetBlockHeight_MethodGroup
    class GetBlockHeight_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetBlockSize due to it being static, abstract and generic.

    GetBlockSize : GetBlockSize_MethodGroup
    class GetBlockSize_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetBlockWidth due to it being static, abstract and generic.

    GetBlockWidth : GetBlockWidth_MethodGroup
    class GetBlockWidth_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetColorComponentCount due to it being static, abstract and generic.

    GetColorComponentCount : GetColorComponentCount_MethodGroup
    class GetColorComponentCount_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetComponentCount due to it being static, abstract and generic.

    GetComponentCount : GetComponentCount_MethodGroup
    class GetComponentCount_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> int:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> int:...

    # Skipped GetFormatString due to it being static, abstract and generic.

    GetFormatString : GetFormatString_MethodGroup
    class GetFormatString_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> str:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> str:...

    # Skipped GetGraphicsFormat due to it being static, abstract and generic.

    GetGraphicsFormat : GetGraphicsFormat_MethodGroup
    class GetGraphicsFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: RenderTextureFormat, readWrite: RenderTextureReadWrite) -> GraphicsFormat:...
        @typing.overload
        def __call__(self, format: TextureFormat, isSRGB: bool) -> GraphicsFormat:...
        @typing.overload
        def __call__(self, format: RenderTextureFormat, isSRGB: bool) -> GraphicsFormat:...

    # Skipped GetSwizzleA due to it being static, abstract and generic.

    GetSwizzleA : GetSwizzleA_MethodGroup
    class GetSwizzleA_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> FormatSwizzle:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> FormatSwizzle:...

    # Skipped GetSwizzleB due to it being static, abstract and generic.

    GetSwizzleB : GetSwizzleB_MethodGroup
    class GetSwizzleB_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> FormatSwizzle:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> FormatSwizzle:...

    # Skipped GetSwizzleG due to it being static, abstract and generic.

    GetSwizzleG : GetSwizzleG_MethodGroup
    class GetSwizzleG_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> FormatSwizzle:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> FormatSwizzle:...

    # Skipped GetSwizzleR due to it being static, abstract and generic.

    GetSwizzleR : GetSwizzleR_MethodGroup
    class GetSwizzleR_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> FormatSwizzle:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> FormatSwizzle:...

    # Skipped HasAlphaChannel due to it being static, abstract and generic.

    HasAlphaChannel : HasAlphaChannel_MethodGroup
    class HasAlphaChannel_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped Is16BitPackedFormat due to it being static, abstract and generic.

    Is16BitPackedFormat : Is16BitPackedFormat_MethodGroup
    class Is16BitPackedFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsAlphaOnlyFormat due to it being static, abstract and generic.

    IsAlphaOnlyFormat : IsAlphaOnlyFormat_MethodGroup
    class IsAlphaOnlyFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsAlphaTestFormat due to it being static, abstract and generic.

    IsAlphaTestFormat : IsAlphaTestFormat_MethodGroup
    class IsAlphaTestFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsASTCFormat due to it being static, abstract and generic.

    IsASTCFormat : IsASTCFormat_MethodGroup
    class IsASTCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsBCFormat due to it being static, abstract and generic.

    IsBCFormat : IsBCFormat_MethodGroup
    class IsBCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsBPTCFormat due to it being static, abstract and generic.

    IsBPTCFormat : IsBPTCFormat_MethodGroup
    class IsBPTCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsCompressedFormat due to it being static, abstract and generic.

    IsCompressedFormat : IsCompressedFormat_MethodGroup
    class IsCompressedFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsDXTCFormat due to it being static, abstract and generic.

    IsDXTCFormat : IsDXTCFormat_MethodGroup
    class IsDXTCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsEACFormat due to it being static, abstract and generic.

    IsEACFormat : IsEACFormat_MethodGroup
    class IsEACFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsETCFormat due to it being static, abstract and generic.

    IsETCFormat : IsETCFormat_MethodGroup
    class IsETCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsHDRFormat due to it being static, abstract and generic.

    IsHDRFormat : IsHDRFormat_MethodGroup
    class IsHDRFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsPackedFormat due to it being static, abstract and generic.

    IsPackedFormat : IsPackedFormat_MethodGroup
    class IsPackedFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsPVRTCFormat due to it being static, abstract and generic.

    IsPVRTCFormat : IsPVRTCFormat_MethodGroup
    class IsPVRTCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsRGTCFormat due to it being static, abstract and generic.

    IsRGTCFormat : IsRGTCFormat_MethodGroup
    class IsRGTCFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsSignedFormat due to it being static, abstract and generic.

    IsSignedFormat : IsSignedFormat_MethodGroup
    class IsSignedFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsSwizzleFormat due to it being static, abstract and generic.

    IsSwizzleFormat : IsSwizzleFormat_MethodGroup
    class IsSwizzleFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...

    # Skipped IsUnsignedFormat due to it being static, abstract and generic.

    IsUnsignedFormat : IsUnsignedFormat_MethodGroup
    class IsUnsignedFormat_MethodGroup:
        @typing.overload
        def __call__(self, format: GraphicsFormat) -> bool:...
        @typing.overload
        def __call__(self, format: TextureFormat) -> bool:...



class GraphicsJobsSyncPoint(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    EndOfFrame : GraphicsJobsSyncPoint # 0
    AfterScriptUpdate : GraphicsJobsSyncPoint # 1
    AfterScriptLateUpdate : GraphicsJobsSyncPoint # 2
    WaitForPresent : GraphicsJobsSyncPoint # 3


class IScriptableRuntimeReflectionSystem(IDisposable, typing.Protocol):
    @abc.abstractmethod
    def TickRealtimeProbes(self) -> bool: ...


class RayTracingAccelerationStructure(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, settings: RayTracingAccelerationStructure.RASSettings) -> None: ...
    def ClearInstances(self) -> None: ...
    def CullInstances(self, cullingConfig: clr.Reference[RayTracingInstanceCullingConfig]) -> RayTracingInstanceCullingResults: ...
    def Dispose(self) -> None: ...
    def GetInstanceCount(self) -> int: ...
    def GetSize(self) -> int: ...
    def Release(self) -> None: ...
    def UpdateInstanceID(self, renderer: Renderer, instanceID: int) -> None: ...
    def UpdateInstanceMask(self, renderer: Renderer, mask: int) -> None: ...
    def UpdateInstancePropertyBlock(self, handle: int, properties: MaterialPropertyBlock) -> None: ...
    # Skipped AddInstance due to it being static, abstract and generic.

    AddInstance : AddInstance_MethodGroup
    class AddInstance_MethodGroup:
        @typing.overload
        def __call__(self, targetRenderer: Renderer, subMeshFlags: Array_1[RayTracingSubMeshFlags], enableTriangleCulling: bool = ..., frontTriangleCounterClockwise: bool = ..., mask: int = ..., id: int = ...) -> None:...
        @typing.overload
        def __call__(self, targetRenderer: Renderer, subMeshMask: Array_1[bool] = ..., subMeshTransparencyFlags: Array_1[bool] = ..., enableTriangleCulling: bool = ..., frontTriangleCounterClockwise: bool = ..., mask: int = ..., id: int = ...) -> None:...
        @typing.overload
        def __call__(self, aabbBuffer: GraphicsBuffer, numElements: int, material: Material, isCutOff: bool, enableTriangleCulling: bool = ..., frontTriangleCounterClockwise: bool = ..., mask: int = ..., reuseBounds: bool = ..., id: int = ...) -> None:...
        @typing.overload
        def __call__(self, aabbBuffer: GraphicsBuffer, aabbCount: int, dynamicData: bool, matrix: Matrix4x4, material: Material, opaqueMaterial: bool, properties: MaterialPropertyBlock, mask: int = ..., id: int = ...) -> int:...
        @typing.overload
        def __call__(self, aabbBuffer: GraphicsBuffer, numElements: int, material: Material, instanceTransform: Matrix4x4, isCutOff: bool, enableTriangleCulling: bool = ..., frontTriangleCounterClockwise: bool = ..., mask: int = ..., reuseBounds: bool = ..., id: int = ...) -> None:...

    # Skipped Build due to it being static, abstract and generic.

    Build : Build_MethodGroup
    class Build_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, relativeOrigin: Vector3) -> None:...

    # Skipped RemoveInstance due to it being static, abstract and generic.

    RemoveInstance : RemoveInstance_MethodGroup
    class RemoveInstance_MethodGroup:
        @typing.overload
        def __call__(self, handle: int) -> None:...
        @typing.overload
        def __call__(self, targetRenderer: Renderer) -> None:...

    # Skipped Update due to it being static, abstract and generic.

    Update : Update_MethodGroup
    class Update_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, relativeOrigin: Vector3) -> None:...

    # Skipped UpdateInstanceTransform due to it being static, abstract and generic.

    UpdateInstanceTransform : UpdateInstanceTransform_MethodGroup
    class UpdateInstanceTransform_MethodGroup:
        @typing.overload
        def __call__(self, renderer: Renderer) -> None:...
        @typing.overload
        def __call__(self, handle: int, matrix: Matrix4x4) -> None:...


    class ManagementMode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Manual : RayTracingAccelerationStructure.ManagementMode # 0
        Automatic : RayTracingAccelerationStructure.ManagementMode # 1


    class RASSettings:
        def __init__(self, sceneManagementMode: RayTracingAccelerationStructure.ManagementMode, rayTracingModeMask: RayTracingAccelerationStructure.RayTracingModeMask, layerMask: int) -> None: ...
        layerMask : int
        managementMode : RayTracingAccelerationStructure.ManagementMode
        rayTracingModeMask : RayTracingAccelerationStructure.RayTracingModeMask


    class RayTracingModeMask(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Nothing : RayTracingAccelerationStructure.RayTracingModeMask # 0
        Static : RayTracingAccelerationStructure.RayTracingModeMask # 2
        DynamicTransform : RayTracingAccelerationStructure.RayTracingModeMask # 4
        DynamicGeometry : RayTracingAccelerationStructure.RayTracingModeMask # 8
        Everything : RayTracingAccelerationStructure.RayTracingModeMask # 14



class RayTracingInstanceCullingConfig:
    alphaTestedMaterialConfig : RayTracingInstanceMaterialConfig
    flags : RayTracingInstanceCullingFlags
    instanceTests : Array_1[RayTracingInstanceCullingTest]
    lodParameters : LODParameters
    materialTest : RayTracingInstanceCullingMaterialTest
    planes : Array_1[Plane]
    sphereCenter : Vector3
    sphereRadius : float
    subMeshFlagsConfig : RayTracingSubMeshFlagsConfig
    transparentMaterialConfig : RayTracingInstanceMaterialConfig
    triangleCullingConfig : RayTracingInstanceTriangleCullingConfig


class RayTracingInstanceCullingFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : RayTracingInstanceCullingFlags # 0
    EnableSphereCulling : RayTracingInstanceCullingFlags # 1
    EnablePlaneCulling : RayTracingInstanceCullingFlags # 2
    EnableLODCulling : RayTracingInstanceCullingFlags # 4
    ComputeMaterialsCRC : RayTracingInstanceCullingFlags # 8
    IgnoreReflectionProbes : RayTracingInstanceCullingFlags # 16


class RayTracingInstanceCullingMaterialTest:
    deniedShaderPasses : Array_1[str]
    requiredShaderTags : Array_1[RayTracingInstanceCullingShaderTagConfig]


class RayTracingInstanceCullingResults:
    materialsCRC : Array_1[RayTracingInstanceMaterialCRC]
    transformsChanged : bool


class RayTracingInstanceCullingShaderTagConfig:
    tagId : ShaderTagId
    tagValueId : ShaderTagId


class RayTracingInstanceCullingTest:
    allowAlphaTestedMaterials : bool
    allowOpaqueMaterials : bool
    allowTransparentMaterials : bool
    instanceMask : int
    layerMask : int
    shadowCastingModeMask : int


class RayTracingInstanceMaterialConfig:
    optionalShaderKeywords : Array_1[str]
    optionalShaderTags : Array_1[RayTracingInstanceCullingShaderTagConfig]
    renderQueueLowerBound : int
    renderQueueUpperBound : int


class RayTracingInstanceMaterialCRC:
    crc : int
    instanceID : int


class RayTracingInstanceTriangleCullingConfig:
    checkDoubleSidedGIMaterial : bool
    forceDoubleSided : bool
    frontTriangleCounterClockwise : bool
    optionalDoubleSidedShaderKeywords : Array_1[str]


class RayTracingMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Off : RayTracingMode # 0
    Static : RayTracingMode # 1
    DynamicTransform : RayTracingMode # 2
    DynamicGeometry : RayTracingMode # 3


class RayTracingShader(Object):
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def maxRecursionDepth(self) -> float: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    def Dispatch(self, rayGenFunctionName: str, width: int, height: int, depth: int, camera: Camera = ...) -> None: ...
    def SetShaderPass(self, passName: str) -> None: ...
    # Skipped SetAccelerationStructure due to it being static, abstract and generic.

    SetAccelerationStructure : SetAccelerationStructure_MethodGroup
    class SetAccelerationStructure_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, accelerationStructure: RayTracingAccelerationStructure) -> None:...
        @typing.overload
        def __call__(self, name: str, accelerationStructure: RayTracingAccelerationStructure) -> None:...

    # Skipped SetBool due to it being static, abstract and generic.

    SetBool : SetBool_MethodGroup
    class SetBool_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, val: bool) -> None:...
        @typing.overload
        def __call__(self, name: str, val: bool) -> None:...

    # Skipped SetBuffer due to it being static, abstract and generic.

    SetBuffer : SetBuffer_MethodGroup
    class SetBuffer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, buffer: ComputeBuffer) -> None:...
        @typing.overload
        def __call__(self, nameID: int, buffer: GraphicsBuffer) -> None:...
        @typing.overload
        def __call__(self, name: str, buffer: ComputeBuffer) -> None:...
        @typing.overload
        def __call__(self, name: str, buffer: GraphicsBuffer) -> None:...

    # Skipped SetConstantBuffer due to it being static, abstract and generic.

    SetConstantBuffer : SetConstantBuffer_MethodGroup
    class SetConstantBuffer_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, buffer: ComputeBuffer, offset: int, size: int) -> None:...
        @typing.overload
        def __call__(self, nameID: int, buffer: GraphicsBuffer, offset: int, size: int) -> None:...
        @typing.overload
        def __call__(self, name: str, buffer: ComputeBuffer, offset: int, size: int) -> None:...
        @typing.overload
        def __call__(self, name: str, buffer: GraphicsBuffer, offset: int, size: int) -> None:...

    # Skipped SetFloat due to it being static, abstract and generic.

    SetFloat : SetFloat_MethodGroup
    class SetFloat_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, val: float) -> None:...
        @typing.overload
        def __call__(self, name: str, val: float) -> None:...

    # Skipped SetFloats due to it being static, abstract and generic.

    SetFloats : SetFloats_MethodGroup
    class SetFloats_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, values: Array_1[float]) -> None:...
        @typing.overload
        def __call__(self, name: str, values: Array_1[float]) -> None:...

    # Skipped SetInt due to it being static, abstract and generic.

    SetInt : SetInt_MethodGroup
    class SetInt_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, val: int) -> None:...
        @typing.overload
        def __call__(self, name: str, val: int) -> None:...

    # Skipped SetInts due to it being static, abstract and generic.

    SetInts : SetInts_MethodGroup
    class SetInts_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, values: Array_1[int]) -> None:...
        @typing.overload
        def __call__(self, name: str, values: Array_1[int]) -> None:...

    # Skipped SetMatrix due to it being static, abstract and generic.

    SetMatrix : SetMatrix_MethodGroup
    class SetMatrix_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, val: Matrix4x4) -> None:...
        @typing.overload
        def __call__(self, name: str, val: Matrix4x4) -> None:...

    # Skipped SetMatrixArray due to it being static, abstract and generic.

    SetMatrixArray : SetMatrixArray_MethodGroup
    class SetMatrixArray_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, values: Array_1[Matrix4x4]) -> None:...
        @typing.overload
        def __call__(self, name: str, values: Array_1[Matrix4x4]) -> None:...

    # Skipped SetTexture due to it being static, abstract and generic.

    SetTexture : SetTexture_MethodGroup
    class SetTexture_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, texture: Texture) -> None:...
        @typing.overload
        def __call__(self, name: str, texture: Texture) -> None:...

    # Skipped SetTextureFromGlobal due to it being static, abstract and generic.

    SetTextureFromGlobal : SetTextureFromGlobal_MethodGroup
    class SetTextureFromGlobal_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, globalTextureNameID: int) -> None:...
        @typing.overload
        def __call__(self, name: str, globalTextureName: str) -> None:...

    # Skipped SetVector due to it being static, abstract and generic.

    SetVector : SetVector_MethodGroup
    class SetVector_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, val: Vector4) -> None:...
        @typing.overload
        def __call__(self, name: str, val: Vector4) -> None:...

    # Skipped SetVectorArray due to it being static, abstract and generic.

    SetVectorArray : SetVectorArray_MethodGroup
    class SetVectorArray_MethodGroup:
        @typing.overload
        def __call__(self, nameID: int, values: Array_1[Vector4]) -> None:...
        @typing.overload
        def __call__(self, name: str, values: Array_1[Vector4]) -> None:...



class RayTracingSubMeshFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Disabled : RayTracingSubMeshFlags # 0
    Enabled : RayTracingSubMeshFlags # 1
    ClosestHitOnly : RayTracingSubMeshFlags # 2
    UniqueAnyHitCalls : RayTracingSubMeshFlags # 4


class RayTracingSubMeshFlagsConfig:
    alphaTestedMaterials : RayTracingSubMeshFlags
    opaqueMaterials : RayTracingSubMeshFlags
    transparentMaterials : RayTracingSubMeshFlags


class ScriptableRuntimeReflectionSystem(IScriptableRuntimeReflectionSystem, abc.ABC):
    def TickRealtimeProbes(self) -> bool: ...


class ScriptableRuntimeReflectionSystemSettings(abc.ABC):
    @classmethod
    @property
    def system(cls) -> IScriptableRuntimeReflectionSystem: ...
    @classmethod
    @system.setter
    def system(cls, value: IScriptableRuntimeReflectionSystem) -> IScriptableRuntimeReflectionSystem: ...


class ShaderWarmup(abc.ABC):
    @staticmethod
    def WarmupShader(shader: Shader, setup: ShaderWarmupSetup) -> None: ...
    @staticmethod
    def WarmupShaderFromCollection(collection: ShaderVariantCollection, shader: Shader, setup: ShaderWarmupSetup) -> None: ...


class ShaderWarmupSetup:
    vdecl : Array_1[VertexAttributeDescriptor]


class TextureCreationFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : TextureCreationFlags # 0
    MipChain : TextureCreationFlags # 1
    DontInitializePixels : TextureCreationFlags # 4
    Crunch : TextureCreationFlags # 64
    DontUploadUponCreate : TextureCreationFlags # 1024
    IgnoreMipmapLimit : TextureCreationFlags # 2048


class WaitForPresentSyncPoint(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    BeginFrame : WaitForPresentSyncPoint # 0
    EndFrame : WaitForPresentSyncPoint # 1

