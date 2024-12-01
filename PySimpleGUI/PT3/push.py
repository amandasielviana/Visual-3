import PySimpleGUI as sg
sg.theme("DarkBlue")
sg.theme_text_color("#f8f3c9")
susunan=[[sg.Push(),
        sg.Text("UNISKA MAAB", font=("Helvetica", 24)), sg.Push()],
        [sg.Push(),
        sg.Text("BANJARMASIN", font=("Courier", 18)), sg.Push()]
        ]
window = sg.Window(title="Elemen Teks", layout=susunan,
                                size=(430,200))
window()
window.close()