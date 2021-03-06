# Translate alphabet based text to braille.
import mapBrailleToAlpha, mapAlphaToSignal, mapAlphaToBraille

CAPITAL = chr(10272)  # ⠠
LOWER1 = chr(10272)
LOWER2 = chr(10244)
NUMBER = chr(10300)  # ⠼
LETTER = chr(10288)
CAPITAL_S = '000001'
LOWER1_S = '000001'
LOWER2_S = '000010'
NUMBER_S = '010111'
LETTER_S = '000101'
UNRECOGNIZED = '?'
ABBREVIATION = list(mapAlphaToSignal.abbreviation.keys())

# There is no braille symbol for a generic quote (").
# There is only open quotation (“) and closed quotation (”).
# Therefore we must keep track of what the last quotation was
# so that we may convert the generic quotation to a specific one.
open_quotes = True


def extract_words(string):
    # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
    words = string.split(" ")
    result = []
    for word in words:
        temp = word.split("\n")
        for item in temp:
            result.append(item)
    return result


def is_braille(char):
    # Return true if a char is braille.
    if len(char) > 1:
        return False
    return char in mapBrailleToAlpha.letters \
        or char in mapBrailleToAlpha.numbers \
        or char in mapBrailleToAlpha.punctuation \
        or char in mapBrailleToAlpha.contractions \
        or char == CAPITAL \
        or char == NUMBER


def trim(word):
    # Remove punctuation around a word. Example: cat." becomes cat
    while len(word) is not 0 and not word[0].isalnum():
        word = word[1:]
    while len(word) is not 0 and not word[-1].isalnum():
        word = word[:-1]
    return word


def numbers_handler(word):
    # Replace each group of numbers in a word to their respective braille representation.
    if word == "":
        return word
    result = word[0]
    if word[0].isdigit():
        result = NUMBER + word[0]
    for i in range(1, len(word)):
        if word[i].isdigit() and word[i-1].isdigit():
            result += word[i]
        elif word[i].isdigit():
            result += NUMBER + word[i]
        elif not word[i].isdigit() and word[i-1].isdigit():
            result += LETTER + word[i]
        else:
            result += word[i]
    return result


def capital_letters_handler(word):
    # Distinguish capital type
    if word == "" or word.islower():
        return word
    
    if word.isupper():
        return CAPITAL * 2 + word

    word_l = seperate_word(word)
    if word_l[0] == NUMBER or word_l[0].isdigit():
        pass
    elif word_l[0].isupper():
        if len(word_l[0]) > 1:
            word_l[0] = CAPITAL * 2 + word_l[0]
        else:
            word_l[0] = CAPITAL + word_l[0]
    elif not word_l[0].islower():
        word_l[0] = CAPITAL + word_l[0]

    for char in range(1,len(word_l)):
        if word_l[char] == NUMBER or word_l[char] == LETTER or word_l[char].isdigit():
            continue
        if word_l[char].isupper() and (word_l[char-1].islower() or word_l[char-1] == LETTER):
            if len(word_l[char]) > 1:
                word_l[char] = CAPITAL * 2 + word_l[char]
            else:
                word_l[char] = CAPITAL + word_l[char]
        elif word_l[char].islower() and word_l[char-1].isupper() and (len(word_l[char-1]) > 1 and ((CAPITAL*2) in word_l[char-1])):
            word_l[char] = LOWER1 + LOWER2 + word_l[char]
        else:
            if not word_l[char].islower() and not word_l[char].isupper():
                word_l[char] = CAPITAL + word_l[char]
    return ''.join(word_l)


def find_utf_code(char):
    # Find the UTF code of a particular character. Used what an unidentified char is found.
    if len(char) != 1:
        return -1
    for i in range(0, 55000):
        if char == chr(i):
            return i


def char_to_braille(char):
    # Convert an alphabetic char to braille.
    #if is_braille(char):
    #    return char
    if char == "\n":
        return "\n"
    elif char == "\"":
        global open_quotes
        if open_quotes:
            open_quotes = not open_quotes
            return mapAlphaToSignal.punctuation.get("“")
        else:
            open_quotes = not open_quotes
            return mapAlphaToSignal.punctuation.get("”")
    elif char in mapAlphaToSignal.abbreviation:
        return mapAlphaToSignal.abbreviation.get(char)
   # elif char in mapAlphaToSignal.letters and char.isupper():
    #    return CAPITAL + mapAlphaToSignal.letters.get(char)
    elif char in mapAlphaToSignal.letters:
        return mapAlphaToSignal.letters.get(char)
    elif char in mapAlphaToSignal.punctuation:
        return mapAlphaToSignal.punctuation.get(char)
    elif char in mapAlphaToSignal.numbers:
        return mapAlphaToSignal.numbers.get(char)
    elif char == CAPITAL:
        return CAPITAL_S
    elif char == NUMBER:
        return NUMBER_S
    elif char == LETTER:
        return LETTER_S
    elif char == LOWER1:
        return LOWER1_S
    elif char == LOWER2:
        return LOWER2_S
    else:
        print("Unrecognized Symbol:", char, "with UTF code:", find_utf_code(char))
        print(char)
        return UNRECOGNIZED


def word_to_braille(word):
    # Convert an alphabetic word to braille.
    if word in mapAlphaToSignal.contractions:
        return mapAlphaToSignal.contractions.get(word)
    ##########################################################
    word_l = seperate_word(word)
    ##########################################################
    result = ""
    for char in range(len(word_l)):
        result += char_to_braille(word_l[char])
    return result

def seperate_word(word):
    # Seperate the word to parts
    abbreviation = {abr:word.find(abr) for abr in ABBREVIATION if abr in word}
    if 'ing' in abbreviation.keys():
        del abbreviation['in'] 
    if 'Ing' in abbreviation.keys():
        del abbreviation['In']
    if 'ING' in abbreviation.keys():
        del abbreviation['IN']
    abbreviation = sorted(abbreviation.items(), key=lambda kv:kv[1], reverse=True)
    
    word_l = list(word)
    for abr, pos in abbreviation:
        word_l[pos:pos+len(abr)] = [''.join(word_l[pos:pos+len(abr)])]
    return word_l

def build_braille_word(trimmed_word, shavings, index, braille):
    # Translate a trimmed word to braille then re-attach the shavings.
    if shavings == "":
        braille += word_to_braille(trimmed_word)
    else:
        for i in range(0, len(shavings)):
            if i == index and trimmed_word is not "":
                braille += word_to_braille(trimmed_word)
            braille += word_to_braille(shavings[i])
        if index == len(shavings):  # If the shavings are all at the beginning.
            braille += word_to_braille(trimmed_word)
    return braille


def translate(string):
    # Convert alphabetic text to braille.
    braille = ""
    words = extract_words(string)
    for word in words:
        word = numbers_handler(word)
        word = capital_letters_handler(word)
        trimmed_word = trim(word)  # Remove punctuation (ex: change dog?" to dog)
        untrimmed_word = word
        index = untrimmed_word.find(trimmed_word)
        shavings = untrimmed_word.replace(trimmed_word, "")
        braille = build_braille_word(trimmed_word, shavings, index, braille) + " "
    return braille[:-1]  # Remove the final space that was added.

'''
The Algorithm for Translating Alphabet Based Text to Grade 2 Braille:
1. Split up the text into words by dividing them based on whitespace characters.
    - Whitespace includes spaces (' ') and new lines ('\n')
2. For each word, handle the numbers first.
    - Numbers in braille use the same symbols as the first 10 letters of the alphabet.
        - The number '7' and the letter 'g' are both represented by '⠛'.
        - To differentiate between numbers and letters, an escape code (⠼) is placed before groups of numbers.
        - Therefore '7' is actually '⠼⠛' whereas 'g' is only '⠛'.
    - In this step, only the numbers are dealt with, so there will be a mix of both braille and Alphabet symbols.
        - Example: "123-456-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK"
3. Handle the capitals.
    - Similarly to numbers in braille, capital letters need an escape code (⠠).
    - The escape code (⠠) is added to the beginning of each capital letter and the letter is changed to lowercase.
        - Example 1: "⠼⠁⠃⠉-⠼⠙⠑⠋-JUNK" becomes "⠼⠁⠃⠉-⠼⠙⠑⠋-⠠j⠠u⠠n⠠k". The dashes still remain.
        - Example 2: "Sweet" becomes "⠠sweet". The non-capital letters remain untouched.
4. Trim the word.
    - Sometimes the words extracted contain punctuation attached to them such as commas or brackets.
    - Words need to be trimmed so that they can be converted to contractions.
        - Example: The word "the" is represented by a single braille symbol (⠮).
        - If the word "the" has punctuation around it ("the!") then it will not be interpreted correctly.
        - This is also why capitals are converted to lowercase in step 3 because "The" would not work either.
    - The characters that are trimmed off are called "shavings".
        - Example: In the word "!where?", the shavings are "!?" and the trimmed word is "where".
5. Build the translation.
    a) Check to see if the trimmed word can be contracted.
        - This includes common words like "the", "in", "you" etc...
    b) Translate the remaining characters that are still alphabetic.
    c) Translate the shavings (this will mostly just be punctuation).
        - Exceptions to be mindful of:
            - There is no braille symbol for a generic quote (")
            - There is only open quotation (“) and closed quotation (”).
            - Therefore we must keep track of what the last quotation was to convert it correctly.
'''
