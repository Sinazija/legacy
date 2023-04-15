import re
import os

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", 'i', "ji", "g")


TRANS = {}

for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def normalize(name: str) -> str:
    name, ext = os.path.splitext(name)  # отримуємо ім'я файлу та розширення
    translate_name = name.translate(TRANS)  # перекладаємо тільки ім'я
    # замінюємо не-буквено-цифрові символи на дефіс
    translate_name = re.sub(r'\W', '-', translate_name)
    # повертаємо ім'я файлу з перекладом та розширенням
    new_name = f"{translate_name}{ext}"
    return new_name
