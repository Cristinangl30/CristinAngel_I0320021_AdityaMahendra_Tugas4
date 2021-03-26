#Untuk Mendaftar kursus online,calon siswa harus berusia minimal 21 tahun dan lulus ujian kualifikasi
usia = 21
x = int(input("Berapa usia anda sekarang:"))

if usia <= x :
    print("======== Anda Cukup Umur ========")
    y = input("Apakah anda telah lulus kualifikasi (Y/T) :")
    if y == "Y" :
        print("======= Anda Dapat Mendaftar =======")
    elif y == "T" :
        print("======= Anda Tidak Dapat Mendaftar =======")
else :
    print("======= Anda belum cukup umur=======")