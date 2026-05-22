from Quanlysinhvien import Quanlysinhvien
qlsv = Quanlysinhvien()
while (1 == 1):
        print("     CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (PYTHON)   ")
        print(" 1. Thêm sinh viên mới")
        print(" 2. Cập nhật thông tin sinh viên theo ID")
        print(" 3. Xóa sinh viên theo ID")
        print(" 4. Tìm kiếm sinh viên theo tên")
        print(" 5. Sắp xếp sinh viên theo điểm trung bình (GPA)")
        print(" 6. Sắp xếp sinh viên theo tên chuyên ngành")
        print(" 7. Hiển thị danh sách sinh viên")
        print(" 0. Thoát chương trình")
        
        choice = input("Nhập lựa chọn của bạn (0-7): ").strip()
        
        if choice == '1':
            qlsv.nhapsinhvien()
            
        elif choice == '2':
            if qlsv.soluongsinhvien() == 0:
                print("\n==> Danh sách trống! Không có sinh viên để cập nhật.")
                continue
            try:
                sv_id = int(input("Nhập ID sinh viên cần cập nhật: "))
                qlsv.updateSinhvien(sv_id)
            except ValueError:
                print("ID phải là một số nguyên hợp lệ!")
                
        elif choice == '3':
            if qlsv.soluongsinhvien() == 0:
                print("\n==> Danh sách trống! Không có sinh viên để xóa.")
                continue
            try:
                sv_id = int(input("Nhập ID sinh viên cần xóa: "))
                qlsv.deleteSinhvien(sv_id)
            except ValueError:
                print("ID phải là một số nguyên hợp lệ!")
                
        elif choice == '4':
            if qlsv.soluongsinhvien() == 0:
                print("\n==> Danh sách trống! Không có dữ liệu để tìm kiếm.")
                continue
            keyword = input("Nhập tên (hoặc một phần tên) cần tìm kiếm: ").strip()
            if keyword:
                results = qlsv.findByName(keyword)
                print(f"\n==> Kết quả tìm kiếm cho từ khóa '{keyword}':")
                qlsv.showSinhvien(results)
            else:
                print("Từ khóa tìm kiếm không được để trống!")
                
        elif choice == '5':
            if qlsv.soluongsinhvien() == 0:
                print("\n==> Danh sách trống!")
                continue
            qlsv.sortByGPA()
            print("\n==> Đã sắp xếp danh sách theo điểm trung bình giảm dần!")
            qlsv.showSinhvien()
            
        elif choice == '6':
            if qlsv.soluongsinhvien() == 0:
                print("\n==> Danh sách trống!")
                continue
            qlsv.sortByMajor()
            print("\n==> Đã sắp xếp danh sách theo chuyên ngành A-Z!")
            qlsv.showSinhvien()
            
        elif choice == '7':
            qlsv.showSinhvien()
            
        elif choice == '0':
            print("\nCảm ơn bạn đã sử dụng chương trình!")
            break
            
        else:
            print("\nLựa chọn không hợp lệ! Vui lòng chọn từ 0 đến 7.")
            
        input("\nNhấn Enter để quay lại menu chính...")

