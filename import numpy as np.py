# Matriks koefisien
A = np.array([[1, 1, 1],
              [1, 2, -1],
              [2, 1, 2]])

# Vektor hasil
b = np.array([6, 2, 10])

# Menggunakan metode numpy untuk menyelesaikan persamaan Ax = b
x = np.linalg.solve(A, b)

# Menampilkan hasil
print("Solusi dari sistem persamaan adalah:")
print(f"x1 = {x[0]}")
print(f"x2 = {x[1]}")
print(f"x3 = {x[2]}")
