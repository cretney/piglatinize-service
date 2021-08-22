import re


def sentence_to_array(sentence):
    return re.findall(r"[\w']+|[.,!?; ]", sentence)

def piglatinize(word):
    callback = lambda pattern: \
        pattern.group(2) + pattern.group(1) + 'ay' \
        if pattern.group(1).islower() or pattern.group(1) == '' \
        else pattern.group(2)[0].upper() + pattern.group(2)[1:] + pattern.group(1).lower() + 'ay'
    return re.sub(r'^([^aeiouAEIOU]*)(\w*)', callback, word)
