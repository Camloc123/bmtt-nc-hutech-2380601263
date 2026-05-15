def tinh_tong_so_chan(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong
input_list = input("Nhập danh sách số (cách nhau bởi dấu phẩy): ")
numbers = [int(i) for i in input_list.split(",")]
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:",tong_chan)