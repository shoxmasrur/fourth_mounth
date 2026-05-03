import json
from PyQt5.QtWidgets import *

class IncomeWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mainwindow=obj

        self.v_edit_lay=QVBoxLayout()
        self.h_ebtn_lay=QHBoxLayout()
        self.main_lay=QVBoxLayout()

        self.edit_name=QLineEdit()
        self.edit_name.setPlaceholderText("product name")

        self.edit_count=QLineEdit()
        self.edit_count.setPlaceholderText("amount poduct")

        self.btn_ok=QPushButton("ok")
        self.btn_ok.clicked.connect(self.ok)

        self.btn_menu=QPushButton("menu")
        self.btn_menu.clicked.connect(self.menu)

        self.v_edit_lay.addWidget(self.edit_name)
        self.v_edit_lay.addWidget(self.edit_count)

        self.h_ebtn_lay.addLayout(self.v_edit_lay)
        self.h_ebtn_lay.addWidget(self.btn_ok)

        self.main_lay.addLayout(self.h_ebtn_lay)
        self.main_lay.addWidget(self.btn_menu)

        self.setLayout(self.main_lay)


    def ok(self):
        
        self.name=self.edit_name.text().lower()
        self.count=self.edit_count.text()
        with open("product.json", "r") as f:
            self.data=json.load(f)

        self.edit_name.clear()
        self.edit_count.clear()
        self.msg=QMessageBox()
        if self.name and self.count:
            self.count=int(self.count)
            if self.name in self.data :
                self.data[self.name]=self.count+self.data[self.name]
            else:
                self.data[self.name]=self.count

            self.matn="Muvafaqiyatli qo'shildi"
            self.icon=QMessageBox.Information

            with open("product.json", "w") as f:
                json.dump(self.data, f, indent=4)
        else:
            
            self.matn="ikkala qator ham to'ldirilishi shart"
            self.icon=QMessageBox.Critical
        self.msg.setText(self.matn)
        self.msg.setIcon(self.icon)

        self.msg.exec_()




    def menu(self):
        self.hide()
        self.mainwindow.show()


