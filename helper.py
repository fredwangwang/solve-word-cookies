import string


def classify(word):
    temp = dict()
    ret = ""

    for c in word:
        if c not in temp:
            temp[c] = 1
        else:
            temp[c] += 1
    for c in string.ascii_lowercase:
        if c in temp:
            ret += c + str(temp[c])
    return ret


def isword(word):
    '''The dictionary file may contain some `non-words` items 
    (e.g. NCO, 1st, 2,4-d). We don\'t want those words appear
    in the final result. But words like `Bear, Camp`, we do
    want to keep them'''
    if len(word) == 0:
        return False

    if word[0] not in string.ascii_letters:
        return False

    for c in word[1:]:
        if c not in string.ascii_lowercase:
            return False
    return True
