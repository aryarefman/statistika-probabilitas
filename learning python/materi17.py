# format string

# contoh generic
# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = "angka =" + str(angka) # format biasa
format_str = f"angka = {angka}" # format string
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str_ribuan = f"ribuan = {angka:,}"
print(format_str_ribuan)

angka = 2000000
format_str_jutaan = f"jutaan = {angka:,}"
print(format_str_jutaan)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # jika ingin mengambil 2 angka di belakang koma
format_str = f"desimal = {angka:.3f}" # jika ingin mengambil 3 angka di belakang koma
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:09.3f}" # menambah 0 di depan angka
print(format_str)
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda plus + atau minus -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp{harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)