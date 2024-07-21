import typing, abc
from UnityEngine.SubsystemsImplementation import SubsystemProxy_2, SubsystemDescriptorWithProvider_2, SubsystemWithProvider_3

class SubsystemDescriptorExtensions(abc.ABC):
    # Skipped CreateProxy due to it being static, abstract and generic.

    CreateProxy : CreateProxy_MethodGroup
    class CreateProxy_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[CreateProxy_2_T1], typing.Type[CreateProxy_2_T2]]) -> CreateProxy_2[CreateProxy_2_T1, CreateProxy_2_T2]: ...

        CreateProxy_2_T1 = typing.TypeVar('CreateProxy_2_T1')
        CreateProxy_2_T2 = typing.TypeVar('CreateProxy_2_T2')
        class CreateProxy_2(typing.Generic[CreateProxy_2_T1, CreateProxy_2_T2]):
            CreateProxy_2_TSubsystem = SubsystemDescriptorExtensions.CreateProxy_MethodGroup.CreateProxy_2_T1
            CreateProxy_2_TProvider = SubsystemDescriptorExtensions.CreateProxy_MethodGroup.CreateProxy_2_T2
            def __call__(self, descriptor: SubsystemDescriptorWithProvider_2[CreateProxy_2_TSubsystem, CreateProxy_2_TProvider]) -> SubsystemProxy_2[CreateProxy_2_TSubsystem, CreateProxy_2_TProvider]:...




class SubsystemExtensions(abc.ABC):
    # Skipped GetProvider due to it being static, abstract and generic.

    GetProvider : GetProvider_MethodGroup
    class GetProvider_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[GetProvider_3_T1], typing.Type[GetProvider_3_T2], typing.Type[GetProvider_3_T3]]) -> GetProvider_3[GetProvider_3_T1, GetProvider_3_T2, GetProvider_3_T3]: ...

        GetProvider_3_T1 = typing.TypeVar('GetProvider_3_T1')
        GetProvider_3_T2 = typing.TypeVar('GetProvider_3_T2')
        GetProvider_3_T3 = typing.TypeVar('GetProvider_3_T3')
        class GetProvider_3(typing.Generic[GetProvider_3_T1, GetProvider_3_T2, GetProvider_3_T3]):
            GetProvider_3_TSubsystem = SubsystemExtensions.GetProvider_MethodGroup.GetProvider_3_T1
            GetProvider_3_TDescriptor = SubsystemExtensions.GetProvider_MethodGroup.GetProvider_3_T2
            GetProvider_3_TProvider = SubsystemExtensions.GetProvider_MethodGroup.GetProvider_3_T3
            def __call__(self, subsystem: SubsystemWithProvider_3[GetProvider_3_TSubsystem, GetProvider_3_TDescriptor, GetProvider_3_TProvider]) -> GetProvider_3_TProvider:...



