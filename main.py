class MorseCode:
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

    def converter(self, pre: str) -> str:
        # morse code doesn't recognize capital and lower letters
        # also our dict has only lower, that is why we use .lower()
        pre = pre.lower()
        # container for final translation
        post = ''
        for x in pre:
            if x in self.morse_code.keys():
                post += self.morse_code[x] + ' '
            if x == ' ':
                # in morse code you are supposed to put to spaces between words
                # since we end each letter with space we only need to put one here
                post += ' '
        return post

    def decipher(self, pre: str) -> str:
        # to avoid putting space between every letter, we'll slice it and get only words
        pre = pre.split(' ')
        post = ''
        for x in pre:
            try:
                post += self.reversed_morse[x]

            # in keys of space we will hit key error
            # because .split had put '' where two spaces were
            # here simply turning it back to one space
            except KeyError:
                post += ' '

        return post


if __name__ == '__main__':
    converter = MorseCode()
    while True:
        choice = input("(1) Convert to morse code\n(2) Convert from morse code to string\n"
                       "(3) Exit\n")
        if choice == '1':
            print(converter.converter(input("Type sentence that you want to convert:\n")))
        elif choice == '2':
            print(converter.decipher(input("Type morse code that you want to convert:\n")))
        elif choice == '3':
            break
