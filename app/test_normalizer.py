from app.normalizer import normalize

def test_normalize_at_mentions():
    assert normalize('@handle') == 'at handle'

def test_normalize_hash_tags():
    assert normalize('#') == 'hash tag'

def test_expand_camel_case():
    assert normalize('hashTag') == 'hash tag'

def test_trim_trailing_space():
    assert normalize('end ') == 'end'

def test_make_lower_case():
    assert normalize('Jordan Eldredge') == 'jordan eldredge'

def test_remove_punctuation():
    assert normalize('wow!!!') == 'wow'

def test_contract_white_space():
    assert normalize('foo    bar') == 'foo bar'

def test_contract_tabs():
    assert normalize('foo\tbar') == 'foo bar'

def test_contract_new_lines():
    assert normalize('foo\nbar') == 'foo bar'

def test_preserve_appostrophe():
    assert normalize("That's all") == "that's all"
