import sys,os
from PyQt6.QtWidgets import QLabel,QPushButton,QComboBox,QWidget,QVBoxLayout,QHBoxLayout,QApplication,QMainWindow
def csslaoder(filename):
    with open(filename,'r') as file:
        icerik = file.read()
        file.close()
    return icerik
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(450,250,500,150)
        self.setWindowTitle("Zamanlı PC Kapatma")
        self.ui()
    def ui(self):
        self.dugme = QPushButton("Onayla")
        self.secim = QComboBox(self)
        self.yazi = QLabel("PC'nin kaç saat sonra kapatılcağı:")
        self.yazi2 = QLabel("'Onayla' tuşuna basıldığında uyarı çıkmıyorsa daha önceden zamanlayıcı kurulmuş demektir")
        for i in range(1,11):
            self.secim.addItem(str(i))
        self.iptal = QPushButton("İptal Et")
        self.iptal.setObjectName("iptal")
        self.yazi.setObjectName("uyarı")
        self.dugme.setObjectName("onayla")
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.yazi)
        vbox.addWidget(self.secim)
        vbox.addWidget(self.dugme)
        vbox.addWidget(self.iptal)
        vbox.addWidget(self.yazi2)
        vbox.addStretch()
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.dugme.clicked.connect(self.yap)
        self.iptal.clicked.connect(self.kapa)
    def yap(self):
        os.system("shutdown -s -f -t {}".format(str(int(self.secim.currentText()) * 60 * 60)))
    def kapa(self):
        os.system("shutdown -a")
app = QApplication(sys.argv)
pencere= Pencere()
pencere.show()
app.setStyleSheet(csslaoder("stylesheet.css"))
app.exec()
