# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lbl_student_info = QtWidgets.QLabel(self.centralwidget)
        self.lbl_student_info.setGeometry(QtCore.QRect(0, 5, 476, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_student_info.setFont(font)
        self.lbl_student_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_student_info.setObjectName("lbl_student_info")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(128, 35, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
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
        
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playfair Cipher - MSSV: 2380601263 - SV: Cam Xuân Lộc"))
        self.lbl_student_info.setText(_translate("MainWindow", "MSSV: 2380601263 - SV: Cam Xuân Lộc"))
        self.label.setText(_translate("MainWindow", "PLAYFAIR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plaintext"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "Ciphertext"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện nút bấm
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText().strip() 
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                try:
                    data = response.json()
                    self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", ""))
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Thành công")
                    msg.setText("Encrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
            else:
                try:
                    error_msg = response.json().get("error", "Error while calling API")
                except:
                    error_msg = "Error while calling API"
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Lỗi")
                msg.setText(error_msg)
                msg.exec_()

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Lỗi")
            msg.setText(f"Không thể kết nối đến server: {e}")
            msg.exec_()

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText().strip()
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                try:
                    data = response.json()
                    self.ui.txt_plain_text.setPlainText(data.get("decrypted_text", ""))
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Thành công")
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                except requests.exceptions.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
            else:
                try:
                    error_msg = response.json().get("error", "Error while calling API")
                except:
                    error_msg = "Error while calling API"
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Lỗi")
                msg.setText(error_msg)
                msg.exec_()

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Lỗi")
            msg.setText(f"Không thể kết nối đến server: {e}")
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
