import abc
from System import Array_1
from UnityEngine import AssetBundle

class AssetBundleUtility(abc.ABC):
    @staticmethod
    def PatchAssetBundles(bundles: Array_1[AssetBundle], filenames: Array_1[str]) -> None: ...

