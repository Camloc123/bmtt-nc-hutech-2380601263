class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0 
        for char in plain_text:
            if char.isalpha(): # Sửa lỗi chính tả: isaphla() -> isalpha()
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))   
                
                # SỬA LỖI: Lùi dòng này ra ngoài, để cả chữ hoa và chữ thường đều tăng key_index
                key_index += 1
            else:
                encrypted_text += char
                
        # SỬA LỖI: Lùi lệnh return ra hoàn toàn khỏi vòng lặp for
        return encrypted_text          
    
    def vigenere_decrypt(self, cipher_text, key): 
        decrypted_text = ""
        key_index = 0 
        for char in cipher_text:
            if char.isalpha():
                # Tìm khoảng dịch chuyển giống hệt như mã hóa
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                
                if char.isupper():
                    # Thay vì cộng (+ key_shift), ta trừ đi (- key_shift) để giải mã
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                    
                key_index += 1
            else:
                # Giữ nguyên dấu câu và khoảng trắng
                decrypted_text += char
                
        return decrypted_text
    