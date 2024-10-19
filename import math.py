def f(x):
    return x - math.exp(-x)

# Definisikan turunan f'(x)
def df(x):
    return 1 + math.exp(-x)

# Menjalankan Metode Newton Raphson
def newton_raphson(x0, Toleransi=1e-7, Max_iterasi=100):
    x = x0
    for i in range(Max_iterasi):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            raise ValueError("Turunan f'(x) adalah nol. Metode gagal.")
        
        x_new = x - fx / dfx
        
        # Melakukan pengecekan konvergensi
        if abs(x_new - x) < Toleransi:
            return x_new
     
        x = x_new
    
    raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")

# Nilai awal x0
x0 = 0