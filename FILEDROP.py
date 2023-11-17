from PySide6 import QtCore, QtWidgets
import re
class PathField(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.yaml_path = False
        self.setAcceptDrops(True)
        self.initUI()
    def initUI(self):
        self.drop_field = QtWidgets.QLabel("文件拖入这里")
        self.drop_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.drop_field)
        self.setLayout(self.hbox)
    def dropEvent(self, event):
        if len(event.mimeData().urls()) > 1:
            self.error_message = QtWidgets.QErrorMessage()
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage("拖入了多个文件")
        elif re.split("\.",event.mimeData().urls()[0].toLocalFile())[-1] == "yaml" or re.split("\.",event.mimeData().urls()[0].toLocalFile())[-1] == "yml":
            self.yaml_path = event.mimeData().urls()[0].toLocalFile()
        else:
            self.error_message = QtWidgets.QErrorMessage(self)
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage("不是yaml或yml文件")
    def dragEnterEvent(self, event):
        event.accept()