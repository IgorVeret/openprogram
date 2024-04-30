from pytube import YouTube

# Ссылка на видео на YouTube
url = "https://www.youtube.com/watch?v=zuumDolzDmc&list=PLduzLN4Mdb4ci6bpHV_buaAGP2sN79lRL&index=15"

# Создать объект YouTube
yt = YouTube(url)

# Получить аудио потока
audio = yt.streams.filter(only_audio=True).first()

# Скачать аудио файл
print(f"Скачивание аудио: {audio.title}")
audio.download()
print("Скачивание завершено")