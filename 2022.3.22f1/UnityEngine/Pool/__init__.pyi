import typing, clr, abc
from System.Collections.Generic import Dictionary_2, KeyValuePair_2, HashSet_1, List_1
from System import IDisposable, Func_1, Action_1

class CollectionPool_GenericClasses(abc.ABCMeta):
    Generic_CollectionPool_GenericClasses_CollectionPool_2_TCollection = typing.TypeVar('Generic_CollectionPool_GenericClasses_CollectionPool_2_TCollection')
    Generic_CollectionPool_GenericClasses_CollectionPool_2_TItem = typing.TypeVar('Generic_CollectionPool_GenericClasses_CollectionPool_2_TItem')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_CollectionPool_GenericClasses_CollectionPool_2_TCollection], typing.Type[Generic_CollectionPool_GenericClasses_CollectionPool_2_TItem]]) -> typing.Type[CollectionPool_2[Generic_CollectionPool_GenericClasses_CollectionPool_2_TCollection, Generic_CollectionPool_GenericClasses_CollectionPool_2_TItem]]: ...

CollectionPool : CollectionPool_GenericClasses

CollectionPool_2_TCollection = typing.TypeVar('CollectionPool_2_TCollection')
CollectionPool_2_TItem = typing.TypeVar('CollectionPool_2_TItem')
class CollectionPool_2(typing.Generic[CollectionPool_2_TCollection, CollectionPool_2_TItem]):
    def __init__(self) -> None: ...
    @staticmethod
    def Release(toRelease: CollectionPool_2_TCollection) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[CollectionPool_2_TCollection, CollectionPool_2_TItem]
    Get_MethodGroup_CollectionPool_2_TCollection = typing.TypeVar('Get_MethodGroup_CollectionPool_2_TCollection')
    Get_MethodGroup_CollectionPool_2_TItem = typing.TypeVar('Get_MethodGroup_CollectionPool_2_TItem')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_CollectionPool_2_TCollection, Get_MethodGroup_CollectionPool_2_TItem]):
        Get_MethodGroup_CollectionPool_2_TCollection = CollectionPool_2.Get_MethodGroup_CollectionPool_2_TCollection
        Get_MethodGroup_CollectionPool_2_TItem = CollectionPool_2.Get_MethodGroup_CollectionPool_2_TItem
        @typing.overload
        def __call__(self) -> Get_MethodGroup_CollectionPool_2_TCollection:...
        @typing.overload
        def __call__(self, value: clr.Reference[Get_MethodGroup_CollectionPool_2_TCollection]) -> PooledObject_1[Get_MethodGroup_CollectionPool_2_TCollection]:...



class DictionaryPool_GenericClasses(abc.ABCMeta):
    Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TKey = typing.TypeVar('Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TKey')
    Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TValue = typing.TypeVar('Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TKey], typing.Type[Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TValue]]) -> typing.Type[DictionaryPool_2[Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TKey, Generic_DictionaryPool_GenericClasses_DictionaryPool_2_TValue]]: ...

DictionaryPool : DictionaryPool_GenericClasses

DictionaryPool_2_TKey = typing.TypeVar('DictionaryPool_2_TKey')
DictionaryPool_2_TValue = typing.TypeVar('DictionaryPool_2_TValue')
class DictionaryPool_2(typing.Generic[DictionaryPool_2_TKey, DictionaryPool_2_TValue], CollectionPool_2[Dictionary_2[DictionaryPool_2_TKey, DictionaryPool_2_TValue], KeyValuePair_2[DictionaryPool_2_TKey, DictionaryPool_2_TValue]]):
    def __init__(self) -> None: ...


class GenericPool_GenericClasses(abc.ABCMeta):
    Generic_GenericPool_GenericClasses_GenericPool_1_T = typing.TypeVar('Generic_GenericPool_GenericClasses_GenericPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_GenericPool_GenericClasses_GenericPool_1_T]) -> typing.Type[GenericPool_1[Generic_GenericPool_GenericClasses_GenericPool_1_T]]: ...

GenericPool : GenericPool_GenericClasses

GenericPool_1_T = typing.TypeVar('GenericPool_1_T')
class GenericPool_1(typing.Generic[GenericPool_1_T]):
    def __init__(self) -> None: ...
    @staticmethod
    def Release(toRelease: GenericPool_1_T) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[GenericPool_1_T]
    Get_MethodGroup_GenericPool_1_T = typing.TypeVar('Get_MethodGroup_GenericPool_1_T')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_GenericPool_1_T]):
        Get_MethodGroup_GenericPool_1_T = GenericPool_1.Get_MethodGroup_GenericPool_1_T
        @typing.overload
        def __call__(self) -> Get_MethodGroup_GenericPool_1_T:...
        @typing.overload
        def __call__(self, value: clr.Reference[Get_MethodGroup_GenericPool_1_T]) -> PooledObject_1[Get_MethodGroup_GenericPool_1_T]:...



class HashSetPool_GenericClasses(abc.ABCMeta):
    Generic_HashSetPool_GenericClasses_HashSetPool_1_T = typing.TypeVar('Generic_HashSetPool_GenericClasses_HashSetPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_HashSetPool_GenericClasses_HashSetPool_1_T]) -> typing.Type[HashSetPool_1[Generic_HashSetPool_GenericClasses_HashSetPool_1_T]]: ...

HashSetPool : HashSetPool_GenericClasses

HashSetPool_1_T = typing.TypeVar('HashSetPool_1_T')
class HashSetPool_1(typing.Generic[HashSetPool_1_T], CollectionPool_2[HashSet_1[HashSetPool_1_T], HashSetPool_1_T]):
    def __init__(self) -> None: ...


class IObjectPool_GenericClasses(abc.ABCMeta):
    Generic_IObjectPool_GenericClasses_IObjectPool_1_T = typing.TypeVar('Generic_IObjectPool_GenericClasses_IObjectPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_IObjectPool_GenericClasses_IObjectPool_1_T]) -> typing.Type[IObjectPool_1[Generic_IObjectPool_GenericClasses_IObjectPool_1_T]]: ...

IObjectPool : IObjectPool_GenericClasses

IObjectPool_1_T = typing.TypeVar('IObjectPool_1_T')
class IObjectPool_1(typing.Generic[IObjectPool_1_T], typing.Protocol):
    @property
    def CountInactive(self) -> int: ...
    @abc.abstractmethod
    def Clear(self) -> None: ...
    @abc.abstractmethod
    def Release(self, element: IObjectPool_1_T) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[IObjectPool_1_T]
    Get_MethodGroup_IObjectPool_1_T = typing.TypeVar('Get_MethodGroup_IObjectPool_1_T')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_IObjectPool_1_T]):
        Get_MethodGroup_IObjectPool_1_T = IObjectPool_1.Get_MethodGroup_IObjectPool_1_T
        @typing.overload
        def __call__(self) -> Get_MethodGroup_IObjectPool_1_T:...
        @typing.overload
        def __call__(self, v: clr.Reference[Get_MethodGroup_IObjectPool_1_T]) -> PooledObject_1[Get_MethodGroup_IObjectPool_1_T]:...



class LinkedPool_GenericClasses(abc.ABCMeta):
    Generic_LinkedPool_GenericClasses_LinkedPool_1_T = typing.TypeVar('Generic_LinkedPool_GenericClasses_LinkedPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_LinkedPool_GenericClasses_LinkedPool_1_T]) -> typing.Type[LinkedPool_1[Generic_LinkedPool_GenericClasses_LinkedPool_1_T]]: ...

LinkedPool : LinkedPool_GenericClasses

LinkedPool_1_T = typing.TypeVar('LinkedPool_1_T')
class LinkedPool_1(typing.Generic[LinkedPool_1_T], IObjectPool_1[LinkedPool_1_T], IDisposable):
    def __init__(self, createFunc: Func_1[LinkedPool_1_T], actionOnGet: Action_1[LinkedPool_1_T] = ..., actionOnRelease: Action_1[LinkedPool_1_T] = ..., actionOnDestroy: Action_1[LinkedPool_1_T] = ..., collectionCheck: bool = ..., maxSize: int = ...) -> None: ...
    @property
    def CountInactive(self) -> int: ...
    @CountInactive.setter
    def CountInactive(self, value: int) -> int: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def Release(self, item: LinkedPool_1_T) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[LinkedPool_1_T]
    Get_MethodGroup_LinkedPool_1_T = typing.TypeVar('Get_MethodGroup_LinkedPool_1_T')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_LinkedPool_1_T]):
        Get_MethodGroup_LinkedPool_1_T = LinkedPool_1.Get_MethodGroup_LinkedPool_1_T
        @typing.overload
        def __call__(self) -> Get_MethodGroup_LinkedPool_1_T:...
        @typing.overload
        def __call__(self, v: clr.Reference[Get_MethodGroup_LinkedPool_1_T]) -> PooledObject_1[Get_MethodGroup_LinkedPool_1_T]:...



class ListPool_GenericClasses(abc.ABCMeta):
    Generic_ListPool_GenericClasses_ListPool_1_T = typing.TypeVar('Generic_ListPool_GenericClasses_ListPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_ListPool_GenericClasses_ListPool_1_T]) -> typing.Type[ListPool_1[Generic_ListPool_GenericClasses_ListPool_1_T]]: ...

ListPool : ListPool_GenericClasses

ListPool_1_T = typing.TypeVar('ListPool_1_T')
class ListPool_1(typing.Generic[ListPool_1_T], CollectionPool_2[List_1[ListPool_1_T], ListPool_1_T]):
    def __init__(self) -> None: ...


class ObjectPool_GenericClasses(abc.ABCMeta):
    Generic_ObjectPool_GenericClasses_ObjectPool_1_T = typing.TypeVar('Generic_ObjectPool_GenericClasses_ObjectPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_ObjectPool_GenericClasses_ObjectPool_1_T]) -> typing.Type[ObjectPool_1[Generic_ObjectPool_GenericClasses_ObjectPool_1_T]]: ...

ObjectPool : ObjectPool_GenericClasses

ObjectPool_1_T = typing.TypeVar('ObjectPool_1_T')
class ObjectPool_1(typing.Generic[ObjectPool_1_T], IObjectPool_1[ObjectPool_1_T], IDisposable):
    def __init__(self, createFunc: Func_1[ObjectPool_1_T], actionOnGet: Action_1[ObjectPool_1_T] = ..., actionOnRelease: Action_1[ObjectPool_1_T] = ..., actionOnDestroy: Action_1[ObjectPool_1_T] = ..., collectionCheck: bool = ..., defaultCapacity: int = ..., maxSize: int = ...) -> None: ...
    @property
    def CountActive(self) -> int: ...
    @property
    def CountAll(self) -> int: ...
    @CountAll.setter
    def CountAll(self, value: int) -> int: ...
    @property
    def CountInactive(self) -> int: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def Release(self, element: ObjectPool_1_T) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[ObjectPool_1_T]
    Get_MethodGroup_ObjectPool_1_T = typing.TypeVar('Get_MethodGroup_ObjectPool_1_T')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_ObjectPool_1_T]):
        Get_MethodGroup_ObjectPool_1_T = ObjectPool_1.Get_MethodGroup_ObjectPool_1_T
        @typing.overload
        def __call__(self) -> Get_MethodGroup_ObjectPool_1_T:...
        @typing.overload
        def __call__(self, v: clr.Reference[Get_MethodGroup_ObjectPool_1_T]) -> PooledObject_1[Get_MethodGroup_ObjectPool_1_T]:...



class PooledObject_GenericClasses(abc.ABCMeta):
    Generic_PooledObject_GenericClasses_PooledObject_1_T = typing.TypeVar('Generic_PooledObject_GenericClasses_PooledObject_1_T')
    def __getitem__(self, types : typing.Type[Generic_PooledObject_GenericClasses_PooledObject_1_T]) -> typing.Type[PooledObject_1[Generic_PooledObject_GenericClasses_PooledObject_1_T]]: ...

PooledObject : PooledObject_GenericClasses

PooledObject_1_T = typing.TypeVar('PooledObject_1_T')
class PooledObject_1(typing.Generic[PooledObject_1_T], IDisposable):
    pass


class UnsafeGenericPool_GenericClasses(abc.ABCMeta):
    Generic_UnsafeGenericPool_GenericClasses_UnsafeGenericPool_1_T = typing.TypeVar('Generic_UnsafeGenericPool_GenericClasses_UnsafeGenericPool_1_T')
    def __getitem__(self, types : typing.Type[Generic_UnsafeGenericPool_GenericClasses_UnsafeGenericPool_1_T]) -> typing.Type[UnsafeGenericPool_1[Generic_UnsafeGenericPool_GenericClasses_UnsafeGenericPool_1_T]]: ...

UnsafeGenericPool : UnsafeGenericPool_GenericClasses

UnsafeGenericPool_1_T = typing.TypeVar('UnsafeGenericPool_1_T')
class UnsafeGenericPool_1(typing.Generic[UnsafeGenericPool_1_T], abc.ABC):
    @staticmethod
    def Release(toRelease: UnsafeGenericPool_1_T) -> None: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup[UnsafeGenericPool_1_T]
    Get_MethodGroup_UnsafeGenericPool_1_T = typing.TypeVar('Get_MethodGroup_UnsafeGenericPool_1_T')
    class Get_MethodGroup(typing.Generic[Get_MethodGroup_UnsafeGenericPool_1_T]):
        Get_MethodGroup_UnsafeGenericPool_1_T = UnsafeGenericPool_1.Get_MethodGroup_UnsafeGenericPool_1_T
        @typing.overload
        def __call__(self) -> Get_MethodGroup_UnsafeGenericPool_1_T:...
        @typing.overload
        def __call__(self, value: clr.Reference[Get_MethodGroup_UnsafeGenericPool_1_T]) -> PooledObject_1[Get_MethodGroup_UnsafeGenericPool_1_T]:...


