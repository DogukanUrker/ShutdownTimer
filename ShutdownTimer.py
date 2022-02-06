import platform
from sys import argv
from os import system
from PyQt5.QtCore import QPoint, QCoreApplication, Qt
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox, QApplication, QWidget
def alert(text):
    message = QMessageBox()
    message.setText(str(text))
    message.setStandardButtons(QMessageBox.Ok)
    message.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
    message.setGeometry(875, 400, 0, 0)
    ret = message.exec_()
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 400, 270, 200)
        self.setWindowTitle("Shutdown Timer")
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.dragPos = QPoint()
        self.ui()
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
    def ui(self):
        self.ok = QPushButton("Start", self)
        self.hours = QLineEdit("", self)
        self.minutes = QLineEdit("", self)
        self.hours_text = QLabel("Hours:", self)
        self.minutes_text = QLabel("Minutes:", self)
        self.exit = QPushButton("", self)
        self.minimized = QPushButton("", self)
        self.abort = QPushButton("Abort", self)
        self.shutdown = QRadioButton("Shutdown", self)
        self.restart = QRadioButton("  Restart", self)
        self.shutdown.setObjectName("shutdown")
        self.restart.setObjectName("restart")
        self.abort.setObjectName("abort")
        self.ok.setObjectName("start")
        self.exit.setObjectName("exit")
        self.minimized.setObjectName("minimized")
        self.exit.setGeometry(245, 3, 20, 20)
        self.minimized.setGeometry(220, 3, 20, 20)
        self.hours.setGeometry(10, 45, 150, 30)
        self.hours_text.setGeometry(10, 25, 300, 20)
        self.minutes.setGeometry(10, 100, 150, 30)
        self.minutes_text.setGeometry(10, 80, 300, 20)
        self.restart.setGeometry(175, 70, 85, 30)
        self.shutdown.setGeometry(175, 40, 85, 30)
        self.ok.setGeometry(10, 135, 120, 60)
        self.abort.setGeometry(140, 135, 120, 60)
        self.ok.clicked.connect(self.process)
        self.abort.clicked.connect(self.shutdown_cancel)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.minimized.clicked.connect(lambda: self.showMinimized())
        self.shutdown.setChecked(True)
    def process(self):
        hours = self.hours.text()
        minutes = self.minutes.text()
        def operation(command, minutes, hours):
            if platform.system() == "Windows":
                if not hours or hours.isspace():
                    time = int(minutes) * 60
                    system("shutdown {} {}".format(command, time))
                elif not minutes or minutes.isspace():
                    time = int(hours) * 60 * 60
                    system("shutdown {} {}".format(command, time))
                else:
                    time = int(hours) * 60 * 60 + int(minutes) * 60
                    system("shutdown {} {}".format(command, time))
            elif platform.system() == "Linux":
                if not hours or hours.isspace():
                    time = int(minutes)
                    system("shutdown {} {}".format(command, time))
                    if command == "-h":
                        alert("Your computer shutdown in {} minutes".format(time))
                    elif command == "-r":
                        alert("Your computer restart in {} minutes".format(time))
                elif not minutes or minutes.isspace():
                    time = int(hours) * 60
                    system("shutdown {} {}".format(command, time))
                    if command == "-h":
                        alert("Your computer shutdown in {} minutes".format(time))
                    elif command == "-r":
                        alert("Your computer restart in {} minutes".format(time))
                else:
                    time = int(hours) * 60 + int(minutes)
                    system("shutdown {} {}".format(command, time))
                    if command == "-h":
                        alert("Your computer shutdown in {} minutes".format(time))
                    elif command == "-r":
                        alert("Your computer restart in {} minutes".format(time))
        try:
            if platform.system() == "Windows":
                if self.shutdown.isChecked():
                    operation("-s -f -t", minutes, hours)
                elif self.restart.isChecked():
                    operation("/r /t", minutes, hours)
            elif platform.system() == "Linux":
                if self.shutdown.isChecked():
                    operation("-h", minutes, hours)
                elif self.restart.isChecked():
                    operation("-r", minutes, hours)
        except:
            alert("Please check the values")
    def shutdown_cancel(self):
        if platform.system() == "Windows":
            system("shutdown -a")
        elif platform.system() == "Linux":
            system("shutdown -c")
            alert("Shutdown schedule is cancelled")
app = QApplication(argv)
Window = Window()
Window.show()
app.setStyleSheet("""
* {
  font-family: Arial, Helvetica, sans-serif;
}
#start {
  background: #34C759;
}
#start:hover {
  background: #30D158;
}
#abort {  
  background: #FF3B30;
}
#abort:hover {
  background: #FF453A;
}
#shutdown, #restart{
    border-radius: 10px;
    text-align: center;
}
#exit{
  border-radius: 10px;
  background: #FF453A;
}
#exit:hover{
  background: #FF3B30;
}
#minimized{
  border-radius: 10px;
  background: #FFCC00;
}
#minimized:hover{
  background: #FFD60A;
}
QPushButton{
  border-radius: 10px ;
  font-size: 20px;
  color: white;
  font-weight: bold;
}
QWidget {
  background: #202020;
  color: aliceblue;
}
QLabel   {
  font-size: 16px;
  font-weight: bold;
}
QLineEdit {
  border: 1px solid darkgrey;
  border-radius: 7px;
  padding: 1 6px;
  font-size: 18px;
}
QMessageBox QLabel {
    padding-right: 20px;
  font-size:20px;
  color: white;
}
QMessageBox QPushButton {
  margin-right: 120px;
  height: 40px;
  width: 55px;
  background: #34C759;
}
QMessageBox QPushButton:hover {
  background: #30D158;
}
QRadioButton {
  font-size: 16px;
}
QRadioButton:checked {
  border: 1px solid #007AFF;
  border-radius: 5px;
  font-size: 18px;
}
QRadioButton::indicator {
  background:transparent;
  width: 1px;
  height: 1px;
}
""")
app.exec()