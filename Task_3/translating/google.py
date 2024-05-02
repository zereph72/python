import tabulate
from googletrans import Translator, LANGUAGES, LANGCODES

translator = Translator()


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        return translator.translate(text=text, dest=dest, scr=scr).text
    except ValueError:
        return "Invalid destination language"


def LangDetect(text: str, set: str = "all") -> str:
    result = translator.detect(text=text)
    if set == "lang":
        return result.lang
    if set == "confidence":
        return result.confidence
    return result


def CodeLang(lang):
    lang = lang.lower()
    if LANGCODES.get(lang):
        return LANGCODES[lang]
    if LANGUAGES.get(lang):
        return LANGUAGES[lang]
    return "Unknown lang"


def LanguageList(out: str = "screen", text: str = "") -> str:
    lst = []
    for i, (lang, code) in enumerate(LANGCODES.items()):
        result = translator.translate(text=text, dest=lang).text
        lst.append([i + 1, lang, code, result])
    table = tabulate.tabulate(lst, headers=["N", "Languages", "ISO-639 code", "Text"])
    if out == "screen":
        print(table)
    else:
        file = open("languages.google", "w", errors="ignore")
        file.write(table)
        file.close()

    return "OK"
