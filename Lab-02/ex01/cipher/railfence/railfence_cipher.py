class RailFenceCipher:
    def __init__(self):
        pass

    def _validate_input(self, text, num_rails):
        # Kiểm tra num_rails
        if not isinstance(num_rails, int):
            raise ValueError("num_rails phải là số nguyên")

        if num_rails <= 1:
            raise ValueError("num_rails phải lớn hơn 1")

        # Kiểm tra dữ liệu đầu vào
        if text is None or not str(text).strip():
            raise ValueError("Văn bản không được để trống")

        text = str(text)

        # Không cho phép khoảng trắng
        if " " in text:
            raise ValueError(
                "Văn bản không được chứa khoảng trắng"
            )

        # Không cho phép số hoặc ký tự đặc biệt
        if not text.isalpha():
            raise ValueError(
                "Chỉ được nhập các chữ cái A-Z"
            )

        # Chuyển sang chữ hoa
        text = text.upper()

        # Kiểm tra rails
        if num_rails > len(text):
            raise ValueError(
                f"num_rails ({num_rails}) không được lớn hơn "
                f"độ dài văn bản ({len(text)})"
            )

        return text

    def railfence_encrypt(self, plaintext, num_rails):
        plaintext = self._validate_input(
            plaintext,
            num_rails
        )

        rails = [[] for _ in range(num_rails)]

        current_rail = 0
        direction = 1

        for char in plaintext:
            rails[current_rail].append(char)

            if current_rail == 0:
                direction = 1
            elif current_rail == num_rails - 1:
                direction = -1

            current_rail += direction

        return ''.join(
            ''.join(rail)
            for rail in rails
        )

    def railfence_decrypt(self, ciphertext, num_rails):
        ciphertext = self._validate_input(
            ciphertext,
            num_rails
        )

        n = len(ciphertext)

        grid = [
            ['' for _ in range(n)]
            for _ in range(num_rails)
        ]

        current_rail = 0
        direction = 1

        # Đánh dấu đường zigzag
        for col in range(n):
            grid[current_rail][col] = '*'

            if current_rail == 0:
                direction = 1
            elif current_rail == num_rails - 1:
                direction = -1

            current_rail += direction

        # Điền ciphertext
        index = 0
        for r in range(num_rails):
            for c in range(n):
                if grid[r][c] == '*':
                    grid[r][c] = ciphertext[index]
                    index += 1

        # Đọc lại zigzag
        plaintext = []

        current_rail = 0
        direction = 1

        for col in range(n):
            plaintext.append(
                grid[current_rail][col]
            )

            if current_rail == 0:
                direction = 1
            elif current_rail == num_rails - 1:
                direction = -1

            current_rail += direction

        return ''.join(plaintext)