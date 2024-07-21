from UnityEditor import BuildTarget

class Il2CppBuildPipelineData:
    def __init__(self, target: BuildTarget, inputDirectory: str) -> None: ...
    inputDirectory : str
    target : BuildTarget

