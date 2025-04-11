
# Dasar-dasar Python

# 1. Variabel dan Tipe Data
nama = "John"               # String (text)
umur = 25                  # Integer (bilangan bulat)
tinggi = 170.5            # Float (bilangan desimal)
is_student = True         # Boolean (True/False)

print("\n--- Variabel dan Tipe Data ---")
print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Tinggi: {tinggi} cm")
print(f"Status Pelajar: {is_student}")

# 2. Operasi Matematika
a = 10
b = 3

print("\n--- Operasi Matematika ---")
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} × {b} = {a * b}")
print(f"Pembagian: {a} ÷ {b} = {a / b}")
print(f"Pembagian Bulat: {a} ÷ {b} = {a // b}")
print(f"Sisa Bagi: {a} mod {b} = {a % b}")
print(f"Pangkat: {a} ^ {b} = {a ** b}")

# 3. String dan Manipulasinya
teks = "Belajar Python"

print("\n--- String ---")
print(f"Teks: {teks}")
print(f"Huruf Kapital: {teks.upper()}")
print(f"Huruf Kecil: {teks.lower()}")
print(f"Jumlah Karakter: {len(teks)}")
print(f"Ganti kata: {teks.replace('Python', 'Pemrograman')}")

# 4. List (Array)
buah = ["apel", "jeruk", "mangga", "pisang"]

print("\n--- List ---")
print(f"Semua buah: {buah}")
print(f"Buah pertama: {buah[0]}")
print(f"Buah terakhir: {buah[-1]}")
buah.append("anggur")
print(f"Setelah menambah anggur: {buah}")
buah.remove("jeruk")
print(f"Setelah menghapus jeruk: {buah}")

# 5. Kondisi (if-else)
nilai = 85

print("\n--- Kondisi ---")
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
else:
    print("Nilai D")

# 6. Perulangan (Loop)
print("\n--- Perulangan For ---")
for i in range(5):
    print(f"Perulangan ke-{i + 1}")

print("\n--- Perulangan While ---")
counter = 1
while counter <= 3:
    print(f"Hitungan ke-{counter}")
    counter += 1

# 7. Fungsi
def sapa(nama, waktu="pagi"):
    return f"Selamat {waktu}, {nama}!"

print("\n--- Fungsi ---")
print(sapa("John"))
print(sapa("Jane", "siang"))

# 8. Dictionary (Kamus)
siswa = {
    "nama": "John Doe",
    "umur": 17,
    "hobi": ["membaca", "menulis", "coding"]
}

print("\n--- Dictionary ---")
print(f"Data Siswa: {siswa}")
print(f"Nama: {siswa['nama']}")
print(f"Hobi: {siswa['hobi']}")
