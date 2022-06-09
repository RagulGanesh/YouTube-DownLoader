from pytube import YouTube

#ask for the link from user
yt = YouTube("https://www.youtube.com/watch?v=cq-cLUASIag&ab_channel=MusicMiniStatus")

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views,type(yt.views))
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download('C:\\Users\\G ragul\\Desktop')
print("Download completed!!")