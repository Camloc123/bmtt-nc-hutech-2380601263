from .alphatbet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        # Nguyên tắc cổ điển: Lọc chữ cái và chuyển thành in hoa
        text = ''.join([c.upper() for c in text if c.isalpha()])
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        
        return ''.join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = ''.join([c.upper() for c in text if c.isalpha()])
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        
        return ''.join(decrypted_text)
