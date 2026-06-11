# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QMessageBox

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(80, 80, 381, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 47, 13))
        self.label_3.setObjectName("label_3")
        
        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(80, 190, 381, 31))
        self.txt_key.setObjectName("txt_key")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 47, 13))
        self.label_4.setObjectName("label_4")
        
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(80, 260, 381, 91))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(80, 360, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(380, 360, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # --- KẾT NỐI SỰ KIỆN NÚT BẤM (BUTTON EVENTS) ---
        self.btn_encrypt.clicked.connect(self.encrypt_vigenere)
        self.btn_decrypt.clicked.connect(self.decrypt_vigenere)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vigenère Cipher Tool"))
        self.label.setText(_translate("MainWindow", "VIGENÈRE CIPHER")) # Đổi tên tiêu đề
        self.label_2.setText(_translate("MainWindow", "Plaintext"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "Ciphertext"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))

    # --- LOGIC THUẬT TOÁN VIGENÈRE ---
    def process_vigenere(self, text, key, mode):
        # Kiểm tra nếu khóa trống hoặc chứa ký tự không phải chữ cái
        if not key or not key.isalpha():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lỗi: Khóa (Key) không hợp lệ!")
            msg.setInformativeText("Khóa không được để trống và chỉ được chứa các chữ cái (A-Z).")
            msg.setWindowTitle("Lỗi đầu vào")
            msg.exec_()
            return ""

        key = key.upper()
        result = []
        key_index = 0

        for char in text:
            if char.isalpha():
                # Tính độ dời (shift) dựa trên ký tự hiện tại của khóa
                shift = ord(key[key_index % len(key)]) - ord('A')
                
                # Nếu là giải mã thì trừ đi độ dời
                if mode == "decrypt":
                    shift = -shift
                
                # Giữ nguyên chữ hoa / chữ thường
                if char.islower():
                    new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                else:
                    new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                
                result.append(new_char)
                key_index += 1
            else:
                # Giữ nguyên khoảng trắng, số, dấu câu...
                result.append(char)
                
        return "".join(result)

    def encrypt_vigenere(self):
        plaintext = self.txt_plain_text.toPlainText()
        key = self.txt_key.text()
        ciphertext = self.process_vigenere(plaintext, key, "encrypt")
        if ciphertext:
            self.txt_cipher_text.setPlainText(ciphertext)

    def decrypt_vigenere(self):
        ciphertext = self.txt_cipher_text.toPlainText()
        key = self.txt_key.text()
        plaintext = self.process_vigenere(ciphertext, key, "decrypt")
        if plaintext:
            self.txt_plain_text.setPlainText(plaintext)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())