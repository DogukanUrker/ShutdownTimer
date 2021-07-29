import os
from sys import argv
from os import system
from PyQt5.QtCore import QPoint,QCoreApplication,Qt
from PyQt5.QtWidgets import QPushButton,QLineEdit,QLabel,QRadioButton,QMessageBox,QApplication,QWidget
x = os.name.count("nt")
os = " "
if(x > 0):
    os = "nt"
def alert(text):
    message = QMessageBox()
    message.setText(str(text))
    message.setStandardButtons(QMessageBox.Ok)
    message.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
    message.setGeometry(900,300,0,0)
    ret = message.exec_() 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,400,270,200)
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
        self.ok = QPushButton("Start",self)
        self.hours = QLineEdit("",self)
        self.minutes = QLineEdit("",self)
        self.hours_text = QLabel("Hours:",self)
        self.minutes_text = QLabel("Minutes:",self)
        self.exit = QPushButton("",self)
        self.minimized = QPushButton("",self)
        self.abort = QPushButton("Abort",self)
        self.shutdown = QRadioButton("Shutdown",self)
        self.restart = QRadioButton("  Restart",self)
        self.shutdown.setObjectName("shutdown")
        self.restart.setObjectName("restart")
        self.abort.setObjectName("abort")
        self.ok.setObjectName("start")
        self.exit.setObjectName("exit")
        self.minimized.setObjectName("minimized")
        self.exit.setGeometry(245,3,20,20)
        self.minimized.setGeometry(220,3,20,20)
        self.hours.setGeometry(10,45,150,30)   
        self.hours_text.setGeometry(10,25,300,20)
        self.minutes.setGeometry(10,100,150,30)
        self.minutes_text.setGeometry(10,80,300,20)
        self.restart.setGeometry(175,70,85,30)
        self.shutdown.setGeometry(175,40,85,30)
        self.ok.setGeometry(10,135,120,60)
        self.abort.setGeometry(140,135,120,60)
        self.ok.clicked.connect(self.process)
        self.abort.clicked.connect(self.shutdown_cancel)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.minimized.clicked.connect(lambda: self.showMinimized())
        self.shutdown.setChecked(True)
    def process(self):
        hours = self.hours.text()
        minutes = self.minutes.text()
        def operation(command,minutes,hours):
          if os =="nt":
            if hours == " " or hours == "":
                time = int(minutes) * 60 
                system("shutdown {} {}".format(command,time))   
            elif minutes == " " or minutes == "":
                time = int(hours) * 60 * 60 
                system("shutdown {} {}".format(command,time))
            else:
                time = int(hours) * 60 * 60 + int(minutes) * 60 
                system("shutdown {} {}".format(command,time))
          else:
            if hours == " " or hours == "":
                time = int(minutes) 
                system("shutdown {} {}".format(command,time))   
            elif minutes == " " or minutes == "":
                time = int(hours) * 60 
                system("shutdown {} {}".format(command,time))
            else:
                time = int(hours) * 60 + int(minutes) 
                system("shutdown {} {}".format(command,time))
        try:
          if os == "nt":
            if self.shutdown.isChecked():
                operation("-s -f -t",minutes,hours)
            if self.restart.isChecked():
                operation("/r /t",minutes,hours)
          else:
            if self.shutdown.isChecked():
                operation("-h",minutes,hours)
            if self.restart.isChecked():
                operation("-r",minutes,hours)
        except:
            alert("Please check the values")        
    def shutdown_cancel(self):
        system("shutdown -a")
app = QApplication(argv)
Window = Window()
Window.show()
app.setStyleSheet(
    """
#start {
  background: rgb(27, 167, 78);
}
#start:hover {
  background: rgba(27, 167, 78,0.6);
}
#abort {  
  background: rgba(255, 56, 56,0.8);
}
#abort:hover {
  background: rgba(255, 56, 56,0.4);
}
#shutdown, #restart{
    border-radius: 10px;
    text-align: center;
}
#exit{
    border-radius: 10px;
  background: rgba(255, 56, 56,1.0);
}
#exit:hover{
  background: rgba(255, 56, 56,0.7);
}
#minimized{
    border-radius: 10px;
  background: rgb(255, 159, 26);
}
#minimized:hover{
  background: rgba(255, 159, 26,0.7);
}
QPushButton{
  border-radius: 10px ;
  font-size: 20px;
  color: white;
  font-weight: bold;
}
QWidget {
  background: rgb(32, 30, 30);
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
    height: 30px;
    width: 45px;
  background: rgb(27, 167, 78);
}
QMessageBox QPushButton:hover {
  background: rgba(27, 167, 78,0.6);
}
QRadioButton {
  font-size: 16px;
}
QRadioButton:checked {
  border: 1px solid rgb(101, 236, 101);
  border-radius: 5px;
}
QRadioButton::indicator {
  color : transparent;
  background:transparent;
  width: 1px;
  height: 1px;
}
    """
)
app.exec()