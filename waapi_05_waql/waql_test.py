from waapi import WaapiClient

with WaapiClient() as client:
    waql_query = '$ from type Event where name:"Play"'
    args = {
        "waql": waql_query,
        "options": {"return": ["id", "name", "type", 'notes']}
    }
    result = client.call("ak.wwise.core.object.get", args)
    print(result)
