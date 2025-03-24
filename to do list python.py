class TugasTidakDitemukanError(Exception):
    """Exception yang diangkat ketika tugas tidak ditemukan."""
    pass

class InputTidakValidError(Exception):
    """Exception yang diangkat untuk input yang tidak valid."""
    pass

class DaftarTugas:
    def __init__(self):
        self.tugas = []

    def tambah_tugas(self, tugas):
        if not tugas:
            raise InputTidakValidError("Tugas tidak boleh kosong.")
        self.tugas.append(tugas)
        print("Tugas berhasil ditambahkan!")

    def hapus_tugas(self, nomor_tugas):
        if nomor_tugas < 1 or nomor_tugas > len(self.tugas):
            raise TugasTidakDitemukanError(f"Tugas dengan nomor {nomor_tugas} tidak ditemukan.")
        tugas_dihapus = self.tugas.pop(nomor_tugas - 1)
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")

    def tampilkan_tugas(self):
        if not self.tugas:
            print("Daftar Tugas kosong.")
            return
        print("Daftar Tugas:")
        for index, tugas in enumerate(self.tugas, start=1):
            print(f"{index}. {tugas}")

def main():
    daftar_tugas = DaftarTugas()

    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
            if pilihan == 1:
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                daftar_tugas.tambah_tugas(tugas)
            elif pilihan == 2:
                nomor_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                daftar_tugas.hapus_tugas(nomor_tugas)
            elif pilihan == 3:
                daftar_tugas.tampilkan_tugas()
            elif pilihan == 4:
                print("Keluar dari program.")
                break
            else:
                raise InputTidakValidError("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")
        except (TugasTidakDitemukanError, InputTidakValidError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()