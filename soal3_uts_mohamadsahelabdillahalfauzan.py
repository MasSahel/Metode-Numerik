import numpy as np
import matplotlib.pyplot as plt

# Nilai tahanan dan suhu
R0 = 5000
B = 3500
suhu = 298  # T dalam Kelvin

# Fungsi tahanan R(T)
def resistance(T):
    return R0 * np.exp(B * (1 / T - 1 / suhu))

# a) ini adalah fungsi turunan menggunakan metode selisih maju, mundur, dan tengah
def forward_difference(T, h):
    return (resistance(T + h) - resistance(T)) / h

def backward_difference(T, h):
    return (resistance(T) - resistance(T - h)) / h

def central_difference(T, h):
    return (resistance(T + h) - resistance(T - h)) / (2 * h)

# b) ini adalah fungsi untuk menghitung turunan eksak dari R(T)
def exact_derivative(T):
    return -R0 * B * np.exp(B * (1 / T - 1 / suhu)) / T**2

# c) menghitung turunan pada rentang suhu dengan interval 10K
T_nilai2 = np.arange(250, 351, 10)
h = 1e-3  # Interval kecil pada metode numerik

maju_diff = [forward_difference(T, h) for T in T_nilai2]
mundur_diff = [backward_difference(T, h) for T in T_nilai2]
sentral_diff = [central_difference(T, h) for T in T_nilai2]
tepat_diff = [exact_derivative(T) for T in T_nilai2]

# d) menghitung error relatif pada setiap metode numerik
maju_error = np.abs((np.array(maju_diff) - tepat_diff) / tepat_diff) * 100
mundur_error = np.abs((np.array(mundur_diff) - tepat_diff) / tepat_diff) * 100
sentral_error = np.abs((np.array(sentral_diff) - tepat_diff) / tepat_diff) * 100

# Plot untuk membandingkan hasil turunan numerik dengan turunan eksak
plt.figure(figsize=(10, 6))
plt.plot(T_nilai2, tepat_diff, label='Eksak', color='black', linestyle='-', linewidth=2)
plt.plot(T_nilai2, maju_diff, label='Selisih Maju', linestyle='--')
plt.plot(T_nilai2, mundur_diff, label='Selisih Mundur', linestyle='--')
plt.plot(T_nilai2, sentral_diff, label='Selisih Tengah', linestyle='--')
plt.xlabel("Temperatur (K)")
plt.ylabel("dR/dT")
plt.legend()
plt.title("Perbandingan Turunan Numerik dengan Turunan Eksak")
plt.grid(True)
plt.show()

# Plot error relatif dari metode numerik
plt.figure(figsize=(10, 6))
plt.plot(T_nilai2, maju_error, label='Error Selisih Maju (%)', linestyle='--')
plt.plot(T_nilai2, mundur_error, label='Error Selisih Mundur (%)', linestyle='--')
plt.plot(T_nilai2, sentral_error, label='Error Selisih Tengah (%)', linestyle='--')
plt.xlabel("Temperatur (K)")
plt.ylabel("Error Relatif (%)")
plt.legend()
plt.title("Error Relatif dari Metode Numerik")
plt.grid(True)
plt.show()

# e) Pemakaian metode Richardson untuk meningkatkan akurasi
def richardson_extrapolation(T, h):
    D1 = central_difference(T, h)
    D2 = central_difference(T, h / 2)
    return (4 * D2 - D1) / 3

richardson_diff = [richardson_extrapolation(T, h) for T in T_nilai2]
richardson_error = np.abs((np.array(richardson_diff) - tepat_diff) / tepat_diff) * 100

# Plot hasil Richardson bersama metode lainnya
plt.figure(figsize=(10, 6))
plt.plot(T_nilai2, tepat_diff, label='Eksak', color='black', linestyle='-', linewidth=2)
plt.plot(T_nilai2, maju_diff, label='Selisih Maju', linestyle='--')
plt.plot(T_nilai2, mundur_diff, label='Selisih Mundur', linestyle='--')
plt.plot(T_nilai2, sentral_diff, label='Selisih Tengah', linestyle='--')
plt.plot(T_nilai2, richardson_diff, label='Richardson', linestyle='-.')
plt.xlabel("Temperatur (K)")
plt.ylabel("dR/dT")
plt.legend()
plt.title("Perbandingan Metode Numerik dan Metode Richardson dengan Turunan Eksak")
plt.grid(True)
plt.show()

# Plot error relatif untuk metode Richardson
plt.figure(figsize=(10, 6))
plt.plot(T_nilai2, maju_error, label='Error Selisih Maju (%)', linestyle='--')
plt.plot(T_nilai2, mundur_error, label='Error Selisih Mundur (%)', linestyle='--')
plt.plot(T_nilai2, sentral_error, label='Error Selisih Tengah (%)', linestyle='--')
plt.plot(T_nilai2, richardson_error, label='Error Richardson (%)', linestyle='-.')
plt.xlabel("Temperatur (K)")
plt.ylabel("Error Relatif (%)")
plt.legend()
plt.title("Error Relatif dari Metode Richardson")
plt.grid(True)
plt.show()

#Secara keseluruhan, metode numerik dapat digunakan untuk menghitung turunan fungsi, tetapi hasilnya dapat bervariasi tergantung pada metode yang digunakan. Metode selisih tengah adalah yang paling akurat di antara metode numerik, dan metode Richardson dapat meningkatkan akurasi lebih lanjut dengan menggabungkan informasi dari beberapa perhitungan. Ini menunjukkan pentingnya memilih metode yang tepat dan mungkin mengombinasikan beberapa metode untuk mendapatkan hasil yang paling akurat.