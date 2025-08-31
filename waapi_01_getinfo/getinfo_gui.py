import FreeSimpleGUI as sg

from getinfo import get_wwise_info

layout = [
    [sg.Button('获取信息', k='-Run-')],
    [sg.Output(size=(100, 20), k='-Output-', wrap_lines=False, expand_x=True, expand_y=True)]
]

window = sg.Window('Wwise信息获取', layout, size=(500, 300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-Run-':
        print('获取Wwise信息中...')
        get_wwise_info()

window.close()
