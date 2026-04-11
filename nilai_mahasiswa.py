# Data Mahasiswa
mahasiswa = {
    "10121001": "Asep",
    "10121002": "Budi",
    "10121003": "Cecep"
}

# Data Nilai
nilai = {
    "10121001": [50, 70, 40, 80],
    "10121002": [78, 78, 80, 65],
    "10121003": [57, 88, 67, 69]
}

# Menghitung rata-rata tiap mahasiswa
rata_mahasiswa = {}
for nim, nilai_list in nilai.items():
    rata = sum(nilai_list) / len(nilai_list)
    rata_mahasiswa[nim] = rata

# Mencari mahasiswa dengan nilai tertinggi
nim_terbaik = max(rata_mahasiswa, key=rata_mahasiswa.get)
nama_terbaik = mahasiswa[nim_terbaik]
nilai_terbaik = rata_mahasiswa[nim_terbaik]

# Menghitung rata-rata tiap mata kuliah
# MK1, MK2, MK3, MK4
jumlah_mk = len(next(iter(nilai.values())))
rata_mk = []

for i in range(jumlah_mk):
    total = sum(nilai[nim][i] for nim in nilai)
    rata = total / len(nilai)
    rata_mk.append(rata)

# Mencari mata kuliah dengan rata-rata terkecil
mk_terkecil_index = rata_mk.index(min(rata_mk))
mk_terkecil = f"MK{mk_terkecil_index + 1}"
nilai_terkecil = rata_mk[mk_terkecil_index]

# Output
print(f"Mahasiswa Terpintar : {nama_terbaik} (Nilai : {nilai_terbaik:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} (Nilai : {nilai_terkecil:.2f})")