male_words = ['he', 'him', 'his', 'husband', 'father', 'dad']
female_words = ['she', 'her', 'hers', 'wife', 'mother', 'mom', 'mum']


def guess(text: str):
    t = text.lower();
    gender = ''

    for w in male_words:
        if t.__contains__(w):
            gender = 'M'
            break

    for w in female_words:
        if t.__contains__(w):
            gender = 'F'
            break


    return gender
