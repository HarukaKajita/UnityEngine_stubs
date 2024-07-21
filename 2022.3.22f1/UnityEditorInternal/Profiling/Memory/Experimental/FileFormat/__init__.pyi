import typing

class EntryType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Metadata_Version : EntryType # 0
    Metadata_RecordDate : EntryType # 1
    Metadata_UserMetadata : EntryType # 2
    Metadata_CaptureFlags : EntryType # 3
    Metadata_VirtualMachineInformation : EntryType # 4
    NativeTypes_Name : EntryType # 5
    NativeTypes_NativeBaseTypeArrayIndex : EntryType # 6
    NativeObjects_NativeTypeArrayIndex : EntryType # 7
    NativeObjects_HideFlags : EntryType # 8
    NativeObjects_Flags : EntryType # 9
    NativeObjects_InstanceId : EntryType # 10
    NativeObjects_Name : EntryType # 11
    NativeObjects_NativeObjectAddress : EntryType # 12
    NativeObjects_Size : EntryType # 13
    NativeObjects_RootReferenceId : EntryType # 14
    GCHandles_Target : EntryType # 15
    Connections_From : EntryType # 16
    Connections_To : EntryType # 17
    ManagedHeapSections_StartAddress : EntryType # 18
    ManagedHeapSections_Bytes : EntryType # 19
    ManagedStacks_StartAddress : EntryType # 20
    ManagedStacks_Bytes : EntryType # 21
    TypeDescriptions_Flags : EntryType # 22
    TypeDescriptions_Name : EntryType # 23
    TypeDescriptions_Assembly : EntryType # 24
    TypeDescriptions_FieldIndices : EntryType # 25
    TypeDescriptions_StaticFieldBytes : EntryType # 26
    TypeDescriptions_BaseOrElementTypeIndex : EntryType # 27
    TypeDescriptions_Size : EntryType # 28
    TypeDescriptions_TypeInfoAddress : EntryType # 29
    TypeDescriptions_TypeIndex : EntryType # 30
    FieldDescriptions_Offset : EntryType # 31
    FieldDescriptions_TypeIndex : EntryType # 32
    FieldDescriptions_Name : EntryType # 33
    FieldDescriptions_IsStatic : EntryType # 34
    NativeRootReferences_Id : EntryType # 35
    NativeRootReferences_AreaName : EntryType # 36
    NativeRootReferences_ObjectName : EntryType # 37
    NativeRootReferences_AccumulatedSize : EntryType # 38
    NativeAllocations_MemoryRegionIndex : EntryType # 39
    NativeAllocations_RootReferenceId : EntryType # 40
    NativeAllocations_AllocationSiteId : EntryType # 41
    NativeAllocations_Address : EntryType # 42
    NativeAllocations_Size : EntryType # 43
    NativeAllocations_OverheadSize : EntryType # 44
    NativeAllocations_PaddingSize : EntryType # 45
    NativeMemoryRegions_Name : EntryType # 46
    NativeMemoryRegions_ParentIndex : EntryType # 47
    NativeMemoryRegions_AddressBase : EntryType # 48
    NativeMemoryRegions_AddressSize : EntryType # 49
    NativeMemoryRegions_FirstAllocationIndex : EntryType # 50
    NativeMemoryRegions_NumAllocations : EntryType # 51
    NativeMemoryLabels_Name : EntryType # 52
    NativeAllocationSites_Id : EntryType # 53
    NativeAllocationSites_MemoryLabelIndex : EntryType # 54
    NativeAllocationSites_CallstackSymbols : EntryType # 55
    NativeCallstackSymbol_Symbol : EntryType # 56
    NativeCallstackSymbol_ReadableStackTrace : EntryType # 57
    NativeObjects_GCHandleIndex : EntryType # 58

