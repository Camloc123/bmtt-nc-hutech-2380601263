from email import charset
def dao_nguoc_list(list):
    return  list[::-1]
input_list  = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")
numbers = list(map(int,input_list.split(",")))
print("Danh sách sau khi đảo ngược là: ", dao_nguoc_list(numbers))