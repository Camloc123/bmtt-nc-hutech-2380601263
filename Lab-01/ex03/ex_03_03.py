def tao_tuple_tu_list(list):
    return tuple(list)
input_list = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")
numbers = list(map(int,input_list.split(",")))
print("List là: ", numbers)
print("Tuple được tạo từ list là: ", tao_tuple_tu_list(numbers))