import tabulate
from deep_translator import GoogleTranslator as Translator
from langdetect import detect_langs


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        return Translator(source=scr, target=dest).translate(text)
    except Exception as e:
        print(e)
        return "Invalid parameters"


def LangDetect(text: str, set: str = "all") -> str:
    result = detect_langs(text)
    result = max(result)

    if set == "lang":
        return result.lang
    if set == "confidence":
        return result.prob
    return result


def CodeLang(lang):
    langs_dict = Translator(target="english").get_supported_languages(as_dict=True)
    if langs_dict.get(lang):
        return langs_dict[lang]
    langs_dict = {value: key for key, value in langs_dict.items()}

    if langs_dict.get(lang):
        return langs_dict[lang]
    return "Unknown lang"


def LanguageList(out: str = "screen", text: str = "") -> str:
    lst = []
    sourse = LangDetect(text, "lang")
    langs_dict = Translator(target="english").get_supported_languages(as_dict=True)
    for i, (lang, code) in enumerate(langs_dict.items()):
        result = TransLate(text, sourse, lang)
        lst.append([i + 1, lang, code, result])
    table = tabulate.tabulate(lst, headers=["N", "Languages", "ISO-639 code", "Text"])
    if out == "screen":
        print(table)
    else:
        file = open("languages.deep", "w", errors="ignore")
        file.write(table)
        file.close()

    return "OK"
