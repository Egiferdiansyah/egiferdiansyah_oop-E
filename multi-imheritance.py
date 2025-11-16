# CLASS PARENT

class Alumni:
    def lulus(self):
        print("Mahasiswa ini lulus tahun 2023")

class MahasiswaAktif:
    def masuk(self):
        print("Mahasiswa ini masuk tahun 2020")


# CLASS CHILD

class KTM(MahasiswaAktif):
    def tampil_ktm(self):
        print("Ini adalah KTM mahasiswa aktif")

class Ijazah(Alumni):
    def tampil_ijazah(self):
        print("Ini adalah ijazah alumni")

class Beasiswa(MahasiswaAktif, Alumni):
    def info_beasiswa(self):
        print("Mahasiswa ini menerima beasiswa")



ktm = KTM()
ijazah = Ijazah()
beasiswa = Beasiswa()

print("KTM")
ktm.masuk()
ktm.tampil_ktm()

print("Ijazah")
ijazah.lulus()
ijazah.tampil_ijazah()

print("beasiswa")
beasiswa.masuk()
beasiswa.lulus()
beasiswa.info_beasiswa()
