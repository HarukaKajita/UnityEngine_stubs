import abc

class SolutionGuidGenerator(abc.ABC):
    @staticmethod
    def GuidForProject(projectName: str) -> str: ...
    @staticmethod
    def GuidForSolution(projectName: str, sourceFileExtension: str) -> str: ...

