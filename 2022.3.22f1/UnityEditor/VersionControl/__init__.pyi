import typing, clr, abc
from System import Array_1, MulticastDelegate, IAsyncResult, AsyncCallback, Attribute
from UnityEngine import Object, Rect, ScriptableObject, HideFlags
from System.Collections.Generic import List_1
from UnityEditor import Editor
from System.Reflection import MethodInfo

class Asset:
    def __init__(self, clientPath: str) -> None: ...
    @property
    def assetPath(self) -> str: ...
    @property
    def fullName(self) -> str: ...
    @property
    def isFolder(self) -> bool: ...
    @property
    def isInCurrentProject(self) -> bool: ...
    @property
    def isMeta(self) -> bool: ...
    @property
    def locked(self) -> bool: ...
    @property
    def metaPath(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def prettyPath(self) -> str: ...
    @property
    def readOnly(self) -> bool: ...
    @property
    def state(self) -> Asset.States: ...
    def Dispose(self) -> None: ...
    def Edit(self) -> None: ...
    def IsChildOf(self, other: Asset) -> bool: ...
    def IsOneOfStates(self, states: Array_1[Asset.States]) -> bool: ...
    def IsState(self, state: Asset.States) -> bool: ...
    def Load(self) -> Object: ...

    class States(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        None_ : Asset.States # 0
        Local : Asset.States # 1
        Synced : Asset.States # 2
        OutOfSync : Asset.States # 4
        Missing : Asset.States # 8
        CheckedOutLocal : Asset.States # 16
        CheckedOutRemote : Asset.States # 32
        DeletedLocal : Asset.States # 64
        DeletedRemote : Asset.States # 128
        AddedLocal : Asset.States # 256
        AddedRemote : Asset.States # 512
        Conflicted : Asset.States # 1024
        LockedLocal : Asset.States # 2048
        LockedRemote : Asset.States # 4096
        Updating : Asset.States # 8192
        ReadOnly : Asset.States # 16384
        MetaFile : Asset.States # 32768
        MovedLocal : Asset.States # 65536
        MovedRemote : Asset.States # 131072
        Unversioned : Asset.States # 262144
        Exclusive : Asset.States # 524288



class AssetList(List_1[Asset]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, src: AssetList) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @Capacity.setter
    def Capacity(self, value: int) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> Asset: ...
    @Item.setter
    def Item(self, value: Asset) -> Asset: ...
    def Filter(self, includeFolder: bool, states: Array_1[Asset.States]) -> AssetList: ...
    def FilterChildren(self) -> AssetList: ...
    def FilterCount(self, includeFolder: bool, states: Array_1[Asset.States]) -> int: ...


class ChangeSet:
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, description: str) -> None: ...
    @typing.overload
    def __init__(self, description: str, revision: str) -> None: ...
    @typing.overload
    def __init__(self, other: ChangeSet) -> None: ...
    defaultID : str
    @property
    def description(self) -> str: ...
    @property
    def id(self) -> str: ...
    def Dispose(self) -> None: ...


class ChangeSets(List_1[ChangeSet]):
    def __init__(self) -> None: ...
    @property
    def Capacity(self) -> int: ...
    @Capacity.setter
    def Capacity(self, value: int) -> int: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> ChangeSet: ...
    @Item.setter
    def Item(self, value: ChangeSet) -> ChangeSet: ...


class CheckoutMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Asset : CheckoutMode # 1
    Meta : CheckoutMode # 2
    Both : CheckoutMode # 3
    Exact : CheckoutMode # 4


class CompletionAction(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    UpdatePendingWindow : CompletionAction # 1
    OnChangeContentsPendingWindow : CompletionAction # 2
    OnIncomingPendingWindow : CompletionAction # 3
    OnChangeSetsPendingWindow : CompletionAction # 4
    OnGotLatestPendingWindow : CompletionAction # 5
    OnSubmittedChangeWindow : CompletionAction # 6
    OnAddedChangeWindow : CompletionAction # 7
    OnCheckoutCompleted : CompletionAction # 8


class ConfigField:
    @property
    def description(self) -> str: ...
    @property
    def isPassword(self) -> bool: ...
    @property
    def isRequired(self) -> bool: ...
    @property
    def label(self) -> str: ...
    @property
    def name(self) -> str: ...
    def Dispose(self) -> None: ...


class FileMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    None_ : FileMode # 0
    Binary : FileMode # 1
    Text : FileMode # 2


class IconOverlayType(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Project : IconOverlayType # 0
    Hierarchy : IconOverlayType # 1
    Other : IconOverlayType # 2


class IIconOverlayExtension(typing.Protocol):
    @abc.abstractmethod
    def DrawOverlay(self, assetPath: str, type: IconOverlayType, rect: Rect) -> None: ...


class IInspectorWindowExtension(typing.Protocol):
    @abc.abstractmethod
    def InvalidateVersionControlBarState(self) -> None: ...
    @abc.abstractmethod
    def OnVersionControlBar(self, editor: Editor) -> None: ...


class IPopupMenuExtension(typing.Protocol):
    @abc.abstractmethod
    def DisplayPopupMenu(self, position: Rect) -> None: ...


class ISettingsInspectorExtension(typing.Protocol):
    @abc.abstractmethod
    def OnInspectorGUI(self) -> None: ...


class MergeMethod(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MergeNone : MergeMethod # 0
    MergeAll : MergeMethod # 1
    MergeNonConflicting : MergeMethod # 2


class Message:
    @property
    def message(self) -> str: ...
    @property
    def severity(self) -> Message.Severity: ...
    def Dispose(self) -> None: ...
    def Show(self) -> None: ...

    class Severity(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Data : Message.Severity # 0
        Verbose : Message.Severity # 1
        Info : Message.Severity # 2
        Warning : Message.Severity # 3
        Error : Message.Severity # 4



class OnlineState(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Updating : OnlineState # 0
    Online : OnlineState # 1
    Offline : OnlineState # 2


class Plugin:
    @classmethod
    @property
    def availablePlugins(cls) -> Array_1[Plugin]: ...
    @property
    def configFields(self) -> Array_1[ConfigField]: ...
    @property
    def name(self) -> str: ...
    def Dispose(self) -> None: ...


class Provider:
    def __init__(self) -> None: ...
    preCheckoutCallback : Provider.PreCheckoutCallback
    preSubmitCallback : Provider.PreSubmitCallback
    @classmethod
    @property
    def activeTask(cls) -> Task: ...
    @classmethod
    @property
    def enabled(cls) -> bool: ...
    @classmethod
    @property
    def hasChangelistSupport(cls) -> bool: ...
    @classmethod
    @property
    def hasCheckoutSupport(cls) -> bool: ...
    @classmethod
    @property
    def hasLockingSupport(cls) -> bool: ...
    @classmethod
    @property
    def isActive(cls) -> bool: ...
    @classmethod
    @property
    def isVersioningFolders(cls) -> bool: ...
    @classmethod
    @property
    def offlineReason(cls) -> str: ...
    @classmethod
    @property
    def onlineState(cls) -> OnlineState: ...
    @classmethod
    @property
    def requiresNetwork(cls) -> bool: ...
    @staticmethod
    def AddIsValid(assets: AssetList) -> bool: ...
    @staticmethod
    def ChangeSetDescription(changeset: ChangeSet) -> Task: ...
    @staticmethod
    def ChangeSets() -> Task: ...
    @staticmethod
    def ClearCache() -> None: ...
    @staticmethod
    def DeleteChangeSets(changesets: ChangeSets) -> Task: ...
    @staticmethod
    def DeleteChangeSetsIsValid(changesets: ChangeSets) -> bool: ...
    @staticmethod
    def DiffHead(assets: AssetList, includingMetaFiles: bool) -> Task: ...
    @staticmethod
    def DiffIsValid(assets: AssetList) -> bool: ...
    @staticmethod
    def GetActiveConfigFields() -> Array_1[ConfigField]: ...
    @staticmethod
    def GetActivePlugin() -> Plugin: ...
    @staticmethod
    def GetAssetByGUID(guid: str) -> Asset: ...
    @staticmethod
    def GetAssetByPath(unityPath: str) -> Asset: ...
    @staticmethod
    def GetAssetListFromSelection() -> AssetList: ...
    @staticmethod
    def Incoming() -> Task: ...
    @staticmethod
    def Internal_ErrorTask(message: str) -> Task: ...
    @staticmethod
    def Internal_WarningTask(message: str) -> Task: ...
    @staticmethod
    def IsOpenForEdit(asset: Asset) -> bool: ...
    @staticmethod
    def Move(from_: str, to: str) -> Task: ...
    @staticmethod
    def Resolve(assets: AssetList, resolveMethod: ResolveMethod) -> Task: ...
    @staticmethod
    def ResolveIsValid(assets: AssetList) -> bool: ...
    @staticmethod
    def Submit(changeset: ChangeSet, list: AssetList, description: str, saveOnly: bool) -> Task: ...
    @staticmethod
    def SubmitIsValid(changeset: ChangeSet, assets: AssetList) -> bool: ...
    @staticmethod
    def UpdateSettings() -> Task: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, recursive: bool) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, recursive: bool) -> Task:...

    # Skipped ChangeSetMove due to it being static, abstract and generic.

    ChangeSetMove : ChangeSetMove_MethodGroup
    class ChangeSetMove_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, changesetID: str) -> Task:...
        @typing.overload
        def __call__(self, assets: AssetList, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, changesetID: str) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, changeset: ChangeSet) -> Task:...

    # Skipped ChangeSetStatus due to it being static, abstract and generic.

    ChangeSetStatus : ChangeSetStatus_MethodGroup
    class ChangeSetStatus_MethodGroup:
        @typing.overload
        def __call__(self, changesetID: str) -> Task:...
        @typing.overload
        def __call__(self, changeset: ChangeSet) -> Task:...

    # Skipped Checkout due to it being static, abstract and generic.

    Checkout : Checkout_MethodGroup
    class Checkout_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[str], mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[Object], mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, asset: str, mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, asset: Object, mode: CheckoutMode) -> Task:...
        @typing.overload
        def __call__(self, assets: AssetList, mode: CheckoutMode, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[str], mode: CheckoutMode, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[Object], mode: CheckoutMode, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, asset: str, mode: CheckoutMode, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, mode: CheckoutMode, changeset: ChangeSet) -> Task:...
        @typing.overload
        def __call__(self, asset: Object, mode: CheckoutMode, changeset: ChangeSet) -> Task:...

    # Skipped CheckoutIsValid due to it being static, abstract and generic.

    CheckoutIsValid : CheckoutIsValid_MethodGroup
    class CheckoutIsValid_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset) -> bool:...
        @typing.overload
        def __call__(self, assets: AssetList, mode: CheckoutMode) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset, mode: CheckoutMode) -> bool:...

    # Skipped Delete due to it being static, abstract and generic.

    Delete : Delete_MethodGroup
    class Delete_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> Task:...
        @typing.overload
        def __call__(self, assetProjectPath: str) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset) -> Task:...

    # Skipped GetLatest due to it being static, abstract and generic.

    GetLatest : GetLatest_MethodGroup
    class GetLatest_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset) -> Task:...

    # Skipped GetLatestIsValid due to it being static, abstract and generic.

    GetLatestIsValid : GetLatestIsValid_MethodGroup
    class GetLatestIsValid_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset) -> bool:...

    # Skipped IncomingChangeSetAssets due to it being static, abstract and generic.

    IncomingChangeSetAssets : IncomingChangeSetAssets_MethodGroup
    class IncomingChangeSetAssets_MethodGroup:
        @typing.overload
        def __call__(self, changesetID: str) -> Task:...
        @typing.overload
        def __call__(self, changeset: ChangeSet) -> Task:...

    # Skipped Lock due to it being static, abstract and generic.

    Lock : Lock_MethodGroup
    class Lock_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, locked: bool) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, locked: bool) -> Task:...

    # Skipped LockIsValid due to it being static, abstract and generic.

    LockIsValid : LockIsValid_MethodGroup
    class LockIsValid_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset) -> bool:...

    # Skipped Merge due to it being static, abstract and generic.

    Merge : Merge_MethodGroup
    class Merge_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> Task:...
        @typing.overload
        def __call__(self, assets: AssetList, method: MergeMethod) -> Task:...

    # Skipped Revert due to it being static, abstract and generic.

    Revert : Revert_MethodGroup
    class Revert_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, mode: RevertMode) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, mode: RevertMode) -> Task:...

    # Skipped RevertIsValid due to it being static, abstract and generic.

    RevertIsValid : RevertIsValid_MethodGroup
    class RevertIsValid_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList, mode: RevertMode) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset, mode: RevertMode) -> bool:...

    # Skipped Status due to it being static, abstract and generic.

    Status : Status_MethodGroup
    class Status_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[str]) -> Task:...
        @typing.overload
        def __call__(self, asset: str) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset) -> Task:...
        @typing.overload
        def __call__(self, assets: AssetList, recursively: bool) -> Task:...
        @typing.overload
        def __call__(self, assets: Array_1[str], recursively: bool) -> Task:...
        @typing.overload
        def __call__(self, asset: str, recursively: bool) -> Task:...
        @typing.overload
        def __call__(self, asset: Asset, recursively: bool) -> Task:...

    # Skipped UnlockIsValid due to it being static, abstract and generic.

    UnlockIsValid : UnlockIsValid_MethodGroup
    class UnlockIsValid_MethodGroup:
        @typing.overload
        def __call__(self, assets: AssetList) -> bool:...
        @typing.overload
        def __call__(self, asset: Asset) -> bool:...


    class PreCheckoutCallback(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, list: AssetList, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str], result: IAsyncResult) -> bool: ...
        def Invoke(self, list: AssetList, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str]) -> bool: ...


    class PreSubmitCallback(MulticastDelegate):
        def __init__(self, object: typing.Any, method: int) -> None: ...
        @property
        def Method(self) -> MethodInfo: ...
        @property
        def Target(self) -> typing.Any: ...
        def BeginInvoke(self, list: AssetList, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str], callback: AsyncCallback, object: typing.Any) -> IAsyncResult: ...
        def EndInvoke(self, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str], result: IAsyncResult) -> bool: ...
        def Invoke(self, list: AssetList, changesetID: clr.Reference[str], changesetDescription: clr.Reference[str]) -> bool: ...



class ResolveMethod(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    UseMine : ResolveMethod # 1
    UseTheirs : ResolveMethod # 2
    UseMerged : ResolveMethod # 3


class RevertMode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Normal : RevertMode # 0
    Unchanged : RevertMode # 1
    KeepModifications : RevertMode # 2


class SubmitResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    OK : SubmitResult # 1
    Error : SubmitResult # 2
    ConflictingFiles : SubmitResult # 4
    UnaddedFiles : SubmitResult # 8


class Task:
    @property
    def assetList(self) -> AssetList: ...
    @property
    def changeSets(self) -> ChangeSets: ...
    @property
    def description(self) -> str: ...
    @property
    def messages(self) -> Array_1[Message]: ...
    @property
    def progressMessage(self) -> str: ...
    @property
    def progressPct(self) -> int: ...
    @property
    def resultCode(self) -> int: ...
    @property
    def secondsSpent(self) -> int: ...
    @property
    def success(self) -> bool: ...
    @property
    def text(self) -> str: ...
    @property
    def userIdentifier(self) -> int: ...
    @userIdentifier.setter
    def userIdentifier(self, value: int) -> int: ...
    def Dispose(self) -> None: ...
    def SetCompletionAction(self, action: CompletionAction) -> None: ...
    def Wait(self) -> None: ...


class VersionControlAttribute(Attribute):
    def __init__(self, name: str, displayName: str = ...) -> None: ...
    @property
    def displayName(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class VersionControlDescriptor:
    @property
    def displayName(self) -> str: ...
    @property
    def name(self) -> str: ...


class VersionControlManager(abc.ABC):
    @classmethod
    @property
    def activeVersionControlObject(cls) -> VersionControlObject: ...
    @classmethod
    @activeVersionControlObject.setter
    def activeVersionControlObject(cls, value: VersionControlObject) -> VersionControlObject: ...
    @classmethod
    @property
    def versionControlDescriptors(cls) -> Array_1[VersionControlDescriptor]: ...
    @staticmethod
    def SetVersionControl(name: str) -> bool: ...


class VersionControlObject(ScriptableObject, abc.ABC):
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def isConnected(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    def OnActivate(self) -> None: ...
    def OnDeactivate(self) -> None: ...
    def Refresh(self) -> None: ...
    # Skipped GetExtension due to it being static, abstract and generic.

    GetExtension : GetExtension_MethodGroup
    class GetExtension_MethodGroup:
        def __getitem__(self, t:typing.Type[GetExtension_1_T1]) -> GetExtension_1[GetExtension_1_T1]: ...

        GetExtension_1_T1 = typing.TypeVar('GetExtension_1_T1')
        class GetExtension_1(typing.Generic[GetExtension_1_T1]):
            GetExtension_1_T = VersionControlObject.GetExtension_MethodGroup.GetExtension_1_T1
            def __call__(self) -> GetExtension_1_T:...




class VersionControlUtils(abc.ABC):
    @staticmethod
    def IsPathVersioned(path: str) -> bool: ...

