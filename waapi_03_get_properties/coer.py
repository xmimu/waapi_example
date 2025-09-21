from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri


def get_types(client: WaapiClient):
    result = client.call(uri.ak_wwise_core_object_gettypes)
    return result['return']


def get_property_and_reference_names(client: WaapiClient, class_id):
    args = {
        'classId': class_id,
    }
    result = client.call(uri.ak_wwise_core_object_getpropertyandreferencenames, args)
    return result['return']


def get_type(client: WaapiClient, guid):
    args = {
        'from': {'id': [guid]}
    }
    options = {'return': ['id', 'name', 'type']}
    result = client.call(uri.ak_wwise_core_object_get, args, options=options)
    return result['return'][0]['type']


def get_property_values(client: WaapiClient, object_id: str, properties: list[str]):
    args = {
        'from': {'id': [object_id]}
    }
    options = {'return': ['id', 'name', 'type'] + properties}
    result = client.call(uri.ak_wwise_core_object_get, args, options=options)
    return result['return']


def get_properties(client: WaapiClient, guid):
    # 通过 guid 查找对象类型
    wtype = get_type(client, guid)
    # print(wtype)
    # 通过对象类型 查找 class id
    types = get_types(client)
    class_id = None
    for t in types:
        if t['name'] == wtype:
            class_id = t['classId']
            break
    # print(class_id)
    # 通过 class id 查找该类型的所有属性、引用名称列表
    names = get_property_and_reference_names(client, class_id)
    # pprint(names)
    # 通过属性名称列表 查找属性值
    return get_property_values(client, guid, names)


if __name__ == '__main__':
    from pprint import pprint

    try:
        with WaapiClient() as client:
            guid = '{B195D0DF-51D7-443B-9BFB-199F471E3080}'
            result = get_properties(client, guid)
            pprint(result)

    except Exception as e:
        print(e)
