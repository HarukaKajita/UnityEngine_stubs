import typing, clr, abc
from UnityEngine import Vector2, Vector3, Quaternion, Light, LightmapBakeType, Color
from System import MulticastDelegate, IAsyncResult, Array_1, AsyncCallback
from System.Reflection import MethodInfo
from Unity.Collections import NativeArray_1

class AngularFalloffType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    LUT : AngularFalloffType # 0
    AnalyticAndInnerAngle : AngularFalloffType # 1


class Cookie:
    instanceID : int
    scale : float
    sizes : Vector2
    @staticmethod
    def Defaults() -> Cookie: ...


class DirectionalLight:
    color : LinearColor
    direction : Vector3
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    penumbraWidthRadian : float
    position : Vector3
    shadow : bool


class DiscLight:
    color : LinearColor
    falloff : FalloffType
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    radius : float
    range : float
    shadow : bool


class FalloffType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    InverseSquared : FalloffType # 0
    InverseSquaredNoRangeAttenuation : FalloffType # 1
    Linear : FalloffType # 2
    Legacy : FalloffType # 3
    Undefined : FalloffType # 4


class LightDataGI:
    color : LinearColor
    coneAngle : float
    cookieID : int
    cookieScale : float
    falloff : FalloffType
    indirectColor : LinearColor
    innerConeAngle : float
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : int
    shape0 : float
    shape1 : float
    type : LightType
    def InitNoBake(self, lightInstanceID: int) -> None: ...
    # Skipped Init due to it being static, abstract and generic.

    Init : Init_MethodGroup
    class Init_MethodGroup:
        @typing.overload
        def __call__(self, light: clr.Reference[DirectionalLight]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[PointLight]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLight]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[RectangleLight]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[DiscLight]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLightBoxShape]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLightPyramidShape]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[DirectionalLight], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[PointLight], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLight], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[RectangleLight], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[DiscLight], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLightBoxShape], cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, light: clr.Reference[SpotLightPyramidShape], cookie: clr.Reference[Cookie]) -> None:...



class LightmapperUtils(abc.ABC):
    @staticmethod
    def ExtractIndirect(l: Light) -> LinearColor: ...
    @staticmethod
    def ExtractInnerCone(l: Light) -> float: ...
    # Skipped Extract due to it being static, abstract and generic.

    Extract : Extract_MethodGroup
    class Extract_MethodGroup:
        @typing.overload
        def __call__(self, baketype: LightmapBakeType) -> LightMode:...
        @typing.overload
        def __call__(self, l: Light, cookie: clr.Reference[Cookie]) -> None:...
        @typing.overload
        def __call__(self, l: Light, dir: clr.Reference[DirectionalLight]) -> None:...
        @typing.overload
        def __call__(self, l: Light, disc: clr.Reference[DiscLight]) -> None:...
        @typing.overload
        def __call__(self, l: Light, point: clr.Reference[PointLight]) -> None:...
        @typing.overload
        def __call__(self, l: Light, rect: clr.Reference[RectangleLight]) -> None:...
        @typing.overload
        def __call__(self, l: Light, spot: clr.Reference[SpotLight]) -> None:...



class Lightmapping(abc.ABC):
    @staticmethod
    def GetDelegate() -> Lightmapping.RequestLightsDelegate: ...
    @staticmethod
    def ResetDelegate() -> None: ...
    @staticmethod
    def SetDelegate(del_: Lightmapping.RequestLightsDelegate) -> None: ...

    class RequestLightsDelegate(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, requests: Array_1[Light], lightsOutput: NativeArray_1[LightDataGI], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, result: IAsyncResult) -> None: ...
        def Invoke(self, requests: Array_1[Light], lightsOutput: NativeArray_1[LightDataGI]) -> None: ...



class LightMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Realtime : LightMode # 0
    Mixed : LightMode # 1
    Baked : LightMode # 2
    Unknown : LightMode # 3


class LightType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Directional : LightType # 0
    Point : LightType # 1
    Spot : LightType # 2
    Rectangle : LightType # 3
    Disc : LightType # 4
    SpotPyramidShape : LightType # 5
    SpotBoxShape : LightType # 6


class LinearColor:
    @property
    def blue(self) -> float: ...
    @blue.setter
    def blue(self, value: float) -> float: ...
    @property
    def green(self) -> float: ...
    @green.setter
    def green(self, value: float) -> float: ...
    @property
    def intensity(self) -> float: ...
    @intensity.setter
    def intensity(self, value: float) -> float: ...
    @property
    def red(self) -> float: ...
    @red.setter
    def red(self, value: float) -> float: ...
    @staticmethod
    def Black() -> LinearColor: ...
    @staticmethod
    def Convert(color: Color, intensity: float) -> LinearColor: ...


class PointLight:
    color : LinearColor
    falloff : FalloffType
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : bool
    sphereRadius : float


class RectangleLight:
    color : LinearColor
    falloff : FalloffType
    height : float
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : bool
    width : float


class RenderSettings:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def useRadianceAmbientProbe(cls) -> bool: ...
    @classmethod
    @useRadianceAmbientProbe.setter
    def useRadianceAmbientProbe(cls, value: bool) -> bool: ...


class SpotLight:
    angularFalloff : AngularFalloffType
    color : LinearColor
    coneAngle : float
    falloff : FalloffType
    indirectColor : LinearColor
    innerConeAngle : float
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : bool
    sphereRadius : float


class SpotLightBoxShape:
    color : LinearColor
    height : float
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : bool
    width : float


class SpotLightPyramidShape:
    angle : float
    aspectRatio : float
    color : LinearColor
    falloff : FalloffType
    indirectColor : LinearColor
    instanceID : int
    mode : LightMode
    orientation : Quaternion
    position : Vector3
    range : float
    shadow : bool

