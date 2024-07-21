import typing
from UnityEngine import PropertyAttribute
from System import Array_1

class SearchContextAttribute(PropertyAttribute):
    @typing.overload
    def __init__(self, query: str) -> None: ...
    @typing.overload
    def __init__(self, query: str, flags: SearchViewFlags) -> None: ...
    @typing.overload
    def __init__(self, query: str, flags: SearchViewFlags, instantiableProviders: Array_1[typing.Type[typing.Any]]) -> None: ...
    @typing.overload
    def __init__(self, query: str, flags: SearchViewFlags, providerIdsCommaSeparated: str, instantiableProviders: Array_1[typing.Type[typing.Any]]) -> None: ...
    @typing.overload
    def __init__(self, query: str, instantiableProviders: Array_1[typing.Type[typing.Any]]) -> None: ...
    @typing.overload
    def __init__(self, query: str, providerIdsCommaSeparated: str) -> None: ...
    @typing.overload
    def __init__(self, query: str, providerIdsCommaSeparated: str, flags: SearchViewFlags) -> None: ...
    @property
    def flags(self) -> SearchViewFlags: ...
    @flags.setter
    def flags(self, value: SearchViewFlags) -> SearchViewFlags: ...
    @property
    def instantiableProviders(self) -> Array_1[typing.Type[typing.Any]]: ...
    @instantiableProviders.setter
    def instantiableProviders(self, value: Array_1[typing.Type[typing.Any]]) -> Array_1[typing.Type[typing.Any]]: ...
    @property
    def order(self) -> int: ...
    @order.setter
    def order(self, value: int) -> int: ...
    @property
    def providerIds(self) -> Array_1[str]: ...
    @providerIds.setter
    def providerIds(self, value: Array_1[str]) -> Array_1[str]: ...
    @property
    def query(self) -> str: ...
    @query.setter
    def query(self, value: str) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SearchViewFlags(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : SearchViewFlags # 0
    Debug : SearchViewFlags # 16
    NoIndexing : SearchViewFlags # 32
    Packages : SearchViewFlags # 256
    OpenLeftSidePanel : SearchViewFlags # 2048
    OpenInspectorPreview : SearchViewFlags # 4096
    Centered : SearchViewFlags # 8192
    HideSearchBar : SearchViewFlags # 16384
    CompactView : SearchViewFlags # 32768
    ListView : SearchViewFlags # 65536
    GridView : SearchViewFlags # 131072
    TableView : SearchViewFlags # 262144
    EnableSearchQuery : SearchViewFlags # 524288
    DisableInspectorPreview : SearchViewFlags # 1048576
    DisableSavedSearchQuery : SearchViewFlags # 2097152
    OpenInBuilderMode : SearchViewFlags # 4194304
    OpenInTextMode : SearchViewFlags # 8388608
    DisableBuilderModeToggle : SearchViewFlags # 16777216
    Borderless : SearchViewFlags # 33554432
    ContextSwitchPreservedMask : SearchViewFlags # 33560576
    DisableQueryHelpers : SearchViewFlags # 67108864
    DisableNoResultTips : SearchViewFlags # 134217728
    IgnoreSavedSearches : SearchViewFlags # 268435456
    ObjectPicker : SearchViewFlags # 536870912
    ObjectPickerAdvancedUI : SearchViewFlags # 1073741824

