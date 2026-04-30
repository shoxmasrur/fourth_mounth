from PyQt5.QtWidgets import *


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_lay=QVBoxLayout()
        self.setStyleSheet("background:white; font-siza: 150px")


        self.lbl=QLabel("1-taomlar ro'yhati")
        self.t1 = QCheckBox("osh          -   30000")
        self.t2 = QCheckBox("sho'rva      -   20000")
        self.t3 = QCheckBox("manti        -   8000")
        self.t4 = QCheckBox("goja shorva  -   20000")
        self.t5 = QCheckBox("somsa        -    8000")
        self.lst=[self.t1,self.t2,self.t3,self.t4,self.t5]
       

        self.lbl1=QLabel("2-taomlar ro'yhati")

        self.t21 = QCheckBox("shashlik    -   50000")
        self.t22 = QCheckBox("jiz         -   200000")
        self.t23 = QCheckBox("tandir      -   28000")
        self.t24 = QCheckBox("kabob        -  80000")
        self.t25 = QCheckBox("jigar        -  180000")
        self.lst2=[self.t21,self.t22,self.t23,self.t24,self.t25]

        self.btn_check=QPushButton("check")
        self.btn_check.clicked.connect(self.test)


        self.main_lay.addWidget(self.lbl)
        for i in self.lst:
            self.main_lay.addWidget(i)
        self.main_lay.addWidget(self.lbl1)
        for i in self.lst2:
            self.main_lay.addWidget(i)
        self.main_lay.addWidget(self.btn_check)
        self.setLayout(self.main_lay)

    def test(self):
     self.lst = [ i.text() for i in self.lst if  i.isChecked()]
     self.msg=QMessageBox()
     self.msg.setText(f"{self.lst}\n xaridingiz uchun raxmat")
     self.msg.exec_()


           

        

        

        



app=QApplication([])
win=Mywindow()


win.show()
app.exec_()

