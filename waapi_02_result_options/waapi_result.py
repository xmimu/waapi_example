from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    with WaapiClient() as client:
        result = client.call('ak.wwise.core.getInfo')
        # pprint(result)

        display_name = result['displayName']
        pprint(display_name)

        version_name = result['version']['displayName']
        pprint(version_name)


except CannotConnectToWaapiException:
    print('连接 WAAPI 失败！')