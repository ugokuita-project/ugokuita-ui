import numpy as np
from scipy.io import wavfile
import os
from pydub import AudioSegment


def generate_sine_wave(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = np.sin(2 * np.pi * freq * t)
    return wave


def create_click_sound():
    duration = 0.1
    wave = generate_sine_wave(1000, duration) * 0.5
    # Add fade out
    fade_samples = int(0.05 * 44100)
    fade_out = np.linspace(1.0, 0.0, fade_samples)
    wave[-fade_samples:] *= fade_out
    return (wave * 32767).astype(np.int16)


def create_start_sound():
    duration = 0.3
    wave1 = generate_sine_wave(800, duration)
    wave2 = generate_sine_wave(1200, duration)
    wave = (wave1 + wave2) * 0.3
    return (wave * 32767).astype(np.int16)


def create_stop_sound():
    duration = 0.4
    wave1 = generate_sine_wave(400, duration)
    wave2 = generate_sine_wave(600, duration)
    wave = (wave1 + wave2) * 0.4
    # Add fade out
    fade_samples = int(0.1 * 44100)
    fade_out = np.linspace(1.0, 0.0, fade_samples)
    wave[-fade_samples:] *= fade_out
    return (wave * 32767).astype(np.int16)


def wav_to_mp3(wav_path, mp3_path):
    audio = AudioSegment.from_wav(wav_path)
    audio.export(mp3_path, format="mp3")
    os.remove(wav_path)  # Remove the temporary WAV file


def main():
    os.makedirs("sounds", exist_ok=True)

    # Generate click sound
    wavfile.write("sounds/click.wav", 44100, create_click_sound())
    wav_to_mp3("sounds/click.wav", "sounds/click.mp3")

    # Generate start sound
    wavfile.write("sounds/start.wav", 44100, create_start_sound())
    wav_to_mp3("sounds/start.wav", "sounds/start.mp3")

    # Generate stop sound
    wavfile.write("sounds/stop.wav", 44100, create_stop_sound())
    wav_to_mp3("sounds/stop.wav", "sounds/stop.mp3")


if __name__ == "__main__":
    main()
