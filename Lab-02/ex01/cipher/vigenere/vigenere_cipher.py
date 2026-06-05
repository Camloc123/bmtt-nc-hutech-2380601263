class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        # Nguyên tắc cổ điển: Lọc chữ cái và chuyển thành in hoa
        plain_text = ''.join([c.upper() for c in plain_text if c.isalpha()])
        key = ''.join([c.upper() for c in key if c.isalpha()])
        
        if not plain_text or not key:
            return ''

        encrypted_text = ''
        for i, char in enumerate(plain_text):
            key_shift = ord(key[i % len(key)]) - ord('A')
            encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                
        return encrypted_text          
    
    def vigenere_decrypt(self, cipher_text, key): 
        cipher_text = ''.join([c.upper() for c in cipher_text if c.isalpha()])
        key = ''.join([c.upper() for c in key if c.isalpha()])
        
        if not cipher_text or not key:
            return ''

        decrypted_text = ''
        for i, char in enumerate(cipher_text):
            key_shift = ord(key[i % len(key)]) - ord('A')
            decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                
        return decrypted_text
