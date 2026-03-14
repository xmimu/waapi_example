import FreeSimpleGUI as sg  # 导入GUI库

from waapi import WaapiClient
from waapi_uri import WAAPI_URI as uri

def run_waql(input_text: str, return_list: list[str]) -> None:
    with WaapiClient() as client:
        waql_query = input_text.strip() # 去除首尾空格
        args = {
            "waql": waql_query,
            "options": {"return": return_list}
        }
        result = client.call(uri.ak_wwise_core_object_get, args)
        print(result)


# 定义窗口布局
layout = [
    [sg.Text('WAQL 查询：'), sg.InputText(k='-WAQL-')],
    [sg.Text('返回列表：'), sg.InputText(k='-RETURN_LIST-')],

    [sg.Button('搜索', k='-Search-')],
    [sg.Text('返回结果：')],
    [sg.Output(size=(80, 20), k='-Output-')]
]

# 创建窗口
window = sg.Window('WAQL 查询工具', layout, size=(800, 600), resizable=True, keep_on_top=True)

# 主事件循环
while True:
    event, values = window.read()  # 读取事件和输入值
    print(event, values)  # 打印事件和输入值，便于调试
    if event == sg.WIN_CLOSED:  # 用户关闭窗口
        break
    if event == '-Search-':
        run_waql(values['-WAQL-'], values['-RETURN_LIST-'].split(' '))

window.close()  # 关闭窗口
