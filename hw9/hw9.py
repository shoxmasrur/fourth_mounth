from PyQt5.QtWidgets import * 


class Mywindow(QWidget):
    def __init__(self):
        super().__init__()


    

        self.main_lay=QVBoxLayout()
        self.jins_lay=QHBoxLayout()
        self.btn_lay=QHBoxLayout()
        self.viloyat_lay=QHBoxLayout()
        self.tuman_lay=QHBoxLayout()

        self.edit_name=QLineEdit()
        self.edit_name.setPlaceholderText("ism")
        self.edit_second=QLineEdit()
        self.edit_second.setPlaceholderText("familiya")
        self.edit_age=QLineEdit()
        self.edit_age.setPlaceholderText("yosh")


        self.jins_M=QRadioButton("M")
        self.jins_F=QRadioButton("F")

        self.cmb_viloyat=QComboBox()
        self.cmb_viloyat.addItems([
    "Toshkent viloyati",
    "Samarqand viloyati",
    "Fargona viloyati",
    "Andijon viloyati",
    "Namangan viloyati",
    "Buxoro viloyati",
    "Qashqadaryo viloyati",
    "Surxondaryo viloyati",
    "Xorazm viloyati",
    "Navoiy viloyati",
    "Jizzax viloyati",
    "Sirdaryo viloyati",
    "Qoraqalpogiston"
])
        self.cmb_viloyat.activated[str].connect(self.test)
        self.cmb_tuman=QComboBox()

        self.lbl_viloyat=QLabel("viloyat")
        self.lbl_tuman=QLabel("tuman")

        self.btn_submit=QPushButton("submit")
        self.btn_submit.clicked.connect(self.write)
        
        self.btn_exit=QPushButton("exit")
        self.btn_exit.clicked.connect(exit)


        self.jins_lay.addWidget(self.jins_M)
        self.jins_lay.addWidget(self.jins_F)

        self.btn_lay.addWidget(self.btn_submit)
        self.btn_lay.addWidget(self.btn_exit)


        self.viloyat_lay.addWidget(self.lbl_viloyat)
        self.viloyat_lay.addWidget(self.cmb_viloyat)

        self.tuman_lay.addWidget(self.lbl_tuman)
        self.tuman_lay.addWidget(self.cmb_tuman)

        self.main_lay.addWidget(self.edit_name)
        self.main_lay.addWidget(self.edit_second)
        self.main_lay.addWidget(self.edit_age)

        self.main_lay.addLayout(self.jins_lay)

        self.main_lay.addLayout(self.viloyat_lay)
        self.main_lay.addLayout(self.tuman_lay)
        self.main_lay.addLayout(self.btn_lay)

        self.setLayout(self.main_lay)

    

        
        
        self.uzbekiston = {
    "Toshkent viloyati": [
        "Bekobod", "Boka", "Bostonliq", "Zangiota", "Qibray",
        "Parkent", "Piskent", "Ohangaron", "Ortachirchiq",
        "Yangiyol", "Yuqorichirchiq", "Quyi Chirchiq"
    ],

    "Samarqand viloyati": [
        "Bulungur", "Ishtixon", "Jomboy", "Kattaqorgon",
        "Narpay", "Nurobod", "Oqdaryo", "Paxtachi",
        "Payariq", "Pastdargom", "Qoshrabot",
        "Samarqand", "Toyloq", "Urgut"
    ],

    "Fargona viloyati": [
        "Oltiariq", "Bagdod", "Beshariq", "Buvayda",
        "Dangara", "Fargona", "Furqat", "Qoqon",
        "Quva", "Quvasoy", "Rishton", "Sox",
        "Toshloq", "Uchkoprik", "Yozyovon"
    ],

    "Andijon viloyati": [
        "Andijon", "Asaka", "Baliqchi", "Boz", "Buloqboshi",
        "Izboskan", "Jalolquduq", "Marhamat", "Oltinkol",
        "Paxtaobod", "Qorgontepa", "Shahrixon",
        "Ulugnor", "Xojaobod"
    ],

    "Namangan viloyati": [
        "Chortoq", "Chust", "Kosonsoy", "Mingbuloq",
        "Namangan", "Norin", "Pop", "Toraqorgon",
        "Uchqorgon", "Uychi", "Yangiqorgon"
    ],

    "Buxoro viloyati": [
        "Buxoro", "Gijduvon", "Jondor", "Kogon",
        "Olot", "Peshku", "Qorakol", "Qorovulbozor",
        "Romitan", "Shofirkon", "Vobkent"
    ],

    "Qashqadaryo viloyati": [
        "Chiroqchi", "Dehqonobod", "Guzor", "Kasbi",
        "Kitob", "Koson", "Mirishkor", "Muborak",
        "Nishon", "Qamashi", "Qarshi", "Shahrisabz",
        "Yakkabog"
    ],

    "Surxondaryo viloyati": [
        "Angor", "Bandixon", "Boysun", "Denov",
        "Jarqorgon", "Muzrabot", "Oltinsoy",
        "Qiziriq", "Qumqorgon", "Sariosiyo",
        "Sherobod", "Shorchi", "Termiz", "Uzun"
    ],

    "Xorazm viloyati": [
        "Bogot", "Gurlan", "Hazorasp", "Khiva",
        "Qoshkopir", "Shovot", "Urganch", "Xonqa",
        "Yangiariq", "Yangibozor"
    ],

    "Navoiy viloyati": [
        "Karmana", "Konimex", "Navbahor",
        "Nurota", "Qiziltepa", "Tomdi", "Uchquduq", "Xatirchi"
    ],

    "Jizzax viloyati": [
        "Arnasoy", "Baxmal", "Dostlik", "Forish",
        "Gallaorol", "Jizzax", "Mirzachol",
        "Paxtakor", "Yangiobod", "Zafarobod", "Zarbdor"
    ],

    "Sirdaryo viloyati": [
        "Boyovut", "Guliston", "Mirzaobod",
        "Oqoltin", "Sardoba", "Sayxunobod",
        "Sirdaryo", "Xovos"
    ],

    "Qoraqalpogiston": [
        "Amudaryo", "Beruniy", "Chimboy", "Ellikqala",
        "Kegeyli", "Moynoq", "Nukus", "Qanlikol",
        "Qongirot", "Qoraozak", "Shumanay",
        "Taxtakopir", "Tortkol", "Xojayli"
    ]
}
    
        
    def test(self, vil):
        for i in self.uzbekiston:
            if i==vil:
                self.cmb_tuman.addItems(self.uzbekiston[i])
                self.viloyat=i
               
        

    def write(self):
        self.name=self.edit_name.text()
        self.sure=self.edit_second.text()
        self.age=self.edit_age.text()
        if self.jins_M.isChecked():
            self.jins="M"
        else :
            self.jins="F"

        self.tuman=self.cmb_tuman.currentText()


        f=open("users_information.txt", "w")
        f.write(f"{self.name}, {self.sure}, {self.age}, {self.jins}, {self.viloyat},{self.tuman}")

        f.close()

        self.edit_name.clear()
        self.edit_second.clear()
        self.edit_age.clear()
        self.jins_F.setChecked(False)
        self.jins_M.setChecked(False)
        self.cmb_viloyat.setCurrentIndex(-1)
        self.cmb_tuman.setCurrentIndex(-1)
                


        











app=QApplication([])
win=Mywindow()

win.show()
app.exec_()
