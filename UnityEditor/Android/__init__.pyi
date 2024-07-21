import typing, abc
from UnityEditor.Build import IOrderedCallback

class IPostGenerateGradleAndroidProject(IOrderedCallback, typing.Protocol):
    @abc.abstractmethod
    def OnPostGenerateGradleAndroidProject(self, path: str) -> None: ...

