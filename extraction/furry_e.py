import math
from timed_decorator.simple_timed import timed

# https://www.youtube.com/watch?v=qgM-DhNazXQ
# https://chat.deepseek.com/share/qmzdgfvx6whf4w46h4
# https://chat.deepseek.com/share/lvp22yuj3vtpb0sm4u
def dft_k(x, k, N):
    # синусоиду и косинусоиду можно разложить из круга на координаты и наоборот

    # берется эталонный косинус и эталонный синус для этого угла
    # пробегаемся по всем частотам до N
    # и сравниваем кажду с эталонами во внутреннем цикле по n (времени), 
    # если итогов сумма большая - похоже (векторы сонаправлены), нет (в разные стороны) - нет
    # output: 5 + 0.0i = чистый косинус, 0.0 + 5i = чистый синус, 6.7 + 5.2i = смешанный

    # двигаемся по координатной окружности
    sum_real = 0.0
    sum_imag = 0.0
    for n in range(N):
        angle = -2 * math.pi * k * n / N

        # любая точка на окружности — это поворот на угол angle.
        # e^{-i*angle} = cos(angle) + i*sin(angle)

        twist_real = math.cos(angle) # эталон косинус
        twist_imag = -math.sin(angle) # эталон синус

        real_part = x[n] * twist_real # проекция на x
        imag_part = x[n] * twist_imag # проекция на y

        sum_real += real_part
        sum_imag += imag_part

    return complex(sum_real, sum_imag)

def dft(x):
    N = len(x)
    result = []
    for k in range(N):
        Xk = dft_k(x, k, N)
        result.append(Xk)
    return result

# @timed(return_time=True)
def fft(x) -> list[complex]:
    N = len(x)
    if N == 1:
        return [x[0] + 0j]

    x_even = [x[i] for i in range(0, N, 2)]
    x_odd = [x[i] for i in range(1, N, 2)]

    E = fft(x_even)
    O = fft(x_odd)

    result = [0] * N
    for k in range(N // 2):
        angle = -2 * math.pi * k / N
        W = complex(math.cos(angle), math.sin(angle))

        result[k]       = E[k] + W * O[k]
        result[k + N//2] = E[k] - W * O[k]

    return result
