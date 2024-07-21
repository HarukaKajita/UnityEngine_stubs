import typing, abc
from System import Array_1
from UnityEngine.Playables import PlayableGraph

class PlayableOutputEditorExtensions(abc.ABC):
    # Skipped GetEditorName due to it being static, abstract and generic.

    GetEditorName : GetEditorName_MethodGroup
    class GetEditorName_MethodGroup:
        def __getitem__(self, t:typing.Type[GetEditorName_1_T1]) -> GetEditorName_1[GetEditorName_1_T1]: ...

        GetEditorName_1_T1 = typing.TypeVar('GetEditorName_1_T1')
        class GetEditorName_1(typing.Generic[GetEditorName_1_T1]):
            GetEditorName_1_U = PlayableOutputEditorExtensions.GetEditorName_MethodGroup.GetEditorName_1_T1
            def __call__(self, output: GetEditorName_1_U) -> str:...




class Utility(abc.ABC):
    @staticmethod
    def GetAllGraphs() -> Array_1[PlayableGraph]: ...

