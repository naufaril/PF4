def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

def panggil_dengan(fungsi, arg1, arg2):
    return fungsi(arg1)(arg2)

hasil_perkalian = panggil_dengan(perkalian, 6, 6)

print(hasil_perkalian)