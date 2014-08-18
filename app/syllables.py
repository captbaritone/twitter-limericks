import re

def count(str):
    """Count syllables in a CMU pronunciation string"""

    # Each vowel is followed by a 0, 1, or 2
    return len(re.findall(r'[0-2]', str))
