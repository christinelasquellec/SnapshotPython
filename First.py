import os
import copy
from pprint import pprint


def snapshot(chemin, profondeur=3, frequence=0, debug=False):
    print(os.listdir(chemin))
    if profondeur != 0:
        for path, dirs, files in os.walk(chemin):
            print(os.path.split(path))
            capture = copy.deepcopy(files)

def walk2(chemin, profondeur):
    dirs, nondirs = [], []
    for name in os.listdir(chemin):
        (dirs if os.path.isdir(os.path.join(chemin, name)) else nondirs).append(name)
    yield chemin, dirs, nondirs
    if profondeur > 0:
        for name in dirs:
            for x in walk2(os.path.join(chemin, name), profondeur-1):
                yield x

def getFiles(chemin, profondeur):
    chemins = []
    for x in walk2(chemin, profondeur):
        #print(x)
        chemins.append(x)
    return chemins




def myMain():
    #snapshot("C:\\Users\Christine\Documents\Travail\ISEN\M1\Cryptographie",2)
    pprint(getFiles("C:\\Users\Christine\Documents\Travail\ISEN\M1",2))


if __name__ == "__main__":
    myMain()
