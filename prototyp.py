import matplotlib
matplotlib.use("Agg")  # bez okna, tylko zapis do pliku
import matplotlib.pyplot as plt


# Parametry

# pole przekroju poprzecznego zbiornika [m^2]
A = 1.5 
# współczynnik wypływu [m^(5/2)/s], Qo = beta * sqrt(h)
beta = 0.035
#Czas symulacji
t_sim = 3600.0
# Kroko symulacji
Tp = 0.1
h_min = 0.0
h_max = 5.0
Qd_min = 0.0
Qd_max = 0.075

N = int(t_sim / Tp)


# Symulacja (czysty Python, bez importów)
t = [n * Tp for n in range(N + 1)]
h = [0.0] * (N + 1)
Qd = [Qd_max] * (N + 1)
Qo = [0.0] * (N + 1)

for n in range(N):
    Qo[n] = beta * h[n] ** 0.5
    h[n + 1] = h[n] + Tp * (Qd[n] - Qo[n]) / A
    h[n + 1] = min(max(h[n + 1], h_min), h_max)
Qo[N] = beta * h[N] ** 0.5

print("h[-1] =", h[-1])


# Wykres do pliku
plt.plot(t, h)
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.grid()
plt.savefig("h.png", dpi=150)
plt.close()

print("Zapisano wykres: h.png")