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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
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

        # --- KẾT NỐI SỰ KIỆN NÚT BẤM ---
        self.btn_encrypt.clicked.connect(self.encrypt_playfair)
        self.btn_decrypt.clicked.connect(self.decrypt_playfair)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Playfair Cipher Tool"))
        self.label.setText(_translate("MainWindow", "PLAYFAIR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plaintext"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "Ciphertext"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))

    # --- LOGIC THUẬT TOÁN PLAYFAIR ---
    
    def generate_key_matrix(self, key):
        """Tạo ma trận 5x5 từ từ khóa."""
        key = key.upper().replace('J', 'I')
        matrix = []
        used_chars = set()
        
        # Thêm các ký tự của khóa vào ma trận
        for char in key:
            if char.isalpha() and char not in used_chars:
                matrix.append(char)
                used_chars.add(char)
                
        # Thêm các ký tự còn lại của bảng chữ cái (bỏ qua 'J')
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in used_chars:
                matrix.append(char)
                used_chars.add(char)
                
        # Chuyển mảng 1 chiều thành mảng 2 chiều 5x5
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def get_position(self, matrix, char):
        """Lấy tọa độ (hàng, cột) của ký tự trong ma trận."""
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == char:
                    return r, c
        return -1, -1

    def process_playfair(self, text, key, mode):
        if not key or not "".join([c for c in key if c.isalpha()]):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lỗi: Khóa (Key) không hợp lệ!")
            msg.setInformativeText("Khóa không được để trống và phải chứa chữ cái.")
            msg.setWindowTitle("Lỗi đầu vào")
            msg.exec_()
            return ""

        matrix = self.generate_key_matrix(key)
        
        # Tiền xử lý văn bản (Chỉ lấy chữ cái, viết hoa, thay J bằng I)
        text = text.upper().replace('J', 'I')
        filtered_text = "".join([c for c in text if c.isalpha()])
        
        if not filtered_text:
            return ""

        digraphs = []
        
        if mode == "encrypt":
            # Tạo các cặp ký tự (digraphs) cho quá trình mã hóa
            i = 0
            while i < len(filtered_text):
                char1 = filtered_text[i]
                if i + 1 < len(filtered_text):
                    char2 = filtered_text[i+1]
                    if char1 == char2:
                        digraphs.append(char1 + 'X')
                        i += 1
                    else:
                        digraphs.append(char1 + char2)
                        i += 2
                else:
                    # Chèn X nếu bị lẻ ở cuối
                    digraphs.append(char1 + 'X')
                    i += 1
        else:
            # Giải mã: Chia cặp trực tiếp (chuỗi Ciphertext luôn chẵn)
            if len(filtered_text) % 2 != 0:
                filtered_text += 'X' # Tránh lỗi crash nếu chuỗi mã hóa bị mất ký tự
            digraphs = [filtered_text[i:i+2] for i in range(0, len(filtered_text), 2)]

        result = []
        
        # Xử lý quy tắc Playfair cho từng cặp
        for pair in digraphs:
            r1, c1 = self.get_position(matrix, pair[0])
            r2, c2 = self.get_position(matrix, pair[1])
            
            if r1 == r2: # Cùng hàng
                if mode == "encrypt":
                    result.append(matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5])
                else:
                    result.append(matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5])
            elif c1 == c2: # Cùng cột
                if mode == "encrypt":
                    result.append(matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2])
                else:
                    result.append(matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2])
            else: # Tạo thành hình chữ nhật
                result.append(matrix[r1][c2] + matrix[r2][c1])

        return "".join(result)

    def encrypt_playfair(self):
        plaintext = self.txt_plain_text.toPlainText()
        key = self.txt_key.text()
        ciphertext = self.process_playfair(plaintext, key, "encrypt")
        if ciphertext:
            self.txt_cipher_text.setPlainText(ciphertext)

    def decrypt_playfair(self):
        ciphertext = self.txt_cipher_text.toPlainText()
        key = self.txt_key.text()
        plaintext = self.process_playfair(ciphertext, key, "decrypt")
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