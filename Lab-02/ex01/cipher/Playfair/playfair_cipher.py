class PlayfairCipher:
    def __init__(self, key):
        self.init_warnings = [] # Dùng để lưu cảnh báo riêng của Key

        # ===== KIỂM TRA KEY =====
        if not key or not str(key).strip():
            raise ValueError(
                "Playfair Cipher: Key không được để trống."
            )

        if not str(key).replace(" ", "").isalpha():
            raise ValueError(
                "Playfair Cipher: Key chỉ được chứa các chữ cái A-Z, không được chứa số hoặc ký tự đặc biệt."
            )

        # Cảnh báo nếu Key có chữ J
        if 'J' in str(key).upper():
            self.init_warnings.append("⚠️ Từ khóa chứa chữ 'J', hệ thống đã tự động chuyển thành 'I'.")

        self.key = key.upper().replace('J', 'I')
        self.matrix = self.create_matrix()
        self.warnings = [] # Khởi tạo danh sách cảnh báo cho quá trình mã hóa

    def create_matrix(self):
        matrix = []
        used_letters = set()

        for char in self.key:
            if char not in used_letters and char.isalpha():
                used_letters.add(char)
                matrix.append(char)

        for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in used_letters:
                used_letters.add(char)
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return (row, col)

        raise ValueError(
            f"Playfair Cipher: Không tìm thấy ký tự {char} trong ma trận."
        )

    def encrypt(self, plaintext):
        # Nạp cảnh báo của Key vào danh sách cảnh báo chung mỗi lần mã hóa
        self.warnings = list(self.init_warnings)

        # ===== KIỂM TRA PLAINTEXT =====
        if not plaintext or not str(plaintext).strip():
            raise ValueError(
                "Playfair Cipher: Plain Text không được để trống."
            )

        if not str(plaintext).replace(" ", "").isalpha():
            raise ValueError(
                "Playfair Cipher: Plain Text chỉ được chứa các chữ cái A-Z, không được chứa số hoặc ký tự đặc biệt."
            )

        # Cảnh báo nếu Plaintext có chữ J
        if 'J' in str(plaintext).upper():
            self.warnings.append("⚠️ Bản rõ chứa chữ 'J', hệ thống đã tự động chuyển thành 'I'.")

        plaintext = "".join(
            [
                char
                for char in plaintext.upper().replace('J', 'I')
                if char.isalpha()
            ]
        )

        ciphertext = ""
        i = 0

        while i < len(plaintext):

            first_letter = plaintext[i]

            if i + 1 < len(plaintext):
                second_letter = plaintext[i + 1]
            else:
                second_letter = 'X'
                # Cảnh báo: Ký tự bị lẻ ở cuối
                self.warnings.append(f"⚠️ Chữ '{first_letter}' đứng một mình ở cuối, hệ thống tự động chèn thêm 'X'.")

            if first_letter == second_letter:
                inserted_char = 'Q' if first_letter == 'X' else 'X'
                second_letter = inserted_char
                # Cảnh báo: 2 chữ cái trùng nhau
                self.warnings.append(f"⚠️ Cặp '{first_letter}{first_letter}' trùng nhau, hệ thống tự động chèn '{inserted_char}' vào giữa.")
                i += 1
            else:
                i += 2

            pos1 = self.find_position(first_letter)
            pos2 = self.find_position(second_letter)

            if pos1[0] == pos2[0]:

                ciphertext += self.matrix[pos1[0]][(pos1[1] + 1) % 5]
                ciphertext += self.matrix[pos2[0]][(pos2[1] + 1) % 5]

            elif pos1[1] == pos2[1]:

                ciphertext += self.matrix[(pos1[0] + 1) % 5][pos1[1]]
                ciphertext += self.matrix[(pos2[0] + 1) % 5][pos2[1]]

            else:

                ciphertext += self.matrix[pos1[0]][pos2[1]]
                ciphertext += self.matrix[pos2[0]][pos1[1]]

        return ciphertext

    def decrypt(self, ciphertext):

        # ===== KIỂM TRA CIPHERTEXT =====
        if not ciphertext or not str(ciphertext).strip():
            raise ValueError(
                "Playfair Cipher: Cipher Text không được để trống."
            )

        if not str(ciphertext).replace(" ", "").isalpha():
            raise ValueError(
                "Playfair Cipher: Cipher Text chỉ được chứa các chữ cái A-Z, không được chứa số hoặc ký tự đặc biệt."
            )

        ciphertext = "".join(
            [
                char
                for char in ciphertext.upper().replace('J', 'I')
                if char.isalpha()
            ]
        )

        plaintext = ""
        i = 0

        while i < len(ciphertext):

            first_letter = ciphertext[i]

            if i + 1 < len(ciphertext):
                second_letter = ciphertext[i + 1]
            else:
                second_letter = 'X'

            pos1 = self.find_position(first_letter)
            pos2 = self.find_position(second_letter)

            if pos1[0] == pos2[0]:

                plaintext += self.matrix[pos1[0]][(pos1[1] - 1) % 5]
                plaintext += self.matrix[pos2[0]][(pos2[1] - 1) % 5]

            elif pos1[1] == pos2[1]:

                plaintext += self.matrix[(pos1[0] - 1) % 5][pos1[1]]
                plaintext += self.matrix[(pos2[0] - 1) % 5][pos2[1]]

            else:

                plaintext += self.matrix[pos1[0]][pos2[1]]
                plaintext += self.matrix[pos2[0]][pos1[1]]

            i += 2

        return plaintext

    def encrypt_text(self, text, key=None):
        return self.encrypt(text)

    def decrypt_text(self, text, key=None):
        return self.decrypt(text)


# ==========================================
# CÁCH TEST ĐỂ XEM CẢNH BÁO
# ==========================================
if __name__ == "__main__":
    try:
        # Cố tình tạo một trường hợp kích hoạt nhiều cảnh báo
        print("Đang mã hóa chuỗi: 'JAPPLE' với Key: 'NINJA'\n")
        
        cipher = PlayfairCipher("NINJA")
        result = cipher.encrypt("JAPPLE")
        
        print(f"✅ Bản mã kết quả: {result}\n")
        
        # In các cảnh báo thu thập được
        if cipher.warnings:
            print("🔔 LỊCH SỬ CHỈNH SỬA TỰ ĐỘNG:")
            for warn in cipher.warnings:
                print(warn)
                
    except ValueError as e:
        print(f"❌ LỖI NGHIÊM TRỌNG: {e}")