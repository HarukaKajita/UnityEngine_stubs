import typing, abc
from System import Array_1, Exception
from UnityEditor import BuildTarget, BuildTargetGroup, ApiCompatibilityLevel
from System.Collections import IDictionary
from System.Reflection import MethodBase

class AssembliesType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Editor : AssembliesType # 0
    Player : AssembliesType # 1
    PlayerWithoutTestAssemblies : AssembliesType # 2


class Assembly:
    @typing.overload
    def __init__(self, name: str, outputPath: str, sourceFiles: Array_1[str], defines: Array_1[str], assemblyReferences: Array_1[Assembly], compiledAssemblyReferences: Array_1[str], flags: AssemblyFlags) -> None: ...
    @typing.overload
    def __init__(self, name: str, outputPath: str, sourceFiles: Array_1[str], defines: Array_1[str], assemblyReferences: Array_1[Assembly], compiledAssemblyReferences: Array_1[str], flags: AssemblyFlags, compilerOptions: ScriptCompilerOptions) -> None: ...
    @typing.overload
    def __init__(self, name: str, outputPath: str, sourceFiles: Array_1[str], defines: Array_1[str], assemblyReferences: Array_1[Assembly], compiledAssemblyReferences: Array_1[str], flags: AssemblyFlags, compilerOptions: ScriptCompilerOptions, rootNamespace: str) -> None: ...
    @property
    def allReferences(self) -> Array_1[str]: ...
    @property
    def assemblyReferences(self) -> Array_1[Assembly]: ...
    @assemblyReferences.setter
    def assemblyReferences(self, value: Array_1[Assembly]) -> Array_1[Assembly]: ...
    @property
    def compiledAssemblyReferences(self) -> Array_1[str]: ...
    @compiledAssemblyReferences.setter
    def compiledAssemblyReferences(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def compilerOptions(self) -> ScriptCompilerOptions: ...
    @compilerOptions.setter
    def compilerOptions(self, value: ScriptCompilerOptions) -> ScriptCompilerOptions: ...
    @property
    def defines(self) -> Array_1[str]: ...
    @defines.setter
    def defines(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def flags(self) -> AssemblyFlags: ...
    @flags.setter
    def flags(self, value: AssemblyFlags) -> AssemblyFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def outputPath(self) -> str: ...
    @outputPath.setter
    def outputPath(self, value: str) -> str: ...
    @property
    def rootNamespace(self) -> str: ...
    @rootNamespace.setter
    def rootNamespace(self, value: str) -> str: ...
    @property
    def sourceFiles(self) -> Array_1[str]: ...
    @sourceFiles.setter
    def sourceFiles(self, value: Array_1[str]) -> Array_1[str]: ...


class AssemblyBuilder:
    def __init__(self, assemblyPath: str, scriptPaths: Array_1[str]) -> None: ...
    @property
    def additionalDefines(self) -> Array_1[str]: ...
    @additionalDefines.setter
    def additionalDefines(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def additionalReferences(self) -> Array_1[str]: ...
    @additionalReferences.setter
    def additionalReferences(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def assemblyPath(self) -> str: ...
    @assemblyPath.setter
    def assemblyPath(self, value: str) -> str: ...
    @property
    def buildTarget(self) -> BuildTarget: ...
    @buildTarget.setter
    def buildTarget(self, value: BuildTarget) -> BuildTarget: ...
    @property
    def buildTargetGroup(self) -> BuildTargetGroup: ...
    @buildTargetGroup.setter
    def buildTargetGroup(self, value: BuildTargetGroup) -> BuildTargetGroup: ...
    @property
    def compilerOptions(self) -> ScriptCompilerOptions: ...
    @compilerOptions.setter
    def compilerOptions(self, value: ScriptCompilerOptions) -> ScriptCompilerOptions: ...
    @property
    def defaultDefines(self) -> Array_1[str]: ...
    @property
    def defaultReferences(self) -> Array_1[str]: ...
    @property
    def excludeReferences(self) -> Array_1[str]: ...
    @excludeReferences.setter
    def excludeReferences(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def flags(self) -> AssemblyBuilderFlags: ...
    @flags.setter
    def flags(self, value: AssemblyBuilderFlags) -> AssemblyBuilderFlags: ...
    @property
    def referencesOptions(self) -> ReferencesOptions: ...
    @referencesOptions.setter
    def referencesOptions(self, value: ReferencesOptions) -> ReferencesOptions: ...
    @property
    def scriptPaths(self) -> Array_1[str]: ...
    @scriptPaths.setter
    def scriptPaths(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def status(self) -> AssemblyBuilderStatus: ...
    def Build(self) -> bool: ...


class AssemblyBuilderFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : AssemblyBuilderFlags # 0
    EditorAssembly : AssemblyBuilderFlags # 1
    DevelopmentBuild : AssemblyBuilderFlags # 2


class AssemblyBuilderStatus(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NotStarted : AssemblyBuilderStatus # 0
    IsCompiling : AssemblyBuilderStatus # 1
    Finished : AssemblyBuilderStatus # 2


class AssemblyDefinitionException(Exception):
    def __init__(self, message: str, filePaths: Array_1[str]) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def filePaths(self) -> Array_1[str]: ...
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


class AssemblyDefinitionPlatform:
    @property
    def BuildTarget(self) -> BuildTarget: ...
    @BuildTarget.setter
    def BuildTarget(self, value: BuildTarget) -> BuildTarget: ...
    @property
    def DisplayName(self) -> str: ...
    @DisplayName.setter
    def DisplayName(self, value: str) -> str: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> str: ...


class AssemblyDefinitionReferenceType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Name : AssemblyDefinitionReferenceType # 0
    Guid : AssemblyDefinitionReferenceType # 1


class AssemblyFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : AssemblyFlags # 0
    EditorAssembly : AssemblyFlags # 1


class CodeOptimization(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CodeOptimization # 0
    Debug : CodeOptimization # 1
    Release : CodeOptimization # 2


class CompilationPipeline(abc.ABC):
    @classmethod
    @property
    def codeOptimization(cls) -> CodeOptimization: ...
    @classmethod
    @codeOptimization.setter
    def codeOptimization(cls, value: CodeOptimization) -> CodeOptimization: ...
    @staticmethod
    def AssemblyDefinitionReferenceGUIDToGUID(reference: str) -> str: ...
    @staticmethod
    def GetAssemblyDefinitionFilePathFromAssemblyName(assemblyName: str) -> str: ...
    @staticmethod
    def GetAssemblyDefinitionFilePathFromAssemblyReference(reference: str) -> str: ...
    @staticmethod
    def GetAssemblyDefinitionFilePathFromScriptPath(sourceFilePath: str) -> str: ...
    @staticmethod
    def GetAssemblyDefinitionPlatforms() -> Array_1[AssemblyDefinitionPlatform]: ...
    @staticmethod
    def GetAssemblyDefinitionReferenceType(reference: str) -> AssemblyDefinitionReferenceType: ...
    @staticmethod
    def GetAssemblyNameFromScriptPath(sourceFilePath: str) -> str: ...
    @staticmethod
    def GetAssemblyRootNamespaceFromScriptPath(sourceFilePath: str) -> str: ...
    @staticmethod
    def GetDefinesFromAssemblyName(assemblyName: str) -> Array_1[str]: ...
    @staticmethod
    def GetPrecompiledAssemblyNames() -> Array_1[str]: ...
    @staticmethod
    def GetPrecompiledAssemblyPathFromAssemblyName(assemblyName: str) -> str: ...
    @staticmethod
    def GetPrecompiledAssemblyPaths(precompiledAssemblySources: CompilationPipeline.PrecompiledAssemblySources) -> Array_1[str]: ...
    @staticmethod
    def GetResponseFileDefinesFromAssemblyName(assemblyName: str) -> Array_1[str]: ...
    @staticmethod
    def GetSystemAssemblyDirectories(apiCompatibilityLevel: ApiCompatibilityLevel) -> Array_1[str]: ...
    @staticmethod
    def GUIDToAssemblyDefinitionReferenceGUID(guid: str) -> str: ...
    @staticmethod
    def IsDefineConstraintsCompatible(defines: Array_1[str], defineConstraints: Array_1[str]) -> bool: ...
    @staticmethod
    def ParseResponseFile(relativePath: str, projectDirectory: str, systemReferenceDirectories: Array_1[str]) -> ResponseFileData: ...
    # Skipped GetAssemblies due to it being static, abstract and generic.

    GetAssemblies : GetAssemblies_MethodGroup
    class GetAssemblies_MethodGroup:
        @typing.overload
        def __call__(self) -> Array_1[Assembly]:...
        @typing.overload
        def __call__(self, assembliesType: AssembliesType) -> Array_1[Assembly]:...

    # Skipped RequestScriptCompilation due to it being static, abstract and generic.

    RequestScriptCompilation : RequestScriptCompilation_MethodGroup
    class RequestScriptCompilation_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, options: RequestScriptCompilationOptions) -> None:...


    class PrecompiledAssemblySources(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        UserAssembly : CompilationPipeline.PrecompiledAssemblySources # 1
        UnityEngine : CompilationPipeline.PrecompiledAssemblySources # 2
        UnityEditor : CompilationPipeline.PrecompiledAssemblySources # 4
        SystemAssembly : CompilationPipeline.PrecompiledAssemblySources # 8
        UnityAssembly : CompilationPipeline.PrecompiledAssemblySources # 16
        All : CompilationPipeline.PrecompiledAssemblySources # -1



class CompilerMessage:
    column : int
    file : str
    line : int
    message : str
    type : CompilerMessageType


class CompilerMessageType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Error : CompilerMessageType # 0
    Warning : CompilerMessageType # 1
    Info : CompilerMessageType # 2


class PrecompiledAssemblyException(Exception):
    def __init__(self, message: str, filePaths: Array_1[str]) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def filePaths(self) -> Array_1[str]: ...
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


class ReferencesOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : ReferencesOptions # 0
    UseEngineModules : ReferencesOptions # 1


class RequestScriptCompilationOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : RequestScriptCompilationOptions # 0
    CleanBuildCache : RequestScriptCompilationOptions # 1


class ResponseFileData:
    def __init__(self) -> None: ...
    Defines : Array_1[str]
    Errors : Array_1[str]
    FullPathReferences : Array_1[str]
    OtherArguments : Array_1[str]
    Unsafe : bool


class ScriptCompilerOptions:
    def __init__(self) -> None: ...
    @property
    def AdditionalCompilerArguments(self) -> Array_1[str]: ...
    @AdditionalCompilerArguments.setter
    def AdditionalCompilerArguments(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def AllowUnsafeCode(self) -> bool: ...
    @AllowUnsafeCode.setter
    def AllowUnsafeCode(self, value: bool) -> bool: ...
    @property
    def AnalyzerConfigPath(self) -> str: ...
    @AnalyzerConfigPath.setter
    def AnalyzerConfigPath(self, value: str) -> str: ...
    @property
    def ApiCompatibilityLevel(self) -> ApiCompatibilityLevel: ...
    @ApiCompatibilityLevel.setter
    def ApiCompatibilityLevel(self, value: ApiCompatibilityLevel) -> ApiCompatibilityLevel: ...
    @property
    def CodeOptimization(self) -> CodeOptimization: ...
    @CodeOptimization.setter
    def CodeOptimization(self, value: CodeOptimization) -> CodeOptimization: ...
    @property
    def EmitReferenceAssembly(self) -> bool: ...
    @EmitReferenceAssembly.setter
    def EmitReferenceAssembly(self, value: bool) -> bool: ...
    @property
    def LanguageVersion(self) -> str: ...
    @LanguageVersion.setter
    def LanguageVersion(self, value: str) -> str: ...
    @property
    def ResponseFiles(self) -> Array_1[str]: ...
    @ResponseFiles.setter
    def ResponseFiles(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def RoslynAdditionalFilePaths(self) -> Array_1[str]: ...
    @RoslynAdditionalFilePaths.setter
    def RoslynAdditionalFilePaths(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def RoslynAnalyzerDllPaths(self) -> Array_1[str]: ...
    @RoslynAnalyzerDllPaths.setter
    def RoslynAnalyzerDllPaths(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def RoslynAnalyzerRulesetPath(self) -> str: ...
    @RoslynAnalyzerRulesetPath.setter
    def RoslynAnalyzerRulesetPath(self, value: str) -> str: ...

