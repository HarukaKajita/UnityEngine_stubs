import abc

class CrashReportingSettings(abc.ABC):
    @classmethod
    @property
    def captureEditorExceptions(cls) -> bool: ...
    @classmethod
    @captureEditorExceptions.setter
    def captureEditorExceptions(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @enabled.setter
    def enabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def logBufferSize(cls) -> int: ...
    @classmethod
    @logBufferSize.setter
    def logBufferSize(cls, value: int) -> int: ...

