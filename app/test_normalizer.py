from app.normalizer import normalize

def test_normalize_at_mentions():
    assert normalize('@handle') == 'AT HANDLE'

def test_normalize_hash_tags():
    assert normalize('#') == 'HASH TAG'

def test_expand_camel_case():
    assert normalize('hashTag') == 'HASH TAG'

def test_trim_trailing_space():
    assert normalize('end ') == 'END'

def test_make_lower_case():
    assert normalize('Jordan Eldredge') == 'JORDAN ELDREDGE'

def test_remove_punctuation():
    assert normalize('wow!!!') == 'WOW'

def test_contract_white_space():
    assert normalize('foo    bar') == 'FOO BAR'

def test_contract_tabs():
    assert normalize('foo\tbar') == 'FOO BAR'

def test_contract_new_lines():
    assert normalize('foo\nbar') == 'FOO BAR'

def test_preserve_appostrophe():
    assert normalize("That's all") == "THAT'S ALL"
