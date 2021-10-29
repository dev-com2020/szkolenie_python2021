import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=4V2C0X4qqLY')
#yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
yt.streams.filter(only_audio=True).first().download("E:\\")
yt.streams.filter(file_extension='mp4').all()