from typing import Optional
from PySide6 import QtWidgets
import PySide6.QtCore
import PySide6.QtWidgets
class ClashField(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.key = False
        self.port = False
        self.path = False
        self.initui()
    def initui(self):
        self.hmainbox = QtWidgets.QHBoxLayout()
        self.vkeybox = QtWidgets.QVBoxLayout()
        self.vportbox = QtWidgets.QVBoxLayout()
        self.vpathbox = QtWidgets.QVBoxLayout()

        self.keygroup = QtWidgets.QButtonGroup()
        self.keybutton = QtWidgets.QRadioButton("自定义密码")
        self.keybutton.toggled.connect(self.KeyEditLine)
        self.keygroup.addButton(self.keybutton)
        self.keygroup.setExclusive(False)

        self.pathgroup = QtWidgets.QButtonGroup()
        self.pathbutton = QtWidgets.QRadioButton("自定义路径")
        self.pathgroup.addButton(self.pathbutton)
        self.pathbutton.toggled.connect(self.PathEditLine)
        self.pathgroup.setExclusive(False)

        self.portgroup = QtWidgets.QButtonGroup()
        self.portbutton = QtWidgets.QRadioButton("自定义端口")
        self.portbutton.toggled.connect(self.PortEditLine)
        self.portgroup.addButton(self.portbutton)
        self.portgroup.setExclusive(False)

        self.keyline = QtWidgets.QLineEdit()
        self.keyline.setPlaceholderText("默认123456")
        self.pathline = QtWidgets.QLineEdit()
        self.pathline.setPlaceholderText("默认ui")
        self.portline = QtWidgets.QLineEdit()
        self.portline.setPlaceholderText("默认9090")

        self.vkeybox.addWidget(self.keybutton)
        self.vkeybox.addWidget(self.keyline)
        self.vpathbox.addWidget(self.pathbutton)
        self.vpathbox.addWidget(self.pathline)
        self.vportbox.addWidget(self.portbutton)
        self.vportbox.addWidget(self.portline)

        self.hmainbox.addLayout(self.vkeybox)
        self.hmainbox.addLayout(self.vpathbox)
        self.hmainbox.addLayout(self.vportbox)
        self.setLayout(self.hmainbox)

        self.KeyEditLine()
        self.PortEditLine()
        self.PathEditLine()
    def KeyEditLine(self):
        if self.key:
            self.keyline.setDisabled(False)
            self.key = False
        else:
            self.keyline.setDisabled(True)
            self.key = True
    def PathEditLine(self):
        if self.path:
            self.pathline.setDisabled(False)
            self.path = False
        else:
            self.pathline.setDisabled(True)
            self.path = True
    def PortEditLine(self):
        if self.port:
            self.portline.setDisabled(False)
            self.port = False
        else:
            self.portline.setDisabled(True)
            self.port = True        