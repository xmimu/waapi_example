from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_delete(object_str: str) -> dict:
    with WaapiClient() as client:
        args = {
            'object': object_str,
        }
        result = client.call(uri.ak_wwise_core_object_delete, args)
        print(result)


if __name__ == '__main__':
    object_delete(
        '{93F38D56-9A09-4243-A38E-8D7819014897}',
    )
