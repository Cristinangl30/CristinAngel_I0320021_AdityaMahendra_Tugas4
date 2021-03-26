s = "we like apple & pear"
# panjangnya harus 20
print("panjang dari s = %d " % len(s))
print("kemunculan pertama a = %d" % s.index("a"))
print("a muncul sebanyak %d kali" % s.count("a"))
print("Lima Karakter Pertama adalah '%s'" % s[:5])              # Strart to 5
print("Lima Karakter Berikutnya adalah '%s'" % s[5:10])         # 5 to 10
print("Karakter Ketiga belas adalah '%s'" % s [12])             # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" % s[1::2])    # (0-based indexing)
print("Lima Karakter terakhir adalah '%s'" % s[-5:1])           # 5 th-from-last to end
# konversi ke upercase
print("string dalam huruf besar: %s" %s.upper())
# konversi kehuruf lowercase
print("string dalam huruf kecil: %s" %s.lower())
# cek bagaimana string itu di mulai
if s.startswith("Str!"):
    print("String di mulai dengan 'Str'. Good!")
# cek bagaimana string itu di akhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome!'. Good")

#pisahkan string menjadi tiga string yang terpisah
# masing - masing hanya berisi 1 kataprint("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))
print("Pisahkan kata-kata dari string tersebut: %s" % s.split(" "))