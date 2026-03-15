from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def object_set_reference(object_str: str, reference_str: str, value_str):
    with WaapiClient() as client:
        args = {
            'object': object_str,
            'reference': reference_str,
            'value': value_str
        }

        result = client.call(uri.ak_wwise_core_object_setreference, args)
        print(result)


if __name__ == '__main__':
    object_set_reference(
        '{23F983CF-1839-4976-881A-32CD6EFE4D83}',
        'Attenuation',
        '{21C9C3CB-17DA-4D39-AD87-46CEB24597F3}'
    )
