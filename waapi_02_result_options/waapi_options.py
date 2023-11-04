from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

try:
    with WaapiClient() as client:
        options = {
            'return': [
                'id',
                'name',
                'notes',
                'type',
                'pluginName',
                'shortId',
                'classId',
                'category',
                'filePath',
                'workunit',
                'parent',
                'owner',
                'path',
                'isPlayable',
                'childrenCount',
                'totalSize',
                'mediaSize',
                'objectSize',
                'structureSize',
                'sound:convertedWemFilePath',
                'sound:originalWavFilePath',
                'soundbank:bnkFilePath',
                'music:transitionRoot',
                'music:playlistRoot',
                'audioSource:playbackDuration',
                'audioSource:maxDurationSource',
                'audioSource:trimValues',
                'audioSource:maxRadiusAttenuation',
                'audioSource:language',
                'workunit:isDefault',
                'workunit:type',
                'workunit:isDirty',
                'switchContainerChild:context',
                'convertedWemFilePath',
                'originalFilePath',
                'convertedFilePath',
                'originalWavFilePath',
                'soundbankBnkFilePath',
                'musicTransitionRoot',
                'musicPlaylistRoot',
                'playbackDuration',
                'duration',
                'maxDurationSource',
                'audioSourceTrimValues',
                'maxRadiusAttenuation',
                'audioSourceLanguage',
                'workunitIsDefault',
                'workunitType',
                'workunitIsDirty',
                'switchContainerChildContext',
                'isExplicitMute',
                'isExplicitSolo',
                'isImplicitMute',
                'isImplicitSolo',
                'points'
            ]
        }

        result = client.call('ak.wwise.ui.getSelectedObjects', options=options)
        pprint(result)

        # for i in result['objects']:
        #     pprint(i['type'])


except CannotConnectToWaapiException:
    print('连接 WAAPI 失败！')
