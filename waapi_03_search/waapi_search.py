from waapi import WaapiClient, CannotConnectToWaapiException

from pprint import pprint


try:
    with WaapiClient() as client:
        args = {
            # 从 什么位置 开始查找， id, name, search, path, ofType
            'from': {'id': ['{2177E4DF-435F-413B-B2DF-F0223EDCF7B4}']},
            # 过滤
            'transform': [
                # 选择哪些内容, parent, children, descendants, ancestors, referencesTo
                {'select': ['parent']},
                # 要符合什么条件, name:contains,name:matches, type:isIn, category:isIn
                {'where': ['name:contains', 'ii']}
            ]
        }
        # 查找到的对象，返回什么属性
        options = {'return': ['id', 'name', 'path', 'type']}
        result = client.call('ak.wwise.core.object.get',
                             args, options=options)
        pprint(result)


except CannotConnectToWaapiException:
    print('CannotConnectToWaapiException')
