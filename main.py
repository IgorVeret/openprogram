from pydub import AudioSegment


def merge_audio_tracks(audio1_path, audio2_path, volume1, volume2, output_path):
    audio1 = AudioSegment.from_file(audio1_path)
    audio2 = AudioSegment.from_file(audio2_path)

    audio1 = audio1 + volume1  # Регулировка громкости первой аудиодорожки
    audio2 = audio2 + volume2  # Регулировка громкости второй аудиодорожки

    combined = audio1.overlay(audio2)

    combined.export(output_path, format='mp3')

# Параметры
audio2_path = 'rain.mp3'
audio1_path = 'golovin.mp3'
volume1 = 7  # Уровень громкости первой аудиодорожки в децибелах (отрицательные значения – понижение громкости)
volume2 = -2  # Уровень громкости второй аудиодорожки в децибелах (0 – без изменений)
output_path = 'nidra2.mp3'

merge_audio_tracks(audio1_path, audio2_path, volume1, volume2, output_path)