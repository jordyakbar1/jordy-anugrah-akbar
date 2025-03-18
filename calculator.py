import math

class KalkulatorSederhana:
    def __init__(self, nilai=0):
        self.nilai = nilai

    def __add__(self, lain):
        return KalkulatorSederhana(self.nilai + lain.nilai)

    def __sub__(self, lain):
        return KalkulatorSederhana(self.nilai - lain.nilai)

    def __mul__(self, lain):
        return KalkulatorSederhana(self.nilai * lain.nilai)

    def __truediv__(self, lain):
        if lain.nilai == 0:
            raise ValueError("Tidak dapat membagi dengan nol.")
        return KalkulatorSederhana(self.nilai / lain.nilai)

    def log(self):
        if self.nilai <= 0:
            raise ValueError("Logaritma hanya dapat dihitung untuk nilai positif.")
        return KalkulatorSederhana(math.log(self.nilai))

    def exp(self):
        return KalkulatorSederhana(math.exp(self.nilai))

    def __repr__(self):
        return f"KalkulatorSederhana({self.nilai})"

# Contoh penggunaan
if __name__ == "__main__":
    a = KalkulatorSederhana(10)
    b = KalkulatorSederhana(5)

    print("Penjumlahan:", (a + b))  # 15
    print("Pengurangan:", (a - b))  # 5
    print("Perkalian:", (a * b))     # 50
    print("Pembagian:", (a / b))     # 2.0
    
    c = KalkulatorSederhana(5)
    print("Logaritma:", c.log())  # Sekitar 1.6
    print("Eksponen:", b.exp())  # e^5
