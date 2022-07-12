from data import TXTLOC

def FromFile(key):
    try:
        f = open(TXTLOC[key])
        for l in f.readlines:
            print(l)
    except:
        print('ERROR - show.FromFile(file)')
