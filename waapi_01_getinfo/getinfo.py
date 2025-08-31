from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

from waapi_uri import WAAPI_URI as uri


def get_wwise_info():
    try:
        with WaapiClient() as client:
            result = client.call(uri.ak_wwise_core_getinfo)
            # pprint(result)
            print('当前Wwise平台', result['platform'])
            print('Wwise 版本号', result['version']['displayName'])
            print('执行文件路径', result['processPath'])

            result = client.call(uri.ak_wwise_core_getprojectinfo)
            # pprint(result)
            print('当前Wwise工程名称', result['name'])
            print('当前Wwise工程路径', result['path'])
            for i in result['platforms']:
                print('当前Wwise工程支持平台', i['name'])
            for i in result['languages']:
                print('当前Wwise工程支持语言', i['name'])
            print('SoundBank生成目录', result['directories']['soundBankOutputRoot'])
            print('音频资源目录', result['directories']['originals'])

    except CannotConnectToWaapiException:
        print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")


if __name__ == '__main__':
    get_wwise_info()
