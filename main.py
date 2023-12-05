from PySide6 import QtWidgets,QtGui
import sys
from Gui import FileZone as fz
from Gui import DnsZone as dz
from Gui import HostZone as hz
from Gui import FormatCheck as fc
from Gui import ClashZone as cz
from jsProcess import MergeJson as mj
import global_var as glv
glv._init()
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.initui()
    def initui(self):
        self.vmainbox = QtWidgets.QVBoxLayout()
        self.vleftbox = QtWidgets.QVBoxLayout()
        self.vrightbox = QtWidgets.QVBoxLayout()
        self.hinfobox = QtWidgets.QHBoxLayout()
        self.hbuttonbox = QtWidgets.QHBoxLayout()

        self.confirm = QtWidgets.QPushButton("确认")
        self.quit = QtWidgets.QPushButton("退出")
        self.file_drop = fz.FileZone()
        self.dns_zone = dz.DnsField()
        self.host_zone = hz.HostField()
        self.clash_zone = cz.ClashField()
        self.confirm.clicked.connect(self.processText)
        self.quit.clicked.connect(self.closeApp)

        self.vleftbox.addWidget(self.file_drop)
        self.vleftbox.addWidget(self.dns_zone)

        self.vrightbox.addWidget(self.host_zone)
        self.vrightbox.addWidget(self.clash_zone)

        self.hinfobox.addLayout(self.vleftbox)
        self.hinfobox.addLayout(self.vrightbox)

        self.hbuttonbox.addWidget(self.confirm)
        self.hbuttonbox.addWidget(self.quit)

        self.vmainbox.addLayout(self.hinfobox)
        self.vmainbox.addLayout(self.hbuttonbox)


        self.setLayout(self.vmainbox)
        
    def closeApp(self):
        self.close()
    def processText(self):
        save_path = QtWidgets.QFileDialog.getExistingDirectory()
        if glv.get_value("nodes"):
            key,path,port = self.ProcessClash()
            if self.host_zone.hostinfo.toPlainText():
                hosts = fc.FormatCheck(self.host_zone.hostinfo.toPlainText())
                if hosts[0]:
                    hosts_info = fc.ProcessHost(hosts[1:])
                    dns_list,ttl = self.ProcessDNS()
                    finished = mj.SaveJsonFile(self.file_drop.yaml_path,
                                                save_path,
                                                dns_list,ttl,
                                                hyjack=True,domains=hosts_info[0],ips=hosts_info[1],ports=hosts_info[2],
                                                uikey=key,uiport=port,uiurl=path)
                else:
                    self.error_message = QtWidgets.QErrorMessage()
                    self.error_message.setWindowTitle("错误提示")
                    self.error_message.showMessage(f"格式错误:{hosts[1]}")
            else:
                dns_list,ttl = self.ProcessDNS()
                finished = mj.SaveJsonFile(save_path,dns_list,ttl,hyjack=False,
                                           uikey=key,uiport=port,uiurl=path)
            if finished:
                message_box = QtWidgets.QMessageBox(self)
                message_box.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                message_box.setWindowTitle("完成提示框")
                message_box.setText("完成")
                message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
                message_box.open()
        else:
            self.error_message = QtWidgets.QErrorMessage()
            self.error_message.setWindowTitle("错误提示")
            self.error_message.showMessage(f"没有有效文件")
    def ProcessDNS(self):
        dnslist = [True]*3
        if bool(self.dns_zone.lcoal_dns.text()):
            dnslist[2] = self.dns_zone.local_dns.text()
        else:
            dnslist[2] = 'https://223.5.5.5/dns-query'
        if bool(self.dns_zone.remote_dns.text()):
            dnslist[0] = self.dns_zone.remote_dns.text()
        else:
            dnslist[0] = 'https://8.8.8.8/dns-query'        
        if bool(self.dns_zone.proxy_dns.text()):
            dnslist[1] = self.dns_zone.proxy_dns.text()
        else:
            dnslist[1] = 'https://1.1.1.1/dns-query'
        if bool(self.dns_zone.ttl_line.text()):
            ttl = int(self.dns_zone.ttl_line.text())*3600
        else:
            ttl = 3600*12            
        return dnslist,ttl
    def ProcessClash(self):
        if self.clash_zone.keyline.text():
            key = self.clash_zone.keyline.text()
        else:
            key = 123456
        if self.clash_zone.pathline.text():
            path = self.clash_zone.pathline.text()
        else:
            path = "ui"
        if self.clash_zone.portline.text():
            port = int(self.clash_zone.portline.text())
        else:
            port = 9090
        return key,path,port

if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MainWindow()  # 实例化一个MyWidget类对象
    widget.setWindowIcon(QtGui.QIcon(r".\static\icon.ico"))
    widget.show()  # 显示窗口
    sys.exit(app.exec()) 