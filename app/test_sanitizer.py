from app.sanitizer import sanitize

def test_sanitize_at_mentions():
    assert sanitize('@handle') == 'at handle'

def test_sanitize_hash_tags():
    assert sanitize('#') == 'hash tag'

def test_expand_camel_case():
    assert sanitize('hashTag') == 'hash tag'

def test_trim_trailing_space():
    assert sanitize('end ') == 'end'

def test_make_lower_case():
    assert sanitize('Jordan Eldredge') == 'jordan eldredge'

def test_remove_punctuation():
    assert sanitize('wow!!!') == 'wow'

def test_contract_white_space():
    assert sanitize('foo    bar') == 'foo bar'

def test_contract_tabs():
    assert sanitize('foo\tbar') == 'foo bar'

def test_contract_new_lines():
    assert sanitize('foo\nbar') == 'foo bar'
