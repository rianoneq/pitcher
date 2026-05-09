import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.02, 1000)
f = 100 # Гц

harmonic_coefs = [1, 3, 5, 7, 9]
square_wave = 0

plt.figure(figsize=(10, 8))

for n, coef in enumerate(harmonic_coefs):
    # n-ая гармоника (в coef раза выше, в coef раза тише)
    # гармоника В физике/акустике: Это частота, кратная основной частоте звука или сигнала.
    harmonic = (1/coef) * np.sin(2 * np.pi * (coef*f) * t)

    # любой сигнал = сумма синусоид, чем больше гармоник суммируем, тем больше график
    # похож на желаемую последовательность прямоугольнков []_[]_[]    
    square_wave += harmonic

    plt.subplot(len(harmonic_coefs) + 1, 1, n + 1)
    plt.plot(t, harmonic)
    plt.title(f'{n + 1}-я гармоника: sin(2π·{coef}·100·t)')


plt.subplot(len(harmonic_coefs) + 1, 1, len(harmonic_coefs) + 1)
plt.plot(t, square_wave)
plt.title('sum = прямоугольный сигнал')

plt.tight_layout()
plt.show()
