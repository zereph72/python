import json
import os
import re

from translating import google


def ReadConfig(configFileName):
    try:
        file = open(configFileName)
        text = file.read()
        config = json.loads(text)

        file.close()
        if "FileName" in config and "Target" in config and "Out" in config and "Sign count" in config \
                and "Word count" in config and "Sentence count" in config:
            return config
    except:
        pass
    print("Invalid config file")


def GetInfoFile(fileName, text):
    filesize = os.stat(fileName).st_size / 1024  # в кілобайтах
    signCount = len(text)
    words = text.split(" ")
    wordsCount = len(words)
    sentences = re.split(r"[.!?]+[\s\n]+", text)
    sentencesCount = len(sentences)
    language = google.LangDetect(text, "lang")
    return filesize, signCount, wordsCount, sentencesCount, language


def Main():
    config = ReadConfig("config.json")
    if config is None:
        return
    try:
        file = open(config["FileName"], encoding="utf-8")

        text = file.read()
        file.close()
    except:
        print("File not foud")
        return
    info = GetInfoFile(config["FileName"], text)
    print("File name is", config["FileName"])
    print("File size is", info[0], "KB")
    print("File sign is", info[1])
    print("File words is", info[2])
    print("File  sentences", info[3])
    print("File language is", info[4])

    if info[1] > config["Sign count"] or info[2] > config["Word count"] or info[3] > config["Sentence count"]:
        print("text is too big")
        return
    result = google.TransLate(text, info[4], config["Target"])
    if config["Out"] == "screen":
        print(config["Target"])
        print(result)
    else:
        file = open(config["Target"] + config["FileName"], "w")
        file.write(result)
        file.close()
        print("ok")


if __name__ == "__main__":
    Main()
