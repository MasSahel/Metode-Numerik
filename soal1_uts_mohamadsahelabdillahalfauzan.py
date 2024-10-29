import numpy as np
import matplotlib.pyplot as plt

# mendefinisikan parameter
L = 0.5  # Henry
C = 10e-6  # Farad
f_target = 1000  # Hz

# Fungsi f(R)
def resonance_frequency(R):
    return (1 / (2 * np.pi)) * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2)))

# ini adalah Fungsi untuk turunan f'(R) pakai analitik
def resonance_frequency_derivative(R):
    return -R / (4 * np.pi * L**2 * np.sqrt((1 / (L * C)) - (R**2 / (4 * L**2))))

# memakai metode Bisection
def bisection_method(target_frekuensi, toleransi=0.1, R_min=0, R_max=100):
    while abs(R_max - R_min) > toleransi:
        R_mid = (R_min + R_max) / 2
        f_mid = resonance_frequency(R_mid)
        
        if f_mid < target_frekuensi:
            R_min = R_mid
        else:
            R_max = R_mid
    
    return (R_min + R_max) / 2

# memakai metode Newton-Raphson
def newton_raphson_method(target_frekuensi, tebakan_awal=50, toleransi=0.1, jumlah_iterasi_maksimum=100):
    R = tebakan_awal
    for i in range(jumlah_iterasi_maksimum):
        f_val = resonance_frequency(R)
        f_deriv = resonance_frequency_derivative(R)
        
        if abs(f_deriv) < 1e-6:
            print("Turunan terlalu kecil, metode Newton-Raphson berhenti.")
            break
        
        R_new = R - (f_val - target_frekuensi) / f_deriv
        if abs(R_new - R) < toleransi:
            return R_new
        R = R_new
    
    return R

# ini adalah Hasil dari kedua metode
R_bisection = bisection_method(f_target)
R_newton_raphson = newton_raphson_method(f_target)

# Menampilkan hasil
print("Hasil metode Bisection: R =", R_bisection)
print("Hasil metode Newton-Raphson: R =", R_newton_raphson)

# Visualisasi konvergensi kedua metode
R_values_bisection = []
R_values_newton_raphson = []

# Menghitung nilai-nilai R selama iterasi metode Bisection
R_min, R_max = 0, 100
while abs(R_max - R_min) > 0.1:
    R_mid = (R_min + R_max) / 2
    R_values_bisection.append(R_mid)
    if resonance_frequency(R_mid) < f_target:
        R_min = R_mid
    else:
        R_max = R_mid

# Menghitung nilai-nilai R selama iterasi metode Newton-Raphson
R = 50
for i in range(100):
    f_val = resonance_frequency(R)
    f_deriv = resonance_frequency_derivative(R)
    if abs(f_deriv) < 1e-6:
        break
    R_new = R - (f_val - f_target) / f_deriv
    R_values_newton_raphson.append(R_new)
    if abs(R_new - R) < 0.1:
        break
    R = R_new

# Plot konvergensi kedua metode
plt.plot(R_values_bisection, label="Metode Bisection")
plt.plot(R_values_newton_raphson, label="Metode Newton-Raphson")
plt.xlabel("Iterasi")
plt.ylabel("Nilai R")
plt.legend()
plt.title("Perbandingan Konvergensi Metode Bisection dan Newton-Raphson")
plt.show()

# Secara keseluruhan, kode ini menunjukkan dua metode yang berbeda untuk menyelesaikan masalah resonansi dalam rangkaian listrik. Masing-masing metode memiliki pendekatan yang berbeda; metode bisection lebih sederhana dan lebih stabil, sedangkan metode Newton-Raphson lebih cepat namun memerlukan perhitungan turunan. Kedua metode dapat digunakan untuk menemukan nilai resistansi yang dibutuhkan untuk mencapai frekuensi resonansi yang diinginkan, dan hasilnya saling melengkapi satu sama lain.