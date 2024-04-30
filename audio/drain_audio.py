from pydub import AudioSegment

# Загрузить аудио файлы
background_audio = AudioSegment.from_file("background.mp3", format="mp3")
overlay_audio = AudioSegment.from_file("overlay.mp3", format="mp3")

# Наложить аудио файл
combined_audio = background_audio.overlay(overlay_audio)

# Экспортировать объединенный аудио файл
combined_audio.export("combined_audio.mp3", format="mp3")

''' Несколько аудио
from pydub import AudioSegment
import os

# Загрузить фоновый аудио файл
background_audio = AudioSegment.from_file("background.mp3", format="mp3")

# Список аудио файлов для наложения
overlay_files = ["overlay1.mp3", "overlay2.mp3", "overlay3.mp3"]

# Итерироваться по списку аудио файлов и накладывать их
for overlay_file in overlay_files:
    overlay_audio = AudioSegment.from_file(overlay_file, format="mp3")
    background_audio = background_audio.overlay(overlay_audio)

# Экспортировать объединенный аудио файл
background_audio.export("combined_audio.mp3", format="mp3")
'''