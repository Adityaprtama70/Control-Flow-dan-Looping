lagi='y'

while lagi=='y':
    
    print ("===============================================================================")

    print ("\t \t Aplikasi Perhitungan Gaji Karyawan \t \t")

    print ("\t \t \t \t \t 2023")

    print ("===============================================================================")

    nip=input("Masukan ID Karyawan \t: ")
    
    nama=input("Masukan Nama Karyawan \t: ")
    
    transpotasi=input("Transpotasi Karyawan \t: ")
    
    jenis_kelamin=input("Jenis Kelamin \t\t: ")
    
    gaji = float(input("Masukkan gaji Anda \t: "))
    
    if gaji >= 8_000_000 and gaji <= 9_000_000:
        jabatan = "Officer"
    elif gaji >= 10_000_000 and gaji <= 11_000_000:
        jabatan = "Supervisor"
    elif gaji >= 12_000_000 and gaji <= 14_000_000:
        jabatan = "Asisten Manajer"
    elif gaji >= 15_000_000:
        jabatan = "Manager"
    else:
        jabatan = "Tidak diketahui"
        
        
    print ("===============================================================================")

    print ("\t \t Aplikasi Perhitungan Gaji Karyawan \t \t")

    print ("\t \t \t \t \t 2023")

    print ("===============================================================================")
    
    print ("")
        
    print ("Nip \t\t: ",nip)
    
    print ("Nama \t\t: ",nama)
    
    print ("Transpotasi \t: ",transpotasi)
        
    print ("Jenis Kelamin \t: ",jenis_kelamin)
    
    print("Gaji Anda \t: Rp. ", gaji)
    
    print("Jabatan Anda \t: ",jabatan)
    
    print ("")
    
    print ("===============================================================================")   
    
    print ("")

lagi=input("Ambil Data Lagi [y/n]? : ")