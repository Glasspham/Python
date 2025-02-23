#? Download a video from Youtube
from pytube import YouTube
def download_video(url):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download()
url = input("Enter link a video: ")
download_video(url)