from data import TXTLOC

def FromFile(key):
    try:
        f = open(TXTLOC[key], 'r')
        for l in f.readlines():
            print(l, end="")
    except:
        print('ERROR - show.FromFile(file)')
