import PySimpleGUI as sg
import datetime
sg.theme("LightBrown8")

layout = [[sg.T("00:00:00", font=("Arial", 24), k="txt1")],
               [sg.ML(font=("Arial", 18), size=(40, 12), k="txt2")]]
win = sg.Window("時間割アプリ", layout,
                            font=(None,14), size=(450, 260), keep_on_top=True)

sch = [["1時限", 8, 50],
           ["2時限", 10, 30],
           ["昼休み", 12, 40],
           ["3時限", 13, 20],
           ["4時限", 15, 10],
           ["5時限", 17, 00],
           ["6時限", 18, 50]]

def execute():
    now = datetime.datetime.now()
    now = now.replace(hour=10)
    win["txt1"].update(f"{now:%H:%M:%S}")
    txt2 = ""
    for s in sch:
        dt = now.replace(hour=s[1], minute=s[2], second=0) - now
        if dt.total_seconds() > 0:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】あと {dt}です。\n"
        else:
            txt2 += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】---\n"
    win["txt2"].update(txt2)

while True:
    e, v = win.read(timeout=500)
    if e == None:
        break
    execute()
win.close()
