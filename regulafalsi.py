def regulafalsi(f, a, b, tolerance=1e-6, max_iteration=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar di interval tersebut.")
        return None
    
    iteration_count = 0
    c = a
    while abs(f(c)) > tolerance and iteration_count < max_iteration:
        # Menghitung nilai c
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration_count += 1
    return c