from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Wait for a bit. Downloading: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download("F:\Youtube downloads")