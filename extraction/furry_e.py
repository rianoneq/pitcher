import math
from timed_decorator.simple_timed import timed


# https://chat.deepseek.com/share/qmzdgfvx6whf4w46h4
def dft_k(x, k, N):
    sum_real = 0.0
    sum_imag = 0.0
    for n in range(N):
        angle = -2 * math.pi * k * n / N
        # e^{-i*angle} = cos(angle) + i*sin(angle)
        twist_real = math.cos(angle)
        twist_imag = -math.sin(angle)

        # (a + 0*i) * (c + d*i) = a*c + a*d*i
        real_part = x[n] * twist_real
        imag_part = x[n] * twist_imag

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
