import typing, abc
from UnityEngine.UIElements import VisualElement
from UnityEngine import Vector2

class DeviceSimulator:
    pass


class DeviceSimulatorPlugin(abc.ABC):
    @property
    def deviceSimulator(self) -> DeviceSimulator: ...
    @deviceSimulator.setter
    def deviceSimulator(self, value: DeviceSimulator) -> DeviceSimulator: ...
    @property
    def title(self) -> str: ...
    def OnCreate(self) -> None: ...
    def OnCreateUI(self) -> VisualElement: ...
    def OnDestroy(self) -> None: ...


class TouchEvent:
    @property
    def phase(self) -> TouchPhase: ...
    @property
    def position(self) -> Vector2: ...
    @property
    def touchId(self) -> int: ...


class TouchPhase(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Began : TouchPhase # 0
    Moved : TouchPhase # 1
    Ended : TouchPhase # 2
    Canceled : TouchPhase # 3
    Stationary : TouchPhase # 4

