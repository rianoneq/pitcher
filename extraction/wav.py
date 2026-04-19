import wave
import numpy as np


def read_wav_standard(filename):
    with wave.open(filename, 'rb') as wav:
        channels = wav.getnchannels()
        samplerate = wav.getframerate()
        sample_width = wav.getsampwidth()
        n_frames = wav.getnframes()

        print(f'{channels=} {samplerate=} {sample_width=} {n_frames=}')

        frames = wav.readframes(n_frames)

        dtype = f'int{sample_width * 8}'
        samples = np.frombuffer(frames, dtype=dtype)

        if channels > 1:
            samples = samples.reshape(-1, channels)
            samples = np.mean(samples, axis=1)

        max_val = 2 ** (sample_width * 8 - 1)
        samples = samples.astype(np.float32) / max_val

        return samplerate, samples

