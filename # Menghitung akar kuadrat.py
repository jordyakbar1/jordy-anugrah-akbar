import math

while True:
    try:
        angka = input("Masukkan sebuah angka: ")
        
        # Cek apakah input adalah angka
        angka = float(angka)
        
        # Cek apakah angka negatif
        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
            continue
        
        # Cek apakah angka nol
        if angka == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            continue
        
        # Hitung akar kuadrat
        akar_kuadrat = math.sqrt(angka)
        print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat:.1f}")
        break  # Keluar dari loop jika input valid

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")