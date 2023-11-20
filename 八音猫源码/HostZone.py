from PySide6 import QtCore, QtWidgets

class HostField(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tag = False
        self.initui()
    def initui(self):
        self.hostinfo = QtWidgets.QPlainTextEdit()
        self.hostinfo.setPlaceholderText("格式:域名,IP,端口.使用逗号分割,多个域名劫持请换行\n如clash.com,192.168.50.1,9090\nadhome.com,192.168.50.1,3000")
        self.hostinfo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.custom_host = QtWidgets.QRadioButton("是否启用HOST劫持")
        self.custom_host.toggled.connect(self.SetEditLine)
        
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.custom_host)
        self.vbox.addWidget(self.hostinfo)
        self.setLayout(self.vbox)
        
        self.SetEditLine()

    def SetEditLine(self):
            if self.tag:
                self.hostinfo.setDisabled(False)
                self.tag = False
            else:
                self.hostinfo.setDisabled(True)
                self.tag = True