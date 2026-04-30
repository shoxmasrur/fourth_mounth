from PyQt5.QtWidgets import *


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_lay=QVBoxLayout()
        self.Mash_lay=QHBoxLayout()
        self.btn_lay=QHBoxLayout()

        self.msg=QMessageBox()

        self.lbl=QLabel("Mashina Bozor")
        self.edit=QLineEdit()
        self.btn=QPushButton("BUY")
        self.btn.clicked.connect(self.test)

        self.Mash_lay.addStretch()
        self.Mash_lay.addWidget(self.lbl)
        self.Mash_lay.addStretch()
        
        self.btn_lay.addStretch()
        self.btn_lay.addWidget(self.btn)
        self.btn_lay.addStretch()

        self.main_lay.addLayout(self.Mash_lay)
        self.main_lay.addWidget(self.edit)
        self.main_lay.addLayout(self.btn_lay)

        self.setLayout(self.main_lay)
    def test(self):
        self.name=self.edit.text()

        self.msg=QMessageBox()
        self.msg.setText("xaridingiz uchun raxmat")
        self.msg.setIconcon(QMessageBox.information)


        self.msg.exec_()





app=QApplication([])
win=Mywindow()


win.show()
app.exec_()



