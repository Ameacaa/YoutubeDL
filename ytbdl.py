import os
import sys
from data import DEFAULTS, MODULES
from show import FromFile
from ytb import IsPlaylist
from menu import TreeMenu

FolderLoc = ''
Type = ''
Link = ''
isPlaylist = False
mod = ''


# Setup variables to default values
def GetDefault():
    global Type, Link, FolderLoc, mod
    FolderLoc = DEFAULTS['FolderLoc']
    Link = DEFAULTS['Link']
    Type = DEFAULTS['Type']
    mod = MODULES[0]


# Show variables value
def PrintValues():
    print(f"Folder Location: {FolderLoc}\nDownload Type: {Type}\nYoutube Link: {Link}\nIs a Playlist: {isPlaylist}")


# ----------------------
if __name__ == "__main__":
    # Tests
    os.system("cls")
    FromFile('Logo')
    GetDefault()
    isPlaylist = IsPlaylist(Link)
    PrintValues()
    for x in MODULES:
        print(x)
    exit()
    
    args = sys.argv
    args.pop(0)
    largs = len(args)
    
    # Putting args in variables to simplify
    match(largs):
        case 0:
            FromFile('Help')
            exit()
        case 1:
            if(args[0] not in MODULES):
                print('ERROR - THIS IS NOT A COMMAND - Please watch the help\n')
                FromFile('Help')
                exit()
            else:
                if (args[0] == MODULES["H"]):
                    FromFile('Help')
                    exit()



    if (largs == 0):
        TreeMenu()
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
    