print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
print("\nCác dòng văn bản bạn đã nhập (viết hoa):")
for line in lines:
    print(line.upper())