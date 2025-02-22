import typing
from UnityEditor import EditorWindow, IDataModeController, ShaderGUI, MaterialEditor, MaterialProperty, Editor, SerializedObject
from UnityEngine import HideFlags, Vector2, Rect, GUIContent, Font, Object
from UnityEditor.Overlays import OverlayCanvas
from UnityEngine.UIElements import VisualElement
from UnityEngine.TextCore.Text import FontAsset
from System import Array_1

class FontAssetCreatorWindow(EditorWindow):
    def __init__(self) -> None: ...
    @property
    def antiAlias(self) -> int: ...
    @antiAlias.setter
    def antiAlias(self, value: int) -> int: ...
    @property
    def autoRepaintOnSceneChange(self) -> bool: ...
    @autoRepaintOnSceneChange.setter
    def autoRepaintOnSceneChange(self, value: bool) -> bool: ...
    @property
    def dataModeController(self) -> IDataModeController: ...
    @property
    def depthBufferBits(self) -> int: ...
    @depthBufferBits.setter
    def depthBufferBits(self, value: int) -> int: ...
    @property
    def docked(self) -> bool: ...
    @property
    def hasFocus(self) -> bool: ...
    @property
    def hasUnsavedChanges(self) -> bool: ...
    @hasUnsavedChanges.setter
    def hasUnsavedChanges(self, value: bool) -> bool: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def maximized(self) -> bool: ...
    @maximized.setter
    def maximized(self, value: bool) -> bool: ...
    @property
    def maxSize(self) -> Vector2: ...
    @maxSize.setter
    def maxSize(self, value: Vector2) -> Vector2: ...
    @property
    def minSize(self) -> Vector2: ...
    @minSize.setter
    def minSize(self, value: Vector2) -> Vector2: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def overlayCanvas(self) -> OverlayCanvas: ...
    @property
    def position(self) -> Rect: ...
    @position.setter
    def position(self, value: Rect) -> Rect: ...
    @property
    def rootVisualElement(self) -> VisualElement: ...
    @property
    def saveChangesMessage(self) -> str: ...
    @saveChangesMessage.setter
    def saveChangesMessage(self, value: str) -> str: ...
    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> str: ...
    @property
    def titleContent(self) -> GUIContent: ...
    @titleContent.setter
    def titleContent(self, value: GUIContent) -> GUIContent: ...
    @property
    def wantsLessLayoutEvents(self) -> bool: ...
    @wantsLessLayoutEvents.setter
    def wantsLessLayoutEvents(self, value: bool) -> bool: ...
    @property
    def wantsMouseEnterLeaveWindow(self) -> bool: ...
    @wantsMouseEnterLeaveWindow.setter
    def wantsMouseEnterLeaveWindow(self, value: bool) -> bool: ...
    @property
    def wantsMouseMove(self) -> bool: ...
    @wantsMouseMove.setter
    def wantsMouseMove(self, value: bool) -> bool: ...
    def OnDisable(self) -> None: ...
    def OnEnable(self) -> None: ...
    def OnGUI(self) -> None: ...
    def Update(self) -> None: ...
    # Skipped ShowFontAtlasCreatorWindow due to it being static, abstract and generic.

    ShowFontAtlasCreatorWindow : ShowFontAtlasCreatorWindow_MethodGroup
    class ShowFontAtlasCreatorWindow_MethodGroup:
        @typing.overload
        def __call__(self, fontAsset: FontAsset) -> None:...
        @typing.overload
        def __call__(self, font: Font) -> None:...



class TextCoreShaderGUI(ShaderGUI):
    def EndPanel(self) -> None: ...
    def OnGUI(self, materialEditor: MaterialEditor, properties: Array_1[MaterialProperty]) -> None: ...


class TextCoreShaderGUIBitmap(TextCoreShaderGUI):
    def __init__(self) -> None: ...


class TextCoreShaderGUISDF(TextCoreShaderGUI):
    def __init__(self) -> None: ...


class TextSettingsEditor(Editor):
    def __init__(self) -> None: ...
    @property
    def hasUnsavedChanges(self) -> bool: ...
    @hasUnsavedChanges.setter
    def hasUnsavedChanges(self, value: bool) -> bool: ...
    @property
    def hideFlags(self) -> HideFlags: ...
    @hideFlags.setter
    def hideFlags(self, value: HideFlags) -> HideFlags: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str) -> str: ...
    @property
    def saveChangesMessage(self) -> str: ...
    @saveChangesMessage.setter
    def saveChangesMessage(self, value: str) -> str: ...
    @property
    def serializedObject(self) -> SerializedObject: ...
    @property
    def target(self) -> Object: ...
    @target.setter
    def target(self, value: Object) -> Object: ...
    @property
    def targets(self) -> Array_1[Object]: ...
    def OnEnable(self) -> None: ...
    def OnInspectorGUI(self) -> None: ...

