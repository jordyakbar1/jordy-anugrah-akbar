import tkinter as tk
from tkinter import messagebox, Scrollbar, Text, END

class AplikasiCatatan:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Catatan")

        self.catatan = []

        # === BAGIAN ATAS ===
        tk.Label(root, text="Judul:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_judul = tk.Entry(root, width=40)
        self.entry_judul.grid(row=0, column=1, columnspan=2, sticky="we", padx=5)

        self.btn_tambah = tk.Button(root, text="Tambah Catatan", command=self.tambah_catatan)
        self.btn_tambah.grid(row=0, column=3, padx=5)

        self.btn_hapus = tk.Button(root, text="Hapus Catatan", command=self.hapus_catatan)
        self.btn_hapus.grid(row=0, column=4, padx=5)

        # === LABEL TENGAH ===
        tk.Label(root, text="Daftar Catatan").grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
        tk.Label(root, text="Isi Catatan").grid(row=1, column=2, columnspan=3, sticky="w", padx=5)

        # === LISTBOX & SCROLLBAR ===
        self.listbox = tk.Listbox(root, width=30, height=15)
        self.listbox.grid(row=2, column=0, columnspan=2, sticky="nswe", padx=(5,0), pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.tampilkan_isi_catatan)

        scrollbar = Scrollbar(root, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=2, column=2, sticky="ns", pady=5)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # === TEXTBOX ISI CATATAN ===
        self.text_isi = Text(root, width=40, height=15)
        self.text_isi.grid(row=2, column=3, columnspan=2, sticky="nswe", padx=5, pady=5)

        # === CONFIGURASI GRID ===
        for i in range(5):
            root.columnconfigure(i, weight=1)
        root.rowconfigure(2, weight=1)

    def tambah_catatan(self):
        judul = self.entry_judul.get().strip()
        isi = self.text_isi.get("1.0", END).strip()

        if not judul or not isi:
            messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
            return

        self.catatan.append({"judul": judul, "isi": isi})
        self.listbox.insert(END, judul)
        self.entry_judul.delete(0, END)
        self.text_isi.delete("1.0", END)

    def tampilkan_isi_catatan(self, event):
        try:
            index = self.listbox.curselection()[0]
            isi = self.catatan[index]["isi"]
            self.text_isi.delete("1.0", END)
            self.text_isi.insert(END, isi)
        except IndexError:
            pass

    def hapus_catatan(self):
        try:
            index = self.listbox.curselection()[0]
            judul = self.catatan[index]["judul"]
            konfirmasi = messagebox.askyesno("Konfirmasi", f"Hapus catatan '{judul}'?")
            if konfirmasi:
                del self.catatan[index]
                self.listbox.delete(index)
                self.text_isi.delete("1.0", END)
        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih catatan yang ingin dihapus.")

# === JALANKAN APLIKASI ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiCatatan(root)
    root.mainloop()
