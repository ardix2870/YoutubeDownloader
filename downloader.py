from pytube import YouTube, Playlist

def GetLink():
    An="N"
    while(An=="N"):
        link = input("insert the link \n")
        yt = YouTube(link)
        pl = Playlist(link)
        print ("\nthe video has these characteristics:")

        print ("Author: ", yt.author)
        print ("Title: ",yt.title)
        print ("Views: ",yt.views)

        print("do you want to download it? Y/N ")
        An=str(input("(write Y to continue or N to change link)\n")).capitalize()
    
    path=input("\nenter the path where you want the video\n")

    return yt, pl, path

def DownloadVideo(yt, path):
    yd = yt.streams.get_highest_resolution()
    print("I'm downloading ... ")
    yd.download(path)

def DownloadPlaylist(pl, path):
    print("I'm downloading ... ")
    for video in pl.videos:
        video.streams.first().download(path)

print("enter the number of the thing you want to do\n")
print("1. download a video")
print("2. download a playlist")

Answer=int(input(""))

yt, pl, path = GetLink()

if Answer==1:
    DownloadVideo(yt, path)

    A=input("Do you want to be able to download the thumbnail? Y/N\n")
    if str(A).capitalize()== "Y":
        print("here is the link:\n",yt.thumbnail_url)
    
elif Answer==2:

    DownloadPlaylist(pl, path)


#https://youtu.be/MbTXCvrxbTY?si=lGLBLd-tfd9nbhmG
#C:\Users\ardix\Desktop\progetti\python\youtube downloader



