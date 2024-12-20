from waapi_uri import WAAPI_URI as uri

from waapi import WaapiClient


def on_name_changed(object, newName, oldName):
    print('名字改变了！！！')
    print(object)
    print(newName)
    print(oldName)


def on_selection_changed(objects):
    print('选区改变！！！')
    print(objects)


try:
    with WaapiClient() as client:

        client.subscribe(uri.ak_wwise_core_object_namechanged,
                         on_name_changed,
                         {'return': ['id', 'name']}
                         )

        client.subscribe(uri.ak_wwise_ui_selectionchanged,
                         on_selection_changed,
                         {'return': ['id', 'name']}
                         )

        while True:
            pass


except Exception as e:
    print(e)
