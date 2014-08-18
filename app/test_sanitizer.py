from app.sanitizer import sanitize

def test_sanitize_at_mentions():
    assert sanitize('@handle') == 'AT HANDLE'

def test_sanitize_hash_tags():
    assert sanitize('#') == 'HASH TAG'

def test_expand_camel_case():
    assert sanitize('hashTag') == 'HASH TAG'

def test_trim_trailing_space():
    assert sanitize('end ') == 'END'

def test_make_lower_case():
    assert sanitize('Jordan Eldredge') == 'JORDAN ELDREDGE'

def test_remove_punctuation():
    assert sanitize('wow!!!') == 'WOW'

def test_contract_white_space():
    assert sanitize('foo    bar') == 'FOO BAR'

def test_contract_tabs():
    assert sanitize('foo\tbar') == 'FOO BAR'

def test_contract_new_lines():
    assert sanitize('foo\nbar') == 'FOO BAR'

def test_preserve_appostrophe():
    assert sanitize("That's all") == "THAT'S ALL"
