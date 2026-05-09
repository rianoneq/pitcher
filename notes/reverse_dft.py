import numpy as np
import matplotlib.pyplot as plt

# 1. СОЗДАЕМ СИГНАЛ (как твой код)
fs = 10000  # частота дискретизации
t = np.linspace(0, 0.02, fs)
f = 100  # базовая частота

# Синтезируем прямоугольный сигнал из гармоник
harmonics = [1, 3, 5, 7, 9]
square_wave = np.zeros_like(t)

for coef in harmonics:
    harmonic = (1/coef) * np.sin(2 * np.pi * coef * f * t)
    square_wave += harmonic

# 2. ПРИМЕНЯЕМ DFT К ЭТОМУ СИГНАЛУ
from scipy.fft import fft, fftfreq

spectrum = fft(square_wave)
freqs = fftfreq(len(t), 1/fs)

# Берем только положительные частоты
positive_freqs = freqs[:len(freqs)//2]
amplitudes = np.abs(spectrum[:len(spectrum)//2]) * 2 / len(t)

# 3. СМОТРИМ РЕЗУЛЬТАТ
print("Амплитуды, найденные DFT (анализ):")
for i, coef in enumerate(harmonics):
    target_freq = coef * f
    # Находим ближайшую частоту в спектре
    idx = np.argmin(np.abs(positive_freqs - target_freq))
    print(f"  Частота {target_freq} Гц: {amplitudes[idx]:.3f}")

print("\nАмплитуды, заданные при синтезе:")
for coef in harmonics:
    print(f"  Частота {coef*f} Гц: {1/coef:.3f}")

# Визуализация
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t[:500], square_wave[:500])
plt.title('Сигнал (синтезированный из гармоник)')
plt.xlabel('Время (с)')

plt.subplot(1, 2, 2)
plt.stem(positive_freqs[:1000], amplitudes[:1000], basefmt=" ")
plt.title('Спектр (результат DFT)')
plt.xlabel('Частота (Гц)')
plt.xlim(0, 1000)

plt.tight_layout()
plt.show()
