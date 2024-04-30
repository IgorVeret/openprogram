# from pydub import AudioSegment
#
# # Загрузить аудио файл
# audio = AudioSegment.from_mp3("background.mp3")
#
# # Обрезать аудио (с 10 секунды по 30 секунду)
# clipped_audio = audio[0:3238000]
#
# # Сохранить обрезанный аудио файл
# clipped_audio.export("output_audio.mp3", format="mp3")
#
from moviepy.editor import VideoFileClip

# Загрузить видео
video = VideoFileClip("rain.mp4")

# Обрезать видео (с 10 секунды по 30 секунду)
clipped_video = video.subclip(0, 2238)

# Сохранить обрезанное видео
clipped_video.write_videofile("output_video.mp4")

# Закрыть клипы
video.close()
clipped_video.close()

#--------------


