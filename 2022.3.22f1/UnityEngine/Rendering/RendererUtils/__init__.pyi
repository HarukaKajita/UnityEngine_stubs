import typing, clr
from UnityEngine.Rendering import ShaderTagId, CullingResults, PerObjectData, RenderQueueRange, SortingCriteria, RenderStateBlock, RendererListParams
from UnityEngine import Camera, Material, Shader
from System import Array_1

class RendererListDesc:
    @typing.overload
    def __init__(self, passName: ShaderTagId, cullingResult: CullingResults, camera: Camera) -> None: ...
    @typing.overload
    def __init__(self, passNames: Array_1[ShaderTagId], cullingResult: CullingResults, camera: Camera) -> None: ...
    excludeObjectMotionVectors : bool
    layerMask : int
    overrideMaterial : Material
    overrideMaterialPassIndex : int
    overrideShader : Shader
    overrideShaderPassIndex : int
    rendererConfiguration : PerObjectData
    renderingLayerMask : int
    renderQueueRange : RenderQueueRange
    sortingCriteria : SortingCriteria
    stateBlock : typing.Optional[RenderStateBlock]
    @staticmethod
    def ConvertToParameters(desc: clr.Reference[RendererListDesc]) -> RendererListParams: ...
    def IsValid(self) -> bool: ...

