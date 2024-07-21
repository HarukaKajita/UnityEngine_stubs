import typing
from System import Array_1, Attribute
from UnityEngine.Rendering import GraphicsDeviceType

class ApplyRulesIfGraphicsAPIAttribute(GraphicsAPIConstraintAttribute):
    def __init__(self, graphicsDeviceTypes: Array_1[GraphicsDeviceType]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ApplyRulesIfNotGraphicsAPIAttribute(GraphicsAPIConstraintAttribute):
    def __init__(self, graphicsDeviceTypes: Array_1[GraphicsDeviceType]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ApplyRulesIfTagsEqualAttribute(TagConstraintAttribute):
    def __init__(self, tags: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ApplyRulesIfTagsNotEqualAttribute(TagConstraintAttribute):
    def __init__(self, tags: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class FilterAction(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Select : FilterAction # 0
    Remove : FilterAction # 1
    SelectOrRemove : FilterAction # 2


class FilterAttribute(Attribute):
    def __init__(self, action: FilterAction, precedence: FilterAttribute.Precedence, evaluationMode: FilterAttribute.EvaluationMode, condition: typing.Any, fileName: str, lineNumber: int, keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

    class EvaluationMode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Normal : FilterAttribute.EvaluationMode # 0
        Negated : FilterAttribute.EvaluationMode # 1


    class Precedence(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Normal : FilterAttribute.Precedence # 0
        Override : FilterAttribute.Precedence # 1



class GraphicsAPIConstraintAttribute(Attribute):
    def __init__(self, negate: bool, graphicsDeviceTypes: Array_1[GraphicsDeviceType]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RemoveIfAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RemoveIfNotAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class RemoveOrSelectAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SelectIfAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SelectIfNotAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SelectOrRemoveAttribute(FilterAttribute):
    def __init__(self, condition: typing.Any, overridePriority: bool = ..., filePath: str = ..., lineNumber: int = ..., keywordNames: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class TagConstraintAttribute(Attribute):
    def __init__(self, negate: bool, tags: Array_1[str]) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

