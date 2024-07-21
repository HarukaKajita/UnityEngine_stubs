import typing, abc
from System.Collections.Generic import Dictionary_2
from UnityEngine import Terrain, Vector2
from System import Predicate_1

class TerrainMap:
    def __init__(self) -> None: ...
    @property
    def terrainTiles(self) -> Dictionary_2[TerrainTileCoord, Terrain]: ...
    @staticmethod
    def CreateFromConnectedNeighbors(originTerrain: Terrain, filter: Predicate_1[Terrain] = ..., fullValidation: bool = ...) -> TerrainMap: ...
    def GetTerrain(self, tileX: int, tileZ: int) -> Terrain: ...
    # Skipped CreateFromPlacement due to it being static, abstract and generic.

    CreateFromPlacement : CreateFromPlacement_MethodGroup
    class CreateFromPlacement_MethodGroup:
        @typing.overload
        def __call__(self, originTerrain: Terrain, filter: Predicate_1[Terrain] = ..., fullValidation: bool = ...) -> TerrainMap:...
        @typing.overload
        def __call__(self, gridOrigin: Vector2, gridSize: Vector2, filter: Predicate_1[Terrain] = ..., fullValidation: bool = ...) -> TerrainMap:...



class TerrainTileCoord:
    def __init__(self, tileX: int, tileZ: int) -> None: ...
    tileX : int
    tileZ : int


class TerrainUtility(abc.ABC):
    @staticmethod
    def AutoConnect() -> None: ...

