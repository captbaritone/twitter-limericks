import re

def sanitize(str):
    '''Convert a tweet string into a space delineated list of words'''
    str = re.sub(r'([a-z])([A-Z])', r'\1 \2', str)
    str = str.replace('@', 'at ')
    str = str.replace('#', 'hash tag ')
    str = str.upper()
    str = re.sub(r'\s+', ' ', str)
    str = re.sub(r' $', '', str)
    str = re.sub(r"[^A-Z ']", '', str)
    return str

