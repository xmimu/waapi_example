from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri

args = {
    'importOperation': 'replaceExisting',
    'default': {
        'importLanguage': 'SFX',  # sound 对象
        'originalsSubFolder': 'Bird',
    },
    'imports': []
}

# 创建音频对象 根据你的实际路径填写
for i in range(1, 7):
    args['imports'].append({
        'audioFile': "C:\\Users\\11015\\Desktop\\live_project\\" + f"bird-00{i}.wav",
        'objectPath': '\\Actor-Mixer Hierarchy\\Default Work Unit\\New Virtual Folder\\New Actor-Mixer\\<Sound>sfx_bird_0' + str(i),
        'event': f'\\Events\\Default Work Unit\\New Virtual Folder\\stop_sfx_bird_0{i}@Stop',
    })

with WaapiClient() as client:
    result = client.call(uri.ak_wwise_core_audio_import, args)
    print(result)
