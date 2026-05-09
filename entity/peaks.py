from dataclasses import dataclass


@dataclass
class PeaksParams:
    window_size: int
    freq_radius: int
    time_radius: int
    min_amplitude: int
    audio_path: str
    use_cache: bool = False

    @property
    def audio_name(self):
        return self.audio_path.split('/')[-1]

    @property
    def parent_folder_path(self):
        return '/'.join(self.audio_path.split('/')[:-1])

    @property
    def cache_key(self):
        return f"/{self.audio_name}_w{self.window_size}_fr{self.freq_radius}_tr{self.time_radius}_amp{self.min_amplitude}.pkl"

    @property
    def cache_path(self):
        return self.parent_folder_path + self.cache_key
