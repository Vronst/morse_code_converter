morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
reversed_morse = dict(zip(list(morse_code.values()), list(morse_code.keys())))


def converter(pre: str) -> str:
    # morse code doesn't recognize capital and lower letters
    # also our dict has only lower, that is why we use .lower()
    pre = pre.lower()
    # container for final translation
    post = ''
    for x in pre:
        if x in morse_code.keys():
            post += morse_code[x] + ' '
        if x == ' ':
            # in morse code you are supposed to put to spaces between words
            # since we end each letter with space we only need to put one here
            post += ' '
    return post


def decipher(pre: str) -> str:
    # to avoid putting space between every letter, we'll slice it and get only words
    pre = pre.split(' ')
    post = ''
    for x in pre:
        try:
            post += reversed_morse[x]

        # in keys of space we will hit key error
        # because .split will put '' where two spaces were
        # simply turning it back to one space
        except KeyError:
            post += ' '

    # [:-1] so we will get rid of space at the end
    return post[:-1]
