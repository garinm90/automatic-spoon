import sys
#from PyQt5.QtWidgets import QApplication, QDialog
from GUI import Ui_MainWindow, QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())