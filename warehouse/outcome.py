import json
from PyQt5.QtWidgets import *

class OutcomeWindow(QWidget):
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
                self.amount=self.data[self.name]-self.count
                if self.amount<0 :
                    self.matn=f"bunday miqdor mavjud emas. omoborda {self.data[self.name]} dona mahsulot qolgan"
                    self.icon=self.icon=QMessageBox.Critical
                elif self.amount>0:
                    self.matn="Muvafaqiyatli "
                    self.icon=QMessageBox.Information
                    self.data[self.name]=self.data[self.name]-self.amount

                else:
                    self.matn="Muvafaqiyatli lekin mahsulot omborda qolmadi"
                    self.icon=QMessageBox.Warning
                    self.data.pop(self.name)


            else:

                self.matn="Bunday mahsulot omborda yo'q"
                self.icon=QMessageBox.Critical

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