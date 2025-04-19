import hashlib
def compute_md5(input_string):
    hash_obj = hashlib.md5()
    hash_obj.update(input_string.encode('utf-8'))
    return hash_obj.hexdigest()
string1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
string2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
md5_string1 = compute_md5(string1)
md5_string2 = compute_md5(string2)
print(f"Chuỗi 1: {string1}")
print(f"MD5 của chuỗi 1: {md5_string1}")
print(f"Chuỗi 2: {string2}")
print(f"MD5 của chuỗi 2: {md5_string2}")
if md5_string1 == md5_string2:
    print("Collision được tìm thấy: Cả hai chuỗi có cùng giá trị MD5!")
