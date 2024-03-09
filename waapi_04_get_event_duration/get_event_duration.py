"""
需求：
    获取 Wwise 内 所有 Event - Duration 对应关系
    支持按名称搜索过滤 Event
    不论 Event 指定到什么类型的容器，都找到对应的播放时长
    不论 Target 容器内有多少声音，都找到最长的时间，并作为最终结果
"""
import sys
from pathlib import Path
# 添加本地模块路径，也就是 waapi_example 目录
sys.path.append(str(Path(__file__).parent.parent))

from pprint import pprint

from waapi_support import WaapiClientX, WaapiObject, QuerySelect, QueryWhere
from waapi_support.waapi_opt_return import *


def get_event_data(client: WaapiClientX, search_name: str = ''):
    event_data = []
    # 获取所有Event类型的对象
    events = client.get_from_type(WaapiObject.Event, return_list=[rt_workunit])
    for event_obj in events:
        event_name = event_obj[rt_name]
        event_duration = 0.00  # 设置初始化变量，用于更新最大值
        # 通过 search_name 过滤指定名字范围，包含关系，忽略大小写
        if not search_name.lower() in event_name.lower(): continue
        # 获取 Event 下所有的 Action
        actions = client.get(
            event_obj[rt_id],
            QuerySelect.children,
            QueryWhere.type_is(WaapiObject.Action),
            return_list=['ActionType', '@Target']
        )
        # 遍历 Action 查找对应 Target
        for action_obj in actions:
            # 只处理 Play 类型的 Action，ActionType 1 = Play
            if action_obj['ActionType'] != 1: continue
            # 判断是否存在 Target
            if '@Target' not in action_obj: continue
            # 检查 Target 对应的容器类型
            target_id = action_obj['@Target'][rt_id]
            # 判断 Target ID 有效性
            if target_id == '{00000000-0000-0000-0000-000000000000}': continue
            # 找 Target 对象下面的所有 AudioFileSource 类型
            sources = client.get(
                target_id,
                QuerySelect.descendants,
                QueryWhere.type_is(WaapiObject.AudioFileSource),
                return_list=[rt_playbackDuration]
            )
            if not sources:
                print('没有 AudioFileSource', client.get(target_id)[0][rt_name])
                continue
            # 取所有 AudioFileSource 对象，取最大的时间
            source_duration = max(
                [i[rt_playbackDuration]['playbackDurationMax']
                 for i in sources if rt_playbackDuration in i]
            )
            # 同一个 Event 下，根据每个 Action 更新最大时间
            event_duration = max(source_duration, event_duration)
        # 添加当前 Event 时长数据到列表
        event_data.append({'event_name': event_name, 'event_duration': event_duration})
        print(len(event_data), event_name, event_duration)

    return event_data


def main():
    try:
        with WaapiClientX() as client:
            event_data = get_event_data(client)
            pprint(event_data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()