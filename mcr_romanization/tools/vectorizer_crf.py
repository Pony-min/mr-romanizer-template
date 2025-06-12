import string
from hanja import hangul
from mcr_romanization.tools.jamo import decompose_character
def get_jamos(character):
    if hangul.is_hangul(character):
        character_jamos = decompose_character(character, final_char=True)
    elif character in string.punctuation:
        character_jamos = ['.', '.', '.']
    elif character.isdigit():
        character_jamos = ['0', '0', '0']
    elif character.isalpha():
        character_jamos = ['a', 'a', 'a']
    else:
        character_jamos = ['x', 'x', 'x']
    return character_jamos

def character_features(sentence, index):
    character = sentence[index]
    character_jamos = get_jamos(character)

    features = [
        'bias',
        f'char={character}',
        f'jamo1={character_jamos[0]}',
        f'jamo2={character_jamos[1]}',
        f'jamo3={character_jamos[2]}'
    ]

    if index > 0:
        before = sentence[index - 1]
        before_jamos = get_jamos(before)
        features += [
            f'before-char={before}',
            f'before-bigram={before}{character}',
            f'before-jamo1={before_jamos[0]}',
            f'before-jamo2={before_jamos[1]}',
            f'before-jamo3={before_jamos[2]}'
        ]
    else:
        features.append('BOS')

    if index < len(sentence) - 1:
        after = sentence[index + 1]
        after_jamos = get_jamos(after)
        features += [
            f'after-char={after}',
            f'after-bigram={character}{after}',
            f'after-jamo1={after_jamos[0]}',
            f'after-jamo2={after_jamos[1]}',
            f'after-jamo3={after_jamos[2]}'
        ]
    else:
        features.append('EOS')

    if index > 1:
        before2 = sentence[index - 2]
        before2_jamos = get_jamos(before2)
        features += [
            f'before2-char={before2}',
            f'before2-bigram={before2}{sentence[index - 1]}',
            f'before2-trigram={before2}{sentence[index - 1]}{character}',
            f'before2-jamo1={before2_jamos[0]}',
            f'before2-jamo2={before2_jamos[1]}',
            f'before2-jamo3={before2_jamos[2]}'
        ]
    else:
        features.append('BOS')

    if index < len(sentence) - 2:
        after2 = sentence[index + 2]
        after2_jamos = get_jamos(after2)
        features += [
            f'after2-char={after2}',
            f'after2-bigram={sentence[index + 1]}{after2}',
            f'after2-trigram={character}{sentence[index + 1]}{after2}',
            f'after2-jamo1={after2_jamos[0]}',
            f'after2-jamo2={after2_jamos[1]}',
            f'after2-jamo3={after2_jamos[2]}'
        ]
    else:
        features.append('EOS')

    return features

def create_sentence_features_crf(sentence):
    return [character_features(sentence, i) for i in range(len(sentence))]
