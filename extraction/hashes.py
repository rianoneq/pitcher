from entity.hashes import HashParams


def get_hashes(peaks: list[tuple[int, int]], params: 'HashParams'):
    hashes = {}

    for i, (current_peak_freq, current_peak_time) in enumerate(peaks):
        start = i + 1
        end = min(start + params.future_peaks_count, len(peaks))
        for j in range(start, end):
            future_peak_freq, future_peak_time = peaks[j]
            time_delta = future_peak_time - current_peak_time

            if time_delta <= 0 or time_delta > params.future_peak_max_delta:
                break

            key = (current_peak_freq, future_peak_freq, time_delta)
            if not hashes.get(key):
                hashes[key] = [current_peak_time]
            else:
                hashes[key].append(current_peak_time)

    return hashes
 