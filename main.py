import sys,os
from PyQt5.QtWidgets import QLabel,QGridLayout,QPushButton,QComboBox,QWidget,QVBoxLayout,QHBoxLayout,QApplication
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
def csslaoder(filename):
    with open(filename,'r') as file:
        icerik = file.read()
        file.close()
    return icerik
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(480,480,0,0)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setWindowTitle("no title")
        self.ui()
    def ui(self):
        self.dugme = QPushButton("Onayla")
        self.secim = QComboBox(self)
        self.yazi = QLabel("PC'nin kaç saat sonra kapatılcağı:")
        self.yazi2 = QLabel("'Onayla' tuşuna basıldığında uyarı çıkmıyorsa daha önceden zamanlayıcı kurulmuş demektir")
        self.exit = QPushButton("")
        self.minimized = QPushButton("")
        for i in range(1,11):
            self.secim.addItem(str(i))
        self.iptal = QPushButton("İptal Et")
        self.iptal.setObjectName("iptal")
        self.yazi.setObjectName("soru1")
        self.yazi2.setObjectName("metin")
        self.dugme.setObjectName("onayla")
        self.exit.setObjectName("exit")
        self.minimized.setObjectName("minimized")
        self.exit.setIcon(QIcon('exit.png'))
        self.minimized.setIcon(QIcon('minimized.png'))
        grid = QGridLayout()
        grid.addWidget(self.exit,0,1)
        grid.addWidget(self.yazi,0,0)
        grid.addWidget(self.minimized,1,1)
        grid.addWidget(self.secim,1,0)
        grid.addWidget(self.dugme,2,0)
        grid.addWidget(self.iptal,3,0)
        grid.addWidget(self.yazi2,4,0)
        self.setLayout(grid)
        self.dugme.clicked.connect(self.yap)
        self.iptal.clicked.connect(self.kapa)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.minimized.clicked.connect(lambda: self.showMinimized())
    def yap(self):
        os.system("shutdown -s -f -t {}".format(str(int(self.secim.currentText()) * 60 * 60)))
    def kapa(self):
        os.system("shutdown -a")
app = QApplication(sys.argv)
pencere= Pencere()
pencere.show()
app.setStyleSheet(csslaoder("stylesheet.css"))
app.exec()
