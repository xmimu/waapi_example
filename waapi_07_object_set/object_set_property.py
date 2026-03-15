from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_set_property(object_str: str, property_str: str, value_str):
    with WaapiClient() as client:
        args = {
            'object': object_str,
            'property': property_str,
            'value': value_str
        }

        result = client.call(uri.ak_wwise_core_object_setproperty, args)
        print(result)


if __name__ == '__main__':
    object_set_property(
        '{23F983CF-1839-4976-881A-32CD6EFE4D83}',
        'Volume',
        -5
    )
