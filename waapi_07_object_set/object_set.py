from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_set(object_str: str, on_name_conflict: str = 'fail', name: str = None, notes: str = None):
    with WaapiClient() as client:
        object_dict = {
            'object': object_str,
            'onNameConflict': on_name_conflict,
            'name': name,
            'notes': notes,
            '@Volume': 0.0,
        }

        args = {
            'objects': [object_dict]
        }

        result = client.call(uri.ak_wwise_core_object_set, args)
        print(result)


if __name__ == '__main__':
    object_set(
        object_str='{23F983CF-1839-4976-881A-32CD6EFE4D83}',
        on_name_conflict='fail',
        name='MyObject',
        notes='My notes'
    )
