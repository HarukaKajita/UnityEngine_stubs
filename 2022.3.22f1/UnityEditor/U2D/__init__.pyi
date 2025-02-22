import abc
from UnityEngine import Object, HideFlags, FilterMode, Sprite
from System import Array_1
from UnityEngine.U2D import SpriteAtlas
from UnityEditor import TextureImporterPlatformSettings, AssetImporter, BuildTarget, GUID

class SpriteAtlasAsset(Object):
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
    def Add(self, objects: Array_1[Object]) -> None: ...
    def GetMasterAtlas(self) -> SpriteAtlas: ...
    def GetPackingSettings(self) -> SpriteAtlasPackingSettings: ...
    def GetPlatformSettings(self, buildTarget: str) -> TextureImporterPlatformSettings: ...
    def GetTextureSettings(self) -> SpriteAtlasTextureSettings: ...
    def IsIncludeInBuild(self) -> bool: ...
    @staticmethod
    def Load(assetPath: str) -> SpriteAtlasAsset: ...
    def Remove(self, objects: Array_1[Object]) -> None: ...
    @staticmethod
    def Save(asset: SpriteAtlasAsset, assetPath: str) -> None: ...
    def SetIncludeInBuild(self, value: bool) -> None: ...
    def SetIsVariant(self, value: bool) -> None: ...
    def SetMasterAtlas(self, atlas: SpriteAtlas) -> None: ...
    def SetPackingSettings(self, src: SpriteAtlasPackingSettings) -> None: ...
    def SetPlatformSettings(self, src: TextureImporterPlatformSettings) -> None: ...
    def SetTextureSettings(self, src: SpriteAtlasTextureSettings) -> None: ...
    def SetVariantScale(self, value: float) -> None: ...


class SpriteAtlasExtensions(abc.ABC):
    @staticmethod
    def Add(spriteAtlas: SpriteAtlas, objects: Array_1[Object]) -> None: ...
    @staticmethod
    def GetMasterAtlas(spriteAtlas: SpriteAtlas) -> SpriteAtlas: ...
    @staticmethod
    def GetPackables(spriteAtlas: SpriteAtlas) -> Array_1[Object]: ...
    @staticmethod
    def GetPackingSettings(spriteAtlas: SpriteAtlas) -> SpriteAtlasPackingSettings: ...
    @staticmethod
    def GetPlatformSettings(spriteAtlas: SpriteAtlas, buildTarget: str) -> TextureImporterPlatformSettings: ...
    @staticmethod
    def GetTextureSettings(spriteAtlas: SpriteAtlas) -> SpriteAtlasTextureSettings: ...
    @staticmethod
    def IsIncludeInBuild(spriteAtlas: SpriteAtlas) -> bool: ...
    @staticmethod
    def Remove(spriteAtlas: SpriteAtlas, objects: Array_1[Object]) -> None: ...
    @staticmethod
    def SetIncludeInBuild(spriteAtlas: SpriteAtlas, value: bool) -> None: ...
    @staticmethod
    def SetIsVariant(spriteAtlas: SpriteAtlas, value: bool) -> None: ...
    @staticmethod
    def SetMasterAtlas(spriteAtlas: SpriteAtlas, value: SpriteAtlas) -> None: ...
    @staticmethod
    def SetPackingSettings(spriteAtlas: SpriteAtlas, src: SpriteAtlasPackingSettings) -> None: ...
    @staticmethod
    def SetPlatformSettings(spriteAtlas: SpriteAtlas, src: TextureImporterPlatformSettings) -> None: ...
    @staticmethod
    def SetTextureSettings(spriteAtlas: SpriteAtlas, src: SpriteAtlasTextureSettings) -> None: ...
    @staticmethod
    def SetVariantScale(spriteAtlas: SpriteAtlas, value: float) -> None: ...


class SpriteAtlasImporter(AssetImporter):
    def __init__(self) -> None: ...
    @property
    def assetBundleName(self) -> str: ...
    @assetBundleName.setter
    def assetBundleName(self, value: str) -> str: ...
    @property
    def assetBundleVariant(self) -> str: ...
    @assetBundleVariant.setter
    def assetBundleVariant(self, value: str) -> str: ...
    @property
    def assetPath(self) -> str: ...
    @property
    def assetTimeStamp(self) -> int: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def importSettingsMissing(self) -> bool: ...
    @property
    def includeInBuild(self) -> bool: ...
    @includeInBuild.setter
    def includeInBuild(self, value: bool) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def packingSettings(self) -> SpriteAtlasPackingSettings: ...
    @packingSettings.setter
    def packingSettings(self, value: SpriteAtlasPackingSettings) -> SpriteAtlasPackingSettings: ...
    @property
    def textureSettings(self) -> SpriteAtlasTextureSettings: ...
    @textureSettings.setter
    def textureSettings(self, value: SpriteAtlasTextureSettings) -> SpriteAtlasTextureSettings: ...
    @property
    def userData(self) -> str: ...
    @userData.setter
    def userData(self, value: str) -> str: ...
    @property
    def variantScale(self) -> float: ...
    @variantScale.setter
    def variantScale(self, value: float) -> float: ...
    def GetPlatformSettings(self, buildTarget: str) -> TextureImporterPlatformSettings: ...
    def SetPlatformSettings(self, src: TextureImporterPlatformSettings) -> None: ...


class SpriteAtlasPackingSettings:
    @property
    def blockOffset(self) -> int: ...
    @blockOffset.setter
    def blockOffset(self, value: int) -> int: ...
    @property
    def enableAlphaDilation(self) -> bool: ...
    @enableAlphaDilation.setter
    def enableAlphaDilation(self, value: bool) -> bool: ...
    @property
    def enableRotation(self) -> bool: ...
    @enableRotation.setter
    def enableRotation(self, value: bool) -> bool: ...
    @property
    def enableTightPacking(self) -> bool: ...
    @enableTightPacking.setter
    def enableTightPacking(self, value: bool) -> bool: ...
    @property
    def padding(self) -> int: ...
    @padding.setter
    def padding(self, value: int) -> int: ...


class SpriteAtlasTextureSettings:
    @property
    def anisoLevel(self) -> int: ...
    @anisoLevel.setter
    def anisoLevel(self, value: int) -> int: ...
    @property
    def filterMode(self) -> FilterMode: ...
    @filterMode.setter
    def filterMode(self, value: FilterMode) -> FilterMode: ...
    @property
    def generateMipMaps(self) -> bool: ...
    @generateMipMaps.setter
    def generateMipMaps(self, value: bool) -> bool: ...
    @property
    def readable(self) -> bool: ...
    @readable.setter
    def readable(self, value: bool) -> bool: ...
    @property
    def sRGB(self) -> bool: ...
    @sRGB.setter
    def sRGB(self, value: bool) -> bool: ...


class SpriteAtlasUtility:
    def __init__(self) -> None: ...
    @staticmethod
    def CleanupAtlasPacking() -> None: ...
    @staticmethod
    def PackAllAtlases(target: BuildTarget, canCancel: bool = ...) -> None: ...
    @staticmethod
    def PackAtlases(atlases: Array_1[SpriteAtlas], target: BuildTarget, canCancel: bool = ...) -> None: ...


class SpriteEditorExtension(abc.ABC):
    @staticmethod
    def GetSpriteID(sprite: Sprite) -> GUID: ...
    @staticmethod
    def SetSpriteID(sprite: Sprite, guid: GUID) -> None: ...

