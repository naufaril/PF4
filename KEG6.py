def point(x, y):
    return x, y

def line_equation_of(p1, M):
    #TODO 1: gunakan inner function dan closure untuk menghitung nilai C
    def calculate_C():
        return p1[1] - M * p1[0]

    #TODO 2: panggil fungsi inner untuk mendapatkan nilai C
    C = calculate_C()

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (2, 4) dan bergradien 0:")
print(line_equation_of(point(2, 4), 0))