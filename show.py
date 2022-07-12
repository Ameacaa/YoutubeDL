from typing import Dict


txtLoc : Dict= {
    'logo' : 'txts\\logo.txt',
    'help' : 'txts\\help.txt'
}

def FromFile(file):
    try:
        f = open(txtLoc[file])
        for l in f.readlines:
            print(l)
    except:
        print('ERROR - show.FromFile(file)')
