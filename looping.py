# Inisialisasi variabel gaji dan jabatan
gaji_officer = []
gaji_supervisor = []
gaji_asisten_manajer = []
gaji_manager = []

# Loop untuk menginput gaji pegawai dan menentukan jenis jabatan
for i in range(10):
    gaji = int(input(f"Masukkan gaji pegawai ke-{i+1}: "))
    if gaji >= 8_000_000 and gaji <= 9_000_000:
        gaji_officer.append(gaji)
    elif gaji >= 10_000_000 and gaji <= 11_000_000:
        gaji_supervisor.append(gaji)
    elif gaji >= 12_000_000 and gaji <= 14_000_000:
        gaji_asisten_manajer.append(gaji)
    elif gaji >= 15_000_000:
        gaji_manager.append(gaji)
    else:
        print("Gaji tidak valid")

# Menampilkan gaji terbesar dan gaji terkecil
if len(gaji_officer) > 0:
    print("Jabatan: Officer")
    print(f"Gaji terbesar: {max(gaji_officer)}")
    print(f"Gaji terkecil: {min(gaji_officer)}")
if len(gaji_supervisor) > 0:
    print("Jabatan: Supervisor")
    print(f"Gaji terbesar: {max(gaji_supervisor)}")
    print(f"Gaji terkecil: {min(gaji_supervisor)}")
if len(gaji_asisten_manajer) > 0:
    print("Jabatan: Asisten Manajer")
    print(f"Gaji terbesar: {max(gaji_asisten_manajer)}")
    print(f"Gaji terkecil: {min(gaji_asisten_manajer)}")
if len(gaji_manager) > 0:
    print("Jabatan: Manager")
    print(f"Gaji terbesar: {max(gaji_manager)}")
    print(f"Gaji terkecil: {min(gaji_manager)}")