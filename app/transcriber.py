from nltk.corpus import cmudict

def transcribe(str):
    transcription = []
    for word in str.split():
        wordTranscription = transcribeWord( word )

        if wordTranscription != False:
            transcription.append(wordTranscription)
        else:
            return False

    return ' '.join(transcription)


def transcribeWord(word):
    dict = cmudict.dict()

    if word in dict:
        pronunciations = dict[word]
        syllables = pronunciations[0]
        pronunciation = ' '.join(syllables)
        return pronunciation
    else:
        return False
