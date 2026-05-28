class TranspositionCipher:
    def __init__(self, key):
        self.key = str(key)  # Đảm bảo khóa luôn ở dạng chuỗi

    def encrypt(self, plaintext):
        if not plaintext:
            return ""
            
        num_cols = len(self.key)
        if num_cols == 0:
            return plaintext
            
        # Tính toán số lượng hàng cần thiết cho ma trận
        num_rows = (len(plaintext) + num_cols - 1) // num_cols
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

        # Điền văn bản vào ma trận theo hàng
        index = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if index < len(plaintext):
                    matrix[r][c] = plaintext[index]
                    index += 1

        # Sắp xếp thứ tự các cột dựa trên khóa để đọc dữ liệu (sắp xếp ổn định)
        col_order = sorted(range(num_cols), key=lambda x: self.key[x])
        
        # Đọc dữ liệu từ ma trận theo cột đã sắp xếp và tối ưu hóa nối chuỗi bằng join()
        return "".join(matrix[r][k] for k in col_order for r in range(num_rows) if matrix[r][k])

    def decrypt(self, ciphertext):
        if not ciphertext:
            return ""
            
        num_cols = len(self.key)
        if num_cols == 0:
            return ciphertext
            
        # Tính toán số lượng hàng cần thiết
        num_rows = (len(ciphertext) + num_cols - 1) // num_cols
        matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

        # Sắp xếp thứ tự các cột dựa trên khóa
        col_order = sorted(range(num_cols), key=lambda x: self.key[x])
        
        # Tính toán số lượng ký tự thực tế có trong từng cột (để giải quyết vấn đề ma trận không đầy đủ)
        rem = len(ciphertext) % num_cols
        col_lengths = {c: (num_rows if (c < rem or rem == 0) else num_rows - 1) for c in range(num_cols)}

        # Đặt văn bản đã mã hóa vào ma trận theo cột dựa trên thứ tự khóa và độ dài thực tế của cột đó
        index = 0
        for k in col_order:
            for r in range(col_lengths[k]):
                if index < len(ciphertext):
                    matrix[r][k] = ciphertext[index]
                    index += 1

        # Đọc dữ liệu theo hàng để khôi phục bản rõ ban đầu, tối ưu hóa bằng join()
        return "".join(matrix[r][c] for r in range(num_rows) for c in range(num_cols) if matrix[r][c])