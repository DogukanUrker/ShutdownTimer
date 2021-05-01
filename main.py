import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
def csslaoder(filename):
    with open(filename,'r') as file:
        icerik = file.read()
        file.close()
    return icerik
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(750,500,270,200)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Süreli PC Kapatma")
        self.setWindowIcon(QIcon('icons/bos.png'))
        self.setWindowFlags(flags)
        self.ui()
    def ui(self):
        self.ok = QPushButton("Onayla",self)
        self.saat = QLineEdit("",self)
        self.dakika = QLineEdit("",self)
        self.yazi = QLabel("Saat:",self)
        self.yazi1 = QLabel("Dakika:",self)
        self.exit = QPushButton("",self)
        self.minimized = QPushButton("",self)
        self.iptal = QPushButton("İptal Et",self)
        self.iptal.setObjectName("iptal")
        self.ok.setObjectName("onayla")
        self.exit.setObjectName("exit")
        self.minimized.setObjectName("minimized")
        self.exit.setIcon(QIcon('icons/exit.png'))
        self.minimized.setIcon(QIcon('icons/minimized.png'))
        self.exit.setGeometry(240,3,25,25)
        self.minimized.setGeometry(215,3,25,25)
        self.yazi.setGeometry(10,25,300,20)
        self.saat.setGeometry(10,45,150,30)      
        self.yazi1.setGeometry(10,80,300,20)
        self.dakika.setGeometry(10,100,150,30)
        self.ok.setGeometry(10,135,120,60)
        self.iptal.setGeometry(140,135,120,60)
        self.ok.clicked.connect(self.yap)
        self.iptal.clicked.connect(self.kapa)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.minimized.clicked.connect(lambda: self.showMinimized())
    def yap(self):
        saat = self.saat.text()
        dk = self.dakika.text()
        if dk == " " or saat == " " or dk == "" or saat == "":
            pass
        elif saat == " " or saat == "":
            os.system("shutdown -s -f -t {}".format(int(dk) * 60 ))   
        elif dk == " " or dk == "":
            os.system("shutdown -s -f -t {}".format(int(saat) * 60 * 60 ))
        else :
            os.system("shutdown -s -f -t {}".format(int(saat) * 60 * 60 + int(dk) * 60 ))
    def kapa(self):
        os.system("shutdown -a")
app = QApplication(sys.argv)
pencere= Pencere()
pencere.show()
app.setStyleSheet(csslaoder("stylesheet.css"))
app.exec()