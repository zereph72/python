from translating import google as trans


def Main():
    text = input("Enter string: ")
    detect = trans.LangDetect(text)
    print(detect)
    language = input("Enter which language you want\nja,en,uk:\n")
    print(trans.CodeLang(language))
    result = trans.TransLate(text, detect, language)
    print(result)
    print(trans.LanguageList("file", text))


if __name__ == "__main__":
    Main()
