class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        # Chỉ giữ chữ cái và chuyển thành in hoa
        plain_text = ''.join(c.upper() for c in plain_text if c.isalpha())
        key = ''.join(c.upper() for c in key if c.isalpha())

        if not plain_text or not key:
            return "Lỗi: Plain Text hoặc Key rỗng!"

        if len(key) > len(plain_text):
            return "Lỗi: Key không được dài hơn Plain Text!"

        encrypted_text = ""

        for i, char in enumerate(plain_text):
            key_shift = ord(key[i % len(key)]) - ord('A')
            encrypted_text += chr(
                (ord(char) - ord('A') + key_shift) % 26 + ord('A')
            )

        return encrypted_text

    def vigenere_decrypt(self, cipher_text, key):
        # Chỉ giữ chữ cái và chuyển thành in hoa
        cipher_text = ''.join(c.upper() for c in cipher_text if c.isalpha())
        key = ''.join(c.upper() for c in key if c.isalpha())

        if not cipher_text or not key:
            return "Lỗi: Cipher Text hoặc Key rỗng!"

        if len(key) > len(cipher_text):
            return "Lỗi: Key không được dài hơn Cipher Text!"

        decrypted_text = ""

        for i, char in enumerate(cipher_text):
            key_shift = ord(key[i % len(key)]) - ord('A')
            decrypted_text += chr(
                (ord(char) - ord('A') - key_shift) % 26 + ord('A')
            )

        return decrypted_text