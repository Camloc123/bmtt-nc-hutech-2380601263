from Sinhvien import Sinhvien

class Quanlysinhvien:
    def __init__(self):
        self.listSinhvien = []

    def generateID(self):
        maxID = 0
        if self.soluongsinhvien() > 0:
            maxID = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if maxID < sv._id:
                    maxID = sv._id
        return maxID + 1

    def soluongsinhvien(self):
        return len(self.listSinhvien)

    def xeploaihocluc(self, sv):
        if sv._diemTb >= 8.0:
            sv._hocluc = "Gioi"
        elif sv._diemTb >= 6.5:
            sv._hocluc = "Kha"
        elif sv._diemTb >= 5.0:
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def nhapsinhvien(self):
        svID = self.generateID()
        print(f"\n--- NHẬP THÔNG TIN SINH VIÊN MỚI (ID: {svID}) ---")
        
        while True:
            name = input("Nhap ten sinh vien: ").strip()
            if name:
                break
            print("Tên sinh viên không được để trống!")
            
        while True:
            sex = input("Nhap gioi tinh sinh vien (Nam/Nu): ").strip()
            if sex:
                break
            print("Giới tính không được để trống!")
            
        while True:
            major = input("Nhap chuyen nghanh sinh vien: ").strip()
            if major:
                break
            print("Chuyên ngành không được để trống!")
            
        while True:
            try:
                diemTb = float(input("Nhap diem sinh vien (0 - 10): "))
                if 0 <= diemTb <= 10:
                    break
                print("Điểm trung bình phải nằm trong khoảng từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập một số thực hợp lệ cho điểm!")
                
        sv = Sinhvien(svID, name, sex, major, diemTb)
        self.xeploaihocluc(sv)
        self.listSinhvien.append(sv)
        print(f"==> Thêm thành công sinh viên: {name} (ID: {svID})")

    def updateSinhvien(self, id):
        sv = self.findByID(id)
        if sv is not None:
            print(f"\n--- CẬP NHẬT THÔNG TIN SINH VIÊN (ID: {id}) ---")
            print("Nhập thông tin mới hoặc nhấn Enter để giữ nguyên giá trị cũ:")
            
            name = input(f"Nhap ten sinh vien ({sv._name}): ").strip()
            if name:
                sv._name = name
                
            sex = input(f"Nhap gioi tinh sinh vien ({sv._sex}): ").strip()
            if sex:
                sv._sex = sex
                
            major = input(f"Nhap chuyen nghanh sinh vien ({sv._major}): ").strip()
            if major:
                sv._major = major
                
            while True:
                diemTb_str = input(f"Nhap diem sinh vien ({sv._diemTb}): ").strip()
                if not diemTb_str:
                    break
                try:
                    diemTb = float(diemTb_str)
                    if 0 <= diemTb <= 10:
                        sv._diemTb = diemTb
                        self.xeploaihocluc(sv)
                        break
                    print("Điểm trung bình phải nằm trong khoảng từ 0 đến 10!")
                except ValueError:
                    print("Vui lòng nhập một số thực hợp lệ!")
                    
            print(f"==> Cập nhật thông tin sinh viên ID {id} thành công!")
        else:
            print(f"==> Không tìm thấy sinh viên có ID = {id}!")

    def deleteSinhvien(self, id):
        sv = self.findByID(id)
        if sv is not None:
            self.listSinhvien.remove(sv)
            print(f"==> Đã xóa thành công sinh viên có ID = {id}!")
            return True
        else:
            print(f"==> Không tìm thấy sinh viên có ID = {id}!")
            return False

    def findByID(self, id):
        for sv in self.listSinhvien:
            if sv._id == id:
                return sv
        return None

    def findByName(self, keyword):
        result = []
        keyword_lower = keyword.lower()
        for sv in self.listSinhvien:
            if keyword_lower in sv._name.lower():
                result.append(sv)
        return result

    def sortByGPA(self):
        self.listSinhvien.sort(key=lambda x: x._diemTb, reverse=True)

    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._name.lower())

    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id)

    def showSinhvien(self, listSV=None):
        if listSV is None:
            listSV = self.listSinhvien
            
        if len(listSV) == 0:
            print("\n==> Danh sách sinh viên trống!")
            return
            
        print("\n" + "="*85)
        print(f"{'ID':<6} | {'Họ và Tên':<25} | {'Giới Tính':<10} | {'Chuyên Ngành':<20} | {'Điểm TB':<8} | {'Học Lực'}")
        print("="*85)
        for sv in listSV:
            print(f"{sv._id:<6} | {sv._name:<25} | {sv._sex:<10} | {sv._major:<20} | {sv._diemTb:<8.2f} | {sv._hocluc}")
        print("="*85)
    def sortByMajor(self):
     # Sắp xếp danh sách sinh viên theo bảng chữ cái của chuyên ngành
     self.listSinhvien.sort(key=lambda x: x._major.lower())