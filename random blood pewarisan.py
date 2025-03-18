import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        # Mengambil alel dari ayah dan ibu
        self.blood_type = self.inherit_blood_type(father.blood_type, mother.blood_type)

    def inherit_blood_type(self, father_blood, mother_blood):
        # Mendapatkan alel dari ayah dan ibu
        father_allele = random.choice(father_blood)
        mother_allele = random.choice(mother_blood)
        
        # Menggabungkan alel untuk menentukan golongan darah
        return self.combine_alleles(father_allele, mother_allele)

    def combine_alleles(self, allele1, allele2):
        # Menggabungkan alel untuk menentukan golongan darah
        if allele1 == 'A' and allele2 == 'A':
            return 'A'
        elif allele1 == 'A' and allele2 == 'B':
            return 'AB'
        elif allele1 == 'B' and allele2 == 'A':
            return 'AB'
        elif allele1 == 'B' and allele2 == 'B':
            return 'B'
        elif allele1 == 'O' and allele2 == 'A':
            return 'A'
        elif allele1 == 'A' and allele2 == 'O':
            return 'A'
        elif allele1 == 'O' and allele2 == 'B':
            return 'B'
        elif allele1 == 'B' and allele2 == 'O':
            return 'B'
        elif allele1 == 'O' and allele2 == 'O':
            return 'O'
        else:
            return 'Unknown'

# Input dari pengguna
father_blood_type = input("Masukkan golongan darah ayah (A, B, AB, O): ").strip().upper()
mother_blood_type = input("Masukkan golongan darah ibu (A, B, AB, O): ").strip().upper()

# Membuat objek Father dan Mother
father = Father(father_blood_type)
mother = Mother(mother_blood_type)

# Membuat objek Child
child = Child(father, mother)

# Menampilkan hasil
print(f"Golongan darah anak: {child.blood_type}")