class PlayfairCipher:
    def __init__(self, key):
        # 1. Chuyển key thành in hoa và thay 'J' bằng 'I' để đồng bộ
        self.key = key.upper().replace('J', 'I')
        self.matrix = self.create_matrix()

    def create_matrix(self):
        # Create a 5x5 matrix for the Playfair cipher
        matrix = []
        used_letters = set()

        # Add letters from the key to the matrix
        for char in self.key:
            if char not in used_letters and char.isalpha():
                used_letters.add(char)
                matrix.append(char)

        # Add remaining letters of the alphabet (excluding 'J')
        for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
            if char not in used_letters:
                used_letters.add(char)
                matrix.append(char)

        # Convert the list to a 5x5 matrix
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    # 2. Bổ sung hàm tìm vị trí (row, col) của ký tự trong ma trận
    def find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == char:
                    return (row, col)
        raise ValueError(f"Character {char} not found in matrix.")

    def encrypt(self, plaintext):
        # 3. Chuẩn bị plaintext: xóa khoảng trắng, in hoa, và thay 'J' bằng 'I'
        plaintext = plaintext.replace(" ", "").upper().replace('J', 'I')
        ciphertext = ""

        # Process the plaintext in pairs of letters
        i = 0
        while i < len(plaintext):
            first_letter = plaintext[i]
            second_letter = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

            # 4. Xử lý triệt để nếu 2 chữ cái giống nhau
            if first_letter == second_letter:
                # Nếu chữ cái trùng là 'X', ta dùng 'Q' để chèn thay vì 'X'
                second_letter = 'Q' if first_letter == 'X' else 'X'
                i += 1
            else:
                i += 2

            # Find the positions of the letters in the matrix
            pos1 = self.find_position(first_letter)
            pos2 = self.find_position(second_letter)

            # Encrypt the letters based on their positions
            if pos1[0] == pos2[0]:  # Same row
                ciphertext += self.matrix[pos1[0]][(pos1[1] + 1) % 5]
                ciphertext += self.matrix[pos2[0]][(pos2[1] + 1) % 5]
            elif pos1[1] == pos2[1]:  # Same column
                ciphertext += self.matrix[(pos1[0] + 1) % 5][pos1[1]]
                ciphertext += self.matrix[(pos2[0] + 1) % 5][pos2[1]]
            else:  # Rectangle
                ciphertext += self.matrix[pos1[0]][pos2[1]]
                ciphertext += self.matrix[pos2[0]][pos1[1]]

        return ciphertext

