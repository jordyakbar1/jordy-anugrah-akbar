from abc import ABC, abstractmethod

# Kelas Abstrak
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Setter untuk nama
    def set_name(self, name: str):
        if not name:
            raise ValueError("Nama tidak boleh kosong.")
        self.__name = name

    # Getter untuk usia
    def get_age(self):
        return self.__age

    # Setter untuk usia
    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Usia tidak boleh negatif.")
        self.__age = age

# Kelas Turunan
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Fungsi untuk menambahkan hewan
def add_animal(animal_type: str, name: str, age: int):
    if not name:
        raise ValueError("Nama hewan tidak boleh kosong.")
    if age < 0:
        raise ValueError("Usia hewan tidak boleh negatif.")

    if animal_type.lower() == "dog":
        return Dog(name, age)
    elif animal_type.lower() == "cat":
        return Cat(name, age)
    else:
        raise ValueError("Tipe hewan tidak dikenali. Harap masukkan 'dog' atau 'cat'.")

# Fungsi untuk mendapatkan input dari pengguna
def get_user_input():
    animal_type = input("Masukkan jenis hewan (dog/cat): ")
    name = input("Masukkan nama hewan: ")
    age = int(input("Masukkan usia hewan: "))
    return animal_type, name, age

# Contoh Penggunaan
def main():
    try:
        animal_type, name, age = get_user_input()
        animal = add_animal(animal_type, name, age)

        print(f"{animal.get_name()} says: {animal.make_sound()}")

        # Mengubah nama dan usia
        new_name = input("Masukkan nama baru untuk hewan: ")
        new_age = int(input("Masukkan usia baru untuk hewan: "))
        animal.set_name(new_name)
        animal.set_age(new_age)

        print(f"{animal.get_name()} is now {animal.get_age()} years old and says: {animal.make_sound()}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()