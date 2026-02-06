
import pandas as pd

df = pd.read_excel("Book1 1 (2).xlsx")
df.drop(df.columns[df.columns.str.contains(
    'Unnamed', case=False)], axis=1, inplace=True)
df

mien_bac = [
    'hanoi', 'hai phong', 'quang ninh', 'hai duong', 'hung yen', 'nam dinh',
    'ninh binh', 'thai binh', 'vinh phuc', 'ha giang', 'cao bang', 'bac kan',
    'lang son', 'tuyen quang', 'thai nguyen', 'phu tho', 'bac giang', 'lao cai',
    'yen bai', 'dien bien', 'hoa binh', 'lai chau', 'son la', 'bac ninh'
]

mien_trung = [
    'thanh hoa', 'nghe an', 'ha tinh', 'quang binh', 'quang tri', 'thua thien hue', 'hue',
    'da nang', 'quang nam', 'quang ngai', 'binh dinh', 'phu yen', 'khanh hoa', 'nha trang',
    'ninh thuan', 'binh thuan', 'kon tum', 'gia lai', 'dak lak', 'dak nong', 'lam dong', 'da lat'
]

mien_nam = [
    'ho chi minh', 'hcm', 'binh duong', 'dong nai', 'tay ninh', 'ba ria', 'vung tau',
    'long an', 'tien giang', 'ben tre', 'tra vinh', 'vinh long', 'dong thap',
    'an giang', 'kien giang', 'can tho', 'hau giang', 'soc trang', 'bac lieu', 'ca mau', 'binh phuoc'
]

def phan_loai_mien(dia_chi):

    # Chuyển địa chỉ về chữ thường để so sánh chính xác
    dia_chi_lower = str(dia_chi).lower()

    # Kiểm tra miền Nam trước (vì TP.HCM xuất hiện nhiều nhất)
    for tinh in mien_nam:
        if tinh in dia_chi_lower:
            return 'Southside'

    # Kiểm tra miền Bắc
    for tinh in mien_bac:
        if tinh in dia_chi_lower:
            return 'Northside'

    # Kiểm tra miền Trung
    for tinh in mien_trung:
        if tinh in dia_chi_lower:
            return 'Central'

    return "Other" # Không tìm thấy từ khóa phù hợp

df["Region"] = df["Addres"].apply(phan_loai_mien)
df

df["Region"].value_counts()

df.to_excel("đây nha chị linh.xlsx", index=False)
