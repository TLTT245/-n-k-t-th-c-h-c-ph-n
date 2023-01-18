from staff import NhanVien
def nhap_danh_sach_nhan_vien(ds_nhan_vien):
    while True:
        hoten = input("Nhập họ tên nhân viên (nhập 'e' để dừng nhập): ")
        if hoten == 'e':
            break
        tuoi = int(input("Nhập tuổi nhân viên: "))
        luong = int(input("Nhập lương nhân viên: "))
        nhan_vien = NhanVien(hoten, tuoi, luong)
        ds_nhan_vien.append(nhan_vien)
    return ds_nhan_vien
def in_danh_sach_nhan_vien(ds_nhan_vien):
    for item in ds_nhan_vien:
        print(item)
    return item
def sap_xep_danh_sach(ds_nhan_vien):
    ds_nhan_vien = sorted(ds_nhan_vien, reverse=True)
    for i in ds_nhan_vien:
        print(i)
    return i
def luu_tap_tinnhiphan(ds_nhan_vien):
    with open('NhanVien.bin','wb') as f:
        pickle.dump(ds_nhan_vien, f)
def doc_tap_tinnhiphan(ds_nhan_vien):
    with open('NhanVien.bin', 'rb') as f:
       nv = pickle.load(f)
    print(ds_nhan_vien)
import pickle
def main():
    sv=[]
    f =  nhap_danh_sach_nhan_vien(sv)
    in_danh_sach_nhan_vien(f)
    print('Sắp xếp danh sách Theo tuổi giảm dần \n')
    sap_xep_danh_sach(f)
    luu_tap_tinnhiphan(f)
    print('Lưu tập tin thành công')
    doc_tap_tinnhiphan(f)
if __name__ == "__main__":
    main()