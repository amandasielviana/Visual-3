import PySimpleGUI as sg
sg.theme("DarkBlue")
sg.theme_text_color("#f8f3c9")
window = sg.Window(title="Profile", layout=[[sg.Text("SELAMAT DATANG DI KELAS", font=("Cambria", 25, "italic", "bold", "underline"))],
                                            [sg.Text("Nama    : Jamilatuzzahra")],
                                            [sg.Text("NPM     : 2210010033")],
                                            [sg.Text("Kelas   : 5M TI Reg BJM")],
                                            [sg.Text("Matkul  : Pemrograman Visual 3")],
                                            [sg.Text("FTI UNISKA")],
                                            [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                                            [sg.Text("UNISKA MAB BANJARMASIN")]], size=(510,300), font=("Times", 16))
window()
window.close()