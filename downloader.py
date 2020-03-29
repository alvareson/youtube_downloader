import pytube

video_url = 'https://www.youtube.com/watch?v=xSE9Qk9wkig' # paste here your Youtube video url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('/home/alister/trash') # path, where to video download