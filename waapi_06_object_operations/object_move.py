from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_move(object_str: str, parent_str: str, on_name_conflict: str = 'fail') -> dict:
    with WaapiClient() as client:
        args = {
            'object': object_str,
            'parent': parent_str,
            'onNameConflict': on_name_conflict
        }
        result = client.call(uri.ak_wwise_core_object_move, args)
        print(result)


if __name__ == '__main__':
    object_move(
        '{93F38D56-9A09-4243-A38E-8D7819014897}',
        '{ABDCF911-2817-4098-BB98-C3B64D426924}'
    )
