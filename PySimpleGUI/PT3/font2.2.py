import PySimpleGUI as sg
sg.theme("DarkBlue")
sg.theme_text_color("#f8f3c9")
window = sg.Window(title="Profile", layout=[[sg.Text("FTI UNISKA", font=("Helvetica", 24))],
                                            [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                                            [sg.Text("UNISKA MAB BANJARMASIN")]], size=(450,150), font=("Times", 16))
window()
window.close()