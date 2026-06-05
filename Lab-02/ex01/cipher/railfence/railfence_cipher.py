class RailFenceCipher:
    def __init__(self):
        pass

    def railfence_encrypt(self, plaintext: str, num_rails: int) -> str:
        # Nguyên tắc cổ điển: Lọc chữ cái và chuyển thành in hoa
        plaintext = ''.join([c.upper() for c in plaintext if c.isalpha()])
        
        if num_rails <= 1 or not plaintext:
            return plaintext
        
        rails = [[] for _ in range(num_rails)]
        current_rail = 0
        direction = 1
        
        for char in plaintext:
            rails[current_rail].append(char)
            current_rail += direction
            if current_rail == 0 or current_rail == num_rails - 1:
                direction *= -1
        return ''.join([''.join(rail) for rail in rails])

    def railfence_decrypt(self, ciphertext: str, num_rails: int) -> str:
        ciphertext = ''.join([c.upper() for c in ciphertext if c.isalpha()])
        
        if num_rails <= 1 or not ciphertext:
            return ciphertext
        
        n = len(ciphertext)
        grid = [['\n' for _ in range(n)] for _ in range(num_rails)]
        
        current_rail = 0
        direction = 1
        for col in range(n):
            grid[current_rail][col] = '*'
            current_rail += direction
            if current_rail == 0 or current_rail == num_rails - 1:
                direction *= -1
        
        char_idx = 0
        for r in range(num_rails):
            for c in range(n):
                if grid[r][c] == '*' and char_idx < n:
                    grid[r][c] = ciphertext[char_idx]
                    char_idx += 1
        
        plaintext = []
        current_rail = 0
        direction = 1
        for col in range(n):
            plaintext.append(grid[current_rail][col])
            current_rail += direction
            if current_rail == 0 or current_rail == num_rails - 1:
                direction *= -1
                
        return ''.join(plaintext)
