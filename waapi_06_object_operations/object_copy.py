from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_copy(object_str: str, parent_str: str, on_name_conflict: str = 'fail') -> dict:
    with WaapiClient() as client:
        args = {
            'object': object_str,
            'parent': parent_str,
            'onNameConflict': on_name_conflict
        }
        result = client.call(uri.ak_wwise_core_object_copy, args)
        print(result)

