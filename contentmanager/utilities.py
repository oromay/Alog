from slugify import slugify
from transliterate import translit


def ruslugify(smth):
    return slugify(translit(smth, 'ru', reversed=True))
