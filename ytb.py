from pytube import YouTube, Playlist
from data import DEFAULTS

FolderLoc = DEFAULTS['FolderLoc']

def IsPlaylist(link):
    isPlaylist = False
    try:
        YouTube(link)
        isPlaylist = False
    except:
        try:
            Playlist(link)
            isPlaylist = True
        except:
            isPlaylist = None
    return isPlaylist


def BestAudioLink(link):
    yt = YouTube(link)
    print(f"Downloading: {yt.title}")
    yt.streams.get_audio_only().download(output_path=FolderLoc)


def BestAudioPlaylist(link):
    yt = Playlist(link)
    for v in yt.videos:
        print(f"Downloading: {v.title}")
        v.streams.get_audio_only().download(output_path=FolderLoc)


def BestVideoLink(link):
    yt = YouTube(link)
    print(f"Downloading: {yt.title}")
    yt.streams.get_audio_only().download(output_path=FolderLoc)


def BestVideoPlaylist(link):
    yt = Playlist(link)
    for v in yt.videos:
        print(f"Downloading: {v.title}")
        v.streams.get_highest_resolution().download(output_path=FolderLoc)


def Download(Type, link, isPlaylist):
    if (Type == "audio"):
        if (isPlaylist):
            BestAudioPlaylist(link)
        else:
            BestAudioLink(link)
    else: 
        if (isPlaylist):
            BestVideoPlaylist(link)
        else:
            BestVideoLink(link)
    print()