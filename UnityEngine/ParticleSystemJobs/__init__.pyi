import typing, abc
from Unity.Jobs import JobHandle
from UnityEngine import ParticleSystem, Color32, Vector3, Vector4
from Unity.Collections import NativeArray_1

class IJobParticleSystem(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, jobData: ParticleSystemJobData) -> None: ...


class IJobParticleSystemExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobParticleSystemExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...




class IJobParticleSystemParallelFor(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, jobData: ParticleSystemJobData, index: int) -> None: ...


class IJobParticleSystemParallelForBatch(typing.Protocol):
    @abc.abstractmethod
    def Execute(self, jobData: ParticleSystemJobData, startIndex: int, count: int) -> None: ...


class IJobParticleSystemParallelForBatchExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobParticleSystemParallelForBatchExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...




class IJobParticleSystemParallelForExtensions(abc.ABC):
    # Skipped EarlyJobInit due to it being static, abstract and generic.

    EarlyJobInit : EarlyJobInit_MethodGroup
    class EarlyJobInit_MethodGroup:
        def __getitem__(self, t:typing.Type[EarlyJobInit_1_T1]) -> EarlyJobInit_1[EarlyJobInit_1_T1]: ...

        EarlyJobInit_1_T1 = typing.TypeVar('EarlyJobInit_1_T1')
        class EarlyJobInit_1(typing.Generic[EarlyJobInit_1_T1]):
            EarlyJobInit_1_T = IJobParticleSystemParallelForExtensions.EarlyJobInit_MethodGroup.EarlyJobInit_1_T1
            def __call__(self) -> None:...




class IParticleSystemJobExtensions(abc.ABC):
    # Skipped Schedule due to it being static, abstract and generic.

    Schedule : Schedule_MethodGroup
    class Schedule_MethodGroup:
        def __getitem__(self, t:typing.Type[Schedule_1_T1]) -> Schedule_1[Schedule_1_T1]: ...

        Schedule_1_T1 = typing.TypeVar('Schedule_1_T1')
        class Schedule_1(typing.Generic[Schedule_1_T1]):
            Schedule_1_T = IParticleSystemJobExtensions.Schedule_MethodGroup.Schedule_1_T1
            @typing.overload
            def __call__(self, jobData: Schedule_1_T, ps: ParticleSystem, dependsOn: JobHandle = ...) -> JobHandle:...
            @typing.overload
            def __call__(self, jobData: Schedule_1_T, ps: ParticleSystem, minIndicesPerJobCount: int, dependsOn: JobHandle = ...) -> JobHandle:...


    # Skipped ScheduleBatch due to it being static, abstract and generic.

    ScheduleBatch : ScheduleBatch_MethodGroup
    class ScheduleBatch_MethodGroup:
        def __getitem__(self, t:typing.Type[ScheduleBatch_1_T1]) -> ScheduleBatch_1[ScheduleBatch_1_T1]: ...

        ScheduleBatch_1_T1 = typing.TypeVar('ScheduleBatch_1_T1')
        class ScheduleBatch_1(typing.Generic[ScheduleBatch_1_T1]):
            ScheduleBatch_1_T = IParticleSystemJobExtensions.ScheduleBatch_MethodGroup.ScheduleBatch_1_T1
            def __call__(self, jobData: ScheduleBatch_1_T, ps: ParticleSystem, innerLoopBatchCount: int, dependsOn: JobHandle = ...) -> JobHandle:...




class ParticleSystemJobData:
    @property
    def aliveTimePercent(self) -> NativeArray_1[float]: ...
    @property
    def axisOfRotations(self) -> ParticleSystemNativeArray3: ...
    @property
    def count(self) -> int: ...
    @property
    def customData1(self) -> ParticleSystemNativeArray4: ...
    @property
    def customData2(self) -> ParticleSystemNativeArray4: ...
    @property
    def inverseStartLifetimes(self) -> NativeArray_1[float]: ...
    @property
    def meshIndices(self) -> NativeArray_1[int]: ...
    @property
    def positions(self) -> ParticleSystemNativeArray3: ...
    @property
    def randomSeeds(self) -> NativeArray_1[int]: ...
    @property
    def rotationalSpeeds(self) -> ParticleSystemNativeArray3: ...
    @property
    def rotations(self) -> ParticleSystemNativeArray3: ...
    @property
    def sizes(self) -> ParticleSystemNativeArray3: ...
    @property
    def startColors(self) -> NativeArray_1[Color32]: ...
    @property
    def velocities(self) -> ParticleSystemNativeArray3: ...


class ParticleSystemNativeArray3:
    x : NativeArray_1[float]
    y : NativeArray_1[float]
    z : NativeArray_1[float]
    @property
    def Item(self) -> Vector3: ...
    @Item.setter
    def Item(self, value: Vector3) -> Vector3: ...


class ParticleSystemNativeArray4:
    w : NativeArray_1[float]
    x : NativeArray_1[float]
    y : NativeArray_1[float]
    z : NativeArray_1[float]
    @property
    def Item(self) -> Vector4: ...
    @Item.setter
    def Item(self, value: Vector4) -> Vector4: ...

