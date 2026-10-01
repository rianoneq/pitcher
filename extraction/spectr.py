import math
import numpy as np

from extraction.furry_e import fft
from extraction.wav import read_wav_standard


def audio_to_spectrogram(filename: str, window_size: int, hop_size: int, use_cache: bool = False):
    samplerate, samples = read_wav_standard(filename)

    print(f'samplerate: {samplerate}')
    print(f'len(x): {len(samples)}')
    print(f'duration sec: {len(samples) / samplerate:.2f}')
    print(f'windows count: {(len(samples) - window_size) // hop_size + 1}')

    if use_cache:
        return None, samplerate

    start = 0
    dB_matrix = []

    while start < len(samples):
        window = samples[start:start + window_size]

        if len(window) < window_size:
            # заполнить нулями если остаток меньше window_size для корректности fft
            window = np.pad(window, (0, window_size - len(window)))

        freq_spectrum = fft(window.tolist())

        window_dB = []
        for c in freq_spectrum[:window_size // 2 + 1]:
            # громкость = амплитуда = сложние векторов (корень из части по оси х ^ 2 + оси y ^ 2)
            # и нормализованная по window_size, чтобы от этого window_size не зависеть
            # https://chat.deepseek.com/share/jy8ec4p9xs24xpamdd
            amp = math.sqrt(c.real**2 + c.imag**2) / (window_size / 2)

            if amp > 1e-10:
                # ухо слышит логарифмически 
                # линейная (0.1 0.01 0.001 -> 0 dB -10dB -20dB) в логарифмическую
                # 20 некая константа хз
                db_val = 20 * math.log10(amp)
            else:
                # лог от 0 = -бесконечность (хотя это тишина, чтоб не ломалось -100dB)
                db_val = -100
            window_dB.append(db_val)

        dB_matrix.append(window_dB)
        start += hop_size

    return np.array(dB_matrix), samplerate
