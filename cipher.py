# Author: Alex Brumfield-Meyers
# Date: 2/22/2021

def cipher(phrase: str, key: int) -> str:
    """Shifts phrase through alphabet by steps = key
    :rtype: String
    """
    if key >= 0:
        while key > 26:
            key -= 26
    else:
        while key < -26:
            key += 26
    lower = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z')
    upper = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z')

    phrase = phrase.strip()
    print(phrase)
    new_phrase = ''
    for letter in phrase:
        if letter in lower:
            let_index = lower.index(letter)
            try:
                new_phrase += lower[let_index + key]
            except IndexError:
                new_phrase += lower[let_index + key - 26]
        elif letter in upper:
            let_index = upper.index(letter)
            try:
                new_phrase += upper[let_index + key]
            except IndexError:
                new_phrase += upper[let_index + key - 26]
        else:
            new_phrase += letter
    return new_phrase

# print(cipher("abcde", 1))
# print(cipher('ZYXWV',-10))
# print(cipher("Wow! What a wonderful audience you've been. I feel so grateful.", 45))
