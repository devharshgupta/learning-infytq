# lex_auth_01269444195664691284

from operator import le
from re import S


def encrypt_sentence(sentence):
    sentence = sentence.split(' ')
    temp = []
    v = ''
    c = ''
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in range(0, len(sentence)):
        # print(i)
        if i % 2 == 0:
            txt = sentence[i][:: -1]
            temp.append(txt)
            # print(txt)
        else:
            v = ''
            c = ''
            for letter in sentence[i]:
                if letter in vowel:
                    v += letter
                else:
                    c += letter
            temp.append(c+v)
    temp = ' '.join(temp)
    return temp


sentence = "She sells sea shells on the sea shore"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
