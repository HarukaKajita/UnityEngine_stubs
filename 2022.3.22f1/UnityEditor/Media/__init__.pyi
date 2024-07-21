import typing
from UnityEditor import VideoEncodingProfile, VideoBitrateMode
from System import IDisposable, Array_1
from UnityEngine import Texture2D, TextureFormat
from Unity.Collections import NativeArray_1

class AudioTrackAttributes:
    channelCount : int
    language : str
    sampleRate : MediaRational


class H264EncoderAttributes:
    gopSize : int
    numConsecutiveBFrames : int
    profile : VideoEncodingProfile


class MediaEncoder(IDisposable):
    @typing.overload
    def __init__(self, filePath: str, audioAttrs: Array_1[AudioTrackAttributes]) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, audioAttrs: AudioTrackAttributes) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackEncoderAttributes) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackAttributes) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackAttributes, audioAttrs: Array_1[AudioTrackAttributes]) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackEncoderAttributes, audioAttrs: Array_1[AudioTrackAttributes]) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackEncoderAttributes, audioAttrs: AudioTrackAttributes) -> None: ...
    @typing.overload
    def __init__(self, filePath: str, videoAttrs: VideoTrackAttributes, audioAttrs: AudioTrackAttributes) -> None: ...
    m_Ptr : int
    def Dispose(self) -> None: ...
    # Skipped AddFrame due to it being static, abstract and generic.

    AddFrame : AddFrame_MethodGroup
    class AddFrame_MethodGroup:
        @typing.overload
        def __call__(self, texture: Texture2D) -> bool:...
        @typing.overload
        def __call__(self, texture: Texture2D, time: MediaTime) -> bool:...
        @typing.overload
        def __call__(self, width: int, height: int, rowBytes: int, format: TextureFormat, data: NativeArray_1[int]) -> bool:...
        @typing.overload
        def __call__(self, width: int, height: int, rowBytes: int, format: TextureFormat, data: NativeArray_1[int], time: MediaTime) -> bool:...

    # Skipped AddSamples due to it being static, abstract and generic.

    AddSamples : AddSamples_MethodGroup
    class AddSamples_MethodGroup:
        @typing.overload
        def __call__(self, interleavedSamples: NativeArray_1[float]) -> bool:...
        @typing.overload
        def __call__(self, trackIndex: int, interleavedSamples: NativeArray_1[float]) -> bool:...



class MediaRational:
    @typing.overload
    def __init__(self, numerator: int) -> None: ...
    @typing.overload
    def __init__(self, numerator: int, denominator: int) -> None: ...
    denominator : int
    Invalid : MediaRational
    numerator : int
    @property
    def inverse(self) -> MediaRational: ...
    @property
    def isNegative(self) -> bool: ...
    @property
    def isValid(self) -> bool: ...
    @property
    def isZero(self) -> bool: ...
    # Operator not supported op_Explicit(r: MediaRational)
    def Set(self, numerator: int, denominator: int = ...) -> None: ...


class MediaTime:
    @typing.overload
    def __init__(self, count: int, rateNumerator: int, rateDenominator: int = ...) -> None: ...
    @typing.overload
    def __init__(self, seconds: int) -> None: ...
    Invalid : MediaTime
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, value: int) -> int: ...
    @property
    def rate(self) -> MediaRational: ...
    @rate.setter
    def rate(self, value: MediaRational) -> MediaRational: ...
    # Operator not supported op_Explicit(t: MediaTime)


class VideoTrackAttributes:
    bitRateMode : VideoBitrateMode
    frameRate : MediaRational
    height : int
    includeAlpha : bool
    width : int


class VideoTrackEncoderAttributes:
    @typing.overload
    def __init__(self, h264Attrs: H264EncoderAttributes) -> None: ...
    @typing.overload
    def __init__(self, vp8Attrs: VP8EncoderAttributes) -> None: ...
    bitRateMode : VideoBitrateMode
    frameRate : MediaRational
    height : int
    includeAlpha : bool
    targetBitRate : int
    width : int


class VP8EncoderAttributes:
    keyframeDistance : int

