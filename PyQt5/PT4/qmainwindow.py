#menggunakan QMainWindow

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()
#cara 1 -> QLabel("Label", window)
label = QLabel(window) #cara2
label.setText("label1")
label.move(200, 0)

#button = QPushButton("MyButton", window) -> cara1
button = QPushButton(window) #cara2
button.setText("Button1")

window.show()
app.exec_()