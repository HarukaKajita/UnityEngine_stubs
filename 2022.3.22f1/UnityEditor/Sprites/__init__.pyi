import clr
from UnityEngine import ColorSpace, FilterMode, TextureFormat, Texture2D, Sprite, SpritePackingMode, SpritePackingRotation, Vector2
from System import Array_1

class AtlasSettings:
    allowsAlphaSplitting : bool
    anisoLevel : int
    colorSpace : ColorSpace
    compressionQuality : int
    enableRotation : bool
    filterMode : FilterMode
    format : TextureFormat
    generateMipMaps : bool
    maxHeight : int
    maxWidth : int
    paddingPower : int


class DataUtility:
    def __init__(self) -> None: ...


class Packer:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def atlasNames(cls) -> Array_1[str]: ...
    @staticmethod
    def GetAlphaTexturesForAtlas(atlasName: str) -> Array_1[Texture2D]: ...
    @staticmethod
    def GetAtlasDataForSprite(sprite: Sprite, atlasName: clr.Reference[str], atlasTexture: clr.Reference[Texture2D]) -> None: ...
    @staticmethod
    def GetTexturesForAtlas(atlasName: str) -> Array_1[Texture2D]: ...


class PackerJob:
    def AddAtlas(self, atlasName: str, settings: AtlasSettings) -> None: ...
    def AssignToAtlas(self, atlasName: str, sprite: Sprite, packingMode: SpritePackingMode, packingRotation: SpritePackingRotation) -> None: ...


class SpriteUtility:
    def __init__(self) -> None: ...
    @staticmethod
    def GetSpriteIndices(sprite: Sprite, getAtlasData: bool) -> Array_1[int]: ...
    @staticmethod
    def GetSpriteMesh(sprite: Sprite, getAtlasData: bool) -> Array_1[Vector2]: ...
    @staticmethod
    def GetSpriteTexture(sprite: Sprite, getAtlasData: bool) -> Texture2D: ...
    @staticmethod
    def GetSpriteUVs(sprite: Sprite, getAtlasData: bool) -> Array_1[Vector2]: ...

