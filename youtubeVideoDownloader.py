#run file in cmd
#python youtubeVideoDownloaser.py

import pytube

print("Enter the video link")
link = input()

yt = pytube.YouTube(link)
stream = yt.streams.first()

stream.download()

print("\n Your Youtube Video Has been downloaded")
#video saved where your file is placed
