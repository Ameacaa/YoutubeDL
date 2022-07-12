from pytube import YouTube, Playlist


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