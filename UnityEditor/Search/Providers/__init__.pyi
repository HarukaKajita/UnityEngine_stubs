import typing
from UnityEditor.Search import QueryEngineFilterAttribute, QueryEngineParameterTransformerAttribute
from System import StringComparison, Array_1

class SceneQueryEngineFilterAttribute(QueryEngineFilterAttribute):
    @typing.overload
    def __init__(self, token: str, options: StringComparison, supportedOperators: Array_1[str] = ...) -> None: ...
    @typing.overload
    def __init__(self, token: str, paramTransformerFunction: str, options: StringComparison, supportedOperators: Array_1[str] = ...) -> None: ...
    @typing.overload
    def __init__(self, token: str, paramTransformerFunction: str, supportedOperators: Array_1[str] = ...) -> None: ...
    @typing.overload
    def __init__(self, token: str, supportedOperators: Array_1[str] = ...) -> None: ...
    comparisonOptions : StringComparison
    overridesStringComparison : bool
    paramTransformerFunction : str
    supportedOperators : Array_1[str]
    token : str
    useParamTransformer : bool
    useRegularExpressionToken : bool
    @property
    def TypeId(self) -> typing.Any: ...


class SceneQueryEngineParameterTransformerAttribute(QueryEngineParameterTransformerAttribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...

