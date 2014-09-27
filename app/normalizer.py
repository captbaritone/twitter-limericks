import re

def normalize(str):
    '''Convert a string into a space delineated list of capitalized words'''
    str = re.sub(r'([a-z])([A-Z])', r'\1 \2', str)
    str = str.replace('@', 'at ')
    str = str.replace('#', 'hash tag ')
    str = str.lower()
    str = re.sub(r'\s+', ' ', str)
    str = re.sub(r' $', '', str)
    str = re.sub(r"[^a-z ']", '', str)
    return str
