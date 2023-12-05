from PySide6 import QtCore, QtWidgets
from jsProcess.OutModule import loadNodes
from jsProcess.OutModule import downloadNodes
import global_var as glv
import re
class FileZone(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.yaml_path = False
        self.setAcceptDrops(True)
        self.initUI()
    def initUI(self):
        self.drop_field = QtWidgets.QLabel("文件拖入这里")
        self.drop_field.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.scrollbar = QtWidgets.QScrollArea()
        self.scrollbar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollbar.setWidgetResizable(True)
        self.url_zone = QtWidgets.QLineEdit()
        self.download_button = QtWidgets.QPushButton("下载")
        self.download_button.clicked.connect(self.download_nodes)

        self.vmainbox = QtWidgets.QVBoxLayout()
        self.hlabelbox = QtWidgets.QHBoxLayout()

        self.hlabelbox.addWidget(self.url_zone)
        self.hlabelbox.addWidget(self.download_button)
        self.scrollbar.setWidget(self.drop_field)
        self.vmainbox.addLayout(self.hlabelbox)
        self.vmainbox.addWidget(self.scrollbar)
        
        self.setLayout(self.vmainbox)
    def dropEvent(self, event):
        if len(event.mimeData().urls()) > 1:
            self.error_message = QtWidgets.QErrorMessage()
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage("拖入了多个文件")
        elif re.split("\.",event.mimeData().urls()[0].toLocalFile())[-1] == "yaml" or re.split("\.",event.mimeData().urls()[0].toLocalFile())[-1] == "yml":
            self.yaml_path = event.mimeData().urls()[0].toLocalFile()
            text_content = self.yaml_path
            # nodes = loadNodes(self.yaml_path)
            glv.set_value("nodes",loadNodes(self.yaml_path))
            for node in glv.get_value("nodes"):
                text_content = text_content + "\n节点名称:" + node['name'] + ",协议类型:" + node["type"]   
            self.drop_field.setText(text_content)
        else:
            self.error_message = QtWidgets.QErrorMessage(self)
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage("不是yaml或yml文件")
    def dragEnterEvent(self, event):
        event.accept()
    def download_nodes(self):
        if self.url_zone.text:
            print(self.url_zone.text())
            download_nodes = downloadNodes(self.url_zone.text())
            if not download_nodes:
                self.error_message = QtWidgets.QErrorMessage(self)
                self.error_message.setWindowTitle("错误提示")
                self.error_message.showMessage("下载失败")
            else:
                glv.set_value("nodes",download_nodes)
                text_content = self.url_zone.text()
                for node in glv.get_value("nodes"):
                    text_content = text_content + "\n节点名称:" + node['name'] + ",协议类型:" + node["type"]   
                self.drop_field.setText(text_content)
                self.setAcceptDrops(False)

