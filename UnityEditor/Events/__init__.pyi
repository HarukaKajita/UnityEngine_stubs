import typing, abc
from UnityEngine.Events import UnityEventBase, UnityAction_1, UnityAction, UnityEvent_1, UnityEvent_2, UnityAction_2, UnityEvent_3, UnityAction_3, UnityEvent_4, UnityAction_4, UnityEvent

class UnityEventTools(abc.ABC):
    @staticmethod
    def AddBoolPersistentListener(unityEvent: UnityEventBase, call: UnityAction_1[bool], argument: bool) -> None: ...
    @staticmethod
    def AddFloatPersistentListener(unityEvent: UnityEventBase, call: UnityAction_1[float], argument: float) -> None: ...
    @staticmethod
    def AddIntPersistentListener(unityEvent: UnityEventBase, call: UnityAction_1[int], argument: int) -> None: ...
    @staticmethod
    def AddStringPersistentListener(unityEvent: UnityEventBase, call: UnityAction_1[str], argument: str) -> None: ...
    @staticmethod
    def AddVoidPersistentListener(unityEvent: UnityEventBase, call: UnityAction) -> None: ...
    @staticmethod
    def RegisterBoolPersistentListener(unityEvent: UnityEventBase, index: int, call: UnityAction_1[bool], argument: bool) -> None: ...
    @staticmethod
    def RegisterFloatPersistentListener(unityEvent: UnityEventBase, index: int, call: UnityAction_1[float], argument: float) -> None: ...
    @staticmethod
    def RegisterIntPersistentListener(unityEvent: UnityEventBase, index: int, call: UnityAction_1[int], argument: int) -> None: ...
    @staticmethod
    def RegisterStringPersistentListener(unityEvent: UnityEventBase, index: int, call: UnityAction_1[str], argument: str) -> None: ...
    @staticmethod
    def RegisterVoidPersistentListener(unityEvent: UnityEventBase, index: int, call: UnityAction) -> None: ...
    @staticmethod
    def UnregisterPersistentListener(unityEvent: UnityEventBase, index: int) -> None: ...
    # Skipped AddObjectPersistentListener due to it being static, abstract and generic.

    AddObjectPersistentListener : AddObjectPersistentListener_MethodGroup
    class AddObjectPersistentListener_MethodGroup:
        def __getitem__(self, t:typing.Type[AddObjectPersistentListener_1_T1]) -> AddObjectPersistentListener_1[AddObjectPersistentListener_1_T1]: ...

        AddObjectPersistentListener_1_T1 = typing.TypeVar('AddObjectPersistentListener_1_T1')
        class AddObjectPersistentListener_1(typing.Generic[AddObjectPersistentListener_1_T1]):
            AddObjectPersistentListener_1_T = UnityEventTools.AddObjectPersistentListener_MethodGroup.AddObjectPersistentListener_1_T1
            def __call__(self, unityEvent: UnityEventBase, call: UnityAction_1[AddObjectPersistentListener_1_T], argument: AddObjectPersistentListener_1_T) -> None:...


    # Skipped AddPersistentListener due to it being static, abstract and generic.

    AddPersistentListener : AddPersistentListener_MethodGroup
    class AddPersistentListener_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[AddPersistentListener_1_T1]) -> AddPersistentListener_1[AddPersistentListener_1_T1]: ...

        AddPersistentListener_1_T1 = typing.TypeVar('AddPersistentListener_1_T1')
        class AddPersistentListener_1(typing.Generic[AddPersistentListener_1_T1]):
            AddPersistentListener_1_T0 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_1_T1
            def __call__(self, unityEvent: UnityEvent_1[AddPersistentListener_1_T0], call: UnityAction_1[AddPersistentListener_1_T0]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AddPersistentListener_2_T1], typing.Type[AddPersistentListener_2_T2]]) -> AddPersistentListener_2[AddPersistentListener_2_T1, AddPersistentListener_2_T2]: ...

        AddPersistentListener_2_T1 = typing.TypeVar('AddPersistentListener_2_T1')
        AddPersistentListener_2_T2 = typing.TypeVar('AddPersistentListener_2_T2')
        class AddPersistentListener_2(typing.Generic[AddPersistentListener_2_T1, AddPersistentListener_2_T2]):
            AddPersistentListener_2_T0 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_2_T1
            AddPersistentListener_2_T1 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_2_T2
            def __call__(self, unityEvent: UnityEvent_2[AddPersistentListener_2_T0, AddPersistentListener_2_T1], call: UnityAction_2[AddPersistentListener_2_T0, AddPersistentListener_2_T1]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AddPersistentListener_3_T1], typing.Type[AddPersistentListener_3_T2], typing.Type[AddPersistentListener_3_T3]]) -> AddPersistentListener_3[AddPersistentListener_3_T1, AddPersistentListener_3_T2, AddPersistentListener_3_T3]: ...

        AddPersistentListener_3_T1 = typing.TypeVar('AddPersistentListener_3_T1')
        AddPersistentListener_3_T2 = typing.TypeVar('AddPersistentListener_3_T2')
        AddPersistentListener_3_T3 = typing.TypeVar('AddPersistentListener_3_T3')
        class AddPersistentListener_3(typing.Generic[AddPersistentListener_3_T1, AddPersistentListener_3_T2, AddPersistentListener_3_T3]):
            AddPersistentListener_3_T0 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_3_T1
            AddPersistentListener_3_T1 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_3_T2
            AddPersistentListener_3_T2 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_3_T3
            def __call__(self, unityEvent: UnityEvent_3[AddPersistentListener_3_T0, AddPersistentListener_3_T1, AddPersistentListener_3_T2], call: UnityAction_3[AddPersistentListener_3_T0, AddPersistentListener_3_T1, AddPersistentListener_3_T2]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[AddPersistentListener_4_T1], typing.Type[AddPersistentListener_4_T2], typing.Type[AddPersistentListener_4_T3], typing.Type[AddPersistentListener_4_T4]]) -> AddPersistentListener_4[AddPersistentListener_4_T1, AddPersistentListener_4_T2, AddPersistentListener_4_T3, AddPersistentListener_4_T4]: ...

        AddPersistentListener_4_T1 = typing.TypeVar('AddPersistentListener_4_T1')
        AddPersistentListener_4_T2 = typing.TypeVar('AddPersistentListener_4_T2')
        AddPersistentListener_4_T3 = typing.TypeVar('AddPersistentListener_4_T3')
        AddPersistentListener_4_T4 = typing.TypeVar('AddPersistentListener_4_T4')
        class AddPersistentListener_4(typing.Generic[AddPersistentListener_4_T1, AddPersistentListener_4_T2, AddPersistentListener_4_T3, AddPersistentListener_4_T4]):
            AddPersistentListener_4_T0 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_4_T1
            AddPersistentListener_4_T1 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_4_T2
            AddPersistentListener_4_T2 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_4_T3
            AddPersistentListener_4_T3 = UnityEventTools.AddPersistentListener_MethodGroup.AddPersistentListener_4_T4
            def __call__(self, unityEvent: UnityEvent_4[AddPersistentListener_4_T0, AddPersistentListener_4_T1, AddPersistentListener_4_T2, AddPersistentListener_4_T3], call: UnityAction_4[AddPersistentListener_4_T0, AddPersistentListener_4_T1, AddPersistentListener_4_T2, AddPersistentListener_4_T3]) -> None:...

        @typing.overload
        def __call__(self, unityEvent: UnityEventBase) -> None:...
        @typing.overload
        def __call__(self, unityEvent: UnityEvent, call: UnityAction) -> None:...

    # Skipped RegisterObjectPersistentListener due to it being static, abstract and generic.

    RegisterObjectPersistentListener : RegisterObjectPersistentListener_MethodGroup
    class RegisterObjectPersistentListener_MethodGroup:
        def __getitem__(self, t:typing.Type[RegisterObjectPersistentListener_1_T1]) -> RegisterObjectPersistentListener_1[RegisterObjectPersistentListener_1_T1]: ...

        RegisterObjectPersistentListener_1_T1 = typing.TypeVar('RegisterObjectPersistentListener_1_T1')
        class RegisterObjectPersistentListener_1(typing.Generic[RegisterObjectPersistentListener_1_T1]):
            RegisterObjectPersistentListener_1_T = UnityEventTools.RegisterObjectPersistentListener_MethodGroup.RegisterObjectPersistentListener_1_T1
            def __call__(self, unityEvent: UnityEventBase, index: int, call: UnityAction_1[RegisterObjectPersistentListener_1_T], argument: RegisterObjectPersistentListener_1_T) -> None:...


    # Skipped RegisterPersistentListener due to it being static, abstract and generic.

    RegisterPersistentListener : RegisterPersistentListener_MethodGroup
    class RegisterPersistentListener_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[RegisterPersistentListener_1_T1]) -> RegisterPersistentListener_1[RegisterPersistentListener_1_T1]: ...

        RegisterPersistentListener_1_T1 = typing.TypeVar('RegisterPersistentListener_1_T1')
        class RegisterPersistentListener_1(typing.Generic[RegisterPersistentListener_1_T1]):
            RegisterPersistentListener_1_T0 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_1_T1
            def __call__(self, unityEvent: UnityEvent_1[RegisterPersistentListener_1_T0], index: int, call: UnityAction_1[RegisterPersistentListener_1_T0]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterPersistentListener_2_T1], typing.Type[RegisterPersistentListener_2_T2]]) -> RegisterPersistentListener_2[RegisterPersistentListener_2_T1, RegisterPersistentListener_2_T2]: ...

        RegisterPersistentListener_2_T1 = typing.TypeVar('RegisterPersistentListener_2_T1')
        RegisterPersistentListener_2_T2 = typing.TypeVar('RegisterPersistentListener_2_T2')
        class RegisterPersistentListener_2(typing.Generic[RegisterPersistentListener_2_T1, RegisterPersistentListener_2_T2]):
            RegisterPersistentListener_2_T0 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_2_T1
            RegisterPersistentListener_2_T1 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_2_T2
            def __call__(self, unityEvent: UnityEvent_2[RegisterPersistentListener_2_T0, RegisterPersistentListener_2_T1], index: int, call: UnityAction_2[RegisterPersistentListener_2_T0, RegisterPersistentListener_2_T1]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterPersistentListener_3_T1], typing.Type[RegisterPersistentListener_3_T2], typing.Type[RegisterPersistentListener_3_T3]]) -> RegisterPersistentListener_3[RegisterPersistentListener_3_T1, RegisterPersistentListener_3_T2, RegisterPersistentListener_3_T3]: ...

        RegisterPersistentListener_3_T1 = typing.TypeVar('RegisterPersistentListener_3_T1')
        RegisterPersistentListener_3_T2 = typing.TypeVar('RegisterPersistentListener_3_T2')
        RegisterPersistentListener_3_T3 = typing.TypeVar('RegisterPersistentListener_3_T3')
        class RegisterPersistentListener_3(typing.Generic[RegisterPersistentListener_3_T1, RegisterPersistentListener_3_T2, RegisterPersistentListener_3_T3]):
            RegisterPersistentListener_3_T0 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_3_T1
            RegisterPersistentListener_3_T1 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_3_T2
            RegisterPersistentListener_3_T2 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_3_T3
            def __call__(self, unityEvent: UnityEvent_3[RegisterPersistentListener_3_T0, RegisterPersistentListener_3_T1, RegisterPersistentListener_3_T2], index: int, call: UnityAction_3[RegisterPersistentListener_3_T0, RegisterPersistentListener_3_T1, RegisterPersistentListener_3_T2]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RegisterPersistentListener_4_T1], typing.Type[RegisterPersistentListener_4_T2], typing.Type[RegisterPersistentListener_4_T3], typing.Type[RegisterPersistentListener_4_T4]]) -> RegisterPersistentListener_4[RegisterPersistentListener_4_T1, RegisterPersistentListener_4_T2, RegisterPersistentListener_4_T3, RegisterPersistentListener_4_T4]: ...

        RegisterPersistentListener_4_T1 = typing.TypeVar('RegisterPersistentListener_4_T1')
        RegisterPersistentListener_4_T2 = typing.TypeVar('RegisterPersistentListener_4_T2')
        RegisterPersistentListener_4_T3 = typing.TypeVar('RegisterPersistentListener_4_T3')
        RegisterPersistentListener_4_T4 = typing.TypeVar('RegisterPersistentListener_4_T4')
        class RegisterPersistentListener_4(typing.Generic[RegisterPersistentListener_4_T1, RegisterPersistentListener_4_T2, RegisterPersistentListener_4_T3, RegisterPersistentListener_4_T4]):
            RegisterPersistentListener_4_T0 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_4_T1
            RegisterPersistentListener_4_T1 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_4_T2
            RegisterPersistentListener_4_T2 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_4_T3
            RegisterPersistentListener_4_T3 = UnityEventTools.RegisterPersistentListener_MethodGroup.RegisterPersistentListener_4_T4
            def __call__(self, unityEvent: UnityEvent_4[RegisterPersistentListener_4_T0, RegisterPersistentListener_4_T1, RegisterPersistentListener_4_T2, RegisterPersistentListener_4_T3], index: int, call: UnityAction_4[RegisterPersistentListener_4_T0, RegisterPersistentListener_4_T1, RegisterPersistentListener_4_T2, RegisterPersistentListener_4_T3]) -> None:...

        def __call__(self, unityEvent: UnityEvent, index: int, call: UnityAction) -> None:...

    # Skipped RemovePersistentListener due to it being static, abstract and generic.

    RemovePersistentListener : RemovePersistentListener_MethodGroup
    class RemovePersistentListener_MethodGroup:
        @typing.overload
        def __getitem__(self, t:typing.Type[RemovePersistentListener_1_T1]) -> RemovePersistentListener_1[RemovePersistentListener_1_T1]: ...

        RemovePersistentListener_1_T1 = typing.TypeVar('RemovePersistentListener_1_T1')
        class RemovePersistentListener_1(typing.Generic[RemovePersistentListener_1_T1]):
            RemovePersistentListener_1_T0 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_1_T1
            def __call__(self, unityEvent: UnityEventBase, call: UnityAction_1[RemovePersistentListener_1_T0]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RemovePersistentListener_2_T1], typing.Type[RemovePersistentListener_2_T2]]) -> RemovePersistentListener_2[RemovePersistentListener_2_T1, RemovePersistentListener_2_T2]: ...

        RemovePersistentListener_2_T1 = typing.TypeVar('RemovePersistentListener_2_T1')
        RemovePersistentListener_2_T2 = typing.TypeVar('RemovePersistentListener_2_T2')
        class RemovePersistentListener_2(typing.Generic[RemovePersistentListener_2_T1, RemovePersistentListener_2_T2]):
            RemovePersistentListener_2_T0 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_2_T1
            RemovePersistentListener_2_T1 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_2_T2
            def __call__(self, unityEvent: UnityEventBase, call: UnityAction_2[RemovePersistentListener_2_T0, RemovePersistentListener_2_T1]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RemovePersistentListener_3_T1], typing.Type[RemovePersistentListener_3_T2], typing.Type[RemovePersistentListener_3_T3]]) -> RemovePersistentListener_3[RemovePersistentListener_3_T1, RemovePersistentListener_3_T2, RemovePersistentListener_3_T3]: ...

        RemovePersistentListener_3_T1 = typing.TypeVar('RemovePersistentListener_3_T1')
        RemovePersistentListener_3_T2 = typing.TypeVar('RemovePersistentListener_3_T2')
        RemovePersistentListener_3_T3 = typing.TypeVar('RemovePersistentListener_3_T3')
        class RemovePersistentListener_3(typing.Generic[RemovePersistentListener_3_T1, RemovePersistentListener_3_T2, RemovePersistentListener_3_T3]):
            RemovePersistentListener_3_T0 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_3_T1
            RemovePersistentListener_3_T1 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_3_T2
            RemovePersistentListener_3_T2 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_3_T3
            def __call__(self, unityEvent: UnityEventBase, call: UnityAction_3[RemovePersistentListener_3_T0, RemovePersistentListener_3_T1, RemovePersistentListener_3_T2]) -> None:...

        @typing.overload
        def __getitem__(self, t:typing.Tuple[typing.Type[RemovePersistentListener_4_T1], typing.Type[RemovePersistentListener_4_T2], typing.Type[RemovePersistentListener_4_T3], typing.Type[RemovePersistentListener_4_T4]]) -> RemovePersistentListener_4[RemovePersistentListener_4_T1, RemovePersistentListener_4_T2, RemovePersistentListener_4_T3, RemovePersistentListener_4_T4]: ...

        RemovePersistentListener_4_T1 = typing.TypeVar('RemovePersistentListener_4_T1')
        RemovePersistentListener_4_T2 = typing.TypeVar('RemovePersistentListener_4_T2')
        RemovePersistentListener_4_T3 = typing.TypeVar('RemovePersistentListener_4_T3')
        RemovePersistentListener_4_T4 = typing.TypeVar('RemovePersistentListener_4_T4')
        class RemovePersistentListener_4(typing.Generic[RemovePersistentListener_4_T1, RemovePersistentListener_4_T2, RemovePersistentListener_4_T3, RemovePersistentListener_4_T4]):
            RemovePersistentListener_4_T0 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_4_T1
            RemovePersistentListener_4_T1 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_4_T2
            RemovePersistentListener_4_T2 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_4_T3
            RemovePersistentListener_4_T3 = UnityEventTools.RemovePersistentListener_MethodGroup.RemovePersistentListener_4_T4
            def __call__(self, unityEvent: UnityEventBase, call: UnityAction_4[RemovePersistentListener_4_T0, RemovePersistentListener_4_T1, RemovePersistentListener_4_T2, RemovePersistentListener_4_T3]) -> None:...

        @typing.overload
        def __call__(self, unityEvent: UnityEventBase, index: int) -> None:...
        @typing.overload
        def __call__(self, unityEvent: UnityEventBase, call: UnityAction) -> None:...


