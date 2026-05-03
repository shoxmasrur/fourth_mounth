import json
from PyQt5.QtWidgets import *
from income import IncomeWindow
from outcome import OutcomeWindow
from products import PorductWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_btn_lay=QVBoxLayout()
        self.main_lay=QHBoxLayout()



        self.btn_add=QPushButton("add")
        self.btn_add.clicked.connect(self.add)

        self.btn_remove=QPushButton("remove")
        self.btn_remove.clicked.connect(self.remove)

        self.btn_pro=QPushButton("product")
        self.btn_pro.clicked.connect(self.product)
        
        self.btn_exit=QPushButton("exit")
        self.btn_exit.clicked.connect(exit)


        self.v_btn_lay.addWidget(self.btn_add)
        self.v_btn_lay.addWidget(self.btn_remove)
        self.v_btn_lay.addWidget(self.btn_pro)
        self.v_btn_lay.addWidget(self.btn_exit)

        self.main_lay.addStretch()
        self.main_lay.addLayout(self.v_btn_lay)
        self.main_lay.addStretch()
        self.setLayout(self.main_lay)


    def add(self):
        self.hide()
        self.incomewindow=IncomeWindow(self)
        self.incomewindow.show()
    def remove(self):
        self.hide()
        self.outcomewindow=OutcomeWindow(self)
        self.outcomewindow.show()
    def product (self):
        self.hide()
        self.productwindow=PorductWindow(self)
        self.productwindow.show()















app=QApplication([])
win=MainWindow()
win.show()
app.exec_()
