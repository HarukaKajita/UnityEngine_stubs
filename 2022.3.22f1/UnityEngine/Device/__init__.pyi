import typing, clr, abc
import UnityEngine
from UnityEngine import ThreadPriority, ApplicationInstallMode, NetworkReachability, RuntimePlatform, ApplicationSandboxType, SystemLanguage, StackTraceLogType, LogType, UserAuthorization, Object, AsyncOperation, Resolution, Rect, FullScreenMode, DisplayInfo, Vector2Int, ScreenOrientation, RefreshRate, BatteryStatus, DeviceType, HDRDisplaySupportFlags, NPOTSupport, OperatingSystemFamily, RenderTextureDescriptor, RenderTextureFormat, TextureFormat
from System.Threading import CancellationToken
from System import Array_1
from System.Collections.Generic import List_1
from UnityEngine.Rendering import CopyTextureSupport, FoveatedRenderingCaps, GraphicsDeviceType, RenderingThreadingMode, VertexAttributeFormat
from UnityEngine.Experimental.Rendering import GraphicsFormat, FormatUsage, DefaultFormat

class Application(abc.ABC):
    @classmethod
    @property
    def absoluteURL(cls) -> str: ...
    @classmethod
    @property
    def backgroundLoadingPriority(cls) -> ThreadPriority: ...
    @classmethod
    @backgroundLoadingPriority.setter
    def backgroundLoadingPriority(cls, value: ThreadPriority) -> ThreadPriority: ...
    @classmethod
    @property
    def buildGUID(cls) -> str: ...
    @classmethod
    @property
    def cloudProjectId(cls) -> str: ...
    @classmethod
    @property
    def companyName(cls) -> str: ...
    @classmethod
    @property
    def consoleLogPath(cls) -> str: ...
    @classmethod
    @property
    def dataPath(cls) -> str: ...
    @classmethod
    @property
    def exitCancellationToken(cls) -> CancellationToken: ...
    @classmethod
    @property
    def genuine(cls) -> bool: ...
    @classmethod
    @property
    def genuineCheckAvailable(cls) -> bool: ...
    @classmethod
    @property
    def identifier(cls) -> str: ...
    @classmethod
    @property
    def installerName(cls) -> str: ...
    @classmethod
    @property
    def installMode(cls) -> ApplicationInstallMode: ...
    @classmethod
    @property
    def internetReachability(cls) -> NetworkReachability: ...
    @classmethod
    @property
    def isBatchMode(cls) -> bool: ...
    @classmethod
    @property
    def isConsolePlatform(cls) -> bool: ...
    @classmethod
    @property
    def isEditor(cls) -> bool: ...
    @classmethod
    @property
    def isFocused(cls) -> bool: ...
    @classmethod
    @property
    def isMobilePlatform(cls) -> bool: ...
    @classmethod
    @property
    def isPlaying(cls) -> bool: ...
    @classmethod
    @property
    def persistentDataPath(cls) -> str: ...
    @classmethod
    @property
    def platform(cls) -> RuntimePlatform: ...
    @classmethod
    @property
    def productName(cls) -> str: ...
    @classmethod
    @property
    def runInBackground(cls) -> bool: ...
    @classmethod
    @runInBackground.setter
    def runInBackground(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def sandboxType(cls) -> ApplicationSandboxType: ...
    @classmethod
    @property
    def streamingAssetsPath(cls) -> str: ...
    @classmethod
    @property
    def systemLanguage(cls) -> SystemLanguage: ...
    @classmethod
    @property
    def targetFrameRate(cls) -> int: ...
    @classmethod
    @targetFrameRate.setter
    def targetFrameRate(cls, value: int) -> int: ...
    @classmethod
    @property
    def temporaryCachePath(cls) -> str: ...
    @classmethod
    @property
    def unityVersion(cls) -> str: ...
    @classmethod
    @property
    def version(cls) -> str: ...
    @staticmethod
    def GetBuildTags() -> Array_1[str]: ...
    @staticmethod
    def GetStackTraceLogType(logType: LogType) -> StackTraceLogType: ...
    @staticmethod
    def HasProLicense() -> bool: ...
    @staticmethod
    def HasUserAuthorization(mode: UserAuthorization) -> bool: ...
    @staticmethod
    def IsPlaying(obj: Object) -> bool: ...
    @staticmethod
    def OpenURL(url: str) -> None: ...
    @staticmethod
    def RequestAdvertisingIdentifierAsync(delegateMethod: UnityEngine.Application.AdvertisingIdentifierCallback) -> bool: ...
    @staticmethod
    def RequestUserAuthorization(mode: UserAuthorization) -> AsyncOperation: ...
    @staticmethod
    def SetBuildTags(buildTags: Array_1[str]) -> None: ...
    @staticmethod
    def SetStackTraceLogType(logType: LogType, stackTraceType: StackTraceLogType) -> None: ...
    @staticmethod
    def Unload() -> None: ...
    # Skipped CanStreamedLevelBeLoaded due to it being static, abstract and generic.

    CanStreamedLevelBeLoaded : CanStreamedLevelBeLoaded_MethodGroup
    class CanStreamedLevelBeLoaded_MethodGroup:
        @typing.overload
        def __call__(self, levelIndex: int) -> bool:...
        @typing.overload
        def __call__(self, levelName: str) -> bool:...

    # Skipped Quit due to it being static, abstract and generic.

    Quit : Quit_MethodGroup
    class Quit_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, exitCode: int) -> None:...



class Screen(abc.ABC):
    @classmethod
    @property
    def autorotateToLandscapeLeft(cls) -> bool: ...
    @classmethod
    @autorotateToLandscapeLeft.setter
    def autorotateToLandscapeLeft(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def autorotateToLandscapeRight(cls) -> bool: ...
    @classmethod
    @autorotateToLandscapeRight.setter
    def autorotateToLandscapeRight(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def autorotateToPortrait(cls) -> bool: ...
    @classmethod
    @autorotateToPortrait.setter
    def autorotateToPortrait(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def autorotateToPortraitUpsideDown(cls) -> bool: ...
    @classmethod
    @autorotateToPortraitUpsideDown.setter
    def autorotateToPortraitUpsideDown(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def brightness(cls) -> float: ...
    @classmethod
    @brightness.setter
    def brightness(cls, value: float) -> float: ...
    @classmethod
    @property
    def currentResolution(cls) -> Resolution: ...
    @classmethod
    @property
    def cutouts(cls) -> Array_1[Rect]: ...
    @classmethod
    @property
    def dpi(cls) -> float: ...
    @classmethod
    @property
    def fullScreen(cls) -> bool: ...
    @classmethod
    @fullScreen.setter
    def fullScreen(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def fullScreenMode(cls) -> FullScreenMode: ...
    @classmethod
    @fullScreenMode.setter
    def fullScreenMode(cls, value: FullScreenMode) -> FullScreenMode: ...
    @classmethod
    @property
    def height(cls) -> int: ...
    @classmethod
    @property
    def mainWindowDisplayInfo(cls) -> DisplayInfo: ...
    @classmethod
    @property
    def mainWindowPosition(cls) -> Vector2Int: ...
    @classmethod
    @property
    def orientation(cls) -> ScreenOrientation: ...
    @classmethod
    @orientation.setter
    def orientation(cls, value: ScreenOrientation) -> ScreenOrientation: ...
    @classmethod
    @property
    def resolutions(cls) -> Array_1[Resolution]: ...
    @classmethod
    @property
    def safeArea(cls) -> Rect: ...
    @classmethod
    @property
    def sleepTimeout(cls) -> int: ...
    @classmethod
    @sleepTimeout.setter
    def sleepTimeout(cls, value: int) -> int: ...
    @classmethod
    @property
    def width(cls) -> int: ...
    @staticmethod
    def GetDisplayLayout(displayLayout: List_1[DisplayInfo]) -> None: ...
    @staticmethod
    def MoveMainWindowTo(display: clr.Reference[DisplayInfo], position: Vector2Int) -> AsyncOperation: ...
    # Skipped SetResolution due to it being static, abstract and generic.

    SetResolution : SetResolution_MethodGroup
    class SetResolution_MethodGroup:
        @typing.overload
        def __call__(self, width: int, height: int, fullscreenMode: FullScreenMode) -> None:...
        @typing.overload
        def __call__(self, width: int, height: int, fullscreen: bool) -> None:...
        @typing.overload
        def __call__(self, width: int, height: int, fullscreenMode: FullScreenMode, preferredRefreshRate: int) -> None:...
        @typing.overload
        def __call__(self, width: int, height: int, fullscreenMode: FullScreenMode, preferredRefreshRate: RefreshRate) -> None:...
        @typing.overload
        def __call__(self, width: int, height: int, fullscreen: bool, preferredRefreshRate: int) -> None:...



class SystemInfo(abc.ABC):
    unsupportedIdentifier : str
    @classmethod
    @property
    def batteryLevel(cls) -> float: ...
    @classmethod
    @property
    def batteryStatus(cls) -> BatteryStatus: ...
    @classmethod
    @property
    def computeSubGroupSize(cls) -> int: ...
    @classmethod
    @property
    def constantBufferOffsetAlignment(cls) -> int: ...
    @classmethod
    @property
    def copyTextureSupport(cls) -> CopyTextureSupport: ...
    @classmethod
    @property
    def deviceModel(cls) -> str: ...
    @classmethod
    @property
    def deviceName(cls) -> str: ...
    @classmethod
    @property
    def deviceType(cls) -> DeviceType: ...
    @classmethod
    @property
    def deviceUniqueIdentifier(cls) -> str: ...
    @classmethod
    @property
    def foveatedRenderingCaps(cls) -> FoveatedRenderingCaps: ...
    @classmethod
    @property
    def graphicsDeviceID(cls) -> int: ...
    @classmethod
    @property
    def graphicsDeviceName(cls) -> str: ...
    @classmethod
    @property
    def graphicsDeviceType(cls) -> GraphicsDeviceType: ...
    @classmethod
    @property
    def graphicsDeviceVendor(cls) -> str: ...
    @classmethod
    @property
    def graphicsDeviceVendorID(cls) -> int: ...
    @classmethod
    @property
    def graphicsDeviceVersion(cls) -> str: ...
    @classmethod
    @property
    def graphicsMemorySize(cls) -> int: ...
    @classmethod
    @property
    def graphicsMultiThreaded(cls) -> bool: ...
    @classmethod
    @property
    def graphicsShaderLevel(cls) -> int: ...
    @classmethod
    @property
    def graphicsUVStartsAtTop(cls) -> bool: ...
    @classmethod
    @property
    def hasDynamicUniformArrayIndexingInFragmentShaders(cls) -> bool: ...
    @classmethod
    @property
    def hasHiddenSurfaceRemovalOnGPU(cls) -> bool: ...
    @classmethod
    @property
    def hasMipMaxLevel(cls) -> bool: ...
    @classmethod
    @property
    def hdrDisplaySupportFlags(cls) -> HDRDisplaySupportFlags: ...
    @classmethod
    @property
    def maxComputeBufferInputsCompute(cls) -> int: ...
    @classmethod
    @property
    def maxComputeBufferInputsDomain(cls) -> int: ...
    @classmethod
    @property
    def maxComputeBufferInputsFragment(cls) -> int: ...
    @classmethod
    @property
    def maxComputeBufferInputsGeometry(cls) -> int: ...
    @classmethod
    @property
    def maxComputeBufferInputsHull(cls) -> int: ...
    @classmethod
    @property
    def maxComputeBufferInputsVertex(cls) -> int: ...
    @classmethod
    @property
    def maxComputeWorkGroupSize(cls) -> int: ...
    @classmethod
    @property
    def maxComputeWorkGroupSizeX(cls) -> int: ...
    @classmethod
    @property
    def maxComputeWorkGroupSizeY(cls) -> int: ...
    @classmethod
    @property
    def maxComputeWorkGroupSizeZ(cls) -> int: ...
    @classmethod
    @property
    def maxConstantBufferSize(cls) -> int: ...
    @classmethod
    @property
    def maxCubemapSize(cls) -> int: ...
    @classmethod
    @property
    def maxGraphicsBufferSize(cls) -> int: ...
    @classmethod
    @property
    def maxTexture3DSize(cls) -> int: ...
    @classmethod
    @property
    def maxTextureArraySlices(cls) -> int: ...
    @classmethod
    @property
    def maxTextureSize(cls) -> int: ...
    @classmethod
    @property
    def npotSupport(cls) -> NPOTSupport: ...
    @classmethod
    @property
    def operatingSystem(cls) -> str: ...
    @classmethod
    @property
    def operatingSystemFamily(cls) -> OperatingSystemFamily: ...
    @classmethod
    @property
    def processorCount(cls) -> int: ...
    @classmethod
    @property
    def processorFrequency(cls) -> int: ...
    @classmethod
    @property
    def processorType(cls) -> str: ...
    @classmethod
    @property
    def renderingThreadingMode(cls) -> RenderingThreadingMode: ...
    @classmethod
    @property
    def supportedRandomWriteTargetCount(cls) -> int: ...
    @classmethod
    @property
    def supportedRenderTargetCount(cls) -> int: ...
    @classmethod
    @property
    def supports2DArrayTextures(cls) -> bool: ...
    @classmethod
    @property
    def supports32bitsIndexBuffer(cls) -> bool: ...
    @classmethod
    @property
    def supports3DRenderTextures(cls) -> bool: ...
    @classmethod
    @property
    def supports3DTextures(cls) -> bool: ...
    @classmethod
    @property
    def supportsAccelerometer(cls) -> bool: ...
    @classmethod
    @property
    def supportsAsyncCompute(cls) -> bool: ...
    @classmethod
    @property
    def supportsAsyncGPUReadback(cls) -> bool: ...
    @classmethod
    @property
    def supportsAudio(cls) -> bool: ...
    @classmethod
    @property
    def supportsCompressed3DTextures(cls) -> bool: ...
    @classmethod
    @property
    def supportsComputeShaders(cls) -> bool: ...
    @classmethod
    @property
    def supportsConservativeRaster(cls) -> bool: ...
    @classmethod
    @property
    def supportsCubemapArrayTextures(cls) -> bool: ...
    @classmethod
    @property
    def supportsGeometryShaders(cls) -> bool: ...
    @classmethod
    @property
    def supportsGpuRecorder(cls) -> bool: ...
    @classmethod
    @property
    def supportsGraphicsFence(cls) -> bool: ...
    @classmethod
    @property
    def supportsGyroscope(cls) -> bool: ...
    @classmethod
    @property
    def supportsHardwareQuadTopology(cls) -> bool: ...
    @classmethod
    @property
    def supportsIndirectArgumentsBuffer(cls) -> bool: ...
    @classmethod
    @property
    def supportsInstancing(cls) -> bool: ...
    @classmethod
    @property
    def supportsLocationService(cls) -> bool: ...
    @classmethod
    @property
    def supportsMipStreaming(cls) -> bool: ...
    @classmethod
    @property
    def supportsMotionVectors(cls) -> bool: ...
    @classmethod
    @property
    def supportsMultisampleAutoResolve(cls) -> bool: ...
    @classmethod
    @property
    def supportsMultisampled2DArrayTextures(cls) -> bool: ...
    @classmethod
    @property
    def supportsMultisampledTextures(cls) -> int: ...
    @classmethod
    @property
    def supportsMultisampleResolveDepth(cls) -> bool: ...
    @classmethod
    @property
    def supportsMultisampleResolveStencil(cls) -> bool: ...
    @classmethod
    @property
    def supportsMultiview(cls) -> bool: ...
    @classmethod
    @property
    def supportsRawShadowDepthSampling(cls) -> bool: ...
    @classmethod
    @property
    def supportsRayTracing(cls) -> bool: ...
    @classmethod
    @property
    def supportsRenderTargetArrayIndexFromVertexShader(cls) -> bool: ...
    @classmethod
    @property
    def supportsSeparatedRenderTargetsBlend(cls) -> bool: ...
    @classmethod
    @property
    def supportsSetConstantBuffer(cls) -> bool: ...
    @classmethod
    @property
    def supportsShadows(cls) -> bool: ...
    @classmethod
    @property
    def supportsSparseTextures(cls) -> bool: ...
    @classmethod
    @property
    def supportsStoreAndResolveAction(cls) -> bool: ...
    @classmethod
    @property
    def supportsTessellationShaders(cls) -> bool: ...
    @classmethod
    @property
    def supportsTextureWrapMirrorOnce(cls) -> int: ...
    @classmethod
    @property
    def supportsVibration(cls) -> bool: ...
    @classmethod
    @property
    def systemMemorySize(cls) -> int: ...
    @classmethod
    @property
    def usesLoadStoreActions(cls) -> bool: ...
    @classmethod
    @property
    def usesReversedZBuffer(cls) -> bool: ...
    @staticmethod
    def GetCompatibleFormat(format: GraphicsFormat, usage: FormatUsage) -> GraphicsFormat: ...
    @staticmethod
    def GetGraphicsFormat(format: DefaultFormat) -> GraphicsFormat: ...
    @staticmethod
    def GetRenderTextureSupportedMSAASampleCount(desc: RenderTextureDescriptor) -> int: ...
    @staticmethod
    def IsFormatSupported(format: GraphicsFormat, usage: FormatUsage) -> bool: ...
    @staticmethod
    def SupportsBlendingOnRenderTextureFormat(format: RenderTextureFormat) -> bool: ...
    @staticmethod
    def SupportsRandomWriteOnRenderTextureFormat(format: RenderTextureFormat) -> bool: ...
    @staticmethod
    def SupportsRenderTextureFormat(format: RenderTextureFormat) -> bool: ...
    @staticmethod
    def SupportsTextureFormat(format: TextureFormat) -> bool: ...
    @staticmethod
    def SupportsVertexAttributeFormat(format: VertexAttributeFormat, dimension: int) -> bool: ...

