import typing

class BuildCompression:
    DefaultLZ4 : BuildCompression
    DefaultLZMA : BuildCompression
    DefaultUncompressed : BuildCompression


class CompressionLevel(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CompressionLevel # 0
    Fastest : CompressionLevel # 1
    Fast : CompressionLevel # 2
    Normal : CompressionLevel # 3
    High : CompressionLevel # 4
    Maximum : CompressionLevel # 5


class CompressionType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : CompressionType # 0
    Lzma : CompressionType # 1
    Lz4 : CompressionType # 2
    Lz4HC : CompressionType # 3

