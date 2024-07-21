import typing, clr, abc
from UnityEngine import Material, Texture, MaterialPropertyBlock, Rect
from System import Array_1, Guid, IDisposable, IEquatable_1
from UnityEngine.Experimental.Rendering import GraphicsFormat
from Unity.Collections import NativeArray_1, NativeSlice_1
from UnityEngine.Rendering import RenderTargetIdentifier, CommandBuffer

class Debugging(abc.ABC):
    @classmethod
    @property
    def debugTilesEnabled(cls) -> bool: ...
    @classmethod
    @debugTilesEnabled.setter
    def debugTilesEnabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def flushEveryTickEnabled(cls) -> bool: ...
    @classmethod
    @flushEveryTickEnabled.setter
    def flushEveryTickEnabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def mipPreloadedTextureCount(cls) -> int: ...
    @classmethod
    @property
    def resolvingEnabled(cls) -> bool: ...
    @classmethod
    @resolvingEnabled.setter
    def resolvingEnabled(cls, value: bool) -> bool: ...
    @staticmethod
    def GetInfoDump() -> str: ...
    @staticmethod
    def GetNumHandles() -> int: ...
    @staticmethod
    def GrabHandleInfo(debugHandle: clr.Reference[Debugging.Handle], index: int) -> None: ...

    class Handle:
        group : str
        handle : int
        material : Material
        name : str
        numLayers : int



class EditorHelpers(abc.ABC):
    @staticmethod
    def QuerySupportedFormats() -> Array_1[GraphicsFormat]: ...
    @staticmethod
    def ValidateTextureStack(textures: Array_1[Texture], errorMessage: clr.Reference[str]) -> bool: ...


class FilterMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Bilinear : FilterMode # 1
    Trilinear : FilterMode # 2


class GPUCacheSetting:
    format : GraphicsFormat
    sizeInMegaBytes : int


class Procedural(abc.ABC):
    @staticmethod
    def GetCPUCacheSize() -> int: ...
    @staticmethod
    def GetGPUCacheSettings() -> Array_1[GPUCacheSetting]: ...
    @staticmethod
    def GetGPUCacheStagingAreaCapacity() -> int: ...
    @staticmethod
    def SetCPUCacheSize(sizeInMegabytes: int) -> None: ...
    @staticmethod
    def SetDebugFlagDouble(guid: Guid, value: float) -> None: ...
    @staticmethod
    def SetDebugFlagInteger(guid: Guid, value: int) -> None: ...
    @staticmethod
    def SetGPUCacheSettings(cacheSettings: Array_1[GPUCacheSetting]) -> None: ...
    @staticmethod
    def SetGPUCacheStagingAreaCapacity(tilesPerFrame: int) -> None: ...

    class CPUTextureStack(Procedural.TextureStackBase_1[Procedural.CPUTextureStackRequestParameters]):
        def __init__(self, _name: str, creationParams: Procedural.CreationParameters) -> None: ...


    class CPUTextureStackRequestLayerParameters:
        @property
        def mipScanlineSize(self) -> int: ...
        @property
        def requiresCachedMip(self) -> bool: ...
        @property
        def scanlineSize(self) -> int: ...
        # Skipped GetData due to it being static, abstract and generic.

        GetData : GetData_MethodGroup
        class GetData_MethodGroup:
            def __getitem__(self, t:typing.Type[GetData_1_T1]) -> GetData_1[GetData_1_T1]: ...

            GetData_1_T1 = typing.TypeVar('GetData_1_T1')
            class GetData_1(typing.Generic[GetData_1_T1]):
                GetData_1_T = Procedural.CPUTextureStackRequestLayerParameters.GetData_MethodGroup.GetData_1_T1
                def __call__(self) -> NativeArray_1[GetData_1_T]:...


        # Skipped GetMipData due to it being static, abstract and generic.

        GetMipData : GetMipData_MethodGroup
        class GetMipData_MethodGroup:
            def __getitem__(self, t:typing.Type[GetMipData_1_T1]) -> GetMipData_1[GetMipData_1_T1]: ...

            GetMipData_1_T1 = typing.TypeVar('GetMipData_1_T1')
            class GetMipData_1(typing.Generic[GetMipData_1_T1]):
                GetMipData_1_T = Procedural.CPUTextureStackRequestLayerParameters.GetMipData_MethodGroup.GetMipData_1_T1
                def __call__(self) -> NativeArray_1[GetMipData_1_T]:...




    class CPUTextureStackRequestParameters:
        height : int
        level : int
        numLayers : int
        width : int
        x : int
        y : int
        def GetLayer(self, index: int) -> Procedural.CPUTextureStackRequestLayerParameters: ...


    class CreationParameters:
        filterMode : FilterMode
        height : int
        layers : Array_1[GraphicsFormat]
        maxActiveRequests : int
        MaxNumLayers : int
        MaxRequestsPerFrameSupported : int
        tilesize : int
        width : int


    class GPUTextureStack(Procedural.TextureStackBase_1[Procedural.GPUTextureStackRequestParameters]):
        def __init__(self, _name: str, creationParams: Procedural.CreationParameters) -> None: ...


    class GPUTextureStackRequestLayerParameters:
        dest : RenderTargetIdentifier
        destX : int
        destY : int
        def GetHeight(self) -> int: ...
        def GetWidth(self) -> int: ...


    class GPUTextureStackRequestParameters:
        height : int
        level : int
        numLayers : int
        width : int
        x : int
        y : int
        def GetLayer(self, index: int) -> Procedural.GPUTextureStackRequestLayerParameters: ...


    class RequestStatus(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Generated : Procedural.RequestStatus # 65538
        Dropped : Procedural.RequestStatus # 65539


    class TextureStackBase_GenericClasses(abc.ABCMeta):
        Generic_TextureStackBase_GenericClasses_TextureStackBase_1_T = typing.TypeVar('Generic_TextureStackBase_GenericClasses_TextureStackBase_1_T')
        def __getitem__(self, types : typing.Type[Generic_TextureStackBase_GenericClasses_TextureStackBase_1_T]) -> typing.Type[Procedural.TextureStackBase_1[Generic_TextureStackBase_GenericClasses_TextureStackBase_1_T]]: ...

    TextureStackBase : TextureStackBase_GenericClasses

    TextureStackBase_1_T = typing.TypeVar('TextureStackBase_1_T')
    class TextureStackBase_1(typing.Generic[TextureStackBase_1_T], IDisposable):
        TextureStackBase_1_T = Procedural.TextureStackBase_1_T
        def __init__(self, _name: str, _creationParams: Procedural.CreationParameters, gpuGeneration: bool) -> None: ...
        AllMips : int
        borderSize : int
        def BindGlobally(self) -> None: ...
        def BindToMaterial(self, mat: Material) -> None: ...
        def BindToMaterialPropertyBlock(self, mpb: MaterialPropertyBlock) -> None: ...
        def Dispose(self) -> None: ...
        def EvictRegion(self, r: Rect, mipMap: int, numMips: int) -> None: ...
        def InvalidateRegion(self, r: Rect, mipMap: int, numMips: int) -> None: ...
        def IsValid(self) -> bool: ...
        def PopRequests(self, requestHandles: NativeSlice_1[Procedural.TextureStackRequestHandle_1[TextureStackBase_1_T]]) -> int: ...
        def RequestRegion(self, r: Rect, mipMap: int, numMips: int) -> None: ...


    class TextureStackRequestHandle_GenericClasses(abc.ABCMeta):
        Generic_TextureStackRequestHandle_GenericClasses_TextureStackRequestHandle_1_T = typing.TypeVar('Generic_TextureStackRequestHandle_GenericClasses_TextureStackRequestHandle_1_T')
        def __getitem__(self, types : typing.Type[Generic_TextureStackRequestHandle_GenericClasses_TextureStackRequestHandle_1_T]) -> typing.Type[Procedural.TextureStackRequestHandle_1[Generic_TextureStackRequestHandle_GenericClasses_TextureStackRequestHandle_1_T]]: ...

    TextureStackRequestHandle : TextureStackRequestHandle_GenericClasses

    TextureStackRequestHandle_1_T = typing.TypeVar('TextureStackRequestHandle_1_T')
    class TextureStackRequestHandle_1(typing.Generic[TextureStackRequestHandle_1_T], IEquatable_1[Procedural.TextureStackRequestHandle_1[TextureStackRequestHandle_1_T]]):
        TextureStackRequestHandle_1_T = Procedural.TextureStackRequestHandle_1_T
        def GetHashCode(self) -> int: ...
        def __eq__(self, h1: Procedural.TextureStackRequestHandle_1[TextureStackRequestHandle_1_T], h2: Procedural.TextureStackRequestHandle_1[TextureStackRequestHandle_1_T]) -> bool: ...
        def __ne__(self, h1: Procedural.TextureStackRequestHandle_1[TextureStackRequestHandle_1_T], h2: Procedural.TextureStackRequestHandle_1[TextureStackRequestHandle_1_T]) -> bool: ...
        # Skipped CompleteRequest due to it being static, abstract and generic.

        CompleteRequest : CompleteRequest_MethodGroup[TextureStackRequestHandle_1_T]
        CompleteRequest_MethodGroup_TextureStackRequestHandle_1_T = typing.TypeVar('CompleteRequest_MethodGroup_TextureStackRequestHandle_1_T')
        class CompleteRequest_MethodGroup(typing.Generic[CompleteRequest_MethodGroup_TextureStackRequestHandle_1_T]):
            CompleteRequest_MethodGroup_TextureStackRequestHandle_1_T = Procedural.TextureStackRequestHandle_1.CompleteRequest_MethodGroup_TextureStackRequestHandle_1_T
            @typing.overload
            def __call__(self, status: Procedural.RequestStatus) -> None:...
            @typing.overload
            def __call__(self, status: Procedural.RequestStatus, fenceBuffer: CommandBuffer) -> None:...

        # Skipped CompleteRequests due to it being static, abstract and generic.

        CompleteRequests : CompleteRequests_MethodGroup[TextureStackRequestHandle_1_T]
        CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T = typing.TypeVar('CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T')
        class CompleteRequests_MethodGroup(typing.Generic[CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T]):
            CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T = Procedural.TextureStackRequestHandle_1.CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T
            @typing.overload
            def __call__(self, requestHandles: NativeSlice_1[Procedural.TextureStackRequestHandle_1[CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T]], status: NativeSlice_1[Procedural.RequestStatus]) -> None:...
            @typing.overload
            def __call__(self, requestHandles: NativeSlice_1[Procedural.TextureStackRequestHandle_1[CompleteRequests_MethodGroup_TextureStackRequestHandle_1_T]], status: NativeSlice_1[Procedural.RequestStatus], fenceBuffer: CommandBuffer) -> None:...

        # Skipped Equals due to it being static, abstract and generic.

        Equals : Equals_MethodGroup[TextureStackRequestHandle_1_T]
        Equals_MethodGroup_TextureStackRequestHandle_1_T = typing.TypeVar('Equals_MethodGroup_TextureStackRequestHandle_1_T')
        class Equals_MethodGroup(typing.Generic[Equals_MethodGroup_TextureStackRequestHandle_1_T]):
            Equals_MethodGroup_TextureStackRequestHandle_1_T = Procedural.TextureStackRequestHandle_1.Equals_MethodGroup_TextureStackRequestHandle_1_T
            @typing.overload
            def __call__(self, other: Procedural.TextureStackRequestHandle_1[Equals_MethodGroup_TextureStackRequestHandle_1_T]) -> bool:...
            @typing.overload
            def __call__(self, obj: typing.Any) -> bool:...

        # Skipped GetRequestParameters due to it being static, abstract and generic.

        GetRequestParameters : GetRequestParameters_MethodGroup[TextureStackRequestHandle_1_T]
        GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T = typing.TypeVar('GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T')
        class GetRequestParameters_MethodGroup(typing.Generic[GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T]):
            GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T = Procedural.TextureStackRequestHandle_1.GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T
            @typing.overload
            def __call__(self) -> GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T:...
            @typing.overload
            def __call__(self, handles: NativeSlice_1[Procedural.TextureStackRequestHandle_1[GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T]], requests: NativeSlice_1[GetRequestParameters_MethodGroup_TextureStackRequestHandle_1_T]) -> None:...




class Resolver(IDisposable):
    def __init__(self) -> None: ...
    @property
    def CurrentHeight(self) -> int: ...
    @CurrentHeight.setter
    def CurrentHeight(self, value: int) -> int: ...
    @property
    def CurrentWidth(self) -> int: ...
    @CurrentWidth.setter
    def CurrentWidth(self, value: int) -> int: ...
    def Dispose(self) -> None: ...
    def UpdateSize(self, width: int, height: int) -> None: ...
    # Skipped Process due to it being static, abstract and generic.

    Process : Process_MethodGroup
    class Process_MethodGroup:
        @typing.overload
        def __call__(self, cmd: CommandBuffer, rt: RenderTargetIdentifier) -> None:...
        @typing.overload
        def __call__(self, cmd: CommandBuffer, rt: RenderTargetIdentifier, x: int, width: int, y: int, height: int, mip: int, slice: int) -> None:...



class Streaming(abc.ABC):
    @staticmethod
    def EnableMipPreloading(texturesPerFrame: int, mipCount: int) -> None: ...
    @staticmethod
    def GetCPUCacheSize() -> int: ...
    @staticmethod
    def GetGPUCacheSettings() -> Array_1[GPUCacheSetting]: ...
    @staticmethod
    def GetTextureStackSize(mat: Material, stackNameId: int, width: clr.Reference[int], height: clr.Reference[int]) -> None: ...
    @staticmethod
    def RequestRegion(mat: Material, stackNameId: int, r: Rect, mipMap: int, numMips: int) -> None: ...
    @staticmethod
    def SetCPUCacheSize(sizeInMegabytes: int) -> None: ...
    @staticmethod
    def SetGPUCacheSettings(cacheSettings: Array_1[GPUCacheSetting]) -> None: ...


class System(abc.ABC):
    AllMips : int
    @staticmethod
    def Update() -> None: ...

