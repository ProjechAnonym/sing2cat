from PySide6 import QtWidgets
import FILEDROP as FD
import DNSZONE as DZ
import HOSTZONE as HZ
import CHECKFUNCTION as CF
import INTEGERATE
import sys

class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("clash2singbox配置文件程序")
        self.resize(800, 600)
        self.initUI()
    def initUI(self):      
        self.filedrop = FD.PathField()
        self.dnsfield = DZ.DnsField()
        self.hostfield = HZ.HostField()
        self.confirm = QtWidgets.QPushButton("确认")
        self.quit = QtWidgets.QPushButton("退出")

        self.quit.clicked.connect(self.CloseApp)
        self.confirm.clicked.connect(self.processText)

        self.v1box = QtWidgets.QVBoxLayout()
        self.v2box = QtWidgets.QVBoxLayout()
        self.h1box = QtWidgets.QHBoxLayout()
        self.h2box = QtWidgets.QHBoxLayout()

        self.v1box.addWidget(self.filedrop)
        self.v1box.addWidget(self.dnsfield)

        self.h1box.addLayout(self.v1box)
        self.h1box.addWidget(self.hostfield)

        self.h2box.addWidget(self.confirm)
        self.h2box.addWidget(self.quit)

        self.v2box.addLayout(self.h1box)
        self.v2box.addLayout(self.h2box)
        self.setLayout(self.v2box)
    def CloseApp(self):
        self.close()
    def processText(self):
        savepath = QtWidgets.QFileDialog.getExistingDirectory()
        if self.filedrop.yaml_path:
            if self.hostfield.hostinfo.toPlainText():
                host = CF.FormatCheck(self.hostfield.hostinfo.toPlainText())
                if host[0]:
                    hostinfos = CF.processHOST(host[1:])
                    dnslist = self.checkDNS()
                    finished = INTEGERATE.GenerateJsonFile(self.filedrop.yaml_path,
                                                savepath,
                                                dnslist,
                                                hyjack=True,domains=hostinfos[0],ips=hostinfos[1],ports=hostinfos[2])
                else:
                    self.error_message = QtWidgets.QErrorMessage()
                    self.error_message.setWindowTitle("错误提示")
                    self.error_message.showMessage(f"格式错误:{host[1]}")
            else:
                dnslist = self.checkDNS()
                finished = INTEGERATE.GenerateJsonFile(self.filedrop.yaml_path,savepath,dnslist,hyjack=False)
            if finished:
                message_box = QtWidgets.QMessageBox(self)
                message_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                message_box.setWindowTitle("这是一个消息提示框")
                message_box.setText("完成")
                message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
                message_box.open()
        else:
            self.error_message = QtWidgets.QErrorMessage()
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage(f"没有拖入文件")
    def checkDNS(self):
        dnslist = [True]*3
        if bool(self.dnsfield.lcoal_dns.text()):
            dnslist[0] = self.dnsfield.lcoal_dns.text()
        else:
            dnslist[0] = 'https://223.5.5.5/dns-query'
        if bool(self.dnsfield.remote_dns.text()):
            dnslist[1] = self.dnsfield.lcoal_dns.text()
        else:
            dnslist[1] = 'https://8.8.8.8/dns-query'        
        if bool(self.dnsfield.proxy_dns.text()):
            dnslist[2] = self.dnsfield.lcoal_dns.text()
        else:
            dnslist[2] = 'https://1.1.1.1/dns-query'        
        return dnslist
if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MainWindow()  # 实例化一个MyWidget类对象
    widget.show()  # 显示窗口
    sys.exit(app.exec()) 
