from .util import piglatinize

def test_with_uppercase():
    assert(piglatinize('Alice') == 'Aliceay')

def test_with_lowercase():
    assert(piglatinize('hello') == 'ellohay')
