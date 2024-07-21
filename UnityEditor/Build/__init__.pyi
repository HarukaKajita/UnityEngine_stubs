import typing, abc
from System import Exception, Array_1, IComparable_1, IEquatable_1
from System.Collections import IDictionary
from System.Reflection import MethodBase
from UnityEditor import BuildPlayerOptions, BuildTarget, BuildOptions, BuildTargetGroup
from UnityEditor.Build.Reporting import BuildReport
from UnityEngine import ComputeShader, Shader
from System.Collections.Generic import IList_1
from UnityEditor.Rendering import ShaderCompilerData, ShaderSnippetData
from UnityEngine.SceneManagement import Scene
from UnityEditor.UnityLinker import UnityLinkerBuildPipelineData

class BuildFailedException(Exception):
    @typing.overload
    def __init__(self, innerException: Exception) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class BuildPlayerContext:
    @property
    def BuildPlayerOptions(self) -> BuildPlayerOptions: ...
    def AddAdditionalPathToStreamingAssets(self, directoryOrFile: str, pathInStreamingAssets: str = ...) -> None: ...


class BuildPlayerProcessor(IOrderedCallback, abc.ABC):
    @property
    def callbackOrder(self) -> int: ...
    @abc.abstractmethod
    def PrepareForBuild(self, buildPlayerContext: BuildPlayerContext) -> None: ...


class IActiveBuildTargetChanged(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnActiveBuildTargetChanged(self, previousTarget: BuildTarget, newTarget: BuildTarget) -> None: ...


class IFilterBuildAssemblies(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnFilterAssemblies(self, buildOptions: BuildOptions, assemblies: Array_1[str]) -> Array_1[str]: ...


class IIl2CppProcessor(IOrderedCallback, typing.Protocol):
    pass


class Il2CppCodeGeneration(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    OptimizeSpeed : Il2CppCodeGeneration # 0
    OptimizeSize : Il2CppCodeGeneration # 1


class IOrderedCallback(typing.Protocol):
    @property
    def callbackOrder(self) -> int: ...


class IPostBuildPlayerScriptDLLs(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPostBuildPlayerScriptDLLs(self, report: BuildReport) -> None: ...


class IPostprocessBuild(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPostprocessBuild(self, target: BuildTarget, path: str) -> None: ...


class IPostprocessBuildWithReport(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPostprocessBuild(self, report: BuildReport) -> None: ...


class IPreprocessBuild(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPreprocessBuild(self, target: BuildTarget, path: str) -> None: ...


class IPreprocessBuildWithReport(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPreprocessBuild(self, report: BuildReport) -> None: ...


class IPreprocessComputeShaders(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnProcessComputeShader(self, shader: ComputeShader, kernelName: str, data: IList_1[ShaderCompilerData]) -> None: ...


class IPreprocessShaders(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnProcessShader(self, shader: Shader, snippet: ShaderSnippetData, data: IList_1[ShaderCompilerData]) -> None: ...


class IProcessScene(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnProcessScene(self, scene: Scene) -> None: ...


class IProcessSceneWithReport(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnProcessScene(self, scene: Scene, report: BuildReport) -> None: ...


class IUnityLinkerProcessor(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def GenerateAdditionalLinkXmlFile(self, report: BuildReport, data: UnityLinkerBuildPipelineData) -> str: ...


class NamedBuildTarget(IComparable_1[NamedBuildTarget], IEquatable_1[NamedBuildTarget]):
    Android : NamedBuildTarget
    CloudRendering : NamedBuildTarget
    EmbeddedLinux : NamedBuildTarget
    iOS : NamedBuildTarget
    LinuxHeadlessSimulation : NamedBuildTarget
    NintendoSwitch : NamedBuildTarget
    PS4 : NamedBuildTarget
    QNX : NamedBuildTarget
    Server : NamedBuildTarget
    Stadia : NamedBuildTarget
    Standalone : NamedBuildTarget
    tvOS : NamedBuildTarget
    Unknown : NamedBuildTarget
    VisionOS : NamedBuildTarget
    WebGL : NamedBuildTarget
    WindowsStoreApps : NamedBuildTarget
    XboxOne : NamedBuildTarget
    @property
    def TargetName(self) -> str: ...
    def CompareTo(self, other: NamedBuildTarget) -> int: ...
    @staticmethod
    def FromBuildTargetGroup(buildTargetGroup: BuildTargetGroup) -> NamedBuildTarget: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, lhs: NamedBuildTarget, rhs: NamedBuildTarget) -> bool: ...
    def __ne__(self, lhs: NamedBuildTarget, rhs: NamedBuildTarget) -> bool: ...
    def ToBuildTargetGroup(self) -> BuildTargetGroup: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: NamedBuildTarget) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class OSArchitecture(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    x64 : OSArchitecture # 0
    ARM64 : OSArchitecture # 1
    x64ARM64 : OSArchitecture # 2
    x86 : OSArchitecture # 3


class OverrideTextureCompression(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NoOverride : OverrideTextureCompression # 0
    ForceUncompressed : OverrideTextureCompression # 1
    ForceFastCompressor : OverrideTextureCompression # 2

