
def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict
input_string = input("Nhập Dánh sách số (cách nhau bởi dấu phẩy): ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của phần tử là: ", so_lan_xuat_hien)