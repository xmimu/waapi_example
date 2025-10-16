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

        def on_selection_changed(*args, **kwargs):
            print("on_selection_changed")
            objects = kwargs.get("objects", [])
            print('对象的数量:', len(objects))
            for obj in objects:
                obj_id = obj.get("id")
                obj_name = obj.get("name")
                print(f"对象ID: {obj_id}, 对象名称: {obj_name}")
                totalSize = obj.get("totalSize", 0)
                mediaSize = obj.get("mediaSize", 0)
                objectSize = obj.get("objectSize", 0)
                structureSize = obj.get("structureSize", 0)
                print(f"totalSize: {totalSize}, mediaSize: {mediaSize}, objectSize: {objectSize}, structureSize: {structureSize}")


        client.subscribe(
            uri.ak_wwise_ui_selectionchanged,
            on_selection_changed,
            {"return": RETURN_LIST}
        )

        while True:

            input_code = input('输入任意键退出...\n')
            if input_code:
                break

except Exception as e:
    print(e)
