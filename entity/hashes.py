from dataclasses import dataclass


@dataclass
class HashParams:
    future_peaks_count: int = 30
    future_peak_max_delta: int = 200
