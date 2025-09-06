from waapi import WaapiClient
import pprint

try:
    with WaapiClient() as client:
        args = {
            'from': {'search': ['amb']},
            'transform': [
                # {'select': ['children']},
                {'where': ['type:isIn', ['Event', 'Sound']]}
            ]
        }

        options = {
            'return': ['id', 'name', 'type', 'isIncluded'],
            'platform': 'Windows',
        }
        result = client.call("ak.wwise.core.object.get", args, options=options)
        pprint.pprint(result)

except Exception as e:
    print(f'运行错误：{e}')
