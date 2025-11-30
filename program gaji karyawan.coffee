# Program menghitung gaji karyawan berdasarkan golongan dan lembur

# Array gaji sesuai golongan
gaji = [5000000, 6500000, 9500000]  # Gaji untuk golongan A, B, C
lembur_persen = [30, 32, 34, 36, 38]  # Persentase lembur

# Input golongan karyawan
golongan = input("Masukkan golongan (A/B/C): ").upper()

# Input jam lembur
jam_lembur = int(input("Masukkan jam lembur: "))

# Mengambil gaji pokok berdasarkan golongan
if golongan == "A":
    gaji_pokok = gaji[0]
elif golongan == "B":
    gaji_pokok = gaji[1]
elif golongan == "C":
    gaji_pokok = gaji[2]
else:
    print("Golongan tidak valid.")
    exit()

# Menghitung gaji lembur
if jam_lembur == 1:
    gaji_lembur = (lembur_persen[0] / 100) * gaji_pokok
elif jam_lembur == 2:
    gaji_lembur = (lembur_persen[1] / 100) * gaji_pokok
elif jam_lembur == 3:
    gaji_lembur = (lembur_persen[2] / 100) * gaji_pokok
elif jam_lembur == 4:
    gaji_lembur = (lembur_persen[3] / 100) * gaji_pokok
elif jam_lembur >= 5:
    gaji_lembur = (lembur_persen[4] / 100) * gaji_pokok
else:
    gaji_lembur = 0

# Menghitung total gaji
total_gaji = gaji_pokok + gaji_lembur

# Menampilkan hasil
print(f"Gaji Pokok: Rp. {gaji_pokok}")
print(f"Gaji Lembur: Rp. {gaji_lembur}")
print(f"Total Gaji: Rp. {total_gaji:.2f}")
