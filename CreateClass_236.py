class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def keliling(self):
        return 2 * (self.p + self.l)

    def luas(self):
        return self.p * self.l

    def __str__(self):
        return f"Persegi panjang, panjang {self.p} cm, dan lebar {self.l} cm"

def main():
    # Meminta input panjang dan lebar dari pengguna
    p = float(input("Masukkan panjang (cm): "))
    l = float(input("Masukkan lebar (cm): "))

    # Membuat objek PersegiPanjang
    persegi_panjang = PersegiPanjang(p, l)

    # Menampilkan hasil
    print(persegi_panjang)  
    print("Keliling:", persegi_panjang.keliling(), "cm")
    print("Luas:", persegi_panjang.luas(), "cm²")

# Menjalankan fungsi main
if __name__ == "__main__":
    main()
