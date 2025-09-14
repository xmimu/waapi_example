from waapi import WaapiClient
import pprint
from waapi_uri import WAAPI_URI as uri


def get_paltforms():
    '''获取当前项目的所有平台'''
    try:
        with WaapiClient() as client:
            result = client.call(uri.ak_wwise_core_getprojectinfo)
            # platforms = []
            # for platform in result['platforms']:
            #     platforms.append(platform['name'])
            # return platforms
            return list(map(lambda p: p['name'], result['platforms']))

    except Exception as e:
        print(f'运行错误：{e}')
        return []


def search(text, search_type, platform, return_list):
    '''搜索对象'''
    try:
        with WaapiClient() as client:
            args = {
                'from': {'search': [text]},
                'transform': [
                    {'where': ['type:isIn', [search_type]]}
                ]
            }

            options = {
                'return': ['id'] + return_list,
                'platform': platform,
            }
            result = client.call(uri.ak_wwise_core_object_get, args, options=options)
            if result and 'return' in result:
                return result['return']

    except Exception as e:
        print(f'运行错误：{e}')

    return []


def go_to(guid):
    '''在Wwise UI中定位对象'''
    try:
        with WaapiClient() as client:
            args = {
                'command': 'FindInProjectExplorerSelectionChannel1',
                'objects': [guid]
            }
            result = client.call(uri.ak_wwise_ui_commands_execute, args)
            return result

    except Exception as e:
        print(f'运行错误：{e}')

    return None


if __name__ == '__main__':
    # search('amb', 'Sound', 'Windows', ['id', 'name', 'Volume', 'type'])
    print(get_paltforms())
