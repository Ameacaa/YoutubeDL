import os
import sys
from data import DEFAULTS
from typing import Dict
from show import FromFile
from ytb import IsPlaylist

FolderLoc = ''
Type = ''
Link = ''
isPlaylist = False

def GetDefault():
    global Type, Link, FolderLoc
    FolderLoc = DEFAULTS['FolderLoc']
    Link = DEFAULTS['Link']
    Type = DEFAULTS['Type']


def PrintValues():
    print(f"Folder Location: {FolderLoc}\nDownload Type: {Type}\nYoutube Link: {Link}\nIs a Playlist: {isPlaylist}")


if __name__ == "__main__":
    FromFile('Logo')
    GetDefault()
    isPlaylist = IsPlaylist(Link)
    PrintValues()
    """
    args = sys.argv
    args.pop(0)
    largs = len(args)
    modules = ["help", "video", "audio"]
    mod = "audio"

    # Putting args in variables to simplify
    if (largs == 0):
        help()
        exit()
    elif (largs == 1):
        if args[0] == "help":
            help()
            exit()
        if args[0] != "default":
            link = args[0]
    elif (largs == 2):
        mod = args[0]
        if args[1] != "default":
            link = args[1]
    else:
        mod = args[0]
        if args[1] != "default":
            link = args[1]
    
    # Verify variables
    if mod not in modules:
        print("Module not recognised")
        help()
        exit()

    # Verify the link // TODO try make 1 try for 3 possiilities (ytb, plist, none)
    try:
        linkClass = YouTube(link)
        linkIsPlaylist = False
    except: # Fail in Youtube()
        try:
            linkClass = Playlist(link)
            linkIsPlaylist = True
        except: # Fail in Playlist()
            print("The link is not valid")
            exit()

    print(linkIsPlaylist)
    # Call pytube functions
    if mod == "audio":
        audio(linkIsPlaylist)
    elif mod == "video":
        video(linkIsPlaylist)
    else:
        print("Something is wrong in the command. Type \'ytbdl.py help\' if you need more help")
    """