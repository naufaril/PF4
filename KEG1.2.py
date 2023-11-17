def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

hasil_perkalian = perkalian(6)(6)

print(hasil_perkalian)
