male_words = [' he ', ' him ', ' his ', ' husband ', ' father ', ' dad ', ' mr. ']
female_words = [' she ', ' her ', ' hers ', ' wife ', ' mother ', ' mom ', ' mrs .']


def guess(text: str):
    t = text.lower();
    gender = ''

    for w in male_words:
        if t.__contains__(w):
            gender = 'M'
            return gender


    for w in female_words:
        if t.__contains__(w):
            gender = 'F'
            return gender


    return gender
