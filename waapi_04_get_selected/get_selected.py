from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


RETURN_LIST = [
    "id",
    "name",
    "notes",
    "type",
    "pluginName",
    "shortId",
    "classId",
    "category",
    "filePath",
    "workunit",
    "parent",
    "owner",
    "path",
    "isPlayable",
    "childrenCount",
    "totalSize",
    "mediaSize",
    "objectSize",
    "structureSize"
]


try:
    with WaapiClient() as client:
        result = client.call(uri.ak_wwise_ui_getselectedobjects, options={"return": RETURN_LIST})
        print(result)

except Exception as e:
    print(e)
