from UnityEngine import TextureFormat
from Unity.Collections import NativeArray_1

class DebugScreenCapture:
    @property
    def height(self) -> int: ...
    @height.setter
    def height(self, value: int) -> int: ...
    @property
    def imageFormat(self) -> TextureFormat: ...
    @imageFormat.setter
    def imageFormat(self, value: TextureFormat) -> TextureFormat: ...
    @property
    def rawImageDataReference(self) -> NativeArray_1[int]: ...
    @rawImageDataReference.setter
    def rawImageDataReference(self, value: NativeArray_1[int]) -> NativeArray_1[int]: ...
    @property
    def width(self) -> int: ...
    @width.setter
    def width(self, value: int) -> int: ...

