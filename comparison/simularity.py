from collections import Counter


DELTA_TOLERANCE = 5

def match_tracks(hashes1, hashes2):
    common_hashes = list(hashes1.keys() & hashes2.keys())
    shifts = []
    for hash in common_hashes:
        shifts.append(hashes1[hash][0] - hashes2[hash][0])

    if not shifts:
        raise Exception

    print(common_hashes, shifts)

    shift_counter = Counter(shifts)
    most_common_shift, count = shift_counter.most_common(1)[0]

    matches = 0
    for s in shifts:
        if abs(s - most_common_shift) <= DELTA_TOLERANCE:
            matches += 1

    total = len(set(hashes1.keys()) | set(hashes2.keys()))
    similarity = matches / total * 100

    print(total)
    if similarity > 50:
        print(f"same! {most_common_shift=} windows, match %: {similarity:.1f}%")
    else:
        print(f"different. match %: {similarity:.1f}%")
