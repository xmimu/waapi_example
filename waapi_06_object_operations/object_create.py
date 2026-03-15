from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_create(parent_str: str, type_str: str, name_str: str, on_name_conflict: str = 'fail') -> dict:
    with WaapiClient() as client:
        args = {
            'parent': parent_str,
            'type': type_str,
            'name': name_str,
            'onNameConflict': on_name_conflict,
        }
        result = client.call(uri.ak_wwise_core_object_create, args)
        print(result)


if __name__ == '__main__':
    object_create(
        '{ABDCF911-2817-4098-BB98-C3B64D426924}',  # 父级对象 id
        'Event',
        'Play_SFX_TEST_WAAPI',
        'merge'
    )
