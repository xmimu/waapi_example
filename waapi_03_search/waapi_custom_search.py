from waapi import WaapiClient, CannotConnectToWaapiException

from pprint import pprint


def search(client: WaapiClient, text: str) -> list:
    """查询函数，找到包含字符串的对象，返回一个列表"""
    args = {
        'from': {'search': [text]}
    }
    options = {'return': ['id', 'name', 'path', 'type']}
    result = client.call('ak.wwise.core.object.get',
                         args, options=options)
    if result and result['return']:
        return result['return']
    return []


def search_by_type(client: WaapiClient, text: str, type_str: str) -> list:
    """查询对应类型，返回包含字符串的对象"""
    args = {
        'from': {'ofType': [type_str]},
        'transform': [
            {'where': ['name:contains', text]}
        ]
    }
    options = {'return': ['id', 'name', 'path', 'type']}
    result = client.call('ak.wwise.core.object.get',
                         args, options=options)
    if result and result['return']:
        return result['return']
    return []


try:
    with WaapiClient() as client:

        result = search(client, 'buttsson')
        pprint(result)

        result = search_by_type(client, 'ui', 'WorkUnit')
        pprint(result)

except CannotConnectToWaapiException:
    print('CannotConnectToWaapiException')
