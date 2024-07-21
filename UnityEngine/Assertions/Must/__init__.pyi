import typing, abc

class MustExtensions(abc.ABC):
    # Skipped MustBeApproximatelyEqual due to it being static, abstract and generic.

    MustBeApproximatelyEqual : MustBeApproximatelyEqual_MethodGroup
    class MustBeApproximatelyEqual_MethodGroup:
        @typing.overload
        def __call__(self, actual: float, expected: float) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, tolerance: float) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, message: str) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, tolerance: float, message: str) -> None:...

    # Skipped MustBeEqual due to it being static, abstract and generic.

    MustBeEqual : MustBeEqual_MethodGroup
    class MustBeEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[MustBeEqual_1_T1]) -> MustBeEqual_1[MustBeEqual_1_T1]: ...

        MustBeEqual_1_T1 = typing.TypeVar('MustBeEqual_1_T1')
        class MustBeEqual_1(typing.Generic[MustBeEqual_1_T1]):
            MustBeEqual_1_T = MustExtensions.MustBeEqual_MethodGroup.MustBeEqual_1_T1
            @typing.overload
            def __call__(self, actual: MustBeEqual_1_T, expected: MustBeEqual_1_T) -> None:...
            @typing.overload
            def __call__(self, actual: MustBeEqual_1_T, expected: MustBeEqual_1_T, message: str) -> None:...


    # Skipped MustBeFalse due to it being static, abstract and generic.

    MustBeFalse : MustBeFalse_MethodGroup
    class MustBeFalse_MethodGroup:
        @typing.overload
        def __call__(self, value: bool) -> None:...
        @typing.overload
        def __call__(self, value: bool, message: str) -> None:...

    # Skipped MustBeNull due to it being static, abstract and generic.

    MustBeNull : MustBeNull_MethodGroup
    class MustBeNull_MethodGroup:
        def __getitem__(self, t:typing.Type[MustBeNull_1_T1]) -> MustBeNull_1[MustBeNull_1_T1]: ...

        MustBeNull_1_T1 = typing.TypeVar('MustBeNull_1_T1')
        class MustBeNull_1(typing.Generic[MustBeNull_1_T1]):
            MustBeNull_1_T = MustExtensions.MustBeNull_MethodGroup.MustBeNull_1_T1
            @typing.overload
            def __call__(self, expected: MustBeNull_1_T) -> None:...
            @typing.overload
            def __call__(self, expected: MustBeNull_1_T, message: str) -> None:...


    # Skipped MustBeTrue due to it being static, abstract and generic.

    MustBeTrue : MustBeTrue_MethodGroup
    class MustBeTrue_MethodGroup:
        @typing.overload
        def __call__(self, value: bool) -> None:...
        @typing.overload
        def __call__(self, value: bool, message: str) -> None:...

    # Skipped MustNotBeApproximatelyEqual due to it being static, abstract and generic.

    MustNotBeApproximatelyEqual : MustNotBeApproximatelyEqual_MethodGroup
    class MustNotBeApproximatelyEqual_MethodGroup:
        @typing.overload
        def __call__(self, actual: float, expected: float) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, tolerance: float) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, message: str) -> None:...
        @typing.overload
        def __call__(self, actual: float, expected: float, tolerance: float, message: str) -> None:...

    # Skipped MustNotBeEqual due to it being static, abstract and generic.

    MustNotBeEqual : MustNotBeEqual_MethodGroup
    class MustNotBeEqual_MethodGroup:
        def __getitem__(self, t:typing.Type[MustNotBeEqual_1_T1]) -> MustNotBeEqual_1[MustNotBeEqual_1_T1]: ...

        MustNotBeEqual_1_T1 = typing.TypeVar('MustNotBeEqual_1_T1')
        class MustNotBeEqual_1(typing.Generic[MustNotBeEqual_1_T1]):
            MustNotBeEqual_1_T = MustExtensions.MustNotBeEqual_MethodGroup.MustNotBeEqual_1_T1
            @typing.overload
            def __call__(self, actual: MustNotBeEqual_1_T, expected: MustNotBeEqual_1_T) -> None:...
            @typing.overload
            def __call__(self, actual: MustNotBeEqual_1_T, expected: MustNotBeEqual_1_T, message: str) -> None:...


    # Skipped MustNotBeNull due to it being static, abstract and generic.

    MustNotBeNull : MustNotBeNull_MethodGroup
    class MustNotBeNull_MethodGroup:
        def __getitem__(self, t:typing.Type[MustNotBeNull_1_T1]) -> MustNotBeNull_1[MustNotBeNull_1_T1]: ...

        MustNotBeNull_1_T1 = typing.TypeVar('MustNotBeNull_1_T1')
        class MustNotBeNull_1(typing.Generic[MustNotBeNull_1_T1]):
            MustNotBeNull_1_T = MustExtensions.MustNotBeNull_MethodGroup.MustNotBeNull_1_T1
            @typing.overload
            def __call__(self, expected: MustNotBeNull_1_T) -> None:...
            @typing.overload
            def __call__(self, expected: MustNotBeNull_1_T, message: str) -> None:...



