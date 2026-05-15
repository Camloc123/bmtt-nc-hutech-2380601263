so_gio_lam =float(input("Nhập số giờ làm mỗi tuần: "))
luong_thuc_linh = float(input("Nhập số lương  Tiêu Chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh_thuc_te = gio_tieu_chuan * luong_thuc_linh + gio_vuot_chuan * luong_thuc_linh * 1.5
print("Số tiền thực lĩnh thực tế là: ", thuc_linh_thuc_te)
