from cache.service import CacheService
from entity.peaks import PeaksParams


def find_peaks(spectrogram, params: PeaksParams):
    peaks = []
    n_freqs, n_times = spectrogram.shape

    for j in range(params.time_radius, n_times - params.time_radius):
        for i in range(params.freq_radius, n_freqs - params.freq_radius):
            current = spectrogram[i][j]

            if current < params.min_amplitude:
                continue

            is_peak = True

            for di in range(-params.freq_radius, params.freq_radius + 1):
                for dj in range(-params.time_radius, params.time_radius + 1):
                    if di == 0 and dj == 0:
                        continue  # skip current
                    if spectrogram[i + di][j + dj] >= current:
                        is_peak = False
                        break
                if not is_peak:
                    break

            if is_peak:
                peaks.append((i, j))

    return peaks


def get_peaks(spectrogram, params: PeaksParams):
    cache_service = CacheService(params)

    if params.use_cache and cache_service.exists():
        return cache_service.load()

    peaks = find_peaks(spectrogram, params)
    cache_service.save(peaks)

    return peaks
