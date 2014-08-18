from app.syllables import count

def test_count_syllables_in_hello_world():
    assert count('HH AH0 L OW1 W ER1 L D') == 3
