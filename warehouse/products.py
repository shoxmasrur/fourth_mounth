import json
from PyQt5.QtWidgets import *
 

class PorductWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mainwindow=obj

        self.lbl_lay=QHBoxLayout()
        self.main_lay=QVBoxLayout()


        self.lbl_name=QLabel("name")
        self.lbl_count=QLabel("count")

        self.lst=QListWidget()
        self.btn_menu=QPushButton("menu")
        self.btn_menu.clicked.connect(self.menu)

        self.lbl_lay.addWidget(self.lbl_name)
        self.lbl_lay.addStretch()
        self.lbl_lay.addStretch()
        self.lbl_lay.addWidget(self.lbl_count)
        self.lbl_lay.addStretch()
        

        self.main_lay.addLayout(self.lbl_lay)
        self.main_lay.addWidget(self.lst)
        self.main_lay.addWidget(self.btn_menu)

        self.setLayout(self.main_lay)


        with open("product.json", "r") as f:
            self.data=json.load(f)
        for i, value in self.data.items():
            self.lst.addItem(f"{i}\t\t{value}")


    def menu(self):
        self.hide()
        self.mainwindow.show()

    