import re

def sanitize(str):
    str = re.sub(r'([a-z])([A-Z])', r'\1 \2', str)
    str = str.lower()
    str = str.replace('@', 'at ')
    str = str.replace('#', 'hash tag ')
    str = re.sub(r'\s+', ' ', str)
    str = re.sub('[^a-z ]', '', str)
    return str

