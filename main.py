from entity.peaks import PeaksParams
from extraction.graph import plot_spectrogram
from extraction.spectr import audio_to_spectrogram
from extraction.twin_peaks import get_peaks


window_size = 2048
hop_size = 512
sample = 'samples/2/scotland-forever-with-song.wav'

print(f'{window_size=} {hop_size=} {sample=}')

spectrogram, samplerate = audio_to_spectrogram(sample, window_size=window_size, hop_size=hop_size, use_cache=True)
peaks = get_peaks(
    spectrogram,
    PeaksParams(
        freq_radius=2,
        time_radius=3,
        min_amplitude=-25,
        window_size=window_size,
        audio_path=sample,
        use_cache=True
    ),
)
# plot_spectrogram(spectrogram, samplerate, hop_size, peaks=peaks)
# plot_spectrogram(spectrogram, samplerate, hop_size)
# cli_volume(spectrogram, samplerate, hop_size)
