from ast import arg
from email.policy import default
import os
import sys
from data import DEFAULTS
from show import FromFile
from ytb import IsPlaylist, Download
from menu import TreeMenu


TYPES = [ 'audio', 'video', 'help', 'menu' ] # Existing types 
Type = ''           # The type to download
Link = ''           # Youtube link
isPlaylist = False  # Is a playlist link or not
ClearCMD = True     # Clear the CMD Windows on new command

# Setup variables to default values
def GetDefault():
    global Type, Link, ClearCMD
    Link = DEFAULTS['Link']
    Type = DEFAULTS['Type']
    ClearCMD = DEFAULTS['ClearCMD']


# Show variables value
def PrintValues():
    print(f"\nFolder Location: {DEFAULTS['FolderLoc']}\nDownload Type: {Type}\nYoutube Link: {Link}\nIs a Playlist: {isPlaylist}")


# ------------------------
if __name__ == "__main__":

    if (ClearCMD):
        os.system("cls")
    FromFile('Logo')
    GetDefault()


    # Simplify the args
    args = sys.argv
    args.pop(0)
    largs = len(args)
    

    # Possibles Commands
    if ( largs == 0 ):
        FromFile('Cmds')
        exit()
    elif ( largs == 1 ):
        if( args[0] not in TYPES ):
            print('Error - Command not reconigned\n')
            FromFile('Cmds')
            exit()
        else:
            if (args[0] == "default"):
                GetDefault()
                print(f'Download {Type} of default link')
            elif (args[0] in [ "video" , "audio" ]):
                Type = args[0]
                print(f'Download {Type} of default link')
            elif (args[0] == "menu"):
                TreeMenu()
                exit()
            elif (args[0] == "help"):
                FromFile('Help')
                exit()
    elif ( largs == 2 ):
        if( args[0] not in TYPES ):
            print('Error - Command not reconigned\n')
            FromFile('Cmds')
            exit()
        else:
            if (args[0] == "default"):
                GetDefault()
                if (args[1] in [ "video" , "audio" ]):
                    Type = args[1]
                print(f'Download {Type} of default link')
            elif (args[0] in [ "video" , "audio" ]):
                Type = args[0]
                Link = args[1]
                isPlaylist = IsPlaylist(Link)
                print(f'Download {Type} of link: {Link} ')
            elif (args[0] == "menu"):
                TreeMenu()
                exit()
            elif (args[0] == "help"):
                if (args[1] == "audio"):
                    # TODO Create a audio help
                    FromFile('Help')
                elif (args[1] == "video"):
                    # TODO Create a video help
                    FromFile('Help')
                else:
                    FromFile('Help')
                exit()


    # Show values
    isPlaylist = IsPlaylist(Link)
    PrintValues()


    # Call pytube functions
    if Type in ["audio", "video"]:
        Download(Type, Link, isPlaylist)
    else:
        print("Error - Type not recognised")
    