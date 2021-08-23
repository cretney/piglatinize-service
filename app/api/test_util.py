from .util import piglatinize

def test_with_uppercase():
    assert(piglatinize('Alice') == 'Aliceay')

def test_with_lowercase():
    assert(piglatinize('hello') == 'ellohay')

def test_with_consonant_cluster():
    assert(piglatinize('smile') == 'ilesmay')

def test_with_vowel_beginning():
    assert(piglatinize('omelet') == 'omeletay')
