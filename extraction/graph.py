import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')

def plot_spectrogram(data, samplerate, hop_size, max_freq=16000):
    time_bins, freq_bins = data.shape

    # (time, frequency) —> (frequency, time)
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')

def plot_spectrogram(data, samplerate, hop_size):
    time_bins, freq_bins = data.shape

    # (time, frequency) —> (frequency, time)
    if time_bins > freq_bins:
        data = data.T
        freq_bins, time_bins = data.shape

    plt.figure(figsize=(12, 6))
    plt.imshow(data, aspect='auto', origin='lower', cmap='inferno', vmin=-100, vmax=0)

    time_max = time_bins * hop_size / samplerate
    freq_max = samplerate / 2  # максимальная частота по Найквисту
    
    plt.gca().set_xlim(0, time_bins)
    plt.gca().set_ylim(0, freq_bins)

    def time_format(x, pos):
        return f'{x * hop_size / samplerate:.1f}'

    def freq_format(y, pos):
        return f'{y * freq_max / freq_bins:.0f}'

    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(time_format))
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(freq_format))

    plt.colorbar(label='volume (dB)')
    plt.xlabel('time (s)')
    plt.ylabel('frequency (Hz)')
    plt.title('Spectrogram')
    plt.tight_layout()
    plt.show()

def cli_volume(dB_matrix, samplerate, hop_size):
    print('\n=== volume/time (average dB from spectrogram) ===')

    num_windows = dB_matrix.shape[0]
    total_duration = num_windows * hop_size / samplerate
    
    interval = 10
    num_intervals = int(np.ceil(total_duration / interval))
    
    for i in range(num_intervals):
        start_time = i * interval
        end_time = min((i + 1) * interval, total_duration)

        start_idx = int(start_time * samplerate / hop_size)
        end_idx = int(end_time * samplerate / hop_size)

        segment = dB_matrix[start_idx:end_idx]

        if len(segment) == 0:
            print(f'{start_time:5.1f}-{end_time:5.1f}s: no data')
            continue

        avg_db = np.mean(segment) # avg
        median_db = np.median(segment)
        max_val = np.max(segment)

        normalized = (avg_db + 100) / 100
        normalized = max(0, min(1, normalized))
        bars = int(normalized * 100)
        bar_str = '█' * bars + '░' * (100 - bars)
        
        print(f'{start_time:5.1f}-{end_time:5.1f}s: AVG={avg_db:6.1f} dB |{bar_str}| MED={median_db:6.1f} dB | MAX={max_val:6.1f} dB')
