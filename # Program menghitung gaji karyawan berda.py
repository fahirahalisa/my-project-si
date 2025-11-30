# Program menghitung gaji karyawan berdasarkan golongan dan jam lembur

# Input golongan
golongan = input("Masukkan golongan (A/B/C): ")

# Input jam lembur dengan penanganan kesalahan
while True:
    try:
        jam_lembur = int(input("Masukkan jam lembur: "))
        if jam_lembur < 0:  # Pastikan jam lembur tidak negatif
            print("Jam lembur tidak bisa negatif. Silakan masukkan angka yang valid.")
            continue
        break  # Keluar dari loop jika input valid
    except ValueError:
        print("Input tidak valid! Silakan masukkan angka yang benar.")

# Tentukan gaji pokok berdasarkan golongan menggunakan statement IF
if golongan == 'A':
    gaji_pokok = 5000000
elif golongan == 'B':
    gaji_pokok = 6500000
elif golongan == 'C':
    gaji_pokok = 9500000
else:
    print("Golongan tidak valid. Program berhenti.")
    exit()

# Tentukan persentase gaji lembur berdasarkan jam lembur menggunakan statement IF
if jam_lembur == 1:
    persen_lembur = 0.30
elif jam_lembur == 2:
    persen_lembur = 0.32
elif jam_lembur == 3:
    persen_lembur = 0.34
elif jam_lembur == 4:
    persen_lembur = 0.36
elif jam_lembur >= 5:
    persen_lembur = 0.38
else:
    persen_lembur = 0.0  # Jika jam lembur 0, gaji lembur 0

# Hitung gaji lembur
gaji_lembur = persen_lembur * gaji_pokok

# Hitung total penghasilan
total_penghasilan = gaji_pokok + gaji_lembur

# Output hasil
print(f"Jumlah penghasilan: Rp. {total_penghasilan:,.0f}")
