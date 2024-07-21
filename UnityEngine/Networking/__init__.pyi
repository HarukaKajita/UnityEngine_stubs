import typing, abc
from System import IDisposable, Array_1, Uri
from Unity.Collections import NativeArray_1
from UnityEngine import CachedAssetBundle, Hash128, AssetBundle, AudioType, AudioClip, MovieTexture, Texture2D, AsyncOperation, WWWForm
from System.Text import Encoding
from System.Collections.Generic import Dictionary_2, List_1

class CertificateHandler(IDisposable):
    def Dispose(self) -> None: ...


class DownloadHandler(IDisposable):
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...
    def Dispose(self) -> None: ...


class DownloadHandlerAssetBundle(DownloadHandler):
    @typing.overload
    def __init__(self, url: str, cachedBundle: CachedAssetBundle, crc: int) -> None: ...
    @typing.overload
    def __init__(self, url: str, crc: int) -> None: ...
    @typing.overload
    def __init__(self, url: str, hash: Hash128, crc: int) -> None: ...
    @typing.overload
    def __init__(self, url: str, name: str, hash: Hash128, crc: int) -> None: ...
    @typing.overload
    def __init__(self, url: str, version: int, crc: int) -> None: ...
    @property
    def assetBundle(self) -> AssetBundle: ...
    @property
    def autoLoadAssetBundle(self) -> bool: ...
    @autoLoadAssetBundle.setter
    def autoLoadAssetBundle(self, value: bool) -> bool: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def isDownloadComplete(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...
    @staticmethod
    def GetContent(www: UnityWebRequest) -> AssetBundle: ...


class DownloadHandlerAudioClip(DownloadHandler):
    @typing.overload
    def __init__(self, uri: Uri, audioType: AudioType) -> None: ...
    @typing.overload
    def __init__(self, url: str, audioType: AudioType) -> None: ...
    @property
    def audioClip(self) -> AudioClip: ...
    @property
    def compressed(self) -> bool: ...
    @compressed.setter
    def compressed(self, value: bool) -> bool: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def streamAudio(self) -> bool: ...
    @streamAudio.setter
    def streamAudio(self, value: bool) -> bool: ...
    @property
    def text(self) -> str: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GetContent(www: UnityWebRequest) -> AudioClip: ...


class DownloadHandlerBuffer(DownloadHandler):
    def __init__(self) -> None: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GetContent(www: UnityWebRequest) -> str: ...


class DownloadHandlerFile(DownloadHandler):
    @typing.overload
    def __init__(self, path: str) -> None: ...
    @typing.overload
    def __init__(self, path: str, append: bool) -> None: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def removeFileOnAbort(self) -> bool: ...
    @removeFileOnAbort.setter
    def removeFileOnAbort(self, value: bool) -> bool: ...
    @property
    def text(self) -> str: ...


class DownloadHandlerMovieTexture(DownloadHandler):
    def __init__(self) -> None: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def movieTexture(self) -> MovieTexture: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...
    @staticmethod
    def GetContent(uwr: UnityWebRequest) -> MovieTexture: ...


class DownloadHandlerScript(DownloadHandler):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, preallocatedBuffer: Array_1[int]) -> None: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...


class DownloadHandlerTexture(DownloadHandler):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, readable: bool) -> None: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def nativeData(self) -> NativeArray_1.ReadOnly_1[int]: ...
    @property
    def text(self) -> str: ...
    @property
    def texture(self) -> Texture2D: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GetContent(www: UnityWebRequest) -> Texture2D: ...


class IMultipartFormSection(typing.Protocol):
    @property
    def contentType(self) -> str: ...
    @property
    def fileName(self) -> str: ...
    @property
    def sectionData(self) -> Array_1[int]: ...
    @property
    def sectionName(self) -> str: ...


class MultipartFormDataSection(IMultipartFormSection):
    @typing.overload
    def __init__(self, data: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, data: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: Array_1[int], contentType: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: str, contentType: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: str, encoding: Encoding, contentType: str) -> None: ...
    @property
    def contentType(self) -> str: ...
    @property
    def fileName(self) -> str: ...
    @property
    def sectionData(self) -> Array_1[int]: ...
    @property
    def sectionName(self) -> str: ...


class MultipartFormFileSection(IMultipartFormSection):
    @typing.overload
    def __init__(self, data: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, data: str, dataEncoding: Encoding, fileName: str) -> None: ...
    @typing.overload
    def __init__(self, data: str, fileName: str) -> None: ...
    @typing.overload
    def __init__(self, fileName: str, data: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: str, dataEncoding: Encoding, fileName: str) -> None: ...
    @typing.overload
    def __init__(self, name: str, data: Array_1[int], fileName: str, contentType: str) -> None: ...
    @property
    def contentType(self) -> str: ...
    @property
    def fileName(self) -> str: ...
    @property
    def sectionData(self) -> Array_1[int]: ...
    @property
    def sectionName(self) -> str: ...


class UnityWebRequest(IDisposable):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, uri: Uri) -> None: ...
    @typing.overload
    def __init__(self, uri: Uri, method: str) -> None: ...
    @typing.overload
    def __init__(self, uri: Uri, method: str, downloadHandler: DownloadHandler, uploadHandler: UploadHandler) -> None: ...
    @typing.overload
    def __init__(self, url: str) -> None: ...
    @typing.overload
    def __init__(self, url: str, method: str) -> None: ...
    @typing.overload
    def __init__(self, url: str, method: str, downloadHandler: DownloadHandler, uploadHandler: UploadHandler) -> None: ...
    kHttpVerbCREATE : str
    kHttpVerbDELETE : str
    kHttpVerbGET : str
    kHttpVerbHEAD : str
    kHttpVerbPOST : str
    kHttpVerbPUT : str
    @property
    def certificateHandler(self) -> CertificateHandler: ...
    @certificateHandler.setter
    def certificateHandler(self, value: CertificateHandler) -> CertificateHandler: ...
    @property
    def chunkedTransfer(self) -> bool: ...
    @chunkedTransfer.setter
    def chunkedTransfer(self, value: bool) -> bool: ...
    @property
    def disposeCertificateHandlerOnDispose(self) -> bool: ...
    @disposeCertificateHandlerOnDispose.setter
    def disposeCertificateHandlerOnDispose(self, value: bool) -> bool: ...
    @property
    def disposeDownloadHandlerOnDispose(self) -> bool: ...
    @disposeDownloadHandlerOnDispose.setter
    def disposeDownloadHandlerOnDispose(self, value: bool) -> bool: ...
    @property
    def disposeUploadHandlerOnDispose(self) -> bool: ...
    @disposeUploadHandlerOnDispose.setter
    def disposeUploadHandlerOnDispose(self, value: bool) -> bool: ...
    @property
    def downloadedBytes(self) -> int: ...
    @property
    def downloadHandler(self) -> DownloadHandler: ...
    @downloadHandler.setter
    def downloadHandler(self, value: DownloadHandler) -> DownloadHandler: ...
    @property
    def downloadProgress(self) -> float: ...
    @property
    def error(self) -> str: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def isError(self) -> bool: ...
    @property
    def isHttpError(self) -> bool: ...
    @property
    def isModifiable(self) -> bool: ...
    @property
    def isNetworkError(self) -> bool: ...
    @property
    def method(self) -> str: ...
    @method.setter
    def method(self, value: str) -> str: ...
    @property
    def redirectLimit(self) -> int: ...
    @redirectLimit.setter
    def redirectLimit(self, value: int) -> int: ...
    @property
    def responseCode(self) -> int: ...
    @property
    def result(self) -> UnityWebRequest.Result: ...
    @property
    def timeout(self) -> int: ...
    @timeout.setter
    def timeout(self, value: int) -> int: ...
    @property
    def uploadedBytes(self) -> int: ...
    @property
    def uploadHandler(self) -> UploadHandler: ...
    @uploadHandler.setter
    def uploadHandler(self, value: UploadHandler) -> UploadHandler: ...
    @property
    def uploadProgress(self) -> float: ...
    @property
    def uri(self) -> Uri: ...
    @uri.setter
    def uri(self, value: Uri) -> Uri: ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str) -> str: ...
    @property
    def useHttpContinue(self) -> bool: ...
    @useHttpContinue.setter
    def useHttpContinue(self, value: bool) -> bool: ...
    def Abort(self) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GenerateBoundary() -> Array_1[int]: ...
    @staticmethod
    def GetAudioClip(uri: str, audioType: AudioType) -> UnityWebRequest: ...
    def GetRequestHeader(self, name: str) -> str: ...
    def GetResponseHeader(self, name: str) -> str: ...
    def GetResponseHeaders(self) -> Dictionary_2[str, str]: ...
    def Send(self) -> AsyncOperation: ...
    def SendWebRequest(self) -> UnityWebRequestAsyncOperation: ...
    @staticmethod
    def SerializeFormSections(multipartFormSections: List_1[IMultipartFormSection], boundary: Array_1[int]) -> Array_1[int]: ...
    @staticmethod
    def SerializeSimpleForm(formFields: Dictionary_2[str, str]) -> Array_1[int]: ...
    def SetRequestHeader(self, name: str, value: str) -> None: ...
    # Skipped ClearCookieCache due to it being static, abstract and generic.

    ClearCookieCache : ClearCookieCache_MethodGroup
    class ClearCookieCache_MethodGroup:
        @typing.overload
        def __call__(self) -> None:...
        @typing.overload
        def __call__(self, uri: Uri) -> None:...

    # Skipped Delete due to it being static, abstract and generic.

    Delete : Delete_MethodGroup
    class Delete_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...

    # Skipped EscapeURL due to it being static, abstract and generic.

    EscapeURL : EscapeURL_MethodGroup
    class EscapeURL_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> str:...
        @typing.overload
        def __call__(self, s: str, e: Encoding) -> str:...

    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup
    class Get_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...

    # Skipped GetAssetBundle due to it being static, abstract and generic.

    GetAssetBundle : GetAssetBundle_MethodGroup
    class GetAssetBundle_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, version: int, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, cachedAssetBundle: CachedAssetBundle, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, hash: Hash128, crc: int) -> UnityWebRequest:...

    # Skipped GetTexture due to it being static, abstract and generic.

    GetTexture : GetTexture_MethodGroup
    class GetTexture_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, nonReadable: bool) -> UnityWebRequest:...

    # Skipped Head due to it being static, abstract and generic.

    Head : Head_MethodGroup
    class Head_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...

    # Skipped Post due to it being static, abstract and generic.

    Post : Post_MethodGroup
    class Post_MethodGroup:
        @typing.overload
        def __call__(self, uri: str, formFields: Dictionary_2[str, str]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, multipartFormSections: List_1[IMultipartFormSection]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, postData: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, formData: WWWForm) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, formFields: Dictionary_2[str, str]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, multipartFormSections: List_1[IMultipartFormSection]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, postData: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, formData: WWWForm) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, multipartFormSections: List_1[IMultipartFormSection], boundary: Array_1[int]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, postData: str, contentType: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, multipartFormSections: List_1[IMultipartFormSection], boundary: Array_1[int]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, postData: str, contentType: str) -> UnityWebRequest:...

    # Skipped PostWwwForm due to it being static, abstract and generic.

    PostWwwForm : PostWwwForm_MethodGroup
    class PostWwwForm_MethodGroup:
        @typing.overload
        def __call__(self, uri: str, form: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, form: str) -> UnityWebRequest:...

    # Skipped Put due to it being static, abstract and generic.

    Put : Put_MethodGroup
    class Put_MethodGroup:
        @typing.overload
        def __call__(self, uri: str, bodyData: Array_1[int]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, bodyData: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, bodyData: Array_1[int]) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, bodyData: str) -> UnityWebRequest:...

    # Skipped UnEscapeURL due to it being static, abstract and generic.

    UnEscapeURL : UnEscapeURL_MethodGroup
    class UnEscapeURL_MethodGroup:
        @typing.overload
        def __call__(self, s: str) -> str:...
        @typing.overload
        def __call__(self, s: str, e: Encoding) -> str:...


    class Result(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        InProgress : UnityWebRequest.Result # 0
        Success : UnityWebRequest.Result # 1
        ConnectionError : UnityWebRequest.Result # 2
        ProtocolError : UnityWebRequest.Result # 3
        DataProcessingError : UnityWebRequest.Result # 4



class UnityWebRequestAssetBundle(abc.ABC):
    # Skipped GetAssetBundle due to it being static, abstract and generic.

    GetAssetBundle : GetAssetBundle_MethodGroup
    class GetAssetBundle_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, version: int, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, cachedAssetBundle: CachedAssetBundle, crc: int = ...) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, hash: Hash128, crc: int = ...) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, version: int, crc: int) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, cachedAssetBundle: CachedAssetBundle, crc: int = ...) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, hash: Hash128, crc: int = ...) -> UnityWebRequest:...



class UnityWebRequestAsyncOperation(AsyncOperation):
    def __init__(self) -> None: ...
    @property
    def allowSceneActivation(self) -> bool: ...
    @allowSceneActivation.setter
    def allowSceneActivation(self, value: bool) -> bool: ...
    @property
    def isDone(self) -> bool: ...
    @property
    def priority(self) -> int: ...
    @priority.setter
    def priority(self, value: int) -> int: ...
    @property
    def progress(self) -> float: ...
    @property
    def webRequest(self) -> UnityWebRequest: ...
    @webRequest.setter
    def webRequest(self, value: UnityWebRequest) -> UnityWebRequest: ...


class UnityWebRequestMultimedia(abc.ABC):
    # Skipped GetAudioClip due to it being static, abstract and generic.

    GetAudioClip : GetAudioClip_MethodGroup
    class GetAudioClip_MethodGroup:
        @typing.overload
        def __call__(self, uri: str, audioType: AudioType) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, audioType: AudioType) -> UnityWebRequest:...

    # Skipped GetMovieTexture due to it being static, abstract and generic.

    GetMovieTexture : GetMovieTexture_MethodGroup
    class GetMovieTexture_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...



class UnityWebRequestTexture(abc.ABC):
    # Skipped GetTexture due to it being static, abstract and generic.

    GetTexture : GetTexture_MethodGroup
    class GetTexture_MethodGroup:
        @typing.overload
        def __call__(self, uri: str) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: str, nonReadable: bool) -> UnityWebRequest:...
        @typing.overload
        def __call__(self, uri: Uri, nonReadable: bool) -> UnityWebRequest:...



class UploadHandler(IDisposable):
    @property
    def contentType(self) -> str: ...
    @contentType.setter
    def contentType(self, value: str) -> str: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def progress(self) -> float: ...
    def Dispose(self) -> None: ...


class UploadHandlerFile(UploadHandler):
    def __init__(self, filePath: str) -> None: ...
    @property
    def contentType(self) -> str: ...
    @contentType.setter
    def contentType(self, value: str) -> str: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def progress(self) -> float: ...


class UploadHandlerRaw(UploadHandler):
    @typing.overload
    def __init__(self, data: Array_1[int]) -> None: ...
    @typing.overload
    def __init__(self, data: NativeArray_1.ReadOnly_1[int]) -> None: ...
    @typing.overload
    def __init__(self, data: NativeArray_1[int], transferOwnership: bool) -> None: ...
    @property
    def contentType(self) -> str: ...
    @contentType.setter
    def contentType(self, value: str) -> str: ...
    @property
    def data(self) -> Array_1[int]: ...
    @property
    def progress(self) -> float: ...
    def Dispose(self) -> None: ...

