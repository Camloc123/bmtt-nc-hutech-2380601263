import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import requests

# Đảm bảo bạn đã có file railfence.py trong thư mục IU
from IU.railfence import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self, key_text):
        """Kiểm tra xem key có phải là số nguyên hợp lệ (>= 2) không."""
        if not key_text.isdigit() or int(key_text) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Lỗi nhập liệu")
            msg.setText("Khóa (Key) không hợp lệ!")
            msg.setInformativeText("Với Rail Fence Cipher, khóa phải là một số nguyên lớn hơn hoặc bằng 2.")
            msg.exec_()
            return False
        return True

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        key_text = self.ui.txt_key.text().strip()
        
        # Kiểm tra tính hợp lệ của Key trước khi gọi API
        if not self.validate_key(key_text):
            return

        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": int(key_text)  # Ép kiểu sang int vì Rail Fence cần số
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)  # Debug dữ liệu API trả về

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
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        key_text = self.ui.txt_key.text().strip()
        
        # Kiểm tra tính hợp lệ của Key trước khi gọi API
        if not self.validate_key(key_text):
            return

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": int(key_text)  # Ép kiểu sang int
        }
        
        try:
            response = requests.post(url, json=payload)
            print("Response status code:", response.status_code)
            print("Response text:", response.text)  # Debug dữ liệu API trả về

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
                print("Error while calling API")

        except requests.exceptions.RequestException as e:
            print(f"Error while calling API: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())