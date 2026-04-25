
# Hayvan Barınağı 
# Dil: Python


#  TEMEL SINIF: Hayvan
class Hayvan:

    # Kurucu metot
    def __init__(self, isim, yas, ses):
        self.isim  = isim    # public: dışarıdan herkes erişebilir
        self.__yas = yas     # private: sadece bu sınıf içinden erişilir , Çift alt çizgi (__)
        self._ses  = ses     # protected: bu sınıf ve alt sınıflar erişebilir ,  Tek alt çizgi (_)

    # Yaşı döndüren metot (private alana dışarıdan erişim)
    def yas_al(self):
        return self.__yas

    # Genel bilgi yazdıran metot
    def bilgi_goster(self):
        print(f"İsim: {self.isim}, Yaş: {self.__yas}")

    # Ses çıkaran metot
    def ses_cikar(self):
        print(f"{self.isim} sesi: {self._ses}")


#  ALT SINIF 1: Kopek (Hayvan'dan kalıtım alır)
class Kopek(Hayvan):

    # Kurucu metot — super() ile üst sınıfı çağırır
    def __init__(self, isim, yas, irk):
        super().__init__(isim, yas, "Hav hav!")  # Hayvan.__init__ çağrısı
        self.irk = irk   # public: köpeğe özgü alan

    # Köpeğe özgü bilgi metodu
    def bilgi_goster(self):
        super().bilgi_goster()       # önce temel bilgileri yazdır
        print(f"Irk: {self.irk}")


# ALT SINIF 2: Kedi (Hayvan'dan kalıtım alır)
class Kedi(Hayvan):

    # Kurucu metot
    def __init__(self, isim, yas, tuy_rengi):
        super().__init__(isim, yas, "Miyav!")    # Hayvan.__init__ çağrısı
        self.tuy_rengi = tuy_rengi   # public: kediye özgü alan

    # Kediye özgü bilgi metodu
    def bilgi_goster(self):
        super().bilgi_goster()       # önce temel bilgileri yazdır
        print(f"Tüy Rengi: {self.tuy_rengi}")


#  ANA PROGRAM
print("=== HAYVAN BARINAGI ===\n")

# Köpek nesnesi oluştur
k = Kopek("Karabaş", 3, "Golden Retriever")

# Kedi nesnesi oluştur
kedi = Kedi("Pamuk", 2, "Beyaz")

# Köpek bilgilerini göster
print("-- Köpek --")
k.bilgi_goster()
k.ses_cikar()

print()

# Kedi bilgilerini göster
print("-- Kedi --")
kedi.bilgi_goster()
kedi.ses_cikar()