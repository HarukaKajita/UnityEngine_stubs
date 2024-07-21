import typing, clr, abc
from System import Array_1, IDisposable, Attribute, Exception, MulticastDelegate, IAsyncResult, AsyncCallback, IEquatable_1, Func_1
from System.Collections.Generic import Dictionary_2, HashSet_1, KeyValuePair_2, IEnumerable_1, List_1, IEnumerator_1
from System.Collections import IDictionary
from System.Reflection import MethodBase, MethodInfo, FieldInfo, PropertyInfo

class ArrayPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_ArrayPropertyBag_GenericClasses_ArrayPropertyBag_1_TElement = typing.TypeVar('Generic_ArrayPropertyBag_GenericClasses_ArrayPropertyBag_1_TElement')
    def __getitem__(self, types : typing.Type[Generic_ArrayPropertyBag_GenericClasses_ArrayPropertyBag_1_TElement]) -> typing.Type[ArrayPropertyBag_1[Generic_ArrayPropertyBag_GenericClasses_ArrayPropertyBag_1_TElement]]: ...

ArrayPropertyBag : ArrayPropertyBag_GenericClasses

ArrayPropertyBag_1_TElement = typing.TypeVar('ArrayPropertyBag_1_TElement')
class ArrayPropertyBag_1(typing.Generic[ArrayPropertyBag_1_TElement], IndexedCollectionPropertyBag_2[Array_1[ArrayPropertyBag_1_TElement], ArrayPropertyBag_1_TElement]):
    def __init__(self) -> None: ...


class AttributesScope(IDisposable):
    def __init__(self, target: IProperty, source: IProperty) -> None: ...
    def Dispose(self) -> None: ...


class ConcreteTypeVisitor(IPropertyBagVisitor, abc.ABC):
    pass


class ContainerPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_ContainerPropertyBag_GenericClasses_ContainerPropertyBag_1_TContainer = typing.TypeVar('Generic_ContainerPropertyBag_GenericClasses_ContainerPropertyBag_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_ContainerPropertyBag_GenericClasses_ContainerPropertyBag_1_TContainer]) -> typing.Type[ContainerPropertyBag_1[Generic_ContainerPropertyBag_GenericClasses_ContainerPropertyBag_1_TContainer]]: ...

ContainerPropertyBag : ContainerPropertyBag_GenericClasses

ContainerPropertyBag_1_TContainer = typing.TypeVar('ContainerPropertyBag_1_TContainer')
class ContainerPropertyBag_1(typing.Generic[ContainerPropertyBag_1_TContainer], PropertyBag_1[ContainerPropertyBag_1_TContainer], INamedProperties_1[ContainerPropertyBag_1_TContainer]):
    def TryGetProperty(self, container: clr.Reference[ContainerPropertyBag_1_TContainer], name: str, property: clr.Reference[IProperty_1[ContainerPropertyBag_1_TContainer]]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[ContainerPropertyBag_1_TContainer]
    GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer = typing.TypeVar('GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer]):
        GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer = ContainerPropertyBag_1.GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer]) -> PropertyCollection_1[GetProperties_MethodGroup_ContainerPropertyBag_1_TContainer]:...



class CreatePropertyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DelegateProperty_GenericClasses(abc.ABCMeta):
    Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TContainer = typing.TypeVar('Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TContainer')
    Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TValue = typing.TypeVar('Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TContainer], typing.Type[Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TValue]]) -> typing.Type[DelegateProperty_2[Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TContainer, Generic_DelegateProperty_GenericClasses_DelegateProperty_2_TValue]]: ...

DelegateProperty : DelegateProperty_GenericClasses

DelegateProperty_2_TContainer = typing.TypeVar('DelegateProperty_2_TContainer')
DelegateProperty_2_TValue = typing.TypeVar('DelegateProperty_2_TValue')
class DelegateProperty_2(typing.Generic[DelegateProperty_2_TContainer, DelegateProperty_2_TValue], Property_2[DelegateProperty_2_TContainer, DelegateProperty_2_TValue]):
    def __init__(self, name: str, getter: PropertyGetter_2[DelegateProperty_2_TContainer, DelegateProperty_2_TValue], setter: PropertySetter_2[DelegateProperty_2_TContainer, DelegateProperty_2_TValue] = ...) -> None: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    def GetValue(self, container: clr.Reference[DelegateProperty_2_TContainer]) -> DelegateProperty_2_TValue: ...
    def SetValue(self, container: clr.Reference[DelegateProperty_2_TContainer], value: DelegateProperty_2_TValue) -> None: ...


class DictionaryPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TKey = typing.TypeVar('Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TKey')
    Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TValue = typing.TypeVar('Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TKey], typing.Type[Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TValue]]) -> typing.Type[DictionaryPropertyBag_2[Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TKey, Generic_DictionaryPropertyBag_GenericClasses_DictionaryPropertyBag_2_TValue]]: ...

DictionaryPropertyBag : DictionaryPropertyBag_GenericClasses

DictionaryPropertyBag_2_TKey = typing.TypeVar('DictionaryPropertyBag_2_TKey')
DictionaryPropertyBag_2_TValue = typing.TypeVar('DictionaryPropertyBag_2_TValue')
class DictionaryPropertyBag_2(typing.Generic[DictionaryPropertyBag_2_TKey, DictionaryPropertyBag_2_TValue], KeyValueCollectionPropertyBag_3[Dictionary_2[DictionaryPropertyBag_2_TKey, DictionaryPropertyBag_2_TValue], DictionaryPropertyBag_2_TKey, DictionaryPropertyBag_2_TValue]):
    def __init__(self) -> None: ...


class DontCreatePropertyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class ExcludeContext_GenericClasses(abc.ABCMeta):
    Generic_ExcludeContext_GenericClasses_ExcludeContext_1_TContainer = typing.TypeVar('Generic_ExcludeContext_GenericClasses_ExcludeContext_1_TContainer')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_ExcludeContext_GenericClasses_ExcludeContext_1_TContainer]) -> typing.Type[ExcludeContext_1[Generic_ExcludeContext_GenericClasses_ExcludeContext_1_TContainer]]: ...
    Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TContainer = typing.TypeVar('Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TContainer')
    Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TValue = typing.TypeVar('Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TContainer], typing.Type[Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TValue]]) -> typing.Type[ExcludeContext_2[Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TContainer, Generic_ExcludeContext_GenericClasses_ExcludeContext_2_TValue]]: ...

ExcludeContext : ExcludeContext_GenericClasses

ExcludeContext_1_TContainer = typing.TypeVar('ExcludeContext_1_TContainer')
class ExcludeContext_1(typing.Generic[ExcludeContext_1_TContainer]):
    @property
    def Property(self) -> IProperty_1[ExcludeContext_1_TContainer]: ...


ExcludeContext_2_TContainer = typing.TypeVar('ExcludeContext_2_TContainer')
ExcludeContext_2_TValue = typing.TypeVar('ExcludeContext_2_TValue')
class ExcludeContext_2(typing.Generic[ExcludeContext_2_TContainer, ExcludeContext_2_TValue]):
    @property
    def Property(self) -> Property_2[ExcludeContext_2_TContainer, ExcludeContext_2_TValue]: ...


class GeneratePropertyBagAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class GeneratePropertyBagsForAssemblyAttribute(Attribute):
    def __init__(self) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class GeneratePropertyBagsForTypeAttribute(Attribute):
    def __init__(self, type: typing.Type[typing.Any]) -> None: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class GeneratePropertyBagsForTypesQualifiedWithAttribute(Attribute):
    def __init__(self, type: typing.Type[typing.Any], options: TypeGenerationOptions = ...) -> None: ...
    @property
    def Options(self) -> TypeGenerationOptions: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class HashSetPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_HashSetPropertyBag_GenericClasses_HashSetPropertyBag_1_TElement = typing.TypeVar('Generic_HashSetPropertyBag_GenericClasses_HashSetPropertyBag_1_TElement')
    def __getitem__(self, types : typing.Type[Generic_HashSetPropertyBag_GenericClasses_HashSetPropertyBag_1_TElement]) -> typing.Type[HashSetPropertyBag_1[Generic_HashSetPropertyBag_GenericClasses_HashSetPropertyBag_1_TElement]]: ...

HashSetPropertyBag : HashSetPropertyBag_GenericClasses

HashSetPropertyBag_1_TElement = typing.TypeVar('HashSetPropertyBag_1_TElement')
class HashSetPropertyBag_1(typing.Generic[HashSetPropertyBag_1_TElement], SetPropertyBagBase_2[HashSet_1[HashSetPropertyBag_1_TElement], HashSetPropertyBag_1_TElement]):
    def __init__(self) -> None: ...


class ICollectionElementProperty(typing.Protocol):
    pass


class ICollectionPropertyAccept_GenericClasses(abc.ABCMeta):
    Generic_ICollectionPropertyAccept_GenericClasses_ICollectionPropertyAccept_1_TCollection = typing.TypeVar('Generic_ICollectionPropertyAccept_GenericClasses_ICollectionPropertyAccept_1_TCollection')
    def __getitem__(self, types : typing.Type[Generic_ICollectionPropertyAccept_GenericClasses_ICollectionPropertyAccept_1_TCollection]) -> typing.Type[ICollectionPropertyAccept_1[Generic_ICollectionPropertyAccept_GenericClasses_ICollectionPropertyAccept_1_TCollection]]: ...

ICollectionPropertyAccept : ICollectionPropertyAccept_GenericClasses

ICollectionPropertyAccept_1_TCollection = typing.TypeVar('ICollectionPropertyAccept_1_TCollection')
class ICollectionPropertyAccept_1(typing.Generic[ICollectionPropertyAccept_1_TCollection], typing.Protocol):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup[ICollectionPropertyAccept_1_TCollection]
    Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection = typing.TypeVar('Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection')
    class Accept_MethodGroup(typing.Generic[Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection]):
        Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection = ICollectionPropertyAccept_1.Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection
        def __getitem__(self, t:typing.Type[Accept_1_T1]) -> Accept_1[Accept_MethodGroup_ICollectionPropertyAccept_1_TCollection, Accept_1_T1]: ...

        Accept_1_ICollectionPropertyAccept_1_TCollection = typing.TypeVar('Accept_1_ICollectionPropertyAccept_1_TCollection')
        Accept_1_T1 = typing.TypeVar('Accept_1_T1')
        class Accept_1(typing.Generic[Accept_1_ICollectionPropertyAccept_1_TCollection, Accept_1_T1]):
            Accept_1_ICollectionPropertyAccept_1_TCollection = ICollectionPropertyAccept_1.Accept_MethodGroup.Accept_1_ICollectionPropertyAccept_1_TCollection
            Accept_1_TContainer = ICollectionPropertyAccept_1.Accept_MethodGroup.Accept_1_T1
            def __call__(self, visitor: ICollectionPropertyVisitor, property: Property_2[Accept_1_TContainer, Accept_1_ICollectionPropertyAccept_1_TCollection], container: clr.Reference[Accept_1_TContainer], collection: clr.Reference[Accept_1_ICollectionPropertyAccept_1_TCollection]) -> None:...




class ICollectionPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TCollection = typing.TypeVar('Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TCollection')
    Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TElement = typing.TypeVar('Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TCollection], typing.Type[Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TElement]]) -> typing.Type[ICollectionPropertyBag_2[Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TCollection, Generic_ICollectionPropertyBag_GenericClasses_ICollectionPropertyBag_2_TElement]]: ...

ICollectionPropertyBag : ICollectionPropertyBag_GenericClasses

ICollectionPropertyBag_2_TCollection = typing.TypeVar('ICollectionPropertyBag_2_TCollection')
ICollectionPropertyBag_2_TElement = typing.TypeVar('ICollectionPropertyBag_2_TElement')
class ICollectionPropertyBag_2(typing.Generic[ICollectionPropertyBag_2_TCollection, ICollectionPropertyBag_2_TElement], IPropertyBag_1[ICollectionPropertyBag_2_TCollection], ICollectionPropertyBagAccept_1[ICollectionPropertyBag_2_TCollection], typing.Protocol):
    pass


class ICollectionPropertyBagAccept_GenericClasses(abc.ABCMeta):
    Generic_ICollectionPropertyBagAccept_GenericClasses_ICollectionPropertyBagAccept_1_TContainer = typing.TypeVar('Generic_ICollectionPropertyBagAccept_GenericClasses_ICollectionPropertyBagAccept_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_ICollectionPropertyBagAccept_GenericClasses_ICollectionPropertyBagAccept_1_TContainer]) -> typing.Type[ICollectionPropertyBagAccept_1[Generic_ICollectionPropertyBagAccept_GenericClasses_ICollectionPropertyBagAccept_1_TContainer]]: ...

ICollectionPropertyBagAccept : ICollectionPropertyBagAccept_GenericClasses

ICollectionPropertyBagAccept_1_TContainer = typing.TypeVar('ICollectionPropertyBagAccept_1_TContainer')
class ICollectionPropertyBagAccept_1(typing.Generic[ICollectionPropertyBagAccept_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: ICollectionPropertyBagVisitor, container: clr.Reference[ICollectionPropertyBagAccept_1_TContainer]) -> None: ...


class ICollectionPropertyBagVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_2_T1], typing.Type[Visit_2_T2]]) -> Visit_2[Visit_2_T1, Visit_2_T2]: ...

        Visit_2_T1 = typing.TypeVar('Visit_2_T1')
        Visit_2_T2 = typing.TypeVar('Visit_2_T2')
        class Visit_2(typing.Generic[Visit_2_T1, Visit_2_T2]):
            Visit_2_TCollection = ICollectionPropertyBagVisitor.Visit_MethodGroup.Visit_2_T1
            Visit_2_TElement = ICollectionPropertyBagVisitor.Visit_MethodGroup.Visit_2_T2
            def __call__(self, properties: ICollectionPropertyBag_2[Visit_2_TCollection, Visit_2_TElement], container: clr.Reference[Visit_2_TCollection]) -> None:...




class ICollectionPropertyVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_3_T1], typing.Type[Visit_3_T2], typing.Type[Visit_3_T3]]) -> Visit_3[Visit_3_T1, Visit_3_T2, Visit_3_T3]: ...

        Visit_3_T1 = typing.TypeVar('Visit_3_T1')
        Visit_3_T2 = typing.TypeVar('Visit_3_T2')
        Visit_3_T3 = typing.TypeVar('Visit_3_T3')
        class Visit_3(typing.Generic[Visit_3_T1, Visit_3_T2, Visit_3_T3]):
            Visit_3_TContainer = ICollectionPropertyVisitor.Visit_MethodGroup.Visit_3_T1
            Visit_3_TCollection = ICollectionPropertyVisitor.Visit_MethodGroup.Visit_3_T2
            Visit_3_TElement = ICollectionPropertyVisitor.Visit_MethodGroup.Visit_3_T3
            def __call__(self, property: Property_2[Visit_3_TContainer, Visit_3_TCollection], container: clr.Reference[Visit_3_TContainer], collection: clr.Reference[Visit_3_TCollection]) -> None:...




class IDictionaryElementProperty_GenericClasses(abc.ABCMeta):
    Generic_IDictionaryElementProperty_GenericClasses_IDictionaryElementProperty_1_TKey = typing.TypeVar('Generic_IDictionaryElementProperty_GenericClasses_IDictionaryElementProperty_1_TKey')
    def __getitem__(self, types : typing.Type[Generic_IDictionaryElementProperty_GenericClasses_IDictionaryElementProperty_1_TKey]) -> typing.Type[IDictionaryElementProperty_1[Generic_IDictionaryElementProperty_GenericClasses_IDictionaryElementProperty_1_TKey]]: ...

class IDictionaryElementProperty(IDictionaryElementProperty_0, metaclass =IDictionaryElementProperty_GenericClasses): ...

class IDictionaryElementProperty_0(ICollectionElementProperty, typing.Protocol):
    @property
    def ObjectKey(self) -> typing.Any: ...


IDictionaryElementProperty_1_TKey = typing.TypeVar('IDictionaryElementProperty_1_TKey', covariant=True)
class IDictionaryElementProperty_1(typing.Generic[IDictionaryElementProperty_1_TKey], IDictionaryElementProperty_0, typing.Protocol):
    @property
    def Key(self) -> IDictionaryElementProperty_1_TKey: ...


class IDictionaryPropertyAccept_GenericClasses(abc.ABCMeta):
    Generic_IDictionaryPropertyAccept_GenericClasses_IDictionaryPropertyAccept_1_TDictionary = typing.TypeVar('Generic_IDictionaryPropertyAccept_GenericClasses_IDictionaryPropertyAccept_1_TDictionary')
    def __getitem__(self, types : typing.Type[Generic_IDictionaryPropertyAccept_GenericClasses_IDictionaryPropertyAccept_1_TDictionary]) -> typing.Type[IDictionaryPropertyAccept_1[Generic_IDictionaryPropertyAccept_GenericClasses_IDictionaryPropertyAccept_1_TDictionary]]: ...

IDictionaryPropertyAccept : IDictionaryPropertyAccept_GenericClasses

IDictionaryPropertyAccept_1_TDictionary = typing.TypeVar('IDictionaryPropertyAccept_1_TDictionary')
class IDictionaryPropertyAccept_1(typing.Generic[IDictionaryPropertyAccept_1_TDictionary], typing.Protocol):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup[IDictionaryPropertyAccept_1_TDictionary]
    Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary = typing.TypeVar('Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary')
    class Accept_MethodGroup(typing.Generic[Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary]):
        Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary = IDictionaryPropertyAccept_1.Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary
        def __getitem__(self, t:typing.Type[Accept_1_T1]) -> Accept_1[Accept_MethodGroup_IDictionaryPropertyAccept_1_TDictionary, Accept_1_T1]: ...

        Accept_1_IDictionaryPropertyAccept_1_TDictionary = typing.TypeVar('Accept_1_IDictionaryPropertyAccept_1_TDictionary')
        Accept_1_T1 = typing.TypeVar('Accept_1_T1')
        class Accept_1(typing.Generic[Accept_1_IDictionaryPropertyAccept_1_TDictionary, Accept_1_T1]):
            Accept_1_IDictionaryPropertyAccept_1_TDictionary = IDictionaryPropertyAccept_1.Accept_MethodGroup.Accept_1_IDictionaryPropertyAccept_1_TDictionary
            Accept_1_TContainer = IDictionaryPropertyAccept_1.Accept_MethodGroup.Accept_1_T1
            def __call__(self, visitor: IDictionaryPropertyVisitor, property: Property_2[Accept_1_TContainer, Accept_1_IDictionaryPropertyAccept_1_TDictionary], container: clr.Reference[Accept_1_TContainer], dictionary: clr.Reference[Accept_1_IDictionaryPropertyAccept_1_TDictionary]) -> None:...




class IDictionaryPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TDictionary = typing.TypeVar('Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TDictionary')
    Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TKey = typing.TypeVar('Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TKey')
    Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TValue = typing.TypeVar('Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TDictionary], typing.Type[Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TKey], typing.Type[Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TValue]]) -> typing.Type[IDictionaryPropertyBag_3[Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TDictionary, Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TKey, Generic_IDictionaryPropertyBag_GenericClasses_IDictionaryPropertyBag_3_TValue]]: ...

IDictionaryPropertyBag : IDictionaryPropertyBag_GenericClasses

IDictionaryPropertyBag_3_TDictionary = typing.TypeVar('IDictionaryPropertyBag_3_TDictionary')
IDictionaryPropertyBag_3_TKey = typing.TypeVar('IDictionaryPropertyBag_3_TKey')
IDictionaryPropertyBag_3_TValue = typing.TypeVar('IDictionaryPropertyBag_3_TValue')
class IDictionaryPropertyBag_3(typing.Generic[IDictionaryPropertyBag_3_TDictionary, IDictionaryPropertyBag_3_TKey, IDictionaryPropertyBag_3_TValue], ICollectionPropertyBag_2[IDictionaryPropertyBag_3_TDictionary, KeyValuePair_2[IDictionaryPropertyBag_3_TKey, IDictionaryPropertyBag_3_TValue]], IKeyedProperties_2[IDictionaryPropertyBag_3_TDictionary, typing.Any], IDictionaryPropertyAccept_1[IDictionaryPropertyBag_3_TDictionary], IDictionaryPropertyBagAccept_1[IDictionaryPropertyBag_3_TDictionary], typing.Protocol):
    pass


class IDictionaryPropertyBagAccept_GenericClasses(abc.ABCMeta):
    Generic_IDictionaryPropertyBagAccept_GenericClasses_IDictionaryPropertyBagAccept_1_TContainer = typing.TypeVar('Generic_IDictionaryPropertyBagAccept_GenericClasses_IDictionaryPropertyBagAccept_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IDictionaryPropertyBagAccept_GenericClasses_IDictionaryPropertyBagAccept_1_TContainer]) -> typing.Type[IDictionaryPropertyBagAccept_1[Generic_IDictionaryPropertyBagAccept_GenericClasses_IDictionaryPropertyBagAccept_1_TContainer]]: ...

IDictionaryPropertyBagAccept : IDictionaryPropertyBagAccept_GenericClasses

IDictionaryPropertyBagAccept_1_TContainer = typing.TypeVar('IDictionaryPropertyBagAccept_1_TContainer')
class IDictionaryPropertyBagAccept_1(typing.Generic[IDictionaryPropertyBagAccept_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: IDictionaryPropertyBagVisitor, container: clr.Reference[IDictionaryPropertyBagAccept_1_TContainer]) -> None: ...


class IDictionaryPropertyBagVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_3_T1], typing.Type[Visit_3_T2], typing.Type[Visit_3_T3]]) -> Visit_3[Visit_3_T1, Visit_3_T2, Visit_3_T3]: ...

        Visit_3_T1 = typing.TypeVar('Visit_3_T1')
        Visit_3_T2 = typing.TypeVar('Visit_3_T2')
        Visit_3_T3 = typing.TypeVar('Visit_3_T3')
        class Visit_3(typing.Generic[Visit_3_T1, Visit_3_T2, Visit_3_T3]):
            Visit_3_TDictionary = IDictionaryPropertyBagVisitor.Visit_MethodGroup.Visit_3_T1
            Visit_3_TKey = IDictionaryPropertyBagVisitor.Visit_MethodGroup.Visit_3_T2
            Visit_3_TValue = IDictionaryPropertyBagVisitor.Visit_MethodGroup.Visit_3_T3
            def __call__(self, properties: IDictionaryPropertyBag_3[Visit_3_TDictionary, Visit_3_TKey, Visit_3_TValue], container: clr.Reference[Visit_3_TDictionary]) -> None:...




class IDictionaryPropertyVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_4_T1], typing.Type[Visit_4_T2], typing.Type[Visit_4_T3], typing.Type[Visit_4_T4]]) -> Visit_4[Visit_4_T1, Visit_4_T2, Visit_4_T3, Visit_4_T4]: ...

        Visit_4_T1 = typing.TypeVar('Visit_4_T1')
        Visit_4_T2 = typing.TypeVar('Visit_4_T2')
        Visit_4_T3 = typing.TypeVar('Visit_4_T3')
        Visit_4_T4 = typing.TypeVar('Visit_4_T4')
        class Visit_4(typing.Generic[Visit_4_T1, Visit_4_T2, Visit_4_T3, Visit_4_T4]):
            Visit_4_TContainer = IDictionaryPropertyVisitor.Visit_MethodGroup.Visit_4_T1
            Visit_4_TDictionary = IDictionaryPropertyVisitor.Visit_MethodGroup.Visit_4_T2
            Visit_4_TKey = IDictionaryPropertyVisitor.Visit_MethodGroup.Visit_4_T3
            Visit_4_TValue = IDictionaryPropertyVisitor.Visit_MethodGroup.Visit_4_T4
            def __call__(self, property: Property_2[Visit_4_TContainer, Visit_4_TDictionary], container: clr.Reference[Visit_4_TContainer], dictionary: clr.Reference[Visit_4_TDictionary]) -> None:...




class IExcludeContravariantPropertyAdapter_GenericClasses(abc.ABCMeta):
    Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_1_TValue = typing.TypeVar('Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_1_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_1_TValue]) -> typing.Type[IExcludeContravariantPropertyAdapter_1[Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_1_TValue]]: ...
    Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TContainer = typing.TypeVar('Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TContainer')
    Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TValue = typing.TypeVar('Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TContainer], typing.Type[Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TValue]]) -> typing.Type[IExcludeContravariantPropertyAdapter_2[Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TContainer, Generic_IExcludeContravariantPropertyAdapter_GenericClasses_IExcludeContravariantPropertyAdapter_2_TValue]]: ...

IExcludeContravariantPropertyAdapter : IExcludeContravariantPropertyAdapter_GenericClasses

IExcludeContravariantPropertyAdapter_1_TValue = typing.TypeVar('IExcludeContravariantPropertyAdapter_1_TValue', contravariant=True)
class IExcludeContravariantPropertyAdapter_1(typing.Generic[IExcludeContravariantPropertyAdapter_1_TValue], IPropertyVisitorAdapter, typing.Protocol):
    # Skipped IsExcluded due to it being static, abstract and generic.

    IsExcluded : IsExcluded_MethodGroup[IExcludeContravariantPropertyAdapter_1_TValue]
    IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue = typing.TypeVar('IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue', contravariant=True)
    class IsExcluded_MethodGroup(typing.Generic[IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue]):
        IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue = IExcludeContravariantPropertyAdapter_1.IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue
        def __getitem__(self, t:typing.Type[IsExcluded_1_T1]) -> IsExcluded_1[IsExcluded_MethodGroup_IExcludeContravariantPropertyAdapter_1_TValue, IsExcluded_1_T1]: ...

        IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue = typing.TypeVar('IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue', contravariant=True)
        IsExcluded_1_T1 = typing.TypeVar('IsExcluded_1_T1')
        class IsExcluded_1(typing.Generic[IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue, IsExcluded_1_T1]):
            IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue = IExcludeContravariantPropertyAdapter_1.IsExcluded_MethodGroup.IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue
            IsExcluded_1_TContainer = IExcludeContravariantPropertyAdapter_1.IsExcluded_MethodGroup.IsExcluded_1_T1
            def __call__(self, context: clr.Reference[ExcludeContext_1[IsExcluded_1_TContainer]], container: clr.Reference[IsExcluded_1_TContainer], value: IsExcluded_1_IExcludeContravariantPropertyAdapter_1_TValue) -> bool:...




IExcludeContravariantPropertyAdapter_2_TContainer = typing.TypeVar('IExcludeContravariantPropertyAdapter_2_TContainer')
IExcludeContravariantPropertyAdapter_2_TValue = typing.TypeVar('IExcludeContravariantPropertyAdapter_2_TValue', contravariant=True)
class IExcludeContravariantPropertyAdapter_2(typing.Generic[IExcludeContravariantPropertyAdapter_2_TContainer, IExcludeContravariantPropertyAdapter_2_TValue], IPropertyVisitorAdapter, typing.Protocol):
    @abc.abstractmethod
    def IsExcluded(self, context: clr.Reference[ExcludeContext_1[IExcludeContravariantPropertyAdapter_2_TContainer]], container: clr.Reference[IExcludeContravariantPropertyAdapter_2_TContainer], value: IExcludeContravariantPropertyAdapter_2_TValue) -> bool: ...


class IExcludePropertyAdapter_GenericClasses(abc.ABCMeta):
    Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_1_TValue = typing.TypeVar('Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_1_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_1_TValue]) -> typing.Type[IExcludePropertyAdapter_1[Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_1_TValue]]: ...
    Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TContainer = typing.TypeVar('Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TContainer')
    Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TValue = typing.TypeVar('Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TContainer], typing.Type[Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TValue]]) -> typing.Type[IExcludePropertyAdapter_2[Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TContainer, Generic_IExcludePropertyAdapter_GenericClasses_IExcludePropertyAdapter_2_TValue]]: ...

class IExcludePropertyAdapter(IExcludePropertyAdapter_0, metaclass =IExcludePropertyAdapter_GenericClasses): ...

class IExcludePropertyAdapter_0(IPropertyVisitorAdapter, typing.Protocol):
    # Skipped IsExcluded due to it being static, abstract and generic.

    IsExcluded : IsExcluded_MethodGroup
    class IsExcluded_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[IsExcluded_2_T1], typing.Type[IsExcluded_2_T2]]) -> IsExcluded_2[IsExcluded_2_T1, IsExcluded_2_T2]: ...

        IsExcluded_2_T1 = typing.TypeVar('IsExcluded_2_T1')
        IsExcluded_2_T2 = typing.TypeVar('IsExcluded_2_T2')
        class IsExcluded_2(typing.Generic[IsExcluded_2_T1, IsExcluded_2_T2]):
            IsExcluded_2_TContainer = IExcludePropertyAdapter_0.IsExcluded_MethodGroup.IsExcluded_2_T1
            IsExcluded_2_TValue = IExcludePropertyAdapter_0.IsExcluded_MethodGroup.IsExcluded_2_T2
            def __call__(self, context: clr.Reference[ExcludeContext_2[IsExcluded_2_TContainer, IsExcluded_2_TValue]], container: clr.Reference[IsExcluded_2_TContainer], value: clr.Reference[IsExcluded_2_TValue]) -> bool:...




IExcludePropertyAdapter_1_TValue = typing.TypeVar('IExcludePropertyAdapter_1_TValue')
class IExcludePropertyAdapter_1(typing.Generic[IExcludePropertyAdapter_1_TValue], IPropertyVisitorAdapter, typing.Protocol):
    # Skipped IsExcluded due to it being static, abstract and generic.

    IsExcluded : IsExcluded_MethodGroup[IExcludePropertyAdapter_1_TValue]
    IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue = typing.TypeVar('IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue')
    class IsExcluded_MethodGroup(typing.Generic[IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue]):
        IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue = IExcludePropertyAdapter_1.IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue
        def __getitem__(self, t:typing.Type[IsExcluded_1_T1]) -> IsExcluded_1[IsExcluded_MethodGroup_IExcludePropertyAdapter_1_TValue, IsExcluded_1_T1]: ...

        IsExcluded_1_IExcludePropertyAdapter_1_TValue = typing.TypeVar('IsExcluded_1_IExcludePropertyAdapter_1_TValue')
        IsExcluded_1_T1 = typing.TypeVar('IsExcluded_1_T1')
        class IsExcluded_1(typing.Generic[IsExcluded_1_IExcludePropertyAdapter_1_TValue, IsExcluded_1_T1]):
            IsExcluded_1_IExcludePropertyAdapter_1_TValue = IExcludePropertyAdapter_1.IsExcluded_MethodGroup.IsExcluded_1_IExcludePropertyAdapter_1_TValue
            IsExcluded_1_TContainer = IExcludePropertyAdapter_1.IsExcluded_MethodGroup.IsExcluded_1_T1
            def __call__(self, context: clr.Reference[ExcludeContext_2[IsExcluded_1_TContainer, IsExcluded_1_IExcludePropertyAdapter_1_TValue]], container: clr.Reference[IsExcluded_1_TContainer], value: clr.Reference[IsExcluded_1_IExcludePropertyAdapter_1_TValue]) -> bool:...




IExcludePropertyAdapter_2_TContainer = typing.TypeVar('IExcludePropertyAdapter_2_TContainer')
IExcludePropertyAdapter_2_TValue = typing.TypeVar('IExcludePropertyAdapter_2_TValue')
class IExcludePropertyAdapter_2(typing.Generic[IExcludePropertyAdapter_2_TContainer, IExcludePropertyAdapter_2_TValue], IPropertyVisitorAdapter, typing.Protocol):
    @abc.abstractmethod
    def IsExcluded(self, context: clr.Reference[ExcludeContext_2[IExcludePropertyAdapter_2_TContainer, IExcludePropertyAdapter_2_TValue]], container: clr.Reference[IExcludePropertyAdapter_2_TContainer], value: clr.Reference[IExcludePropertyAdapter_2_TValue]) -> bool: ...


class IIndexedProperties_GenericClasses(abc.ABCMeta):
    Generic_IIndexedProperties_GenericClasses_IIndexedProperties_1_TContainer = typing.TypeVar('Generic_IIndexedProperties_GenericClasses_IIndexedProperties_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IIndexedProperties_GenericClasses_IIndexedProperties_1_TContainer]) -> typing.Type[IIndexedProperties_1[Generic_IIndexedProperties_GenericClasses_IIndexedProperties_1_TContainer]]: ...

IIndexedProperties : IIndexedProperties_GenericClasses

IIndexedProperties_1_TContainer = typing.TypeVar('IIndexedProperties_1_TContainer')
class IIndexedProperties_1(typing.Generic[IIndexedProperties_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def TryGetProperty(self, container: clr.Reference[IIndexedProperties_1_TContainer], index: int, property: clr.Reference[IProperty_1[IIndexedProperties_1_TContainer]]) -> bool: ...


class IKeyedProperties_GenericClasses(abc.ABCMeta):
    Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TContainer = typing.TypeVar('Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TContainer')
    Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TKey = typing.TypeVar('Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TKey')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TContainer], typing.Type[Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TKey]]) -> typing.Type[IKeyedProperties_2[Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TContainer, Generic_IKeyedProperties_GenericClasses_IKeyedProperties_2_TKey]]: ...

IKeyedProperties : IKeyedProperties_GenericClasses

IKeyedProperties_2_TContainer = typing.TypeVar('IKeyedProperties_2_TContainer')
IKeyedProperties_2_TKey = typing.TypeVar('IKeyedProperties_2_TKey')
class IKeyedProperties_2(typing.Generic[IKeyedProperties_2_TContainer, IKeyedProperties_2_TKey], typing.Protocol):
    @abc.abstractmethod
    def TryGetProperty(self, container: clr.Reference[IKeyedProperties_2_TContainer], key: IKeyedProperties_2_TKey, property: clr.Reference[IProperty_1[IKeyedProperties_2_TContainer]]) -> bool: ...


class IListElementProperty(ICollectionElementProperty, typing.Protocol):
    @property
    def Index(self) -> int: ...


class IListPropertyAccept_GenericClasses(abc.ABCMeta):
    Generic_IListPropertyAccept_GenericClasses_IListPropertyAccept_1_TList = typing.TypeVar('Generic_IListPropertyAccept_GenericClasses_IListPropertyAccept_1_TList')
    def __getitem__(self, types : typing.Type[Generic_IListPropertyAccept_GenericClasses_IListPropertyAccept_1_TList]) -> typing.Type[IListPropertyAccept_1[Generic_IListPropertyAccept_GenericClasses_IListPropertyAccept_1_TList]]: ...

IListPropertyAccept : IListPropertyAccept_GenericClasses

IListPropertyAccept_1_TList = typing.TypeVar('IListPropertyAccept_1_TList')
class IListPropertyAccept_1(typing.Generic[IListPropertyAccept_1_TList], typing.Protocol):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup[IListPropertyAccept_1_TList]
    Accept_MethodGroup_IListPropertyAccept_1_TList = typing.TypeVar('Accept_MethodGroup_IListPropertyAccept_1_TList')
    class Accept_MethodGroup(typing.Generic[Accept_MethodGroup_IListPropertyAccept_1_TList]):
        Accept_MethodGroup_IListPropertyAccept_1_TList = IListPropertyAccept_1.Accept_MethodGroup_IListPropertyAccept_1_TList
        def __getitem__(self, t:typing.Type[Accept_1_T1]) -> Accept_1[Accept_MethodGroup_IListPropertyAccept_1_TList, Accept_1_T1]: ...

        Accept_1_IListPropertyAccept_1_TList = typing.TypeVar('Accept_1_IListPropertyAccept_1_TList')
        Accept_1_T1 = typing.TypeVar('Accept_1_T1')
        class Accept_1(typing.Generic[Accept_1_IListPropertyAccept_1_TList, Accept_1_T1]):
            Accept_1_IListPropertyAccept_1_TList = IListPropertyAccept_1.Accept_MethodGroup.Accept_1_IListPropertyAccept_1_TList
            Accept_1_TContainer = IListPropertyAccept_1.Accept_MethodGroup.Accept_1_T1
            def __call__(self, visitor: IListPropertyVisitor, property: Property_2[Accept_1_TContainer, Accept_1_IListPropertyAccept_1_TList], container: clr.Reference[Accept_1_TContainer], list: clr.Reference[Accept_1_IListPropertyAccept_1_TList]) -> None:...




class IListPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TList = typing.TypeVar('Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TList')
    Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TElement = typing.TypeVar('Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TList], typing.Type[Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TElement]]) -> typing.Type[IListPropertyBag_2[Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TList, Generic_IListPropertyBag_GenericClasses_IListPropertyBag_2_TElement]]: ...

IListPropertyBag : IListPropertyBag_GenericClasses

IListPropertyBag_2_TList = typing.TypeVar('IListPropertyBag_2_TList')
IListPropertyBag_2_TElement = typing.TypeVar('IListPropertyBag_2_TElement')
class IListPropertyBag_2(typing.Generic[IListPropertyBag_2_TList, IListPropertyBag_2_TElement], ICollectionPropertyBag_2[IListPropertyBag_2_TList, IListPropertyBag_2_TElement], IIndexedProperties_1[IListPropertyBag_2_TList], IListPropertyAccept_1[IListPropertyBag_2_TList], IListPropertyBagAccept_1[IListPropertyBag_2_TList], typing.Protocol):
    pass


class IListPropertyBagAccept_GenericClasses(abc.ABCMeta):
    Generic_IListPropertyBagAccept_GenericClasses_IListPropertyBagAccept_1_TContainer = typing.TypeVar('Generic_IListPropertyBagAccept_GenericClasses_IListPropertyBagAccept_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IListPropertyBagAccept_GenericClasses_IListPropertyBagAccept_1_TContainer]) -> typing.Type[IListPropertyBagAccept_1[Generic_IListPropertyBagAccept_GenericClasses_IListPropertyBagAccept_1_TContainer]]: ...

IListPropertyBagAccept : IListPropertyBagAccept_GenericClasses

IListPropertyBagAccept_1_TContainer = typing.TypeVar('IListPropertyBagAccept_1_TContainer')
class IListPropertyBagAccept_1(typing.Generic[IListPropertyBagAccept_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: IListPropertyBagVisitor, container: clr.Reference[IListPropertyBagAccept_1_TContainer]) -> None: ...


class IListPropertyBagVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_2_T1], typing.Type[Visit_2_T2]]) -> Visit_2[Visit_2_T1, Visit_2_T2]: ...

        Visit_2_T1 = typing.TypeVar('Visit_2_T1')
        Visit_2_T2 = typing.TypeVar('Visit_2_T2')
        class Visit_2(typing.Generic[Visit_2_T1, Visit_2_T2]):
            Visit_2_TList = IListPropertyBagVisitor.Visit_MethodGroup.Visit_2_T1
            Visit_2_TElement = IListPropertyBagVisitor.Visit_MethodGroup.Visit_2_T2
            def __call__(self, properties: IListPropertyBag_2[Visit_2_TList, Visit_2_TElement], container: clr.Reference[Visit_2_TList]) -> None:...




class IListPropertyVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_3_T1], typing.Type[Visit_3_T2], typing.Type[Visit_3_T3]]) -> Visit_3[Visit_3_T1, Visit_3_T2, Visit_3_T3]: ...

        Visit_3_T1 = typing.TypeVar('Visit_3_T1')
        Visit_3_T2 = typing.TypeVar('Visit_3_T2')
        Visit_3_T3 = typing.TypeVar('Visit_3_T3')
        class Visit_3(typing.Generic[Visit_3_T1, Visit_3_T2, Visit_3_T3]):
            Visit_3_TContainer = IListPropertyVisitor.Visit_MethodGroup.Visit_3_T1
            Visit_3_TList = IListPropertyVisitor.Visit_MethodGroup.Visit_3_T2
            Visit_3_TElement = IListPropertyVisitor.Visit_MethodGroup.Visit_3_T3
            def __call__(self, property: Property_2[Visit_3_TContainer, Visit_3_TList], container: clr.Reference[Visit_3_TContainer], list: clr.Reference[Visit_3_TList]) -> None:...




class INamedProperties_GenericClasses(abc.ABCMeta):
    Generic_INamedProperties_GenericClasses_INamedProperties_1_TContainer = typing.TypeVar('Generic_INamedProperties_GenericClasses_INamedProperties_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_INamedProperties_GenericClasses_INamedProperties_1_TContainer]) -> typing.Type[INamedProperties_1[Generic_INamedProperties_GenericClasses_INamedProperties_1_TContainer]]: ...

INamedProperties : INamedProperties_GenericClasses

INamedProperties_1_TContainer = typing.TypeVar('INamedProperties_1_TContainer')
class INamedProperties_1(typing.Generic[INamedProperties_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def TryGetProperty(self, container: clr.Reference[INamedProperties_1_TContainer], name: str, property: clr.Reference[IProperty_1[INamedProperties_1_TContainer]]) -> bool: ...


class IndexedCollectionPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TList = typing.TypeVar('Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TList')
    Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TElement = typing.TypeVar('Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TList], typing.Type[Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TElement]]) -> typing.Type[IndexedCollectionPropertyBag_2[Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TList, Generic_IndexedCollectionPropertyBag_GenericClasses_IndexedCollectionPropertyBag_2_TElement]]: ...

IndexedCollectionPropertyBag : IndexedCollectionPropertyBag_GenericClasses

IndexedCollectionPropertyBag_2_TList = typing.TypeVar('IndexedCollectionPropertyBag_2_TList')
IndexedCollectionPropertyBag_2_TElement = typing.TypeVar('IndexedCollectionPropertyBag_2_TElement')
class IndexedCollectionPropertyBag_2(typing.Generic[IndexedCollectionPropertyBag_2_TList, IndexedCollectionPropertyBag_2_TElement], PropertyBag_1[IndexedCollectionPropertyBag_2_TList], IListPropertyBag_2[IndexedCollectionPropertyBag_2_TList, IndexedCollectionPropertyBag_2_TElement]):
    def __init__(self) -> None: ...
    def TryGetProperty(self, container: clr.Reference[IndexedCollectionPropertyBag_2_TList], index: int, property: clr.Reference[IProperty_1[IndexedCollectionPropertyBag_2_TList]]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[IndexedCollectionPropertyBag_2_TList, IndexedCollectionPropertyBag_2_TElement]
    GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList = typing.TypeVar('GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList')
    GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TElement = typing.TypeVar('GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TElement')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList, GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TElement]):
        GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList = IndexedCollectionPropertyBag_2.GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList
        GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TElement = IndexedCollectionPropertyBag_2.GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TElement
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList]) -> PropertyCollection_1[GetProperties_MethodGroup_IndexedCollectionPropertyBag_2_TList]:...



class InstantiationKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Activator : InstantiationKind # 0
    PropertyBagOverride : InstantiationKind # 1
    NotInstantiatable : InstantiationKind # 2


class InvalidContainerTypeException(Exception):
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any], inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...


class InvalidPathException(Exception):
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @typing.overload
    def __init__(self, message: str, inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...


class IProperty_GenericClasses(abc.ABCMeta):
    Generic_IProperty_GenericClasses_IProperty_1_TContainer = typing.TypeVar('Generic_IProperty_GenericClasses_IProperty_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IProperty_GenericClasses_IProperty_1_TContainer]) -> typing.Type[IProperty_1[Generic_IProperty_GenericClasses_IProperty_1_TContainer]]: ...

class IProperty(IProperty_0, metaclass =IProperty_GenericClasses): ...

class IProperty_0(typing.Protocol):
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @abc.abstractmethod
    def DeclaredValueType(self) -> typing.Type[typing.Any]: ...
    # Skipped GetAttribute due to it being static, abstract and generic.

    GetAttribute : GetAttribute_MethodGroup
    class GetAttribute_MethodGroup:
        def __getitem__(self, t:typing.Type[GetAttribute_1_T1]) -> GetAttribute_1[GetAttribute_1_T1]: ...

        GetAttribute_1_T1 = typing.TypeVar('GetAttribute_1_T1')
        class GetAttribute_1(typing.Generic[GetAttribute_1_T1]):
            GetAttribute_1_TAttribute = IProperty_0.GetAttribute_MethodGroup.GetAttribute_1_T1
            def __call__(self) -> GetAttribute_1_TAttribute:...


    # Skipped GetAttributes due to it being static, abstract and generic.

    GetAttributes : GetAttributes_MethodGroup
    class GetAttributes_MethodGroup:
        def __getitem__(self, t:typing.Type[GetAttributes_1_T1]) -> GetAttributes_1[GetAttributes_1_T1]: ...

        GetAttributes_1_T1 = typing.TypeVar('GetAttributes_1_T1')
        class GetAttributes_1(typing.Generic[GetAttributes_1_T1]):
            GetAttributes_1_TAttribute = IProperty_0.GetAttributes_MethodGroup.GetAttributes_1_T1
            def __call__(self) -> IEnumerable_1[GetAttributes_1_TAttribute]:...

        def __call__(self) -> IEnumerable_1[Attribute]:...

    # Skipped HasAttribute due to it being static, abstract and generic.

    HasAttribute : HasAttribute_MethodGroup
    class HasAttribute_MethodGroup:
        def __getitem__(self, t:typing.Type[HasAttribute_1_T1]) -> HasAttribute_1[HasAttribute_1_T1]: ...

        HasAttribute_1_T1 = typing.TypeVar('HasAttribute_1_T1')
        class HasAttribute_1(typing.Generic[HasAttribute_1_T1]):
            HasAttribute_1_TAttribute = IProperty_0.HasAttribute_MethodGroup.HasAttribute_1_T1
            def __call__(self) -> bool:...




IProperty_1_TContainer = typing.TypeVar('IProperty_1_TContainer')
class IProperty_1(typing.Generic[IProperty_1_TContainer], IPropertyAccept_1[IProperty_1_TContainer], IProperty_0, typing.Protocol):
    @abc.abstractmethod
    def GetValue(self, container: clr.Reference[IProperty_1_TContainer]) -> typing.Any: ...
    @abc.abstractmethod
    def SetValue(self, container: clr.Reference[IProperty_1_TContainer], value: typing.Any) -> None: ...


class IPropertyAccept_GenericClasses(abc.ABCMeta):
    Generic_IPropertyAccept_GenericClasses_IPropertyAccept_1_TContainer = typing.TypeVar('Generic_IPropertyAccept_GenericClasses_IPropertyAccept_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IPropertyAccept_GenericClasses_IPropertyAccept_1_TContainer]) -> typing.Type[IPropertyAccept_1[Generic_IPropertyAccept_GenericClasses_IPropertyAccept_1_TContainer]]: ...

IPropertyAccept : IPropertyAccept_GenericClasses

IPropertyAccept_1_TContainer = typing.TypeVar('IPropertyAccept_1_TContainer')
class IPropertyAccept_1(typing.Generic[IPropertyAccept_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: IPropertyVisitor, container: clr.Reference[IPropertyAccept_1_TContainer]) -> None: ...


class IPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_IPropertyBag_GenericClasses_IPropertyBag_1_TContainer = typing.TypeVar('Generic_IPropertyBag_GenericClasses_IPropertyBag_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_IPropertyBag_GenericClasses_IPropertyBag_1_TContainer]) -> typing.Type[IPropertyBag_1[Generic_IPropertyBag_GenericClasses_IPropertyBag_1_TContainer]]: ...

class IPropertyBag(IPropertyBag_0, metaclass =IPropertyBag_GenericClasses): ...

class IPropertyBag_0(typing.Protocol):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup
    class Accept_MethodGroup:
        @typing.overload
        def __call__(self, visitor: ITypeVisitor) -> None:...
        @typing.overload
        def __call__(self, visitor: IPropertyBagVisitor, container: clr.Reference[typing.Any]) -> None:...



IPropertyBag_1_TContainer = typing.TypeVar('IPropertyBag_1_TContainer')
class IPropertyBag_1(typing.Generic[IPropertyBag_1_TContainer], IPropertyBag_0, typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: IPropertyBagVisitor, container: clr.Reference[IPropertyBag_1_TContainer]) -> None: ...
    @abc.abstractmethod
    def CreateInstance(self) -> IPropertyBag_1_TContainer: ...
    @abc.abstractmethod
    def TryCreateInstance(self, instance: clr.Reference[IPropertyBag_1_TContainer]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[IPropertyBag_1_TContainer]
    GetProperties_MethodGroup_IPropertyBag_1_TContainer = typing.TypeVar('GetProperties_MethodGroup_IPropertyBag_1_TContainer')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_IPropertyBag_1_TContainer]):
        GetProperties_MethodGroup_IPropertyBag_1_TContainer = IPropertyBag_1.GetProperties_MethodGroup_IPropertyBag_1_TContainer
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_IPropertyBag_1_TContainer]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_IPropertyBag_1_TContainer]) -> PropertyCollection_1[GetProperties_MethodGroup_IPropertyBag_1_TContainer]:...



class IPropertyBagVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Type[Visit_1_T1]) -> Visit_1[Visit_1_T1]: ...

        Visit_1_T1 = typing.TypeVar('Visit_1_T1')
        class Visit_1(typing.Generic[Visit_1_T1]):
            Visit_1_TContainer = IPropertyBagVisitor.Visit_MethodGroup.Visit_1_T1
            def __call__(self, properties: IPropertyBag_1[Visit_1_TContainer], container: clr.Reference[Visit_1_TContainer]) -> None:...




class IPropertyVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_2_T1], typing.Type[Visit_2_T2]]) -> Visit_2[Visit_2_T1, Visit_2_T2]: ...

        Visit_2_T1 = typing.TypeVar('Visit_2_T1')
        Visit_2_T2 = typing.TypeVar('Visit_2_T2')
        class Visit_2(typing.Generic[Visit_2_T1, Visit_2_T2]):
            Visit_2_TContainer = IPropertyVisitor.Visit_MethodGroup.Visit_2_T1
            Visit_2_TValue = IPropertyVisitor.Visit_MethodGroup.Visit_2_T2
            def __call__(self, property: Property_2[Visit_2_TContainer, Visit_2_TValue], container: clr.Reference[Visit_2_TContainer]) -> None:...




class IPropertyVisitorAdapter(typing.Protocol):
    pass


class ISetElementProperty_GenericClasses(abc.ABCMeta):
    Generic_ISetElementProperty_GenericClasses_ISetElementProperty_1_TKey = typing.TypeVar('Generic_ISetElementProperty_GenericClasses_ISetElementProperty_1_TKey')
    def __getitem__(self, types : typing.Type[Generic_ISetElementProperty_GenericClasses_ISetElementProperty_1_TKey]) -> typing.Type[ISetElementProperty_1[Generic_ISetElementProperty_GenericClasses_ISetElementProperty_1_TKey]]: ...

class ISetElementProperty(ISetElementProperty_0, metaclass =ISetElementProperty_GenericClasses): ...

class ISetElementProperty_0(ICollectionElementProperty, typing.Protocol):
    @property
    def ObjectKey(self) -> typing.Any: ...


ISetElementProperty_1_TKey = typing.TypeVar('ISetElementProperty_1_TKey', covariant=True)
class ISetElementProperty_1(typing.Generic[ISetElementProperty_1_TKey], ISetElementProperty_0, typing.Protocol):
    @property
    def Key(self) -> ISetElementProperty_1_TKey: ...


class ISetPropertyAccept_GenericClasses(abc.ABCMeta):
    Generic_ISetPropertyAccept_GenericClasses_ISetPropertyAccept_1_TSet = typing.TypeVar('Generic_ISetPropertyAccept_GenericClasses_ISetPropertyAccept_1_TSet')
    def __getitem__(self, types : typing.Type[Generic_ISetPropertyAccept_GenericClasses_ISetPropertyAccept_1_TSet]) -> typing.Type[ISetPropertyAccept_1[Generic_ISetPropertyAccept_GenericClasses_ISetPropertyAccept_1_TSet]]: ...

ISetPropertyAccept : ISetPropertyAccept_GenericClasses

ISetPropertyAccept_1_TSet = typing.TypeVar('ISetPropertyAccept_1_TSet')
class ISetPropertyAccept_1(typing.Generic[ISetPropertyAccept_1_TSet], typing.Protocol):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup[ISetPropertyAccept_1_TSet]
    Accept_MethodGroup_ISetPropertyAccept_1_TSet = typing.TypeVar('Accept_MethodGroup_ISetPropertyAccept_1_TSet')
    class Accept_MethodGroup(typing.Generic[Accept_MethodGroup_ISetPropertyAccept_1_TSet]):
        Accept_MethodGroup_ISetPropertyAccept_1_TSet = ISetPropertyAccept_1.Accept_MethodGroup_ISetPropertyAccept_1_TSet
        def __getitem__(self, t:typing.Type[Accept_1_T1]) -> Accept_1[Accept_MethodGroup_ISetPropertyAccept_1_TSet, Accept_1_T1]: ...

        Accept_1_ISetPropertyAccept_1_TSet = typing.TypeVar('Accept_1_ISetPropertyAccept_1_TSet')
        Accept_1_T1 = typing.TypeVar('Accept_1_T1')
        class Accept_1(typing.Generic[Accept_1_ISetPropertyAccept_1_TSet, Accept_1_T1]):
            Accept_1_ISetPropertyAccept_1_TSet = ISetPropertyAccept_1.Accept_MethodGroup.Accept_1_ISetPropertyAccept_1_TSet
            Accept_1_TContainer = ISetPropertyAccept_1.Accept_MethodGroup.Accept_1_T1
            def __call__(self, visitor: ISetPropertyVisitor, property: Property_2[Accept_1_TContainer, Accept_1_ISetPropertyAccept_1_TSet], container: clr.Reference[Accept_1_TContainer], set: clr.Reference[Accept_1_ISetPropertyAccept_1_TSet]) -> None:...




class ISetPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TSet = typing.TypeVar('Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TSet')
    Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TElement = typing.TypeVar('Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TSet], typing.Type[Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TElement]]) -> typing.Type[ISetPropertyBag_2[Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TSet, Generic_ISetPropertyBag_GenericClasses_ISetPropertyBag_2_TElement]]: ...

ISetPropertyBag : ISetPropertyBag_GenericClasses

ISetPropertyBag_2_TSet = typing.TypeVar('ISetPropertyBag_2_TSet')
ISetPropertyBag_2_TElement = typing.TypeVar('ISetPropertyBag_2_TElement')
class ISetPropertyBag_2(typing.Generic[ISetPropertyBag_2_TSet, ISetPropertyBag_2_TElement], ICollectionPropertyBag_2[ISetPropertyBag_2_TSet, ISetPropertyBag_2_TElement], IKeyedProperties_2[ISetPropertyBag_2_TSet, typing.Any], ISetPropertyAccept_1[ISetPropertyBag_2_TSet], ISetPropertyBagAccept_1[ISetPropertyBag_2_TSet], typing.Protocol):
    pass


class ISetPropertyBagAccept_GenericClasses(abc.ABCMeta):
    Generic_ISetPropertyBagAccept_GenericClasses_ISetPropertyBagAccept_1_TContainer = typing.TypeVar('Generic_ISetPropertyBagAccept_GenericClasses_ISetPropertyBagAccept_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_ISetPropertyBagAccept_GenericClasses_ISetPropertyBagAccept_1_TContainer]) -> typing.Type[ISetPropertyBagAccept_1[Generic_ISetPropertyBagAccept_GenericClasses_ISetPropertyBagAccept_1_TContainer]]: ...

ISetPropertyBagAccept : ISetPropertyBagAccept_GenericClasses

ISetPropertyBagAccept_1_TContainer = typing.TypeVar('ISetPropertyBagAccept_1_TContainer')
class ISetPropertyBagAccept_1(typing.Generic[ISetPropertyBagAccept_1_TContainer], typing.Protocol):
    @abc.abstractmethod
    def Accept(self, visitor: ISetPropertyBagVisitor, container: clr.Reference[ISetPropertyBagAccept_1_TContainer]) -> None: ...


class ISetPropertyBagVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_2_T1], typing.Type[Visit_2_T2]]) -> Visit_2[Visit_2_T1, Visit_2_T2]: ...

        Visit_2_T1 = typing.TypeVar('Visit_2_T1')
        Visit_2_T2 = typing.TypeVar('Visit_2_T2')
        class Visit_2(typing.Generic[Visit_2_T1, Visit_2_T2]):
            Visit_2_TSet = ISetPropertyBagVisitor.Visit_MethodGroup.Visit_2_T1
            Visit_2_TValue = ISetPropertyBagVisitor.Visit_MethodGroup.Visit_2_T2
            def __call__(self, properties: ISetPropertyBag_2[Visit_2_TSet, Visit_2_TValue], container: clr.Reference[Visit_2_TSet]) -> None:...




class ISetPropertyVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_3_T1], typing.Type[Visit_3_T2], typing.Type[Visit_3_T3]]) -> Visit_3[Visit_3_T1, Visit_3_T2, Visit_3_T3]: ...

        Visit_3_T1 = typing.TypeVar('Visit_3_T1')
        Visit_3_T2 = typing.TypeVar('Visit_3_T2')
        Visit_3_T3 = typing.TypeVar('Visit_3_T3')
        class Visit_3(typing.Generic[Visit_3_T1, Visit_3_T2, Visit_3_T3]):
            Visit_3_TContainer = ISetPropertyVisitor.Visit_MethodGroup.Visit_3_T1
            Visit_3_TSet = ISetPropertyVisitor.Visit_MethodGroup.Visit_3_T2
            Visit_3_TValue = ISetPropertyVisitor.Visit_MethodGroup.Visit_3_T3
            def __call__(self, property: Property_2[Visit_3_TContainer, Visit_3_TSet], container: clr.Reference[Visit_3_TContainer], set: clr.Reference[Visit_3_TSet]) -> None:...




class ITypeVisitor(typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Type[Visit_1_T1]) -> Visit_1[Visit_1_T1]: ...

        Visit_1_T1 = typing.TypeVar('Visit_1_T1')
        class Visit_1(typing.Generic[Visit_1_T1]):
            Visit_1_TContainer = ITypeVisitor.Visit_MethodGroup.Visit_1_T1
            def __call__(self) -> None:...




class IVisitContravariantPropertyAdapter_GenericClasses(abc.ABCMeta):
    Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_1_TValue = typing.TypeVar('Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_1_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_1_TValue]) -> typing.Type[IVisitContravariantPropertyAdapter_1[Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_1_TValue]]: ...
    Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TContainer = typing.TypeVar('Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TContainer')
    Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TValue = typing.TypeVar('Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TContainer], typing.Type[Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TValue]]) -> typing.Type[IVisitContravariantPropertyAdapter_2[Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TContainer, Generic_IVisitContravariantPropertyAdapter_GenericClasses_IVisitContravariantPropertyAdapter_2_TValue]]: ...

IVisitContravariantPropertyAdapter : IVisitContravariantPropertyAdapter_GenericClasses

IVisitContravariantPropertyAdapter_1_TValue = typing.TypeVar('IVisitContravariantPropertyAdapter_1_TValue', contravariant=True)
class IVisitContravariantPropertyAdapter_1(typing.Generic[IVisitContravariantPropertyAdapter_1_TValue], IPropertyVisitorAdapter, typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup[IVisitContravariantPropertyAdapter_1_TValue]
    Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue = typing.TypeVar('Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue', contravariant=True)
    class Visit_MethodGroup(typing.Generic[Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue]):
        Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue = IVisitContravariantPropertyAdapter_1.Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue
        def __getitem__(self, t:typing.Type[Visit_1_T1]) -> Visit_1[Visit_MethodGroup_IVisitContravariantPropertyAdapter_1_TValue, Visit_1_T1]: ...

        Visit_1_IVisitContravariantPropertyAdapter_1_TValue = typing.TypeVar('Visit_1_IVisitContravariantPropertyAdapter_1_TValue', contravariant=True)
        Visit_1_T1 = typing.TypeVar('Visit_1_T1')
        class Visit_1(typing.Generic[Visit_1_IVisitContravariantPropertyAdapter_1_TValue, Visit_1_T1]):
            Visit_1_IVisitContravariantPropertyAdapter_1_TValue = IVisitContravariantPropertyAdapter_1.Visit_MethodGroup.Visit_1_IVisitContravariantPropertyAdapter_1_TValue
            Visit_1_TContainer = IVisitContravariantPropertyAdapter_1.Visit_MethodGroup.Visit_1_T1
            def __call__(self, context: clr.Reference[VisitContext_1[Visit_1_TContainer]], container: clr.Reference[Visit_1_TContainer], value: Visit_1_IVisitContravariantPropertyAdapter_1_TValue) -> None:...




IVisitContravariantPropertyAdapter_2_TContainer = typing.TypeVar('IVisitContravariantPropertyAdapter_2_TContainer')
IVisitContravariantPropertyAdapter_2_TValue = typing.TypeVar('IVisitContravariantPropertyAdapter_2_TValue', contravariant=True)
class IVisitContravariantPropertyAdapter_2(typing.Generic[IVisitContravariantPropertyAdapter_2_TContainer, IVisitContravariantPropertyAdapter_2_TValue], IPropertyVisitorAdapter, typing.Protocol):
    @abc.abstractmethod
    def Visit(self, context: clr.Reference[VisitContext_1[IVisitContravariantPropertyAdapter_2_TContainer]], container: clr.Reference[IVisitContravariantPropertyAdapter_2_TContainer], value: IVisitContravariantPropertyAdapter_2_TValue) -> None: ...


class IVisitPrimitivesPropertyAdapter(IVisitPropertyAdapter_1[str], IVisitPropertyAdapter_1[bool], IVisitPropertyAdapter_1[float], IVisitPropertyAdapter_1[float], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], IVisitPropertyAdapter_1[int], typing.Protocol):
    pass


class IVisitPropertyAdapter_GenericClasses(abc.ABCMeta):
    Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_1_TValue = typing.TypeVar('Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_1_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_1_TValue]) -> typing.Type[IVisitPropertyAdapter_1[Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_1_TValue]]: ...
    Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TContainer = typing.TypeVar('Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TContainer')
    Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TValue = typing.TypeVar('Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TContainer], typing.Type[Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TValue]]) -> typing.Type[IVisitPropertyAdapter_2[Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TContainer, Generic_IVisitPropertyAdapter_GenericClasses_IVisitPropertyAdapter_2_TValue]]: ...

class IVisitPropertyAdapter(IVisitPropertyAdapter_0, metaclass =IVisitPropertyAdapter_GenericClasses): ...

class IVisitPropertyAdapter_0(IPropertyVisitorAdapter, typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup
    class Visit_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Visit_2_T1], typing.Type[Visit_2_T2]]) -> Visit_2[Visit_2_T1, Visit_2_T2]: ...

        Visit_2_T1 = typing.TypeVar('Visit_2_T1')
        Visit_2_T2 = typing.TypeVar('Visit_2_T2')
        class Visit_2(typing.Generic[Visit_2_T1, Visit_2_T2]):
            Visit_2_TContainer = IVisitPropertyAdapter_0.Visit_MethodGroup.Visit_2_T1
            Visit_2_TValue = IVisitPropertyAdapter_0.Visit_MethodGroup.Visit_2_T2
            def __call__(self, context: clr.Reference[VisitContext_2[Visit_2_TContainer, Visit_2_TValue]], container: clr.Reference[Visit_2_TContainer], value: clr.Reference[Visit_2_TValue]) -> None:...




IVisitPropertyAdapter_1_TValue = typing.TypeVar('IVisitPropertyAdapter_1_TValue')
class IVisitPropertyAdapter_1(typing.Generic[IVisitPropertyAdapter_1_TValue], IPropertyVisitorAdapter, typing.Protocol):
    # Skipped Visit due to it being static, abstract and generic.

    Visit : Visit_MethodGroup[IVisitPropertyAdapter_1_TValue]
    Visit_MethodGroup_IVisitPropertyAdapter_1_TValue = typing.TypeVar('Visit_MethodGroup_IVisitPropertyAdapter_1_TValue')
    class Visit_MethodGroup(typing.Generic[Visit_MethodGroup_IVisitPropertyAdapter_1_TValue]):
        Visit_MethodGroup_IVisitPropertyAdapter_1_TValue = IVisitPropertyAdapter_1.Visit_MethodGroup_IVisitPropertyAdapter_1_TValue
        def __getitem__(self, t:typing.Type[Visit_1_T1]) -> Visit_1[Visit_MethodGroup_IVisitPropertyAdapter_1_TValue, Visit_1_T1]: ...

        Visit_1_IVisitPropertyAdapter_1_TValue = typing.TypeVar('Visit_1_IVisitPropertyAdapter_1_TValue')
        Visit_1_T1 = typing.TypeVar('Visit_1_T1')
        class Visit_1(typing.Generic[Visit_1_IVisitPropertyAdapter_1_TValue, Visit_1_T1]):
            Visit_1_IVisitPropertyAdapter_1_TValue = IVisitPropertyAdapter_1.Visit_MethodGroup.Visit_1_IVisitPropertyAdapter_1_TValue
            Visit_1_TContainer = IVisitPropertyAdapter_1.Visit_MethodGroup.Visit_1_T1
            def __call__(self, context: clr.Reference[VisitContext_2[Visit_1_TContainer, Visit_1_IVisitPropertyAdapter_1_TValue]], container: clr.Reference[Visit_1_TContainer], value: clr.Reference[Visit_1_IVisitPropertyAdapter_1_TValue]) -> None:...




IVisitPropertyAdapter_2_TContainer = typing.TypeVar('IVisitPropertyAdapter_2_TContainer')
IVisitPropertyAdapter_2_TValue = typing.TypeVar('IVisitPropertyAdapter_2_TValue')
class IVisitPropertyAdapter_2(typing.Generic[IVisitPropertyAdapter_2_TContainer, IVisitPropertyAdapter_2_TValue], IPropertyVisitorAdapter, typing.Protocol):
    @abc.abstractmethod
    def Visit(self, context: clr.Reference[VisitContext_2[IVisitPropertyAdapter_2_TContainer, IVisitPropertyAdapter_2_TValue]], container: clr.Reference[IVisitPropertyAdapter_2_TContainer], value: clr.Reference[IVisitPropertyAdapter_2_TValue]) -> None: ...


class KeyValueCollectionPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TDictionary = typing.TypeVar('Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TDictionary')
    Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TKey = typing.TypeVar('Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TKey')
    Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TValue = typing.TypeVar('Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TDictionary], typing.Type[Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TKey], typing.Type[Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TValue]]) -> typing.Type[KeyValueCollectionPropertyBag_3[Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TDictionary, Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TKey, Generic_KeyValueCollectionPropertyBag_GenericClasses_KeyValueCollectionPropertyBag_3_TValue]]: ...

KeyValueCollectionPropertyBag : KeyValueCollectionPropertyBag_GenericClasses

KeyValueCollectionPropertyBag_3_TDictionary = typing.TypeVar('KeyValueCollectionPropertyBag_3_TDictionary')
KeyValueCollectionPropertyBag_3_TKey = typing.TypeVar('KeyValueCollectionPropertyBag_3_TKey')
KeyValueCollectionPropertyBag_3_TValue = typing.TypeVar('KeyValueCollectionPropertyBag_3_TValue')
class KeyValueCollectionPropertyBag_3(typing.Generic[KeyValueCollectionPropertyBag_3_TDictionary, KeyValueCollectionPropertyBag_3_TKey, KeyValueCollectionPropertyBag_3_TValue], PropertyBag_1[KeyValueCollectionPropertyBag_3_TDictionary], IDictionaryPropertyBag_3[KeyValueCollectionPropertyBag_3_TDictionary, KeyValueCollectionPropertyBag_3_TKey, KeyValueCollectionPropertyBag_3_TValue]):
    def __init__(self) -> None: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[KeyValueCollectionPropertyBag_3_TDictionary, KeyValueCollectionPropertyBag_3_TKey, KeyValueCollectionPropertyBag_3_TValue]
    GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary = typing.TypeVar('GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary')
    GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TKey = typing.TypeVar('GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TKey')
    GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TValue = typing.TypeVar('GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TValue')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary, GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TKey, GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TValue]):
        GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary = KeyValueCollectionPropertyBag_3.GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary
        GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TKey = KeyValueCollectionPropertyBag_3.GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TKey
        GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TValue = KeyValueCollectionPropertyBag_3.GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TValue
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary]) -> PropertyCollection_1[GetProperties_MethodGroup_KeyValueCollectionPropertyBag_3_TDictionary]:...



class KeyValuePairPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TKey = typing.TypeVar('Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TKey')
    Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TValue = typing.TypeVar('Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TKey], typing.Type[Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TValue]]) -> typing.Type[KeyValuePairPropertyBag_2[Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TKey, Generic_KeyValuePairPropertyBag_GenericClasses_KeyValuePairPropertyBag_2_TValue]]: ...

KeyValuePairPropertyBag : KeyValuePairPropertyBag_GenericClasses

KeyValuePairPropertyBag_2_TKey = typing.TypeVar('KeyValuePairPropertyBag_2_TKey')
KeyValuePairPropertyBag_2_TValue = typing.TypeVar('KeyValuePairPropertyBag_2_TValue')
class KeyValuePairPropertyBag_2(typing.Generic[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue], PropertyBag_1[KeyValuePair_2[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue]], INamedProperties_1[KeyValuePair_2[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue]]):
    def __init__(self) -> None: ...
    def TryGetProperty(self, container: clr.Reference[KeyValuePair_2[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue]], name: str, property: clr.Reference[IProperty_1[KeyValuePair_2[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue]]]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[KeyValuePairPropertyBag_2_TKey, KeyValuePairPropertyBag_2_TValue]
    GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey = typing.TypeVar('GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey')
    GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue = typing.TypeVar('GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey, GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue]):
        GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey = KeyValuePairPropertyBag_2.GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey
        GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue = KeyValuePairPropertyBag_2.GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue
        @typing.overload
        def __call__(self) -> PropertyCollection_1[KeyValuePair_2[GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey, GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue]]:...
        @typing.overload
        def __call__(self, container: clr.Reference[KeyValuePair_2[GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey, GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue]]) -> PropertyCollection_1[KeyValuePair_2[GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TKey, GetProperties_MethodGroup_KeyValuePairPropertyBag_2_TValue]]:...



class ListPropertyBag_GenericClasses(abc.ABCMeta):
    Generic_ListPropertyBag_GenericClasses_ListPropertyBag_1_TElement = typing.TypeVar('Generic_ListPropertyBag_GenericClasses_ListPropertyBag_1_TElement')
    def __getitem__(self, types : typing.Type[Generic_ListPropertyBag_GenericClasses_ListPropertyBag_1_TElement]) -> typing.Type[ListPropertyBag_1[Generic_ListPropertyBag_GenericClasses_ListPropertyBag_1_TElement]]: ...

ListPropertyBag : ListPropertyBag_GenericClasses

ListPropertyBag_1_TElement = typing.TypeVar('ListPropertyBag_1_TElement')
class ListPropertyBag_1(typing.Generic[ListPropertyBag_1_TElement], IndexedCollectionPropertyBag_2[List_1[ListPropertyBag_1_TElement], ListPropertyBag_1_TElement]):
    def __init__(self) -> None: ...


class MissingPropertyBagException(Exception):
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any]) -> None: ...
    @typing.overload
    def __init__(self, type: typing.Type[typing.Any], inner: Exception) -> None: ...
    @property
    def Data(self) -> IDictionary: ...
    @property
    def HelpLink(self) -> str: ...
    @HelpLink.setter
    def HelpLink(self, value: str) -> str: ...
    @property
    def HResult(self) -> int: ...
    @HResult.setter
    def HResult(self, value: int) -> int: ...
    @property
    def InnerException(self) -> Exception: ...
    @property
    def Message(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @Source.setter
    def Source(self, value: str) -> str: ...
    @property
    def StackTrace(self) -> str: ...
    @property
    def TargetSite(self) -> MethodBase: ...
    @property
    def Type(self) -> typing.Type[typing.Any]: ...


class PathVisitor(IPropertyVisitor, IPropertyBagVisitor, abc.ABC):
    @property
    def Path(self) -> PropertyPath: ...
    @Path.setter
    def Path(self, value: PropertyPath) -> PropertyPath: ...
    @property
    def ReadonlyVisit(self) -> bool: ...
    @ReadonlyVisit.setter
    def ReadonlyVisit(self, value: bool) -> bool: ...
    @property
    def ReturnCode(self) -> VisitReturnCode: ...
    @ReturnCode.setter
    def ReturnCode(self, value: VisitReturnCode) -> VisitReturnCode: ...
    def Reset(self) -> None: ...


class Property_GenericClasses(abc.ABCMeta):
    Generic_Property_GenericClasses_Property_2_TContainer = typing.TypeVar('Generic_Property_GenericClasses_Property_2_TContainer')
    Generic_Property_GenericClasses_Property_2_TValue = typing.TypeVar('Generic_Property_GenericClasses_Property_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_Property_GenericClasses_Property_2_TContainer], typing.Type[Generic_Property_GenericClasses_Property_2_TValue]]) -> typing.Type[Property_2[Generic_Property_GenericClasses_Property_2_TContainer, Generic_Property_GenericClasses_Property_2_TValue]]: ...

Property : Property_GenericClasses

Property_2_TContainer = typing.TypeVar('Property_2_TContainer')
Property_2_TValue = typing.TypeVar('Property_2_TValue')
class Property_2(typing.Generic[Property_2_TContainer, Property_2_TValue], IProperty_1[Property_2_TContainer], abc.ABC):
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    def Accept(self, visitor: IPropertyVisitor, container: clr.Reference[Property_2_TContainer]) -> None: ...
    def DeclaredValueType(self) -> typing.Type[typing.Any]: ...
    @abc.abstractmethod
    def GetValue(self, container: clr.Reference[Property_2_TContainer]) -> Property_2_TValue: ...
    @abc.abstractmethod
    def SetValue(self, container: clr.Reference[Property_2_TContainer], value: Property_2_TValue) -> None: ...
    # Skipped GetAttribute due to it being static, abstract and generic.

    GetAttribute : GetAttribute_MethodGroup[Property_2_TContainer, Property_2_TValue]
    GetAttribute_MethodGroup_Property_2_TContainer = typing.TypeVar('GetAttribute_MethodGroup_Property_2_TContainer')
    GetAttribute_MethodGroup_Property_2_TValue = typing.TypeVar('GetAttribute_MethodGroup_Property_2_TValue')
    class GetAttribute_MethodGroup(typing.Generic[GetAttribute_MethodGroup_Property_2_TContainer, GetAttribute_MethodGroup_Property_2_TValue]):
        GetAttribute_MethodGroup_Property_2_TContainer = Property_2.GetAttribute_MethodGroup_Property_2_TContainer
        GetAttribute_MethodGroup_Property_2_TValue = Property_2.GetAttribute_MethodGroup_Property_2_TValue
        def __getitem__(self, t:typing.Type[GetAttribute_1_T1]) -> GetAttribute_1[GetAttribute_MethodGroup_Property_2_TContainer, GetAttribute_MethodGroup_Property_2_TValue, GetAttribute_1_T1]: ...

        GetAttribute_1_Property_2_TContainer = typing.TypeVar('GetAttribute_1_Property_2_TContainer')
        GetAttribute_1_Property_2_TValue = typing.TypeVar('GetAttribute_1_Property_2_TValue')
        GetAttribute_1_T1 = typing.TypeVar('GetAttribute_1_T1')
        class GetAttribute_1(typing.Generic[GetAttribute_1_Property_2_TContainer, GetAttribute_1_Property_2_TValue, GetAttribute_1_T1]):
            GetAttribute_1_Property_2_TContainer = Property_2.GetAttribute_MethodGroup.GetAttribute_1_Property_2_TContainer
            GetAttribute_1_Property_2_TValue = Property_2.GetAttribute_MethodGroup.GetAttribute_1_Property_2_TValue
            GetAttribute_1_TAttribute = Property_2.GetAttribute_MethodGroup.GetAttribute_1_T1
            def __call__(self) -> GetAttribute_1_TAttribute:...


    # Skipped GetAttributes due to it being static, abstract and generic.

    GetAttributes : GetAttributes_MethodGroup[Property_2_TContainer, Property_2_TValue]
    GetAttributes_MethodGroup_Property_2_TContainer = typing.TypeVar('GetAttributes_MethodGroup_Property_2_TContainer')
    GetAttributes_MethodGroup_Property_2_TValue = typing.TypeVar('GetAttributes_MethodGroup_Property_2_TValue')
    class GetAttributes_MethodGroup(typing.Generic[GetAttributes_MethodGroup_Property_2_TContainer, GetAttributes_MethodGroup_Property_2_TValue]):
        GetAttributes_MethodGroup_Property_2_TContainer = Property_2.GetAttributes_MethodGroup_Property_2_TContainer
        GetAttributes_MethodGroup_Property_2_TValue = Property_2.GetAttributes_MethodGroup_Property_2_TValue
        def __getitem__(self, t:typing.Type[GetAttributes_1_T1]) -> GetAttributes_1[GetAttributes_MethodGroup_Property_2_TContainer, GetAttributes_MethodGroup_Property_2_TValue, GetAttributes_1_T1]: ...

        GetAttributes_1_Property_2_TContainer = typing.TypeVar('GetAttributes_1_Property_2_TContainer')
        GetAttributes_1_Property_2_TValue = typing.TypeVar('GetAttributes_1_Property_2_TValue')
        GetAttributes_1_T1 = typing.TypeVar('GetAttributes_1_T1')
        class GetAttributes_1(typing.Generic[GetAttributes_1_Property_2_TContainer, GetAttributes_1_Property_2_TValue, GetAttributes_1_T1]):
            GetAttributes_1_Property_2_TContainer = Property_2.GetAttributes_MethodGroup.GetAttributes_1_Property_2_TContainer
            GetAttributes_1_Property_2_TValue = Property_2.GetAttributes_MethodGroup.GetAttributes_1_Property_2_TValue
            GetAttributes_1_TAttribute = Property_2.GetAttributes_MethodGroup.GetAttributes_1_T1
            def __call__(self) -> IEnumerable_1[GetAttributes_1_TAttribute]:...

        def __call__(self) -> IEnumerable_1[Attribute]:...

    # Skipped HasAttribute due to it being static, abstract and generic.

    HasAttribute : HasAttribute_MethodGroup[Property_2_TContainer, Property_2_TValue]
    HasAttribute_MethodGroup_Property_2_TContainer = typing.TypeVar('HasAttribute_MethodGroup_Property_2_TContainer')
    HasAttribute_MethodGroup_Property_2_TValue = typing.TypeVar('HasAttribute_MethodGroup_Property_2_TValue')
    class HasAttribute_MethodGroup(typing.Generic[HasAttribute_MethodGroup_Property_2_TContainer, HasAttribute_MethodGroup_Property_2_TValue]):
        HasAttribute_MethodGroup_Property_2_TContainer = Property_2.HasAttribute_MethodGroup_Property_2_TContainer
        HasAttribute_MethodGroup_Property_2_TValue = Property_2.HasAttribute_MethodGroup_Property_2_TValue
        def __getitem__(self, t:typing.Type[HasAttribute_1_T1]) -> HasAttribute_1[HasAttribute_MethodGroup_Property_2_TContainer, HasAttribute_MethodGroup_Property_2_TValue, HasAttribute_1_T1]: ...

        HasAttribute_1_Property_2_TContainer = typing.TypeVar('HasAttribute_1_Property_2_TContainer')
        HasAttribute_1_Property_2_TValue = typing.TypeVar('HasAttribute_1_Property_2_TValue')
        HasAttribute_1_T1 = typing.TypeVar('HasAttribute_1_T1')
        class HasAttribute_1(typing.Generic[HasAttribute_1_Property_2_TContainer, HasAttribute_1_Property_2_TValue, HasAttribute_1_T1]):
            HasAttribute_1_Property_2_TContainer = Property_2.HasAttribute_MethodGroup.HasAttribute_1_Property_2_TContainer
            HasAttribute_1_Property_2_TValue = Property_2.HasAttribute_MethodGroup.HasAttribute_1_Property_2_TValue
            HasAttribute_1_TAttribute = Property_2.HasAttribute_MethodGroup.HasAttribute_1_T1
            def __call__(self) -> bool:...




class PropertyBag_GenericClasses(abc.ABCMeta):
    Generic_PropertyBag_GenericClasses_PropertyBag_1_TContainer = typing.TypeVar('Generic_PropertyBag_GenericClasses_PropertyBag_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_PropertyBag_GenericClasses_PropertyBag_1_TContainer]) -> typing.Type[PropertyBag_1[Generic_PropertyBag_GenericClasses_PropertyBag_1_TContainer]]: ...

class PropertyBag(PropertyBag_0, metaclass =PropertyBag_GenericClasses): ...

class PropertyBag_0(abc.ABC):
    @staticmethod
    def GetAllTypesWithAPropertyBag() -> IEnumerable_1[typing.Type[typing.Any]]: ...
    # Skipped AcceptWithSpecializedVisitor due to it being static, abstract and generic.

    AcceptWithSpecializedVisitor : AcceptWithSpecializedVisitor_MethodGroup
    class AcceptWithSpecializedVisitor_MethodGroup:
        def __getitem__(self, t:typing.Type[AcceptWithSpecializedVisitor_1_T1]) -> AcceptWithSpecializedVisitor_1[AcceptWithSpecializedVisitor_1_T1]: ...

        AcceptWithSpecializedVisitor_1_T1 = typing.TypeVar('AcceptWithSpecializedVisitor_1_T1')
        class AcceptWithSpecializedVisitor_1(typing.Generic[AcceptWithSpecializedVisitor_1_T1]):
            AcceptWithSpecializedVisitor_1_TContainer = PropertyBag_0.AcceptWithSpecializedVisitor_MethodGroup.AcceptWithSpecializedVisitor_1_T1
            def __call__(self, properties: IPropertyBag_1[AcceptWithSpecializedVisitor_1_TContainer], visitor: IPropertyBagVisitor, container: clr.Reference[AcceptWithSpecializedVisitor_1_TContainer]) -> None:...


    # Skipped CreateInstance due to it being static, abstract and generic.

    CreateInstance : CreateInstance_MethodGroup
    class CreateInstance_MethodGroup:
        def __getitem__(self, t:typing.Type[CreateInstance_1_T1]) -> CreateInstance_1[CreateInstance_1_T1]: ...

        CreateInstance_1_T1 = typing.TypeVar('CreateInstance_1_T1')
        class CreateInstance_1(typing.Generic[CreateInstance_1_T1]):
            CreateInstance_1_TContainer = PropertyBag_0.CreateInstance_MethodGroup.CreateInstance_1_T1
            def __call__(self) -> CreateInstance_1_TContainer:...


    # Skipped Exists due to it being static, abstract and generic.

    Exists : Exists_MethodGroup
    class Exists_MethodGroup:
        def __getitem__(self, t:typing.Type[Exists_1_T1]) -> Exists_1[Exists_1_T1]: ...

        Exists_1_T1 = typing.TypeVar('Exists_1_T1')
        class Exists_1(typing.Generic[Exists_1_T1]):
            Exists_1_TContainer = PropertyBag_0.Exists_MethodGroup.Exists_1_T1
            def __call__(self) -> bool:...

        def __call__(self, type: typing.Type[typing.Any]) -> bool:...

    # Skipped GetPropertyBag due to it being static, abstract and generic.

    GetPropertyBag : GetPropertyBag_MethodGroup
    class GetPropertyBag_MethodGroup:
        def __getitem__(self, t:typing.Type[GetPropertyBag_1_T1]) -> GetPropertyBag_1[GetPropertyBag_1_T1]: ...

        GetPropertyBag_1_T1 = typing.TypeVar('GetPropertyBag_1_T1')
        class GetPropertyBag_1(typing.Generic[GetPropertyBag_1_T1]):
            GetPropertyBag_1_TContainer = PropertyBag_0.GetPropertyBag_MethodGroup.GetPropertyBag_1_T1
            def __call__(self) -> IPropertyBag_1[GetPropertyBag_1_TContainer]:...

        def __call__(self, type: typing.Type[typing.Any]) -> IPropertyBag:...

    # Skipped Register due to it being static, abstract and generic.

    Register : Register_MethodGroup
    class Register_MethodGroup:
        def __getitem__(self, t:typing.Type[Register_1_T1]) -> Register_1[Register_1_T1]: ...

        Register_1_T1 = typing.TypeVar('Register_1_T1')
        class Register_1(typing.Generic[Register_1_T1]):
            Register_1_TContainer = PropertyBag_0.Register_MethodGroup.Register_1_T1
            def __call__(self, propertyBag: PropertyBag_1[Register_1_TContainer]) -> None:...


    # Skipped RegisterArray due to it being static, abstract and generic.

    RegisterArray : RegisterArray_MethodGroup
    class RegisterArray_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[RegisterArray_1_T1]) -> RegisterArray_1[RegisterArray_1_T1]: ...

        RegisterArray_1_T1 = typing.TypeVar('RegisterArray_1_T1')
        class RegisterArray_1(typing.Generic[RegisterArray_1_T1]):
            RegisterArray_1_TElement = PropertyBag_0.RegisterArray_MethodGroup.RegisterArray_1_T1
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterArray_2_T1], typing.Type[RegisterArray_2_T2]]) -> RegisterArray_2[RegisterArray_2_T1, RegisterArray_2_T2]: ...

        RegisterArray_2_T1 = typing.TypeVar('RegisterArray_2_T1')
        RegisterArray_2_T2 = typing.TypeVar('RegisterArray_2_T2')
        class RegisterArray_2(typing.Generic[RegisterArray_2_T1, RegisterArray_2_T2]):
            RegisterArray_2_TContainer = PropertyBag_0.RegisterArray_MethodGroup.RegisterArray_2_T1
            RegisterArray_2_TElement = PropertyBag_0.RegisterArray_MethodGroup.RegisterArray_2_T2
            def __call__(self) -> None:...


    # Skipped RegisterDictionary due to it being static, abstract and generic.

    RegisterDictionary : RegisterDictionary_MethodGroup
    class RegisterDictionary_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterDictionary_2_T1], typing.Type[RegisterDictionary_2_T2]]) -> RegisterDictionary_2[RegisterDictionary_2_T1, RegisterDictionary_2_T2]: ...

        RegisterDictionary_2_T1 = typing.TypeVar('RegisterDictionary_2_T1')
        RegisterDictionary_2_T2 = typing.TypeVar('RegisterDictionary_2_T2')
        class RegisterDictionary_2(typing.Generic[RegisterDictionary_2_T1, RegisterDictionary_2_T2]):
            RegisterDictionary_2_TKey = PropertyBag_0.RegisterDictionary_MethodGroup.RegisterDictionary_2_T1
            RegisterDictionary_2_TValue = PropertyBag_0.RegisterDictionary_MethodGroup.RegisterDictionary_2_T2
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterDictionary_3_T1], typing.Type[RegisterDictionary_3_T2], typing.Type[RegisterDictionary_3_T3]]) -> RegisterDictionary_3[RegisterDictionary_3_T1, RegisterDictionary_3_T2, RegisterDictionary_3_T3]: ...

        RegisterDictionary_3_T1 = typing.TypeVar('RegisterDictionary_3_T1')
        RegisterDictionary_3_T2 = typing.TypeVar('RegisterDictionary_3_T2')
        RegisterDictionary_3_T3 = typing.TypeVar('RegisterDictionary_3_T3')
        class RegisterDictionary_3(typing.Generic[RegisterDictionary_3_T1, RegisterDictionary_3_T2, RegisterDictionary_3_T3]):
            RegisterDictionary_3_TContainer = PropertyBag_0.RegisterDictionary_MethodGroup.RegisterDictionary_3_T1
            RegisterDictionary_3_TKey = PropertyBag_0.RegisterDictionary_MethodGroup.RegisterDictionary_3_T2
            RegisterDictionary_3_TValue = PropertyBag_0.RegisterDictionary_MethodGroup.RegisterDictionary_3_T3
            def __call__(self) -> None:...


    # Skipped RegisterHashSet due to it being static, abstract and generic.

    RegisterHashSet : RegisterHashSet_MethodGroup
    class RegisterHashSet_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[RegisterHashSet_1_T1]) -> RegisterHashSet_1[RegisterHashSet_1_T1]: ...

        RegisterHashSet_1_T1 = typing.TypeVar('RegisterHashSet_1_T1')
        class RegisterHashSet_1(typing.Generic[RegisterHashSet_1_T1]):
            RegisterHashSet_1_TElement = PropertyBag_0.RegisterHashSet_MethodGroup.RegisterHashSet_1_T1
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterHashSet_2_T1], typing.Type[RegisterHashSet_2_T2]]) -> RegisterHashSet_2[RegisterHashSet_2_T1, RegisterHashSet_2_T2]: ...

        RegisterHashSet_2_T1 = typing.TypeVar('RegisterHashSet_2_T1')
        RegisterHashSet_2_T2 = typing.TypeVar('RegisterHashSet_2_T2')
        class RegisterHashSet_2(typing.Generic[RegisterHashSet_2_T1, RegisterHashSet_2_T2]):
            RegisterHashSet_2_TContainer = PropertyBag_0.RegisterHashSet_MethodGroup.RegisterHashSet_2_T1
            RegisterHashSet_2_TElement = PropertyBag_0.RegisterHashSet_MethodGroup.RegisterHashSet_2_T2
            def __call__(self) -> None:...


    # Skipped RegisterIDictionary due to it being static, abstract and generic.

    RegisterIDictionary : RegisterIDictionary_MethodGroup
    class RegisterIDictionary_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterIDictionary_3_T1], typing.Type[RegisterIDictionary_3_T2], typing.Type[RegisterIDictionary_3_T3]]) -> RegisterIDictionary_3[RegisterIDictionary_3_T1, RegisterIDictionary_3_T2, RegisterIDictionary_3_T3]: ...

        RegisterIDictionary_3_T1 = typing.TypeVar('RegisterIDictionary_3_T1')
        RegisterIDictionary_3_T2 = typing.TypeVar('RegisterIDictionary_3_T2')
        RegisterIDictionary_3_T3 = typing.TypeVar('RegisterIDictionary_3_T3')
        class RegisterIDictionary_3(typing.Generic[RegisterIDictionary_3_T1, RegisterIDictionary_3_T2, RegisterIDictionary_3_T3]):
            RegisterIDictionary_3_TDictionary = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_3_T1
            RegisterIDictionary_3_TKey = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_3_T2
            RegisterIDictionary_3_TValue = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_3_T3
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterIDictionary_4_T1], typing.Type[RegisterIDictionary_4_T2], typing.Type[RegisterIDictionary_4_T3], typing.Type[RegisterIDictionary_4_T4]]) -> RegisterIDictionary_4[RegisterIDictionary_4_T1, RegisterIDictionary_4_T2, RegisterIDictionary_4_T3, RegisterIDictionary_4_T4]: ...

        RegisterIDictionary_4_T1 = typing.TypeVar('RegisterIDictionary_4_T1')
        RegisterIDictionary_4_T2 = typing.TypeVar('RegisterIDictionary_4_T2')
        RegisterIDictionary_4_T3 = typing.TypeVar('RegisterIDictionary_4_T3')
        RegisterIDictionary_4_T4 = typing.TypeVar('RegisterIDictionary_4_T4')
        class RegisterIDictionary_4(typing.Generic[RegisterIDictionary_4_T1, RegisterIDictionary_4_T2, RegisterIDictionary_4_T3, RegisterIDictionary_4_T4]):
            RegisterIDictionary_4_TContainer = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_4_T1
            RegisterIDictionary_4_TDictionary = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_4_T2
            RegisterIDictionary_4_TKey = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_4_T3
            RegisterIDictionary_4_TValue = PropertyBag_0.RegisterIDictionary_MethodGroup.RegisterIDictionary_4_T4
            def __call__(self) -> None:...


    # Skipped RegisterIList due to it being static, abstract and generic.

    RegisterIList : RegisterIList_MethodGroup
    class RegisterIList_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterIList_2_T1], typing.Type[RegisterIList_2_T2]]) -> RegisterIList_2[RegisterIList_2_T1, RegisterIList_2_T2]: ...

        RegisterIList_2_T1 = typing.TypeVar('RegisterIList_2_T1')
        RegisterIList_2_T2 = typing.TypeVar('RegisterIList_2_T2')
        class RegisterIList_2(typing.Generic[RegisterIList_2_T1, RegisterIList_2_T2]):
            RegisterIList_2_TList = PropertyBag_0.RegisterIList_MethodGroup.RegisterIList_2_T1
            RegisterIList_2_TElement = PropertyBag_0.RegisterIList_MethodGroup.RegisterIList_2_T2
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterIList_3_T1], typing.Type[RegisterIList_3_T2], typing.Type[RegisterIList_3_T3]]) -> RegisterIList_3[RegisterIList_3_T1, RegisterIList_3_T2, RegisterIList_3_T3]: ...

        RegisterIList_3_T1 = typing.TypeVar('RegisterIList_3_T1')
        RegisterIList_3_T2 = typing.TypeVar('RegisterIList_3_T2')
        RegisterIList_3_T3 = typing.TypeVar('RegisterIList_3_T3')
        class RegisterIList_3(typing.Generic[RegisterIList_3_T1, RegisterIList_3_T2, RegisterIList_3_T3]):
            RegisterIList_3_TContainer = PropertyBag_0.RegisterIList_MethodGroup.RegisterIList_3_T1
            RegisterIList_3_TList = PropertyBag_0.RegisterIList_MethodGroup.RegisterIList_3_T2
            RegisterIList_3_TElement = PropertyBag_0.RegisterIList_MethodGroup.RegisterIList_3_T3
            def __call__(self) -> None:...


    # Skipped RegisterISet due to it being static, abstract and generic.

    RegisterISet : RegisterISet_MethodGroup
    class RegisterISet_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterISet_2_T1], typing.Type[RegisterISet_2_T2]]) -> RegisterISet_2[RegisterISet_2_T1, RegisterISet_2_T2]: ...

        RegisterISet_2_T1 = typing.TypeVar('RegisterISet_2_T1')
        RegisterISet_2_T2 = typing.TypeVar('RegisterISet_2_T2')
        class RegisterISet_2(typing.Generic[RegisterISet_2_T1, RegisterISet_2_T2]):
            RegisterISet_2_TSet = PropertyBag_0.RegisterISet_MethodGroup.RegisterISet_2_T1
            RegisterISet_2_TElement = PropertyBag_0.RegisterISet_MethodGroup.RegisterISet_2_T2
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterISet_3_T1], typing.Type[RegisterISet_3_T2], typing.Type[RegisterISet_3_T3]]) -> RegisterISet_3[RegisterISet_3_T1, RegisterISet_3_T2, RegisterISet_3_T3]: ...

        RegisterISet_3_T1 = typing.TypeVar('RegisterISet_3_T1')
        RegisterISet_3_T2 = typing.TypeVar('RegisterISet_3_T2')
        RegisterISet_3_T3 = typing.TypeVar('RegisterISet_3_T3')
        class RegisterISet_3(typing.Generic[RegisterISet_3_T1, RegisterISet_3_T2, RegisterISet_3_T3]):
            RegisterISet_3_TContainer = PropertyBag_0.RegisterISet_MethodGroup.RegisterISet_3_T1
            RegisterISet_3_TSet = PropertyBag_0.RegisterISet_MethodGroup.RegisterISet_3_T2
            RegisterISet_3_TElement = PropertyBag_0.RegisterISet_MethodGroup.RegisterISet_3_T3
            def __call__(self) -> None:...


    # Skipped RegisterList due to it being static, abstract and generic.

    RegisterList : RegisterList_MethodGroup
    class RegisterList_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[RegisterList_1_T1]) -> RegisterList_1[RegisterList_1_T1]: ...

        RegisterList_1_T1 = typing.TypeVar('RegisterList_1_T1')
        class RegisterList_1(typing.Generic[RegisterList_1_T1]):
            RegisterList_1_TElement = PropertyBag_0.RegisterList_MethodGroup.RegisterList_1_T1
            def __call__(self) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterList_2_T1], typing.Type[RegisterList_2_T2]]) -> RegisterList_2[RegisterList_2_T1, RegisterList_2_T2]: ...

        RegisterList_2_T1 = typing.TypeVar('RegisterList_2_T1')
        RegisterList_2_T2 = typing.TypeVar('RegisterList_2_T2')
        class RegisterList_2(typing.Generic[RegisterList_2_T1, RegisterList_2_T2]):
            RegisterList_2_TContainer = PropertyBag_0.RegisterList_MethodGroup.RegisterList_2_T1
            RegisterList_2_TElement = PropertyBag_0.RegisterList_MethodGroup.RegisterList_2_T2
            def __call__(self) -> None:...


    # Skipped TryGetPropertyBagForValue due to it being static, abstract and generic.

    TryGetPropertyBagForValue : TryGetPropertyBagForValue_MethodGroup
    class TryGetPropertyBagForValue_MethodGroup:
        def __getitem__(self, t:typing.Type[TryGetPropertyBagForValue_1_T1]) -> TryGetPropertyBagForValue_1[TryGetPropertyBagForValue_1_T1]: ...

        TryGetPropertyBagForValue_1_T1 = typing.TypeVar('TryGetPropertyBagForValue_1_T1')
        class TryGetPropertyBagForValue_1(typing.Generic[TryGetPropertyBagForValue_1_T1]):
            TryGetPropertyBagForValue_1_TValue = PropertyBag_0.TryGetPropertyBagForValue_MethodGroup.TryGetPropertyBagForValue_1_T1
            def __call__(self, value: clr.Reference[TryGetPropertyBagForValue_1_TValue], propertyBag: clr.Reference[IPropertyBag]) -> bool:...




PropertyBag_1_TContainer = typing.TypeVar('PropertyBag_1_TContainer')
class PropertyBag_1(typing.Generic[PropertyBag_1_TContainer], IPropertyBag_1[PropertyBag_1_TContainer], abc.ABC):
    def Accept(self, visitor: ITypeVisitor) -> None: ...
    def CreateInstance(self) -> PropertyBag_1_TContainer: ...
    def TryCreateInstance(self, instance: clr.Reference[PropertyBag_1_TContainer]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[PropertyBag_1_TContainer]
    GetProperties_MethodGroup_PropertyBag_1_TContainer = typing.TypeVar('GetProperties_MethodGroup_PropertyBag_1_TContainer')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_PropertyBag_1_TContainer]):
        GetProperties_MethodGroup_PropertyBag_1_TContainer = PropertyBag_1.GetProperties_MethodGroup_PropertyBag_1_TContainer
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_PropertyBag_1_TContainer]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_PropertyBag_1_TContainer]) -> PropertyCollection_1[GetProperties_MethodGroup_PropertyBag_1_TContainer]:...



class PropertyCollection_GenericClasses(abc.ABCMeta):
    Generic_PropertyCollection_GenericClasses_PropertyCollection_1_TContainer = typing.TypeVar('Generic_PropertyCollection_GenericClasses_PropertyCollection_1_TContainer')
    def __getitem__(self, types : typing.Type[Generic_PropertyCollection_GenericClasses_PropertyCollection_1_TContainer]) -> typing.Type[PropertyCollection_1[Generic_PropertyCollection_GenericClasses_PropertyCollection_1_TContainer]]: ...

PropertyCollection : PropertyCollection_GenericClasses

PropertyCollection_1_TContainer = typing.TypeVar('PropertyCollection_1_TContainer')
class PropertyCollection_1(typing.Generic[PropertyCollection_1_TContainer], IEnumerable_1[IProperty_1[PropertyCollection_1_TContainer]]):
    @typing.overload
    def __init__(self, enumerable: IEnumerable_1[IProperty_1[PropertyCollection_1_TContainer]]) -> None: ...
    @typing.overload
    def __init__(self, properties: List_1[IProperty_1[PropertyCollection_1_TContainer]]) -> None: ...
    @classmethod
    @property
    def Empty(cls) -> PropertyCollection_1[PropertyCollection_1_TContainer]: ...
    def GetEnumerator(self) -> PropertyCollection_1.Enumerator_1[PropertyCollection_1_TContainer]: ...

    Enumerator_GenericClasses_PropertyCollection_1_TContainer = typing.TypeVar('Enumerator_GenericClasses_PropertyCollection_1_TContainer')
    class Enumerator_GenericClasses(typing.Generic[Enumerator_GenericClasses_PropertyCollection_1_TContainer], abc.ABCMeta):
        Enumerator_GenericClasses_PropertyCollection_1_TContainer = PropertyCollection_1.Enumerator_GenericClasses_PropertyCollection_1_TContainer
        def __call__(self) -> PropertyCollection_1.Enumerator_1[Enumerator_GenericClasses_PropertyCollection_1_TContainer]: ...

    Enumerator : Enumerator_GenericClasses[PropertyCollection_1_TContainer]

    Enumerator_1_TContainer = typing.TypeVar('Enumerator_1_TContainer')
    class Enumerator_1(typing.Generic[Enumerator_1_TContainer], IEnumerator_1[IProperty_1[Enumerator_1_TContainer]]):
        Enumerator_1_TContainer = PropertyCollection_1.Enumerator_1_TContainer
        @property
        def Current(self) -> IProperty_1[Enumerator_1_TContainer]: ...
        @Current.setter
        def Current(self, value: IProperty_1[Enumerator_1_TContainer]) -> IProperty_1[Enumerator_1_TContainer]: ...
        def Dispose(self) -> None: ...
        def MoveNext(self) -> bool: ...
        def Reset(self) -> None: ...



class PropertyContainer(abc.ABC):
    # Skipped Accept due to it being static, abstract and generic.

    Accept : Accept_MethodGroup
    class Accept_MethodGroup:
        def __getitem__(self, t:typing.Type[Accept_1_T1]) -> Accept_1[Accept_1_T1]: ...

        Accept_1_T1 = typing.TypeVar('Accept_1_T1')
        class Accept_1(typing.Generic[Accept_1_T1]):
            Accept_1_TContainer = PropertyContainer.Accept_MethodGroup.Accept_1_T1
            @typing.overload
            def __call__(self, visitor: IPropertyBagVisitor, container: Accept_1_TContainer, parameters: VisitParameters = ...) -> None:...
            @typing.overload
            def __call__(self, visitor: IPropertyBagVisitor, container: clr.Reference[Accept_1_TContainer], parameters: VisitParameters = ...) -> None:...
            @typing.overload
            def __call__(self, visitor: IPropertyVisitor, container: clr.Reference[Accept_1_TContainer], path: clr.Reference[PropertyPath], parameters: VisitParameters = ...) -> None:...


    # Skipped GetProperty due to it being static, abstract and generic.

    GetProperty : GetProperty_MethodGroup
    class GetProperty_MethodGroup:
        def __getitem__(self, t:typing.Type[GetProperty_1_T1]) -> GetProperty_1[GetProperty_1_T1]: ...

        GetProperty_1_T1 = typing.TypeVar('GetProperty_1_T1')
        class GetProperty_1(typing.Generic[GetProperty_1_T1]):
            GetProperty_1_TContainer = PropertyContainer.GetProperty_MethodGroup.GetProperty_1_T1
            @typing.overload
            def __call__(self, container: GetProperty_1_TContainer, path: clr.Reference[PropertyPath]) -> IProperty:...
            @typing.overload
            def __call__(self, container: clr.Reference[GetProperty_1_TContainer], path: clr.Reference[PropertyPath]) -> IProperty:...


    # Skipped GetValue due to it being static, abstract and generic.

    GetValue : GetValue_MethodGroup
    class GetValue_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GetValue_2_T1], typing.Type[GetValue_2_T2]]) -> GetValue_2[GetValue_2_T1, GetValue_2_T2]: ...

        GetValue_2_T1 = typing.TypeVar('GetValue_2_T1')
        GetValue_2_T2 = typing.TypeVar('GetValue_2_T2')
        class GetValue_2(typing.Generic[GetValue_2_T1, GetValue_2_T2]):
            GetValue_2_TContainer = PropertyContainer.GetValue_MethodGroup.GetValue_2_T1
            GetValue_2_TValue = PropertyContainer.GetValue_MethodGroup.GetValue_2_T2
            @typing.overload
            def __call__(self, container: GetValue_2_TContainer, name: str) -> GetValue_2_TValue:...
            @typing.overload
            def __call__(self, container: GetValue_2_TContainer, path: clr.Reference[PropertyPath]) -> GetValue_2_TValue:...
            @typing.overload
            def __call__(self, container: clr.Reference[GetValue_2_TContainer], name: str) -> GetValue_2_TValue:...
            @typing.overload
            def __call__(self, container: clr.Reference[GetValue_2_TContainer], path: clr.Reference[PropertyPath]) -> GetValue_2_TValue:...


    # Skipped IsPathValid due to it being static, abstract and generic.

    IsPathValid : IsPathValid_MethodGroup
    class IsPathValid_MethodGroup:
        def __getitem__(self, t:typing.Type[IsPathValid_1_T1]) -> IsPathValid_1[IsPathValid_1_T1]: ...

        IsPathValid_1_T1 = typing.TypeVar('IsPathValid_1_T1')
        class IsPathValid_1(typing.Generic[IsPathValid_1_T1]):
            IsPathValid_1_TContainer = PropertyContainer.IsPathValid_MethodGroup.IsPathValid_1_T1
            @typing.overload
            def __call__(self, container: IsPathValid_1_TContainer, path: str) -> bool:...
            @typing.overload
            def __call__(self, container: IsPathValid_1_TContainer, path: clr.Reference[PropertyPath]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[IsPathValid_1_TContainer], path: str) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[IsPathValid_1_TContainer], path: clr.Reference[PropertyPath]) -> bool:...


    # Skipped SetValue due to it being static, abstract and generic.

    SetValue : SetValue_MethodGroup
    class SetValue_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[SetValue_2_T1], typing.Type[SetValue_2_T2]]) -> SetValue_2[SetValue_2_T1, SetValue_2_T2]: ...

        SetValue_2_T1 = typing.TypeVar('SetValue_2_T1')
        SetValue_2_T2 = typing.TypeVar('SetValue_2_T2')
        class SetValue_2(typing.Generic[SetValue_2_T1, SetValue_2_T2]):
            SetValue_2_TContainer = PropertyContainer.SetValue_MethodGroup.SetValue_2_T1
            SetValue_2_TValue = PropertyContainer.SetValue_MethodGroup.SetValue_2_T2
            @typing.overload
            def __call__(self, container: SetValue_2_TContainer, name: str, value: SetValue_2_TValue) -> None:...
            @typing.overload
            def __call__(self, container: SetValue_2_TContainer, path: clr.Reference[PropertyPath], value: SetValue_2_TValue) -> None:...
            @typing.overload
            def __call__(self, container: clr.Reference[SetValue_2_TContainer], name: str, value: SetValue_2_TValue) -> None:...
            @typing.overload
            def __call__(self, container: clr.Reference[SetValue_2_TContainer], path: clr.Reference[PropertyPath], value: SetValue_2_TValue) -> None:...


    # Skipped TryAccept due to it being static, abstract and generic.

    TryAccept : TryAccept_MethodGroup
    class TryAccept_MethodGroup:
        def __getitem__(self, t:typing.Type[TryAccept_1_T1]) -> TryAccept_1[TryAccept_1_T1]: ...

        TryAccept_1_T1 = typing.TypeVar('TryAccept_1_T1')
        class TryAccept_1(typing.Generic[TryAccept_1_T1]):
            TryAccept_1_TContainer = PropertyContainer.TryAccept_MethodGroup.TryAccept_1_T1
            @typing.overload
            def __call__(self, visitor: IPropertyBagVisitor, container: clr.Reference[TryAccept_1_TContainer], parameters: VisitParameters = ...) -> bool:...
            @typing.overload
            def __call__(self, visitor: IPropertyBagVisitor, container: clr.Reference[TryAccept_1_TContainer], returnCode: clr.Reference[VisitReturnCode], parameters: VisitParameters = ...) -> bool:...
            @typing.overload
            def __call__(self, visitor: IPropertyVisitor, container: clr.Reference[TryAccept_1_TContainer], path: clr.Reference[PropertyPath], returnCode: clr.Reference[VisitReturnCode], parameters: VisitParameters = ...) -> bool:...


    # Skipped TryGetProperty due to it being static, abstract and generic.

    TryGetProperty : TryGetProperty_MethodGroup
    class TryGetProperty_MethodGroup:
        def __getitem__(self, t:typing.Type[TryGetProperty_1_T1]) -> TryGetProperty_1[TryGetProperty_1_T1]: ...

        TryGetProperty_1_T1 = typing.TypeVar('TryGetProperty_1_T1')
        class TryGetProperty_1(typing.Generic[TryGetProperty_1_T1]):
            TryGetProperty_1_TContainer = PropertyContainer.TryGetProperty_MethodGroup.TryGetProperty_1_T1
            @typing.overload
            def __call__(self, container: TryGetProperty_1_TContainer, path: clr.Reference[PropertyPath], property: clr.Reference[IProperty]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TryGetProperty_1_TContainer], path: clr.Reference[PropertyPath], property: clr.Reference[IProperty]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TryGetProperty_1_TContainer], path: clr.Reference[PropertyPath], property: clr.Reference[IProperty], returnCode: clr.Reference[VisitReturnCode]) -> bool:...


    # Skipped TryGetValue due to it being static, abstract and generic.

    TryGetValue : TryGetValue_MethodGroup
    class TryGetValue_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[TryGetValue_2_T1], typing.Type[TryGetValue_2_T2]]) -> TryGetValue_2[TryGetValue_2_T1, TryGetValue_2_T2]: ...

        TryGetValue_2_T1 = typing.TypeVar('TryGetValue_2_T1')
        TryGetValue_2_T2 = typing.TypeVar('TryGetValue_2_T2')
        class TryGetValue_2(typing.Generic[TryGetValue_2_T1, TryGetValue_2_T2]):
            TryGetValue_2_TContainer = PropertyContainer.TryGetValue_MethodGroup.TryGetValue_2_T1
            TryGetValue_2_TValue = PropertyContainer.TryGetValue_MethodGroup.TryGetValue_2_T2
            @typing.overload
            def __call__(self, container: TryGetValue_2_TContainer, name: str, value: clr.Reference[TryGetValue_2_TValue]) -> bool:...
            @typing.overload
            def __call__(self, container: TryGetValue_2_TContainer, path: clr.Reference[PropertyPath], value: clr.Reference[TryGetValue_2_TValue]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TryGetValue_2_TContainer], name: str, value: clr.Reference[TryGetValue_2_TValue]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TryGetValue_2_TContainer], path: clr.Reference[PropertyPath], value: clr.Reference[TryGetValue_2_TValue]) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TryGetValue_2_TContainer], path: clr.Reference[PropertyPath], value: clr.Reference[TryGetValue_2_TValue], returnCode: clr.Reference[VisitReturnCode]) -> bool:...


    # Skipped TrySetValue due to it being static, abstract and generic.

    TrySetValue : TrySetValue_MethodGroup
    class TrySetValue_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[TrySetValue_2_T1], typing.Type[TrySetValue_2_T2]]) -> TrySetValue_2[TrySetValue_2_T1, TrySetValue_2_T2]: ...

        TrySetValue_2_T1 = typing.TypeVar('TrySetValue_2_T1')
        TrySetValue_2_T2 = typing.TypeVar('TrySetValue_2_T2')
        class TrySetValue_2(typing.Generic[TrySetValue_2_T1, TrySetValue_2_T2]):
            TrySetValue_2_TContainer = PropertyContainer.TrySetValue_MethodGroup.TrySetValue_2_T1
            TrySetValue_2_TValue = PropertyContainer.TrySetValue_MethodGroup.TrySetValue_2_T2
            @typing.overload
            def __call__(self, container: TrySetValue_2_TContainer, name: str, value: TrySetValue_2_TValue) -> bool:...
            @typing.overload
            def __call__(self, container: TrySetValue_2_TContainer, path: clr.Reference[PropertyPath], value: TrySetValue_2_TValue) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TrySetValue_2_TContainer], name: str, value: TrySetValue_2_TValue) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TrySetValue_2_TContainer], path: clr.Reference[PropertyPath], value: TrySetValue_2_TValue) -> bool:...
            @typing.overload
            def __call__(self, container: clr.Reference[TrySetValue_2_TContainer], path: clr.Reference[PropertyPath], value: TrySetValue_2_TValue, returnCode: clr.Reference[VisitReturnCode]) -> bool:...




class PropertyGetter_GenericClasses(abc.ABCMeta):
    Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TContainer = typing.TypeVar('Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TContainer')
    Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TValue = typing.TypeVar('Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TContainer], typing.Type[Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TValue]]) -> typing.Type[PropertyGetter_2[Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TContainer, Generic_PropertyGetter_GenericClasses_PropertyGetter_2_TValue]]: ...

PropertyGetter : PropertyGetter_GenericClasses

PropertyGetter_2_TContainer = typing.TypeVar('PropertyGetter_2_TContainer')
PropertyGetter_2_TValue = typing.TypeVar('PropertyGetter_2_TValue', covariant=True)
class PropertyGetter_2(typing.Generic[PropertyGetter_2_TContainer, PropertyGetter_2_TValue], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, container: clr.Reference[PropertyGetter_2_TContainer], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, container: clr.Reference[PropertyGetter_2_TContainer], result: IAsyncResult) -> PropertyGetter_2_TValue: ...
    def Invoke(self, container: clr.Reference[PropertyGetter_2_TContainer]) -> PropertyGetter_2_TValue: ...


class PropertyPath(IEquatable_1[PropertyPath]):
    def __init__(self, path: str) -> None: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def Item(self) -> PropertyPathPart: ...
    @property
    def Length(self) -> int: ...
    @staticmethod
    def AppendIndex(path: clr.Reference[PropertyPath], index: int) -> PropertyPath: ...
    @staticmethod
    def AppendKey(path: clr.Reference[PropertyPath], key: typing.Any) -> PropertyPath: ...
    @staticmethod
    def AppendName(path: clr.Reference[PropertyPath], name: str) -> PropertyPath: ...
    @staticmethod
    def AppendPart(path: clr.Reference[PropertyPath], part: clr.Reference[PropertyPathPart]) -> PropertyPath: ...
    @staticmethod
    def AppendProperty(path: clr.Reference[PropertyPath], property: IProperty) -> PropertyPath: ...
    @staticmethod
    def FromIndex(index: int) -> PropertyPath: ...
    @staticmethod
    def FromKey(key: typing.Any) -> PropertyPath: ...
    @staticmethod
    def FromName(name: str) -> PropertyPath: ...
    @staticmethod
    def FromPart(part: clr.Reference[PropertyPathPart]) -> PropertyPath: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Pop(path: clr.Reference[PropertyPath]) -> PropertyPath: ...
    def ToString(self) -> str: ...
    # Skipped Combine due to it being static, abstract and generic.

    Combine : Combine_MethodGroup
    class Combine_MethodGroup:
        @typing.overload
        def __call__(self, path: clr.Reference[PropertyPath], pathToAppend: str) -> PropertyPath:...
        @typing.overload
        def __call__(self, path: clr.Reference[PropertyPath], pathToAppend: clr.Reference[PropertyPath]) -> PropertyPath:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: PropertyPath) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped SubPath due to it being static, abstract and generic.

    SubPath : SubPath_MethodGroup
    class SubPath_MethodGroup:
        @typing.overload
        def __call__(self, path: clr.Reference[PropertyPath], startIndex: int) -> PropertyPath:...
        @typing.overload
        def __call__(self, path: clr.Reference[PropertyPath], startIndex: int, length: int) -> PropertyPath:...



class PropertyPathPart(IEquatable_1[PropertyPathPart]):
    @typing.overload
    def __init__(self, index: int) -> None: ...
    @typing.overload
    def __init__(self, key: typing.Any) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @property
    def Index(self) -> int: ...
    @property
    def IsIndex(self) -> bool: ...
    @property
    def IsKey(self) -> bool: ...
    @property
    def IsName(self) -> bool: ...
    @property
    def Key(self) -> typing.Any: ...
    @property
    def Kind(self) -> PropertyPathPartKind: ...
    @property
    def Name(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: PropertyPathPart) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class PropertyPathPartKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Name : PropertyPathPartKind # 0
    Index : PropertyPathPartKind # 1
    Key : PropertyPathPartKind # 2


class PropertySetter_GenericClasses(abc.ABCMeta):
    Generic_PropertySetter_GenericClasses_PropertySetter_2_TContainer = typing.TypeVar('Generic_PropertySetter_GenericClasses_PropertySetter_2_TContainer')
    Generic_PropertySetter_GenericClasses_PropertySetter_2_TValue = typing.TypeVar('Generic_PropertySetter_GenericClasses_PropertySetter_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_PropertySetter_GenericClasses_PropertySetter_2_TContainer], typing.Type[Generic_PropertySetter_GenericClasses_PropertySetter_2_TValue]]) -> typing.Type[PropertySetter_2[Generic_PropertySetter_GenericClasses_PropertySetter_2_TContainer, Generic_PropertySetter_GenericClasses_PropertySetter_2_TValue]]: ...

PropertySetter : PropertySetter_GenericClasses

PropertySetter_2_TContainer = typing.TypeVar('PropertySetter_2_TContainer')
PropertySetter_2_TValue = typing.TypeVar('PropertySetter_2_TValue', contravariant=True)
class PropertySetter_2(typing.Generic[PropertySetter_2_TContainer, PropertySetter_2_TValue], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, container: clr.Reference[PropertySetter_2_TContainer], value: PropertySetter_2_TValue, callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, container: clr.Reference[PropertySetter_2_TContainer], result: IAsyncResult) -> None: ...
    def Invoke(self, container: clr.Reference[PropertySetter_2_TContainer], value: PropertySetter_2_TValue) -> None: ...


class PropertyVisitor(IDictionaryPropertyVisitor, ISetPropertyVisitor, IListPropertyVisitor, ICollectionPropertyVisitor, IPropertyVisitor, IDictionaryPropertyBagVisitor, IListPropertyBagVisitor, IPropertyBagVisitor, abc.ABC):
    def AddAdapter(self, adapter: IPropertyVisitorAdapter) -> None: ...
    def RemoveAdapter(self, adapter: IPropertyVisitorAdapter) -> None: ...


class ReflectedMemberProperty_GenericClasses(abc.ABCMeta):
    Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TContainer = typing.TypeVar('Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TContainer')
    Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TValue = typing.TypeVar('Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TContainer], typing.Type[Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TValue]]) -> typing.Type[ReflectedMemberProperty_2[Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TContainer, Generic_ReflectedMemberProperty_GenericClasses_ReflectedMemberProperty_2_TValue]]: ...

ReflectedMemberProperty : ReflectedMemberProperty_GenericClasses

ReflectedMemberProperty_2_TContainer = typing.TypeVar('ReflectedMemberProperty_2_TContainer')
ReflectedMemberProperty_2_TValue = typing.TypeVar('ReflectedMemberProperty_2_TValue')
class ReflectedMemberProperty_2(typing.Generic[ReflectedMemberProperty_2_TContainer, ReflectedMemberProperty_2_TValue], Property_2[ReflectedMemberProperty_2_TContainer, ReflectedMemberProperty_2_TValue]):
    @typing.overload
    def __init__(self, info: FieldInfo, name: str) -> None: ...
    @typing.overload
    def __init__(self, info: PropertyInfo, name: str) -> None: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    def GetValue(self, container: clr.Reference[ReflectedMemberProperty_2_TContainer]) -> ReflectedMemberProperty_2_TValue: ...
    def SetValue(self, container: clr.Reference[ReflectedMemberProperty_2_TContainer], value: ReflectedMemberProperty_2_TValue) -> None: ...


class SetPropertyBagBase_GenericClasses(abc.ABCMeta):
    Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TSet = typing.TypeVar('Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TSet')
    Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TElement = typing.TypeVar('Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TElement')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TSet], typing.Type[Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TElement]]) -> typing.Type[SetPropertyBagBase_2[Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TSet, Generic_SetPropertyBagBase_GenericClasses_SetPropertyBagBase_2_TElement]]: ...

SetPropertyBagBase : SetPropertyBagBase_GenericClasses

SetPropertyBagBase_2_TSet = typing.TypeVar('SetPropertyBagBase_2_TSet')
SetPropertyBagBase_2_TElement = typing.TypeVar('SetPropertyBagBase_2_TElement')
class SetPropertyBagBase_2(typing.Generic[SetPropertyBagBase_2_TSet, SetPropertyBagBase_2_TElement], PropertyBag_1[SetPropertyBagBase_2_TSet], ISetPropertyBag_2[SetPropertyBagBase_2_TSet, SetPropertyBagBase_2_TElement]):
    def __init__(self) -> None: ...
    def TryGetProperty(self, container: clr.Reference[SetPropertyBagBase_2_TSet], key: typing.Any, property: clr.Reference[IProperty_1[SetPropertyBagBase_2_TSet]]) -> bool: ...
    # Skipped GetProperties due to it being static, abstract and generic.

    GetProperties : GetProperties_MethodGroup[SetPropertyBagBase_2_TSet, SetPropertyBagBase_2_TElement]
    GetProperties_MethodGroup_SetPropertyBagBase_2_TSet = typing.TypeVar('GetProperties_MethodGroup_SetPropertyBagBase_2_TSet')
    GetProperties_MethodGroup_SetPropertyBagBase_2_TElement = typing.TypeVar('GetProperties_MethodGroup_SetPropertyBagBase_2_TElement')
    class GetProperties_MethodGroup(typing.Generic[GetProperties_MethodGroup_SetPropertyBagBase_2_TSet, GetProperties_MethodGroup_SetPropertyBagBase_2_TElement]):
        GetProperties_MethodGroup_SetPropertyBagBase_2_TSet = SetPropertyBagBase_2.GetProperties_MethodGroup_SetPropertyBagBase_2_TSet
        GetProperties_MethodGroup_SetPropertyBagBase_2_TElement = SetPropertyBagBase_2.GetProperties_MethodGroup_SetPropertyBagBase_2_TElement
        @typing.overload
        def __call__(self) -> PropertyCollection_1[GetProperties_MethodGroup_SetPropertyBagBase_2_TSet]:...
        @typing.overload
        def __call__(self, container: clr.Reference[GetProperties_MethodGroup_SetPropertyBagBase_2_TSet]) -> PropertyCollection_1[GetProperties_MethodGroup_SetPropertyBagBase_2_TSet]:...



class TypeConversion(abc.ABC):
    # Skipped Convert due to it being static, abstract and generic.

    Convert : Convert_MethodGroup
    class Convert_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Convert_2_T1], typing.Type[Convert_2_T2]]) -> Convert_2[Convert_2_T1, Convert_2_T2]: ...

        Convert_2_T1 = typing.TypeVar('Convert_2_T1')
        Convert_2_T2 = typing.TypeVar('Convert_2_T2')
        class Convert_2(typing.Generic[Convert_2_T1, Convert_2_T2]):
            Convert_2_TSource = TypeConversion.Convert_MethodGroup.Convert_2_T1
            Convert_2_TDestination = TypeConversion.Convert_MethodGroup.Convert_2_T2
            def __call__(self, value: clr.Reference[Convert_2_TSource]) -> Convert_2_TDestination:...


    # Skipped Register due to it being static, abstract and generic.

    Register : Register_MethodGroup
    class Register_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[Register_2_T1], typing.Type[Register_2_T2]]) -> Register_2[Register_2_T1, Register_2_T2]: ...

        Register_2_T1 = typing.TypeVar('Register_2_T1')
        Register_2_T2 = typing.TypeVar('Register_2_T2')
        class Register_2(typing.Generic[Register_2_T1, Register_2_T2]):
            Register_2_TSource = TypeConversion.Register_MethodGroup.Register_2_T1
            Register_2_TDestination = TypeConversion.Register_MethodGroup.Register_2_T2
            def __call__(self, converter: TypeConverter_2[Register_2_TSource, Register_2_TDestination]) -> None:...


    # Skipped TryConvert due to it being static, abstract and generic.

    TryConvert : TryConvert_MethodGroup
    class TryConvert_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[TryConvert_2_T1], typing.Type[TryConvert_2_T2]]) -> TryConvert_2[TryConvert_2_T1, TryConvert_2_T2]: ...

        TryConvert_2_T1 = typing.TypeVar('TryConvert_2_T1')
        TryConvert_2_T2 = typing.TypeVar('TryConvert_2_T2')
        class TryConvert_2(typing.Generic[TryConvert_2_T1, TryConvert_2_T2]):
            TryConvert_2_TSource = TypeConversion.TryConvert_MethodGroup.TryConvert_2_T1
            TryConvert_2_TDestination = TypeConversion.TryConvert_MethodGroup.TryConvert_2_T2
            def __call__(self, source: clr.Reference[TryConvert_2_TSource], destination: clr.Reference[TryConvert_2_TDestination]) -> bool:...




class TypeConverter_GenericClasses(abc.ABCMeta):
    Generic_TypeConverter_GenericClasses_TypeConverter_2_TSource = typing.TypeVar('Generic_TypeConverter_GenericClasses_TypeConverter_2_TSource')
    Generic_TypeConverter_GenericClasses_TypeConverter_2_TDestination = typing.TypeVar('Generic_TypeConverter_GenericClasses_TypeConverter_2_TDestination')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_TypeConverter_GenericClasses_TypeConverter_2_TSource], typing.Type[Generic_TypeConverter_GenericClasses_TypeConverter_2_TDestination]]) -> typing.Type[TypeConverter_2[Generic_TypeConverter_GenericClasses_TypeConverter_2_TSource, Generic_TypeConverter_GenericClasses_TypeConverter_2_TDestination]]: ...

TypeConverter : TypeConverter_GenericClasses

TypeConverter_2_TSource = typing.TypeVar('TypeConverter_2_TSource')
TypeConverter_2_TDestination = typing.TypeVar('TypeConverter_2_TDestination', covariant=True)
class TypeConverter_2(typing.Generic[TypeConverter_2_TSource, TypeConverter_2_TDestination], MulticastDelegate):
    def __init__(self, object: typing.Any, method: int) -> None: ...
    @property
    def Method(self) -> MethodInfo: ...
    @property
    def Target(self) -> typing.Any: ...
    def BeginInvoke(self, value: clr.Reference[TypeConverter_2_TSource], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
    def EndInvoke(self, value: clr.Reference[TypeConverter_2_TSource], result: IAsyncResult) -> TypeConverter_2_TDestination: ...
    def Invoke(self, value: clr.Reference[TypeConverter_2_TSource]) -> TypeConverter_2_TDestination: ...


class TypeGenerationOptions(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : TypeGenerationOptions # 0
    ValueType : TypeGenerationOptions # 2
    ReferenceType : TypeGenerationOptions # 4
    Default : TypeGenerationOptions # 6


class TypeTraits_GenericClasses(abc.ABCMeta):
    Generic_TypeTraits_GenericClasses_TypeTraits_1_T = typing.TypeVar('Generic_TypeTraits_GenericClasses_TypeTraits_1_T')
    def __getitem__(self, types : typing.Type[Generic_TypeTraits_GenericClasses_TypeTraits_1_T]) -> typing.Type[TypeTraits_1[Generic_TypeTraits_GenericClasses_TypeTraits_1_T]]: ...

class TypeTraits(TypeTraits_0, metaclass =TypeTraits_GenericClasses): ...

class TypeTraits_0(abc.ABC):
    @staticmethod
    def IsContainer(type: typing.Type[typing.Any]) -> bool: ...


TypeTraits_1_T = typing.TypeVar('TypeTraits_1_T')
class TypeTraits_1(typing.Generic[TypeTraits_1_T], abc.ABC):
    @classmethod
    @property
    def CanBeNull(cls) -> bool: ...
    @classmethod
    @property
    def IsAbstract(cls) -> bool: ...
    @classmethod
    @property
    def IsAbstractOrInterface(cls) -> bool: ...
    @classmethod
    @property
    def IsArray(cls) -> bool: ...
    @classmethod
    @property
    def IsContainer(cls) -> bool: ...
    @classmethod
    @property
    def IsEnum(cls) -> bool: ...
    @classmethod
    @property
    def IsEnumFlags(cls) -> bool: ...
    @classmethod
    @property
    def IsInterface(cls) -> bool: ...
    @classmethod
    @property
    def IsLazyLoadReference(cls) -> bool: ...
    @classmethod
    @property
    def IsMultidimensionalArray(cls) -> bool: ...
    @classmethod
    @property
    def IsNullable(cls) -> bool: ...
    @classmethod
    @property
    def IsObject(cls) -> bool: ...
    @classmethod
    @property
    def IsPrimitive(cls) -> bool: ...
    @classmethod
    @property
    def IsPrimitiveOrString(cls) -> bool: ...
    @classmethod
    @property
    def IsString(cls) -> bool: ...
    @classmethod
    @property
    def IsUnityObject(cls) -> bool: ...
    @classmethod
    @property
    def IsValueType(cls) -> bool: ...


class TypeUtility(abc.ABC):
    @staticmethod
    def GetRootType(type: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    @staticmethod
    def GetTypeDisplayName(type: typing.Type[typing.Any]) -> str: ...
    # Skipped CanBeInstantiated due to it being static, abstract and generic.

    CanBeInstantiated : CanBeInstantiated_MethodGroup
    class CanBeInstantiated_MethodGroup:
        def __getitem__(self, t:typing.Type[CanBeInstantiated_1_T1]) -> CanBeInstantiated_1[CanBeInstantiated_1_T1]: ...

        CanBeInstantiated_1_T1 = typing.TypeVar('CanBeInstantiated_1_T1')
        class CanBeInstantiated_1(typing.Generic[CanBeInstantiated_1_T1]):
            CanBeInstantiated_1_T = TypeUtility.CanBeInstantiated_MethodGroup.CanBeInstantiated_1_T1
            def __call__(self) -> bool:...

        def __call__(self, type: typing.Type[typing.Any]) -> bool:...

    # Skipped Instantiate due to it being static, abstract and generic.

    Instantiate : Instantiate_MethodGroup
    class Instantiate_MethodGroup:
        def __getitem__(self, t:typing.Type[Instantiate_1_T1]) -> Instantiate_1[Instantiate_1_T1]: ...

        Instantiate_1_T1 = typing.TypeVar('Instantiate_1_T1')
        class Instantiate_1(typing.Generic[Instantiate_1_T1]):
            Instantiate_1_T = TypeUtility.Instantiate_MethodGroup.Instantiate_1_T1
            @typing.overload
            def __call__(self) -> Instantiate_1_T:...
            @typing.overload
            def __call__(self, derivedType: typing.Type[typing.Any]) -> Instantiate_1_T:...


    # Skipped InstantiateArray due to it being static, abstract and generic.

    InstantiateArray : InstantiateArray_MethodGroup
    class InstantiateArray_MethodGroup:
        def __getitem__(self, t:typing.Type[InstantiateArray_1_T1]) -> InstantiateArray_1[InstantiateArray_1_T1]: ...

        InstantiateArray_1_T1 = typing.TypeVar('InstantiateArray_1_T1')
        class InstantiateArray_1(typing.Generic[InstantiateArray_1_T1]):
            InstantiateArray_1_TArray = TypeUtility.InstantiateArray_MethodGroup.InstantiateArray_1_T1
            @typing.overload
            def __call__(self, count: int = ...) -> InstantiateArray_1_TArray:...
            @typing.overload
            def __call__(self, derivedType: typing.Type[typing.Any], count: int = ...) -> InstantiateArray_1_TArray:...


    # Skipped SetExplicitInstantiationMethod due to it being static, abstract and generic.

    SetExplicitInstantiationMethod : SetExplicitInstantiationMethod_MethodGroup
    class SetExplicitInstantiationMethod_MethodGroup:
        def __getitem__(self, t:typing.Type[SetExplicitInstantiationMethod_1_T1]) -> SetExplicitInstantiationMethod_1[SetExplicitInstantiationMethod_1_T1]: ...

        SetExplicitInstantiationMethod_1_T1 = typing.TypeVar('SetExplicitInstantiationMethod_1_T1')
        class SetExplicitInstantiationMethod_1(typing.Generic[SetExplicitInstantiationMethod_1_T1]):
            SetExplicitInstantiationMethod_1_T = TypeUtility.SetExplicitInstantiationMethod_MethodGroup.SetExplicitInstantiationMethod_1_T1
            def __call__(self, constructor: Func_1[SetExplicitInstantiationMethod_1_T]) -> None:...


    # Skipped TryInstantiate due to it being static, abstract and generic.

    TryInstantiate : TryInstantiate_MethodGroup
    class TryInstantiate_MethodGroup:
        def __getitem__(self, t:typing.Type[TryInstantiate_1_T1]) -> TryInstantiate_1[TryInstantiate_1_T1]: ...

        TryInstantiate_1_T1 = typing.TypeVar('TryInstantiate_1_T1')
        class TryInstantiate_1(typing.Generic[TryInstantiate_1_T1]):
            TryInstantiate_1_T = TypeUtility.TryInstantiate_MethodGroup.TryInstantiate_1_T1
            @typing.overload
            def __call__(self, instance: clr.Reference[TryInstantiate_1_T]) -> bool:...
            @typing.overload
            def __call__(self, derivedType: typing.Type[typing.Any], value: clr.Reference[TryInstantiate_1_T]) -> bool:...


    # Skipped TryInstantiateArray due to it being static, abstract and generic.

    TryInstantiateArray : TryInstantiateArray_MethodGroup
    class TryInstantiateArray_MethodGroup:
        def __getitem__(self, t:typing.Type[TryInstantiateArray_1_T1]) -> TryInstantiateArray_1[TryInstantiateArray_1_T1]: ...

        TryInstantiateArray_1_T1 = typing.TypeVar('TryInstantiateArray_1_T1')
        class TryInstantiateArray_1(typing.Generic[TryInstantiateArray_1_T1]):
            TryInstantiateArray_1_TArray = TypeUtility.TryInstantiateArray_MethodGroup.TryInstantiateArray_1_T1
            def __call__(self, count: int, instance: clr.Reference[TryInstantiateArray_1_TArray]) -> bool:...




class VisitContext_GenericClasses(abc.ABCMeta):
    Generic_VisitContext_GenericClasses_VisitContext_1_TContainer = typing.TypeVar('Generic_VisitContext_GenericClasses_VisitContext_1_TContainer')
    @typing.overload
    def __getitem__(self, types : typing.Type[Generic_VisitContext_GenericClasses_VisitContext_1_TContainer]) -> typing.Type[VisitContext_1[Generic_VisitContext_GenericClasses_VisitContext_1_TContainer]]: ...
    Generic_VisitContext_GenericClasses_VisitContext_2_TContainer = typing.TypeVar('Generic_VisitContext_GenericClasses_VisitContext_2_TContainer')
    Generic_VisitContext_GenericClasses_VisitContext_2_TValue = typing.TypeVar('Generic_VisitContext_GenericClasses_VisitContext_2_TValue')
    @typing.overload
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_VisitContext_GenericClasses_VisitContext_2_TContainer], typing.Type[Generic_VisitContext_GenericClasses_VisitContext_2_TValue]]) -> typing.Type[VisitContext_2[Generic_VisitContext_GenericClasses_VisitContext_2_TContainer, Generic_VisitContext_GenericClasses_VisitContext_2_TValue]]: ...

VisitContext : VisitContext_GenericClasses

VisitContext_1_TContainer = typing.TypeVar('VisitContext_1_TContainer')
class VisitContext_1(typing.Generic[VisitContext_1_TContainer]):
    @property
    def Property(self) -> IProperty_1[VisitContext_1_TContainer]: ...
    def ContinueVisitation(self, container: clr.Reference[VisitContext_1_TContainer]) -> None: ...
    def ContinueVisitationWithoutAdapters(self, container: clr.Reference[VisitContext_1_TContainer]) -> None: ...


VisitContext_2_TContainer = typing.TypeVar('VisitContext_2_TContainer')
VisitContext_2_TValue = typing.TypeVar('VisitContext_2_TValue')
class VisitContext_2(typing.Generic[VisitContext_2_TContainer, VisitContext_2_TValue]):
    @property
    def Property(self) -> Property_2[VisitContext_2_TContainer, VisitContext_2_TValue]: ...
    def ContinueVisitation(self, container: clr.Reference[VisitContext_2_TContainer], value: clr.Reference[VisitContext_2_TValue]) -> None: ...
    def ContinueVisitationWithoutAdapters(self, container: clr.Reference[VisitContext_2_TContainer], value: clr.Reference[VisitContext_2_TValue]) -> None: ...


class VisitExceptionKind(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : VisitExceptionKind # 0
    Internal : VisitExceptionKind # 1
    Visitor : VisitExceptionKind # 2
    All : VisitExceptionKind # 3


class VisitParameters:
    @property
    def IgnoreExceptions(self) -> VisitExceptionKind: ...
    @IgnoreExceptions.setter
    def IgnoreExceptions(self, value: VisitExceptionKind) -> VisitExceptionKind: ...


class VisitReturnCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Ok : VisitReturnCode # 0
    NullContainer : VisitReturnCode # 1
    InvalidContainerType : VisitReturnCode # 2
    MissingPropertyBag : VisitReturnCode # 3
    InvalidPath : VisitReturnCode # 4
    InvalidCast : VisitReturnCode # 5
    AccessViolation : VisitReturnCode # 6

