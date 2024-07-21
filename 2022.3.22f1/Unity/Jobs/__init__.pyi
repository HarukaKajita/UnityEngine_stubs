import typing, clr, abc
from System import IEquatable_1
from Unity.Collections import NativeArray_1, NativeSlice_1

class IJob(typing.Protocol):
    @abc.abstractmethod
    def Execute(self) -> None: ...


class IJobExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...


    # Skipped Run due to it being static, abstract and generic.

    Run : Run_MethodGroup
    class Run_MethodGroup:
        def __getitem__(self, t:typing.Type[Run_1_T1]) -> Run_1[Run_1_T1]: ...

        Run_1_T1 = typing.TypeVar('Run_1_T1')
        class Run_1(typing.Generic[Run_1_T1]):
            Run_1_T = IJobExtensions.Run_MethodGroup.Run_1_T1
            def __call__(self, jobData: Run_1_T) -> None:...


    # Skipped RunByRef due to it being static, abstract and generic.

    RunByRef : RunByRef_MethodGroup
    class RunByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[RunByRef_1_T1]) -> RunByRef_1[RunByRef_1_T1]: ...

        RunByRef_1_T1 = typing.TypeVar('RunByRef_1_T1')
        class RunByRef_1(typing.Generic[RunByRef_1_T1]):
            RunByRef_1_T = IJobExtensions.RunByRef_MethodGroup.RunByRef_1_T1
            def __call__(self, jobData: clr.Reference[RunByRef_1_T]) -> None:...


    # Skipped Schedule due to it being static, abstract and generic.

    Schedule : Schedule_MethodGroup
    class Schedule_MethodGroup:
        def __getitem__(self, t:typing.Type[Schedule_1_T1]) -> Schedule_1[Schedule_1_T1]: ...

        Schedule_1_T1 = typing.TypeVar('Schedule_1_T1')
        class Schedule_1(typing.Generic[Schedule_1_T1]):
            Schedule_1_T = IJobExtensions.Schedule_MethodGroup.Schedule_1_T1
            def __call__(self, jobData: Schedule_1_T, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleByRef due to it being static, abstract and generic.

    ScheduleByRef : ScheduleByRef_MethodGroup
    class ScheduleByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleByRef_1_T1]) -> ScheduleByRef_1[ScheduleByRef_1_T1]: ...

        ScheduleByRef_1_T1 = typing.TypeVar('ScheduleByRef_1_T1')
        class ScheduleByRef_1(typing.Generic[ScheduleByRef_1_T1]):
            ScheduleByRef_1_T = IJobExtensions.ScheduleByRef_MethodGroup.ScheduleByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleByRef_1_T], dependsOn: JobHandle = ...) -> JobHandle:...




class IJobFor(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, index: int) -> None: ...


class IJobForExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobForExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...


    # Skipped Run due to it being static, abstract and generic.

    Run : Run_MethodGroup
    class Run_MethodGroup:
        def __getitem__(self, t:typing.Type[Run_1_T1]) -> Run_1[Run_1_T1]: ...

        Run_1_T1 = typing.TypeVar('Run_1_T1')
        class Run_1(typing.Generic[Run_1_T1]):
            Run_1_T = IJobForExtensions.Run_MethodGroup.Run_1_T1
            def __call__(self, jobData: Run_1_T, arrayLength: int) -> None:...


    # Skipped RunByRef due to it being static, abstract and generic.

    RunByRef : RunByRef_MethodGroup
    class RunByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[RunByRef_1_T1]) -> RunByRef_1[RunByRef_1_T1]: ...

        RunByRef_1_T1 = typing.TypeVar('RunByRef_1_T1')
        class RunByRef_1(typing.Generic[RunByRef_1_T1]):
            RunByRef_1_T = IJobForExtensions.RunByRef_MethodGroup.RunByRef_1_T1
            def __call__(self, jobData: clr.Reference[RunByRef_1_T], arrayLength: int) -> None:...


    # Skipped Schedule due to it being static, abstract and generic.

    Schedule : Schedule_MethodGroup
    class Schedule_MethodGroup:
        def __getitem__(self, t:typing.Type[Schedule_1_T1]) -> Schedule_1[Schedule_1_T1]: ...

        Schedule_1_T1 = typing.TypeVar('Schedule_1_T1')
        class Schedule_1(typing.Generic[Schedule_1_T1]):
            Schedule_1_T = IJobForExtensions.Schedule_MethodGroup.Schedule_1_T1
            def __call__(self, jobData: Schedule_1_T, arrayLength: int, dependency: JobHandle) -> JobHandle:...


    # Skipped ScheduleByRef due to it being static, abstract and generic.

    ScheduleByRef : ScheduleByRef_MethodGroup
    class ScheduleByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleByRef_1_T1]) -> ScheduleByRef_1[ScheduleByRef_1_T1]: ...

        ScheduleByRef_1_T1 = typing.TypeVar('ScheduleByRef_1_T1')
        class ScheduleByRef_1(typing.Generic[ScheduleByRef_1_T1]):
            ScheduleByRef_1_T = IJobForExtensions.ScheduleByRef_MethodGroup.ScheduleByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleByRef_1_T], arrayLength: int, dependency: JobHandle) -> JobHandle:...


    # Skipped ScheduleParallel due to it being static, abstract and generic.

    ScheduleParallel : ScheduleParallel_MethodGroup
    class ScheduleParallel_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleParallel_1_T1]) -> ScheduleParallel_1[ScheduleParallel_1_T1]: ...

        ScheduleParallel_1_T1 = typing.TypeVar('ScheduleParallel_1_T1')
        class ScheduleParallel_1(typing.Generic[ScheduleParallel_1_T1]):
            ScheduleParallel_1_T = IJobForExtensions.ScheduleParallel_MethodGroup.ScheduleParallel_1_T1
            def __call__(self, jobData: ScheduleParallel_1_T, arrayLength: int, innerloopBatchCount: int, dependency: JobHandle) -> JobHandle:...


    # Skipped ScheduleParallelByRef due to it being static, abstract and generic.

    ScheduleParallelByRef : ScheduleParallelByRef_MethodGroup
    class ScheduleParallelByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleParallelByRef_1_T1]) -> ScheduleParallelByRef_1[ScheduleParallelByRef_1_T1]: ...

        ScheduleParallelByRef_1_T1 = typing.TypeVar('ScheduleParallelByRef_1_T1')
        class ScheduleParallelByRef_1(typing.Generic[ScheduleParallelByRef_1_T1]):
            ScheduleParallelByRef_1_T = IJobForExtensions.ScheduleParallelByRef_MethodGroup.ScheduleParallelByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleParallelByRef_1_T], arrayLength: int, innerloopBatchCount: int, dependency: JobHandle) -> JobHandle:...




class IJobParallelFor(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, index: int) -> None: ...


class IJobParallelForExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobParallelForExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...


    # Skipped Run due to it being static, abstract and generic.

    Run : Run_MethodGroup
    class Run_MethodGroup:
        def __getitem__(self, t:typing.Type[Run_1_T1]) -> Run_1[Run_1_T1]: ...

        Run_1_T1 = typing.TypeVar('Run_1_T1')
        class Run_1(typing.Generic[Run_1_T1]):
            Run_1_T = IJobParallelForExtensions.Run_MethodGroup.Run_1_T1
            def __call__(self, jobData: Run_1_T, arrayLength: int) -> None:...


    # Skipped RunByRef due to it being static, abstract and generic.

    RunByRef : RunByRef_MethodGroup
    class RunByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[RunByRef_1_T1]) -> RunByRef_1[RunByRef_1_T1]: ...

        RunByRef_1_T1 = typing.TypeVar('RunByRef_1_T1')
        class RunByRef_1(typing.Generic[RunByRef_1_T1]):
            RunByRef_1_T = IJobParallelForExtensions.RunByRef_MethodGroup.RunByRef_1_T1
            def __call__(self, jobData: clr.Reference[RunByRef_1_T], arrayLength: int) -> None:...


    # Skipped Schedule due to it being static, abstract and generic.

    Schedule : Schedule_MethodGroup
    class Schedule_MethodGroup:
        def __getitem__(self, t:typing.Type[Schedule_1_T1]) -> Schedule_1[Schedule_1_T1]: ...

        Schedule_1_T1 = typing.TypeVar('Schedule_1_T1')
        class Schedule_1(typing.Generic[Schedule_1_T1]):
            Schedule_1_T = IJobParallelForExtensions.Schedule_MethodGroup.Schedule_1_T1
            def __call__(self, jobData: Schedule_1_T, arrayLength: int, innerloopBatchCount: int, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleByRef due to it being static, abstract and generic.

    ScheduleByRef : ScheduleByRef_MethodGroup
    class ScheduleByRef_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleByRef_1_T1]) -> ScheduleByRef_1[ScheduleByRef_1_T1]: ...

        ScheduleByRef_1_T1 = typing.TypeVar('ScheduleByRef_1_T1')
        class ScheduleByRef_1(typing.Generic[ScheduleByRef_1_T1]):
            ScheduleByRef_1_T = IJobParallelForExtensions.ScheduleByRef_MethodGroup.ScheduleByRef_1_T1
            def __call__(self, jobData: clr.Reference[ScheduleByRef_1_T], arrayLength: int, innerloopBatchCount: int, dependsOn: JobHandle = ...) -> JobHandle:...




class JobHandle(IEquatable_1[JobHandle]):
    @property
    def IsCompleted(self) -> bool: ...
    @staticmethod
    def CheckFenceIsDependencyOrDidSyncFence(jobHandle: JobHandle, dependsOn: JobHandle) -> bool: ...
    def Complete(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, a: JobHandle, b: JobHandle) -> bool: ...
    def __ne__(self, a: JobHandle, b: JobHandle) -> bool: ...
    @staticmethod
    def ScheduleBatchedJobs() -> None: ...
    # Skipped CombineDependencies due to it being static, abstract and generic.

    CombineDependencies : CombineDependencies_MethodGroup
    class CombineDependencies_MethodGroup:
        @typing.overload
        def __call__(self, jobs: NativeArray_1[JobHandle]) -> JobHandle:...
        @typing.overload
        def __call__(self, jobs: NativeSlice_1[JobHandle]) -> JobHandle:...
        @typing.overload
        def __call__(self, job0: JobHandle, job1: JobHandle) -> JobHandle:...
        @typing.overload
        def __call__(self, job0: JobHandle, job1: JobHandle, job2: JobHandle) -> JobHandle:...

    # Skipped CompleteAll due to it being static, abstract and generic.

    CompleteAll : CompleteAll_MethodGroup
    class CompleteAll_MethodGroup:
        @typing.overload
        def __call__(self, jobs: NativeArray_1[JobHandle]) -> None:...
        @typing.overload
        def __call__(self, job0: clr.Reference[JobHandle], job1: clr.Reference[JobHandle]) -> None:...
        @typing.overload
        def __call__(self, job0: clr.Reference[JobHandle], job1: clr.Reference[JobHandle], job2: clr.Reference[JobHandle]) -> None:...

    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: JobHandle) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...


