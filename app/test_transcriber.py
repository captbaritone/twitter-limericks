from app.transcriber import transcribe

def test_transcribe_string():
    assert transcribe('hello world') == 'HH AH0 L OW1 W ER1 L D'

def test_transcribe_string_with_bogus_words():
    assert transcribe('thisisnotarealword') == False
