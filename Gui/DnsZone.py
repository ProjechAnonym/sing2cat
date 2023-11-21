from PySide6 import QtWidgets
class DnsField(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()
        self.tag = False
        self.initui()
        
    def initui(self):
        
        self.custom_dns = QtWidgets.QRadioButton("是否启用自定义DNS")
        self.custom_dns.toggled.connect(self.SetEditLine)
        
        self.ttl_line = QtWidgets.QLineEdit()
        self.ttl_line.setPlaceholderText("单位:h,默认12h")

        self.button_zone = QtWidgets.QHBoxLayout()
        self.button_zone.addWidget(self.custom_dns)
        self.button_zone.addWidget(self.ttl_line)

        self.lcoal_dns_label = QtWidgets.QLabel("国内dns服务器")
        self.lcoal_dns = QtWidgets.QLineEdit()
        self.lcoal_dns.setPlaceholderText("尽量加密的dns服务器,如https://223.5.5.5/dns-query")
        
        self.remote_dns_label = QtWidgets.QLabel("国外dns服务器")
        self.remote_dns = QtWidgets.QLineEdit()
        self.remote_dns.setPlaceholderText("尽量加密的dns服务器,如https://8.8.8.8/dns-query")
        
        self.proxy_dns_label = QtWidgets.QLabel("查询节点IP的dns服务器")
        self.proxy_dns = QtWidgets.QLineEdit()
        self.proxy_dns.setPlaceholderText("尽量选用加密的dns服务器,如https://1.1.1.1/dns-query")
        
        self.vmainbox = QtWidgets.QVBoxLayout()
        self.addWidgets()
        self.SetEditLine()
        self.setLayout(self.vmainbox)
    def addWidgets(self):
        self.vmainbox.addLayout(self.button_zone)
        self.vmainbox.addWidget(self.lcoal_dns_label)
        self.vmainbox.addWidget(self.lcoal_dns)
        self.vmainbox.addWidget(self.remote_dns_label)
        self.vmainbox.addWidget(self.remote_dns)
        self.vmainbox.addWidget(self.proxy_dns_label)
        self.vmainbox.addWidget(self.proxy_dns)
    def SetEditLine(self):
        if self.tag:
            self.lcoal_dns.setDisabled(False)
            self.remote_dns.setDisabled(False)
            self.proxy_dns.setDisabled(False)
            self.ttl_line.setDisabled(False)
            self.tag = False
        else:
            self.lcoal_dns.setDisabled(True)
            self.remote_dns.setDisabled(True)
            self.proxy_dns.setDisabled(True)
            self.ttl_line.setDisabled(True)
            self.tag = True