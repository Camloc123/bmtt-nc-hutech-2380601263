from .alphatbet import ALPHABET


class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet: # Kiểm tra xem ký tự có trong bảng chữ cái không
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                # Nếu là khoảng trắng hoặc dấu câu, giữ nguyên không mã hóa
                encrypted_text.append(letter) 
        
        # ĐƯA LỆNH RETURN RA NGOÀI VÒNG LẶP
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)
        
        # ĐƯA LỆNH RETURN RA NGOÀI VÒNG LẶP
        return "".join(decrypted_text)