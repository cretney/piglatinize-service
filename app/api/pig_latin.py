from fastapi import APIRouter
import re

from .util import piglatinize

pig_latin = APIRouter()

@pig_latin.get('/')
async def index(text: str):
    sentence_array = re.findall(r"[\w']+|[.,!?; ]", text)
    pig_latin_array = []

    for item in sentence_array:
        is_word = re.search(r'\w', item)
        if not is_word:
            pig_latin_array.append(item)
        else:
            pig_latin_array.append(piglatinize(item))
    return {'original': text, 'piglatinized': "".join(pig_latin_array)}
