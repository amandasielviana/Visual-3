#QtGUI QTCore QtWidgets
#Cara1
from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QPushButton("MyButton")
window.show()
app.exec_()

#cara2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()

#cara3
from PyQt5 import QtWidgets as qtw

app = qtw.QApplication([])
window = qtw.QPushButton("MyButton")
window.show()
app.exec_()

#cara4_recommended
from PyQt5.QtWidgets import QApplication, QPushButton
app = QApplication([])
window = QPushButton("MyButton")
window.show()
app.exec_()