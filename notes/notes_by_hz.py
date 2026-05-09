import numpy as np
import matplotlib.pyplot as plt

f = 440
t = np.linspace(0, .1, 10000)  # 100 миллисекунд

# Давление воздуха в момент времени t
pressure = np.sin(2 * np.pi * f * t)

plt.plot(t, pressure)
plt.xlabel('Время (секунды)')
plt.ylabel('Давление (относительное)')
plt.title(f'Чистый тон {f} Гц (нота xx)')
plt.show()

# любой сигнал это сумма синусоид
# любая чистая нота это синусоида с определнной герцовкой
# в таблице инфа соответствие герцовки для каждой ноты 
