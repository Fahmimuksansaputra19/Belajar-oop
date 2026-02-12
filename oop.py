#Program oop sederhana
class Siswa:
    def __init__(self, nama, kelas, nilai):
     self.nama = nama
     self.kelas = kelas
     self.nilai = nilai

    def status(self):
     if self.nilai >= 98:
      return "Terbaik"
     elif self.nilai >= 88:
      return "Bagus"
     elif self.nilai >= 75:
      return "Cukup"
     else:
      return "Tidak Lulus"

class No_Siswa(Siswa):
    def __init__(self, nama, kelas, nilai, nomor, gander):
     super().__init__(nama, kelas, nilai)
     self.nomor = nomor
     self.gander = gander

    def info(self):
     print ("Nama: ", self.nama)
     print ("Gander:", self.gander)
     print ("Kelas: ",self.kelas)
     print ("No absen: ", self.nomor)
     print ("Nilai: ",self.nilai)
     print ("Status: ",self.status())

data_siswa = []

data_siswa.append(No_Siswa("Kevin Triputra Sucipto", "XII TJKT 4", 100, 1, "laki-laki"))
data_siswa.append(No_Siswa("Shakila Virginia", "XII TJKT 4", 90, 2 , "perempuan"))
data_siswa.append(No_Siswa("Muhammad Shafwan Maulana", "XII TJKT 4", 85, 3, "laki-laki"))

while True:
 tanya = input("Apakah anda ingin melihat data siswa (ya/tidak)???")
 if tanya.lower() == "ya":
  for siswa in data_siswa:
   print ("=============================")
   siswa.info()
  break
 elif tanya.lower() == "tidak":
   print ("========== Sampai Jumpa ==========")
   break
 else:
  print ("========== Data yang anda carai tidai ada ==========")
