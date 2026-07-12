from entity.hashes import HashParams


SHIFT_CURRENT_FREQ = 10
SHIFT_FUTURE_FREQ = 22
DELTA_TOLERANCE = 7
FREQ_STEP = 7

def normalize_hashes(hashes, freq_step=3, delta_step=5):
    norm = {}
    for key, times in hashes.items():
        f1 = key >> SHIFT_CURRENT_FREQ
        f2 = (key >> SHIFT_FUTURE_FREQ) & ((1 << (SHIFT_FUTURE_FREQ - SHIFT_CURRENT_FREQ)) - 1)
        delta = key & ((1 << SHIFT_CURRENT_FREQ) - 1)
        
        new_key = ((f1 // freq_step) << SHIFT_CURRENT_FREQ) | ((f2 // freq_step) << SHIFT_FUTURE_FREQ) | (delta // delta_step)
        
        if new_key not in norm:
            norm[new_key] = []
        norm[new_key].extend(times)
    
    return norm

def get_hashes(peaks: list[tuple[int, int]], params: 'HashParams'):
    hashes = {}

    for i, (current_peak_freq, current_peak_time) in enumerate(peaks):
        start = i + 1
        end = min(start + params.future_peaks_count, len(peaks))
        for j in range(start, end):
            future_peak_freq, future_peak_time = peaks[j]
            delta = future_peak_time - current_peak_time

            if delta <= 0 or delta > params.future_peak_max_delta:
                break

            f1_group = current_peak_freq // FREQ_STEP
            f2_group = future_peak_freq // FREQ_STEP

            for d_delta in range(-DELTA_TOLERANCE, DELTA_TOLERANCE + 1):
                delta_variant = delta + d_delta
                if delta_variant <= 0:
                    continue
                key = (f1_group << SHIFT_CURRENT_FREQ) | (f2_group << SHIFT_FUTURE_FREQ) | delta_variant
                if not hashes.get(key):
                    hashes[key] = [current_peak_time]
                else:
                    hashes[key].append(current_peak_time)

    return hashes
 