import typing, clr, abc
from Unity.Collections import NativeArray_1
from Unity.Jobs import JobHandle
from System import Attribute

class BatchQueryJob_GenericClasses(abc.ABCMeta):
    Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_CommandT = typing.TypeVar('Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_CommandT')
    Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_ResultT = typing.TypeVar('Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_ResultT')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_CommandT], typing.Type[Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_ResultT]]) -> typing.Type[BatchQueryJob_2[Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_CommandT, Generic_BatchQueryJob_GenericClasses_BatchQueryJob_2_ResultT]]: ...

BatchQueryJob : BatchQueryJob_GenericClasses

BatchQueryJob_2_CommandT = typing.TypeVar('BatchQueryJob_2_CommandT')
BatchQueryJob_2_ResultT = typing.TypeVar('BatchQueryJob_2_ResultT')
class BatchQueryJob_2(typing.Generic[BatchQueryJob_2_CommandT, BatchQueryJob_2_ResultT]):
    def __init__(self, commands: NativeArray_1[BatchQueryJob_2_CommandT], results: NativeArray_1[BatchQueryJob_2_ResultT]) -> None: ...


class BatchQueryJobStruct_GenericClasses(abc.ABCMeta):
    Generic_BatchQueryJobStruct_GenericClasses_BatchQueryJobStruct_1_T = typing.TypeVar('Generic_BatchQueryJobStruct_GenericClasses_BatchQueryJobStruct_1_T')
    def __getitem__(self, types : typing.Type[Generic_BatchQueryJobStruct_GenericClasses_BatchQueryJobStruct_1_T]) -> typing.Type[BatchQueryJobStruct_1[Generic_BatchQueryJobStruct_GenericClasses_BatchQueryJobStruct_1_T]]: ...

BatchQueryJobStruct : BatchQueryJobStruct_GenericClasses

BatchQueryJobStruct_1_T = typing.TypeVar('BatchQueryJobStruct_1_T')
class BatchQueryJobStruct_1(typing.Generic[BatchQueryJobStruct_1_T]):
    @staticmethod
    def Initialize() -> int: ...


class JobHandleUnsafeUtility(abc.ABC):
    @staticmethod
    def CombineDependencies(jobs: clr.Reference[JobHandle], count: int) -> JobHandle: ...


class JobProducerTypeAttribute(Attribute):
    def __init__(self, producerType: typing.Type[typing.Any]) -> None: ...
    @property
    def ProducerType(self) -> typing.Type[typing.Any]: ...
    @property
    def TypeId(self) -> typing.Any: ...


class JobRanges:
    TotalIterationCount : int


class JobsUtility(abc.ABC):
    CacheLineSize : int
    MaxJobThreadCount : int
    @classmethod
    @property
    def IsExecutingJob(cls) -> bool: ...
    @classmethod
    @property
    def JobCompilerEnabled(cls) -> bool: ...
    @classmethod
    @JobCompilerEnabled.setter
    def JobCompilerEnabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def JobDebuggerEnabled(cls) -> bool: ...
    @classmethod
    @JobDebuggerEnabled.setter
    def JobDebuggerEnabled(cls, value: bool) -> bool: ...
    @classmethod
    @property
    def JobWorkerCount(cls) -> int: ...
    @classmethod
    @JobWorkerCount.setter
    def JobWorkerCount(cls, value: int) -> int: ...
    @classmethod
    @property
    def JobWorkerMaximumCount(cls) -> int: ...
    @classmethod
    @property
    def ThreadIndex(cls) -> int: ...
    @classmethod
    @property
    def ThreadIndexCount(cls) -> int: ...
    @staticmethod
    def GetJobRange(ranges: clr.Reference[JobRanges], jobIndex: int, beginIndex: clr.Reference[int], endIndex: clr.Reference[int]) -> None: ...
    @staticmethod
    def GetWorkStealingRange(ranges: clr.Reference[JobRanges], jobIndex: int, beginIndex: clr.Reference[int], endIndex: clr.Reference[int]) -> bool: ...
    @staticmethod
    def PatchBufferMinMaxRanges(bufferRangePatchData: int, jobdata: clr.Reference[None], startIndex: int, rangeSize: int) -> None: ...
    @staticmethod
    def ResetJobWorkerCount() -> None: ...
    @staticmethod
    def Schedule(parameters: clr.Reference[JobsUtility.JobScheduleParameters]) -> JobHandle: ...
    @staticmethod
    def ScheduleParallelFor(parameters: clr.Reference[JobsUtility.JobScheduleParameters], arrayLength: int, innerloopBatchCount: int) -> JobHandle: ...
    @staticmethod
    def ScheduleParallelForDeferArraySize(parameters: clr.Reference[JobsUtility.JobScheduleParameters], innerloopBatchCount: int, listData: clr.Reference[None], listDataAtomicSafetyHandle: clr.Reference[None]) -> JobHandle: ...
    @staticmethod
    def ScheduleParallelForTransform(parameters: clr.Reference[JobsUtility.JobScheduleParameters], transfromAccesssArray: int) -> JobHandle: ...
    @staticmethod
    def ScheduleParallelForTransformReadOnly(parameters: clr.Reference[JobsUtility.JobScheduleParameters], transfromAccesssArray: int, innerloopBatchCount: int) -> JobHandle: ...
    # Skipped CreateJobReflectionData due to it being static, abstract and generic.

    CreateJobReflectionData : CreateJobReflectionData_MethodGroup
    class CreateJobReflectionData_MethodGroup:
        @typing.overload
        def __call__(self, wrapperJobType: typing.Type[typing.Any], userJobType: typing.Type[typing.Any], managedJobFunction0: typing.Any) -> int:...
        @typing.overload
        def __call__(self, wrapperJobType: typing.Type[typing.Any], userJobType: typing.Type[typing.Any], jobType: JobType, managedJobFunction0: typing.Any) -> int:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], managedJobFunction0: typing.Any, managedJobFunction1: typing.Any = ..., managedJobFunction2: typing.Any = ...) -> int:...
        @typing.overload
        def __call__(self, type: typing.Type[typing.Any], jobType: JobType, managedJobFunction0: typing.Any, managedJobFunction1: typing.Any = ..., managedJobFunction2: typing.Any = ...) -> int:...


    class JobScheduleParameters:
        def __init__(self, i_jobData: clr.Reference[None], i_reflectionData: int, i_dependency: JobHandle, i_scheduleMode: ScheduleMode) -> None: ...
        Dependency : JobHandle
        JobDataPtr : int
        ReflectionData : int
        ScheduleMode : int



class JobType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Single : JobType # 0
    ParallelFor : JobType # 1


class ScheduleMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Run : ScheduleMode # 0
    Batched : ScheduleMode # 1
    Parallel : ScheduleMode # 1
    Single : ScheduleMode # 2

