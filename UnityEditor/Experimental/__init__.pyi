import typing, clr, abc
from UnityEngine import Hash128, Object, Vector4, Light, Vector3
from UnityEditor import GUID, BuildTarget
from System import Array_1, IEquatable_1, ReadOnlySpan_1, Span_1
from Unity.Collections import NativeArray_1
from System.Collections.Generic import HashSet_1
from UnityEngine.SceneManagement import Scene
from UnityEngine.Rendering import SphericalHarmonicsL2

class ArtifactID:
    value : Hash128
    @property
    def isValid(self) -> bool: ...


class ArtifactKey:
    @typing.overload
    def __init__(self, g: GUID) -> None: ...
    @typing.overload
    def __init__(self, guid: GUID, importerType: typing.Type[typing.Any]) -> None: ...
    guid : GUID
    importerType : typing.Type[typing.Any]
    @property
    def isValid(self) -> bool: ...


class AssetDatabaseExperimental:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def ActiveOnDemandMode(cls) -> AssetDatabaseExperimental.OnDemandMode: ...
    @classmethod
    @ActiveOnDemandMode.setter
    def ActiveOnDemandMode(cls, value: AssetDatabaseExperimental.OnDemandMode) -> AssetDatabaseExperimental.OnDemandMode: ...
    @classmethod
    @property
    def counters(cls) -> AssetDatabaseExperimental.AssetDatabaseCounters: ...
    @staticmethod
    def CanConnectToCacheServer(ip: str, port: int) -> bool: ...
    @staticmethod
    def ClearImporterOverride(path: str) -> None: ...
    @staticmethod
    def ForceProduceArtifact(artifactKey: ArtifactKey) -> ArtifactID: ...
    @staticmethod
    def GetArtifactHashes(guids: Array_1[str], mode: AssetDatabaseExperimental.ImportSyncMode = ...) -> Array_1[Hash128]: ...
    @staticmethod
    def GetAvailableImporterTypes(path: str) -> Array_1[typing.Type[typing.Any]]: ...
    @staticmethod
    def GetCacheServerAddress() -> str: ...
    @staticmethod
    def GetCacheServerEnableDownload() -> bool: ...
    @staticmethod
    def GetCacheServerEnableUpload() -> bool: ...
    @staticmethod
    def GetCacheServerNamespacePrefix() -> str: ...
    @staticmethod
    def GetCacheServerPort() -> int: ...
    @staticmethod
    def GetImporterOverride(path: str) -> typing.Type[typing.Any]: ...
    @staticmethod
    def IsAssetImportWorkerProcess() -> bool: ...
    @staticmethod
    def IsCacheServerEnabled() -> bool: ...
    @staticmethod
    def IsConnectedToCacheServer() -> bool: ...
    @staticmethod
    def IsDirectoryMonitoringEnabled() -> bool: ...
    @staticmethod
    def LookupArtifact(artifactKey: ArtifactKey) -> ArtifactID: ...
    @staticmethod
    def ProduceArtifact(artifactKey: ArtifactKey) -> ArtifactID: ...
    @staticmethod
    def ProduceArtifactAsync(artifactKey: ArtifactKey) -> ArtifactID: ...
    @staticmethod
    def ProduceArtifactsAsync(artifactKey: Array_1[GUID], importerType: typing.Type[typing.Any] = ...) -> Array_1[ArtifactID]: ...
    @staticmethod
    def ReconnectToCacheServer() -> None: ...
    @staticmethod
    def RefreshSettings() -> None: ...
    @staticmethod
    def RegisterCustomDependency(dependency: str, hashOfValue: Hash128) -> None: ...
    @staticmethod
    def UnregisterCustomDependencyPrefixFilter(prefixFilter: str) -> int: ...
    # Skipped GetArtifactHash due to it being static, abstract and generic.

    GetArtifactHash : GetArtifactHash_MethodGroup
    class GetArtifactHash_MethodGroup:
        @typing.overload
        def __call__(self, guid: str, mode: AssetDatabaseExperimental.ImportSyncMode = ...) -> Hash128:...
        @typing.overload
        def __call__(self, guid: str, importerType: typing.Type[typing.Any], mode: AssetDatabaseExperimental.ImportSyncMode = ...) -> Hash128:...

    # Skipped GetArtifactPaths due to it being static, abstract and generic.

    GetArtifactPaths : GetArtifactPaths_MethodGroup
    class GetArtifactPaths_MethodGroup:
        @typing.overload
        def __call__(self, hash: ArtifactID, paths: clr.Reference[Array_1[str]]) -> bool:...
        @typing.overload
        def __call__(self, hash: Hash128, paths: clr.Reference[Array_1[str]]) -> bool:...

    # Skipped GetOnDemandArtifactProgress due to it being static, abstract and generic.

    GetOnDemandArtifactProgress : GetOnDemandArtifactProgress_MethodGroup
    class GetOnDemandArtifactProgress_MethodGroup:
        @typing.overload
        def __call__(self, artifactKey: ArtifactKey) -> OnDemandProgress:...
        @typing.overload
        def __call__(self, guid: str) -> OnDemandProgress:...
        @typing.overload
        def __call__(self, guid: str, importerType: typing.Type[typing.Any]) -> OnDemandProgress:...

    # Skipped LookupArtifacts due to it being static, abstract and generic.

    LookupArtifacts : LookupArtifacts_MethodGroup
    class LookupArtifacts_MethodGroup:
        @typing.overload
        def __call__(self, guids: NativeArray_1[GUID], hashesOut: NativeArray_1[ArtifactID]) -> None:...
        @typing.overload
        def __call__(self, guids: NativeArray_1[GUID], hashes: NativeArray_1[ArtifactID], importerType: typing.Type[typing.Any]) -> None:...

    # Skipped SetImporterOverride due to it being static, abstract and generic.

    SetImporterOverride : SetImporterOverride_MethodGroup
    class SetImporterOverride_MethodGroup:
        def __getitem__(self, t:typing.Type[SetImporterOverride_1_T1]) -> SetImporterOverride_1[SetImporterOverride_1_T1]: ...

        SetImporterOverride_1_T1 = typing.TypeVar('SetImporterOverride_1_T1')
        class SetImporterOverride_1(typing.Generic[SetImporterOverride_1_T1]):
            SetImporterOverride_1_T = AssetDatabaseExperimental.SetImporterOverride_MethodGroup.SetImporterOverride_1_T1
            def __call__(self, path: str) -> None:...



    class AssetDatabaseCounters:
        cacheServer : AssetDatabaseExperimental.AssetDatabaseCounters.CacheServerCounters
        import : AssetDatabaseExperimental.AssetDatabaseCounters.ImportCounters
        def ResetDeltas(self) -> None: ...

        class CacheServerCounters:
            artifactFilesDownloaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            artifactFilesFailedToDownload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            artifactFilesFailedToUpload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            artifactFilesUploaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            artifactsDownloaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            artifactsUploaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            batchesUsedForDownload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            connects : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            disconnects : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataDownloaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataFailedToDownload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataFailedToUpload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataMatched : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataRequested : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataUploaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            metadataVersionsDownloaded : AssetDatabaseExperimental.AssetDatabaseCounters.Counter


        class Counter:
            delta : int
            total : int


        class ImportCounters:
            domainReload : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            imported : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            importedInProcess : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            importedOutOfProcess : AssetDatabaseExperimental.AssetDatabaseCounters.Counter
            refresh : AssetDatabaseExperimental.AssetDatabaseCounters.Counter



    class CacheServerConnectionChangedParameters:
        pass


    class ImportSyncMode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Block : AssetDatabaseExperimental.ImportSyncMode # 0
        Queue : AssetDatabaseExperimental.ImportSyncMode # 1
        Poll : AssetDatabaseExperimental.ImportSyncMode # 2


    class OnDemandMode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Off : AssetDatabaseExperimental.OnDemandMode # 0
        Lazy : AssetDatabaseExperimental.OnDemandMode # 1
        Background : AssetDatabaseExperimental.OnDemandMode # 2



class AssetMoveInfo(IEquatable_1[AssetMoveInfo]):
    def __init__(self, sourceAssetPath: str, destinationAssetPath: str) -> None: ...
    @property
    def destinationAssetPath(self) -> str: ...
    @property
    def sourceAssetPath(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, left: AssetMoveInfo, right: AssetMoveInfo) -> bool: ...
    def __ne__(self, left: AssetMoveInfo, right: AssetMoveInfo) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: AssetMoveInfo) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class AssetsModifiedProcessor(abc.ABC):
    @property
    def assetsReportedChanged(self) -> HashSet_1[str]: ...
    @assetsReportedChanged.setter
    def assetsReportedChanged(self, value: HashSet_1[str]) -> HashSet_1[str]: ...


class BuildPipelineExperimental(abc.ABC):
    @staticmethod
    def GetSessionIdForBuildTarget(target: BuildTarget) -> str: ...


class EditorResources:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def brushesPath(cls) -> str: ...
    @classmethod
    @property
    def darkSkinIndex(cls) -> int: ...
    @classmethod
    @property
    def darkSkinSourcePath(cls) -> str: ...
    @classmethod
    @property
    def dataPath(cls) -> str: ...
    @classmethod
    @property
    def editorDefaultResourcesPath(cls) -> str: ...
    @classmethod
    @property
    def emptyFolderIconName(cls) -> str: ...
    @classmethod
    @property
    def folderIconName(cls) -> str: ...
    @classmethod
    @property
    def fontsPath(cls) -> str: ...
    @classmethod
    @property
    def generatedIconsPath(cls) -> str: ...
    @classmethod
    @property
    def iconsPath(cls) -> str: ...
    @classmethod
    @property
    def libraryBundlePath(cls) -> str: ...
    @classmethod
    @property
    def lightSkinSourcePath(cls) -> str: ...
    @classmethod
    @property
    def normalSkinIndex(cls) -> int: ...
    @staticmethod
    def Exists(path: str) -> bool: ...
    @staticmethod
    def ExpandPath(path: str) -> str: ...
    @staticmethod
    def GetAssetPath(obj: Object) -> str: ...
    @staticmethod
    def GetFullPath(path: str) -> str: ...
    # Skipped Load due to it being static, abstract and generic.

    Load : Load_MethodGroup
    class Load_MethodGroup:
        def __getitem__(self, t:typing.Type[Load_1_T1]) -> Load_1[Load_1_T1]: ...

        Load_1_T1 = typing.TypeVar('Load_1_T1')
        class Load_1(typing.Generic[Load_1_T1]):
            Load_1_T = EditorResources.Load_MethodGroup.Load_1_T1
            def __call__(self, assetPath: str, isRequired: bool = ...) -> Load_1_T:...

        def __call__(self, assetPath: str, type: typing.Type[typing.Any]) -> Object:...



class Lightmapping:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def extractAmbientOcclusion(cls) -> bool: ...
    @classmethod
    @extractAmbientOcclusion.setter
    def extractAmbientOcclusion(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def probesIgnoreDirectEnvironment(cls) -> bool: ...
    @classmethod
    @probesIgnoreDirectEnvironment.setter
    def probesIgnoreDirectEnvironment(cls, value: bool) -> bool: ...
    @staticmethod
    def Bake(targetScene: Scene) -> bool: ...
    @staticmethod
    def BakeAsync(targetScene: Scene) -> bool: ...
    @staticmethod
    def GetCustomBakeResultsNoCopy() -> ReadOnlySpan_1[Vector4]: ...
    @staticmethod
    def SetLightDirty(light: Light) -> None: ...
    # Skipped GetAdditionalBakedProbes due to it being static, abstract and generic.

    GetAdditionalBakedProbes : GetAdditionalBakedProbes_MethodGroup
    class GetAdditionalBakedProbes_MethodGroup:
        @typing.overload
        def __call__(self, id: int, outBakedProbeSH: NativeArray_1[SphericalHarmonicsL2], outBakedProbeValidity: NativeArray_1[float]) -> bool:...
        @typing.overload
        def __call__(self, id: int, outBakedProbeSH: Span_1[SphericalHarmonicsL2], outBakedProbeValidity: Span_1[float], outBakedProbeOctahedralDepth: Span_1[float]) -> bool:...
        @typing.overload
        def __call__(self, id: int, outBakedProbeSH: NativeArray_1[SphericalHarmonicsL2], outBakedProbeValidity: NativeArray_1[float], outBakedProbeOctahedralDepth: NativeArray_1[float]) -> bool:...

    # Skipped GetCustomBakeResults due to it being static, abstract and generic.

    GetCustomBakeResults : GetCustomBakeResults_MethodGroup
    class GetCustomBakeResults_MethodGroup:
        @typing.overload
        def __call__(self, results: Array_1[Vector4]) -> bool:...
        @typing.overload
        def __call__(self, results: Span_1[Vector4]) -> bool:...

    # Skipped SetAdditionalBakedProbes due to it being static, abstract and generic.

    SetAdditionalBakedProbes : SetAdditionalBakedProbes_MethodGroup
    class SetAdditionalBakedProbes_MethodGroup:
        @typing.overload
        def __call__(self, id: int, positions: Array_1[Vector3]) -> None:...
        @typing.overload
        def __call__(self, id: int, positions: ReadOnlySpan_1[Vector3]) -> None:...
        @typing.overload
        def __call__(self, id: int, positions: ReadOnlySpan_1[Vector3], dering: bool) -> None:...

    # Skipped SetCustomBakeInputs due to it being static, abstract and generic.

    SetCustomBakeInputs : SetCustomBakeInputs_MethodGroup
    class SetCustomBakeInputs_MethodGroup:
        @typing.overload
        def __call__(self, inputData: Array_1[Vector4], sampleCount: int) -> None:...
        @typing.overload
        def __call__(self, inputData: ReadOnlySpan_1[Vector4], sampleCount: int) -> None:...



class OnDemandProgress:
    progress : float
    state : OnDemandState


class OnDemandState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Unavailable : OnDemandState # 0
    Processing : OnDemandState # 1
    Downloading : OnDemandState # 2
    Available : OnDemandState # 3
    Failed : OnDemandState # 4


class RenderSettings:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def useRadianceAmbientProbe(cls) -> bool: ...
    @classmethod
    @useRadianceAmbientProbe.setter
    def useRadianceAmbientProbe(cls, value: bool) -> bool: ...

