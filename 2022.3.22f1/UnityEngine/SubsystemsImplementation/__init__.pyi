import typing, abc
from UnityEngine import ISubsystemDescriptor, ISubsystem

class SubsystemDescriptorStore(abc.ABC):
    @staticmethod
    def RegisterDescriptor(descriptor: SubsystemDescriptorWithProvider) -> None: ...


class SubsystemDescriptorWithProvider_GenericClasses(abc.ABCMeta):
    Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TSubsystem = typing.TypeVar('Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TSubsystem')
    Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TProvider = typing.TypeVar('Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TProvider')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TSubsystem], typing.Type[Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TProvider]]) -> typing.Type[SubsystemDescriptorWithProvider_2[Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TSubsystem, Generic_SubsystemDescriptorWithProvider_GenericClasses_SubsystemDescriptorWithProvider_2_TProvider]]: ...

class SubsystemDescriptorWithProvider(SubsystemDescriptorWithProvider_0, metaclass =SubsystemDescriptorWithProvider_GenericClasses): ...

class SubsystemDescriptorWithProvider_0(ISubsystemDescriptor, abc.ABC):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> str: ...


SubsystemDescriptorWithProvider_2_TSubsystem = typing.TypeVar('SubsystemDescriptorWithProvider_2_TSubsystem')
SubsystemDescriptorWithProvider_2_TProvider = typing.TypeVar('SubsystemDescriptorWithProvider_2_TProvider')
class SubsystemDescriptorWithProvider_2(typing.Generic[SubsystemDescriptorWithProvider_2_TSubsystem, SubsystemDescriptorWithProvider_2_TProvider], SubsystemDescriptorWithProvider_0):
    def __init__(self) -> None: ...
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str) -> str: ...
    def Create(self) -> SubsystemDescriptorWithProvider_2_TSubsystem: ...


class SubsystemProvider_GenericClasses(abc.ABCMeta):
    Generic_SubsystemProvider_GenericClasses_SubsystemProvider_1_TSubsystem = typing.TypeVar('Generic_SubsystemProvider_GenericClasses_SubsystemProvider_1_TSubsystem')
    def __getitem__(self, types : typing.Type[Generic_SubsystemProvider_GenericClasses_SubsystemProvider_1_TSubsystem]) -> typing.Type[SubsystemProvider_1[Generic_SubsystemProvider_GenericClasses_SubsystemProvider_1_TSubsystem]]: ...

class SubsystemProvider(SubsystemProvider_0, metaclass =SubsystemProvider_GenericClasses): ...

class SubsystemProvider_0(abc.ABC):
    @property
    def running(self) -> bool: ...


SubsystemProvider_1_TSubsystem = typing.TypeVar('SubsystemProvider_1_TSubsystem')
class SubsystemProvider_1(typing.Generic[SubsystemProvider_1_TSubsystem], SubsystemProvider_0):
    @property
    def running(self) -> bool: ...
    @abc.abstractmethod
    def Destroy(self) -> None: ...
    @abc.abstractmethod
    def Start(self) -> None: ...
    @abc.abstractmethod
    def Stop(self) -> None: ...


class SubsystemProxy_GenericClasses(abc.ABCMeta):
    Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TSubsystem = typing.TypeVar('Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TSubsystem')
    Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TProvider = typing.TypeVar('Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TProvider')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TSubsystem], typing.Type[Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TProvider]]) -> typing.Type[SubsystemProxy_2[Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TSubsystem, Generic_SubsystemProxy_GenericClasses_SubsystemProxy_2_TProvider]]: ...

SubsystemProxy : SubsystemProxy_GenericClasses

SubsystemProxy_2_TSubsystem = typing.TypeVar('SubsystemProxy_2_TSubsystem')
SubsystemProxy_2_TProvider = typing.TypeVar('SubsystemProxy_2_TProvider')
class SubsystemProxy_2(typing.Generic[SubsystemProxy_2_TSubsystem, SubsystemProxy_2_TProvider]):
    @property
    def provider(self) -> SubsystemProxy_2_TProvider: ...
    @provider.setter
    def provider(self, value: SubsystemProxy_2_TProvider) -> SubsystemProxy_2_TProvider: ...
    @property
    def running(self) -> bool: ...
    @running.setter
    def running(self, value: bool) -> bool: ...


class SubsystemWithProvider_GenericClasses(abc.ABCMeta):
    Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystem = typing.TypeVar('Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystem')
    Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystemDescriptor = typing.TypeVar('Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystemDescriptor')
    Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TProvider = typing.TypeVar('Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TProvider')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystem], typing.Type[Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystemDescriptor], typing.Type[Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TProvider]]) -> typing.Type[SubsystemWithProvider_3[Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystem, Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TSubsystemDescriptor, Generic_SubsystemWithProvider_GenericClasses_SubsystemWithProvider_3_TProvider]]: ...

class SubsystemWithProvider(SubsystemWithProvider_0, metaclass =SubsystemWithProvider_GenericClasses): ...

class SubsystemWithProvider_0(ISubsystem, abc.ABC):
    @property
    def running(self) -> bool: ...
    @running.setter
    def running(self, value: bool) -> bool: ...
    def Destroy(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...


SubsystemWithProvider_3_TSubsystem = typing.TypeVar('SubsystemWithProvider_3_TSubsystem')
SubsystemWithProvider_3_TSubsystemDescriptor = typing.TypeVar('SubsystemWithProvider_3_TSubsystemDescriptor')
SubsystemWithProvider_3_TProvider = typing.TypeVar('SubsystemWithProvider_3_TProvider')
class SubsystemWithProvider_3(typing.Generic[SubsystemWithProvider_3_TSubsystem, SubsystemWithProvider_3_TSubsystemDescriptor, SubsystemWithProvider_3_TProvider], SubsystemWithProvider_0):
    @property
    def running(self) -> bool: ...
    @property
    def subsystemDescriptor(self) -> SubsystemWithProvider_3_TSubsystemDescriptor: ...
    @subsystemDescriptor.setter
    def subsystemDescriptor(self, value: SubsystemWithProvider_3_TSubsystemDescriptor) -> SubsystemWithProvider_3_TSubsystemDescriptor: ...

