from sys import argv
from os import system
from PyQt5.QtWidgets import QPushButton,QLineEdit,QLabel,QRadioButton,QMessageBox,QApplication,QWidget
from PyQt5.QtCore import QPoint,QCoreApplication,Qt
from PyQt5.QtGui import QIcon
def css(isim):
    with open(isim,'r') as dosya:
        icerik = dosya.read()
        dosya.close()
    return icerik
def uyarı(yazi):
    mesaj = QMessageBox()
    mesaj.setText(str(yazi))
    mesaj.setStandardButtons(QMessageBox.Ok)
    mesaj.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
    mesaj.setGeometry(900,300,100,100)
    ret = mesaj.exec_() 
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,400,270,200)
        self.setWindowTitle("Süreli PC Kapatma")
        self.setWindowIcon(QIcon('icons/bos.png'))
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
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
        self.ok = QPushButton("Onayla",self)
        self.saat = QLineEdit("",self)
        self.dakika = QLineEdit("",self)
        self.yazi = QLabel("Saat:",self)
        self.yazi1 = QLabel("Dakika:",self)
        self.exit = QPushButton("",self)
        self.minimized = QPushButton("",self)
        self.iptal = QPushButton("İptal Et",self)
        self.kapat = QRadioButton("Kapat",self)
        self.yenidenbaslat = QRadioButton("Restart",self)
        self.kapat.setObjectName("kapat")
        self.yenidenbaslat.setObjectName("yenidenbaslat")
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
        self.yenidenbaslat.setGeometry(175,70,70,30)
        self.kapat.setGeometry(175,40,70,30)
        self.ok.setGeometry(10,135,120,60)
        self.iptal.setGeometry(140,135,120,60)
        self.ok.clicked.connect(self.yap)
        self.iptal.clicked.connect(self.islemiptal)
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.minimized.clicked.connect(lambda: self.showMinimized())
        self.kapat.setChecked(True)
    def yap(self):
        kapat = "Bilgisayarınız {} dk içinde kapatılacaktır"
        res = "Bilgisayarınız {} dk içinde yeniden başlatılacaktır"
        def islem(komut,dk,saat):
            if saat == " " or saat == "":
                sure = int(dk) * 60 
                system("shutdown {} {}".format(komut,sure))   
                if komut == "-s -f -t":
                    uyarı(kapat.format(dk))
                else:
                    uyarı(res.format(dk))
            elif dk == " " or dk == "":
                sure = int(saat) * 60 * 60 
                sure2 = int(sure / 60 )
                system("shutdown {} {}".format(komut,sure))
                if komut == "-s -f -t":
                    uyarı(kapat.format(sure2))
                else:
                    uyarı(res.format(sure2))
            else:
                sure = int(saat) * 60 * 60 + int(dk) * 60 
                sure2 = int(sure / 60 )
                system("shutdown {} {}".format(komut,sure))
                if komut == "-s -f -t":
                    uyarı(kapat.format(sure2))
                else:
                    uyarı(res.format(sure2))
        saat = self.saat.text()
        dk = self.dakika.text()
        try:
            if self.kapat.isChecked():
                islem("-s -f -t",dk,saat)
            if self.yenidenbaslat.isChecked():
                islem("/r /t",dk,saat)
        except:
            uyarı("Lütfen Girdiğiniz değerleri kontrol edin")        
    def islemiptal(self):
        system("shutdown -a")
        uyarı("İşlem iptal edildi")
app = QApplication(argv)
pencere= Pencere()
pencere.show()
app.setStyleSheet(css("stylesheet.css"))
app.exec()