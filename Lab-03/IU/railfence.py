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
        self.label.setGeometry(QtCore.QRect(130, 20, 240, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(80, 80, 381, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 50, 13))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 60, 31))
        self.label_3.setObjectName("label_3")
        
        self.txt_key = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(80, 190, 381, 31))
        self.txt_key.setObjectName("txt_key")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 55, 13))
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

        # --- KẾT NỐI SỰ KIỆN NÚT BẤM ---
        self.btn_encrypt.clicked.connect(self.encrypt_railfence)
        self.btn_decrypt.clicked.connect(self.decrypt_railfence)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rail Fence Cipher Tool"))
        self.label.setText(_translate("MainWindow", "RAIL FENCE CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plaintext"))
        self.label_3.setText(_translate("MainWindow", "Key (Số)")) # Nhấn mạnh key là số
        self.label_4.setText(_translate("MainWindow", "Ciphertext"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))

    # --- LOGIC THUẬT TOÁN RAIL FENCE ---

    def validate_key(self):
        """Kiểm tra và lấy giá trị khóa (phải là số nguyên >= 2)."""
        key_str = self.txt_key.text().strip()
        if not key_str.isdigit() or int(key_str) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lỗi: Khóa (Key) không hợp lệ!")
            msg.setInformativeText("Khóa của Rail Fence phải là một số nguyên lớn hơn hoặc bằng 2.")
            msg.setWindowTitle("Lỗi đầu vào")
            msg.exec_()
            return None
        return int(key_str)

    def process_encrypt(self, text, key):
        if not text:
            return ""
        
        # Tạo ma trận rỗng
        rail = [['\n' for i in range(len(text))] for j in range(key)]
        dir_down = False
        row, col = 0, 0
        
        # Xếp chữ cái theo đường zig-zag
        for i in range(len(text)):
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
            
            rail[row][col] = text[i]
            col += 1
            
            if dir_down:
                row += 1
            else:
                row -= 1
                
        # Đọc theo từng hàng ngang
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return "".join(result)

    def process_decrypt(self, cipher, key):
        if not cipher:
            return ""
            
        # Tạo ma trận rỗng đánh dấu vị trí
        rail = [['\n' for i in range(len(cipher))] for j in range(key)]
        dir_down = None
        row, col = 0, 0
        
        # Đánh dấu các vị trí có chứa ký tự bằng dấu '*'
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
                
            rail[row][col] = '*'
            col += 1
            
            if dir_down:
                row += 1
            else:
                row -= 1
                
        # Điền các ký tự của ciphertext vào các vị trí đã đánh dấu
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1
                    
        # Đọc lại theo đường zig-zag để lấy plaintext
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
                
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1
                
            if dir_down:
                row += 1
            else:
                row -= 1
        return "".join(result)

    def encrypt_railfence(self):
        key = self.validate_key()
        if key is None:
            return
            
        plaintext = self.txt_plain_text.toPlainText()
        ciphertext = self.process_encrypt(plaintext, key)
        self.txt_cipher_text.setPlainText(ciphertext)

    def decrypt_railfence(self):
        key = self.validate_key()
        if key is None:
            return
            
        ciphertext = self.txt_cipher_text.toPlainText()
        plaintext = self.process_decrypt(ciphertext, key)
        self.txt_plain_text.setPlainText(plaintext)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())