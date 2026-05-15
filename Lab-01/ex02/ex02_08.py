def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan,2)
    if  so_thap_phan % 5 == 0:
        return  True
    else:   
        return False
chuoi_so_nhi_phan = input("Nhập số Nhị phân: ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(",")
so_chia_het_cho_5 = [so_nhi_phan for so_nhi_phan in so_nhi_phan_list if chia_het_cho_5(so_nhi_phan)]
if  len(so_chia_het_cho_5) > 0:
    ket_qua = ",".join(so_chia_het_cho_5)
    print("Các số chia hết cho 5 là: ", ket_qua)
else:
    print("Không có số nào chia hết cho 5 trong chuỗi đã nhâp.")
