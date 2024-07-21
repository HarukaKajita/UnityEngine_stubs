from UnityEditor import BuildTarget

class UnityLinkerBuildPipelineData:
    def __init__(self, target: BuildTarget, inputDirectory: str) -> None: ...
    inputDirectory : str
    target : BuildTarget

