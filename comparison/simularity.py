from collections import Counter

from comparison.hashes import normalize_hashes


DELTA_TOLERANCE = 10
FREQ_STEP = 3
DELTA_STEP = 5

def match_tracks(hashes1, hashes2):
    hashes1_norm = normalize_hashes(hashes1, freq_step=FREQ_STEP, delta_step=DELTA_STEP)
    hashes2_norm = normalize_hashes(hashes2, freq_step=FREQ_STEP, delta_step=DELTA_STEP)

    common_hashes = list(hashes1_norm.keys() & hashes2_norm.keys())
    shifts = []
    for hash in common_hashes:
        shifts.append(hashes1_norm[hash][0] - hashes2_norm[hash][0])

    if not shifts:
        return print('different. 0 common hashes')

    shift_counter = Counter(shifts)
    most_common_shift, count = shift_counter.most_common(1)[0]

    matches = 0
    for s in shifts:
        if abs(s - most_common_shift) <= DELTA_TOLERANCE:
            matches += 1

    total = len(set(hashes1_norm.keys()) | set(hashes2_norm.keys()))
    similarity = matches / total * 100

    print(f'total: {total}, common: {len(common_hashes)}')
    if similarity > 50:
        print(f"same! {most_common_shift=} windows, match %: {similarity:.1f}%")
    else:
        print(f"different. match %: {similarity:.1f}%")
