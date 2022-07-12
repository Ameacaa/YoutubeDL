from typing import Dict



def getDefault():
    f = open("C:\\Users\\Ameaça\\Documents\\.Projects\\Programs\\Python\\YoutubeDL\\txts\\default.txt", "r")
    defaults : Dict = f.readline()
    print(defaults)


if __name__ == "__main__":
    getDefault()