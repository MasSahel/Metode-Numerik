import numpy as np

# mendefinisikan matriks dengan angka-angka di dalamnya sebagai A dan vektor yang jadi jawabannya sebagai B.
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)
B = np.array([5, 3, 4], dtype=float)

# a) ini adalah Fungsi untuk menyelesaikan sistem persamaan linier dengan eliminasi Gauss
def gauss_elimination(A, B):
    n = len(B)
    # Membentuk matriks yang di perbesar
    M = np.hstack([A, B.reshape(-1, 1)])
    
    # Eliminasi maju
    for i in range(n):
        # Pivots
        baris_maksimal = np.argmax(abs(M[i:, i])) + i
        M[[i, baris_maksimal]] = M[[baris_maksimal, i]]
        
        for j in range(i+1, n):
            faktor = M[j][i] / M[i][i]
            M[j] = M[j] - faktor * M[i]
    
    # Substitusi Mundur
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:])) / M[i, i]
    return x

# b) ini adalah Fungsi untuk menghitung determinan matriks menggunakan ekspansi kofaktor
def determinant(matriks):
    if matriks.shape[0] == 1:
        return matriks[0, 0]
    det = 0
    for kolom in range(matriks.shape[1]):
        minor = np.delete(np.delete(matriks, 0, axis=0), kolom, axis=1)
        det += ((-1) ** kolom) * matriks[0, kolom] * determinant(minor)
    return det

# c) memakai fungsi eliminasi Gauss dengan tujuan mencari solusi
solusi_gauss = gauss_elimination(A.copy(), B.copy())
print("Solusi memakai cara Eliminasi Gauss:", solusi_gauss)

# d) Implementasi metode Gauss-Jordan
def gauss_jordan(A, B):
    n = len(B)
    # Membentuk matriks augmented
    M = np.hstack([A, B.reshape(-1, 1)])
    
    # Eliminasi Gauss-Jordan
    for i in range(n):
        M[i] = M[i] / M[i, i]  # Buat pivot menjadi 1
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j, i] * M[i]
    
    return M[:, -1]

solusi_gauss_jordan = gauss_jordan(A.copy(), B.copy())
print("Solusi memakai cara Gauss-Jordan:", solusi_gauss_jordan)

# e) ini adalah Fungsi untuk menghitung invers matriks dengan metode adjoint
def cofactor(matriks, baris, kolom):
    minor = np.delete(np.delete(matriks, baris, axis=0), kolom, axis=1)
    return ((-1) ** (baris + kolom)) * determinant(minor)

def adjoint(matriks):
    n = matriks.shape[0]
    adj = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            adj[j, i] = cofactor(matriks, i, j)  # Catatan: Transpos (adjoin)
    return adj

def inverse_adjoint(matriks):
    det = determinant(matriks)
    if det == 0:
        raise ValueError("Matriks singular, nggak punya invers.")
    adj = adjoint(matriks)
    return adj / det

inverse_A = inverse_adjoint(A)
print("Invers matriks A menggunakan metode adjoint:")
print(inverse_A)

# menverifikasi solusi dengan invers
solusi_pakai_invers = np.dot(inverse_A, B)
print("Solusi pakai invers matriks:", solusi_pakai_invers)

#Secara keseluruhan, kode ini menunjukkan beberapa metode yang efektif untuk menyelesaikan sistem persamaan linier. Masing-masing metode memiliki keunggulan tersendiri, tetapi semua menghasilkan solusi yang sama. Ini menunjukkan fleksibilitas dalam pendekatan penyelesaian masalah matematika, dan pentingnya memahami berbagai metode untuk mendapatkan hasil yang akurat.