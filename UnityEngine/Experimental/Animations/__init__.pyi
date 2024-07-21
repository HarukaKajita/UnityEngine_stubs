import typing, abc
from UnityEngine.Animations import AnimationPlayableOutput

class AnimationPlayableOutputExtensions(abc.ABC):
    @staticmethod
    def GetAnimationStreamSource(output: AnimationPlayableOutput) -> AnimationStreamSource: ...
    @staticmethod
    def GetSortingOrder(output: AnimationPlayableOutput) -> int: ...
    @staticmethod
    def SetAnimationStreamSource(output: AnimationPlayableOutput, streamSource: AnimationStreamSource) -> None: ...
    @staticmethod
    def SetSortingOrder(output: AnimationPlayableOutput, sortingOrder: int) -> None: ...


class AnimationStreamSource(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    DefaultValues : AnimationStreamSource # 0
    PreviousInputs : AnimationStreamSource # 1

