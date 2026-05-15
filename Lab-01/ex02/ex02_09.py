import numbers
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = int(input("Nhập số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(numbers):
    print("Là số nguyên tố.")
else:
    print("Không phải số nguyên tố.")
    