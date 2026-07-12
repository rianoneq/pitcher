from dataclasses import dataclass


@dataclass
class HashParams:
    future_peaks_count: int = 100
    future_peak_max_delta: int = 20
