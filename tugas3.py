class Data:
    def __init__(self, nama, usia, matakuliah, status, jurusan):
        self.nama = nama
        self.usia = usia
        self.matakuliah = matakuliah
        self.status = status
        self.jurusan = jurusan



    def infoDosen(self):
        return(f"{self.nama} sedang {self.status} {self.matakuliah}")
    
    def infoMahasiswa(self):
        return(f"{self.nama} sedang {self.status} {self.jurusan}")
    


class Dosen(Data):
    def __init__(self,nidn):
        self.nidn = nidn


class Mahasiswa(Data):
    def __init__(self,nim):
        self.nim = nim


Dosen1 = Dosen("123456")
Dosen1.nama = "edy"
Dosen1.usia = "17"
Dosen1.status = "mengajar"
Dosen1.matakuliah = "pemorgaman Beroentasi objek"
print(Dosen1.infoDosen())


Mahasiswa1 = Mahasiswa("24241176")
Mahasiswa1.nama = "egi ferdiansyah"
Mahasiswa1.usia = "20"
Mahasiswa1.status = "belajar"
Mahasiswa1.jurusan = "PTI"
print(Mahasiswa1.infoMahasiswa())