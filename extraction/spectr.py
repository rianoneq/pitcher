import math
import numpy as np

from extraction.furry_e import fft
from extraction.graph import cli_volume, plot_spectrogram
from extraction.wav import read_wav_standard


def audio_to_spectrogram(filename, window_size, hop_size):
    samplerate, x = read_wav_standard(filename)

    start = 0
    dB_matrix = []

    print(f'samplerate: {samplerate}')
    print(f'len(x): {len(x)}')
    print(f'duration sec: {len(x) / samplerate:.2f}')
    print(f'windows count: {(len(x) - window_size) // hop_size + 1}')

    while start < len(x):
        window = x[start:start + window_size]

        if len(window) < window_size:
            window = np.pad(window, (0, window_size - len(window)))

        complex_values = fft(window.tolist())

        window_dB = []
        for c in complex_values[:window_size // 2 + 1]:
            amp = math.sqrt(c.real**2 + c.imag**2) / (window_size / 2)

            if amp > 1e-10:
                db_val = 20 * math.log10(amp)
            else:
                db_val = -100
            window_dB.append(db_val)

        dB_matrix.append(window_dB)
        start += hop_size

    return np.array(dB_matrix), samplerate


window_size = 2048
hop_size = 512
sample = 'samples/2/scotland-forever-with-song.wav'

print(f'{window_size=} {hop_size=} {sample=}')

spectrogram, samplerate = audio_to_spectrogram(sample, window_size=window_size, hop_size=hop_size)
plot_spectrogram(spectrogram, samplerate, hop_size)
# cli_volume(spectrogram, samplerate, hop_size)
