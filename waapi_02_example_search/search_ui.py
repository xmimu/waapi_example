import FreeSimpleGUI as sg  # 导入GUI库
from search_core import search, get_paltforms, go_to  # 导入核心搜索功能

# 支持的对象类型列表
object_types = [
    'ActorMixer',
    'AudioFileSource',
    'BlendContainer',
    'Bus',
    'Effect',
    'Event',
    'Folder',
    'GameParameter',
    'MusicSegment',
    'MusicSwitchContainer',
    'RandomContainer',
    'Sound',
    'State',
    'SwitchContainer',
    'Trigger']

# 获取平台列表，若获取失败则使用默认平台
platforms = get_paltforms() or ['Windows', 'PS4', 'Switch', 'iOS', 'Android']

# 定义窗口布局
layout = [
    [sg.Button('搜索', k='-Search-'), sg.Input(k='-Input-')],  # 搜索按钮和输入框
    [sg.Text('类型:'), sg.Combo(object_types, default_value=object_types[0], k='-ComboTypes-', readonly=True),
     sg.Text('平台:'), sg.Combo(platforms, default_value=platforms[0], k='-ComboPlatforms-', readonly=True), ],  # 类型和平台选择
    [sg.Text('返回属性:'), sg.Input('id name', k='-ReturnList-')],  # 返回属性输入框
    [sg.Listbox(values=[], size=(100, 30), k='-ListBox-', expand_x=True, expand_y=True, enable_events=True)],  # 结果列表框
]

# 创建窗口
window = sg.Window('对象搜索', layout, size=(800, 600), resizable=True, keep_on_top=True)

# 主事件循环
while True:
    event, values = window.read()  # 读取事件和输入值
    print(event, values)  # 打印事件和输入值，便于调试
    if event == sg.WIN_CLOSED:  # 用户关闭窗口
        break
    if event == '-Search-':  # 用户点击搜索按钮
        text = values['-Input-'].strip()  # 获取搜索内容
        if not text:
            print('请输入搜索内容')  # 未输入内容时提示
            continue
        search_type = values['-ComboTypes-']  # 获取选择的类型
        platform = values['-ComboPlatforms-']  # 获取选择的平台
        return_list = values['-ReturnList-'].strip().split(' ')  # 获取返回属性列表
        # print(text, search_type, platform, return_list)

        result = search(text, search_type, platform, return_list)  # 执行搜索
        window['-ListBox-'].update(values=result)  # 更新结果列表

    if event == '-ListBox-':  # 用户点击结果列表项
        item = values['-ListBox-']
        if item:
            object_id = item[0]['id']  # 获取选中对象的id
            go_to(object_id)  # 跳转到对象

window.close()  # 关闭窗口
