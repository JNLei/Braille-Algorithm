# Access point for translating braille to text and vice verse.
import printer, alphaToBraille, brailleToAlpha, alphaToSignal
import errorDefine
import fileConversion
from sys import argv

def menu():
    print('''
    Usage:
        main.py <parameter>
        main.py <file name> <parameter>
    Parameters:
        --braille | -b      translate braille to text
        --text    | -t      translate text to braille
        --help    | -h      display this screen
        --map     | -m      print translation map
    ''')


def user_braille():
    print("Input Braille: ", end="")
    print(brailleToAlpha.translate(input()))


def user_text():
    print("Input Text: ", end="")
    print(alphaToBraille.translate(input()))


def open_braille(filename):
    file = open(filename)
    content = file.read()
    print(brailleToAlpha.translate(content))


def open_text(filename):
    file = open(filename)
    content = file.read()
    print(alphaToBraille.translate(content))


def argument_handler():
    print("\nEnter this function, argv length: ", len(argv));
    print("\nargv: ", type(argv[0]));
    try:
        if len(argv) != 3 or ((not isinstance(argv[1], str)) and (not isinstance(argv[2], str))):
            raise errorDefine.TargetNameError
        file = open(argv[1], "r")
        text = file.read()
        file.close()
        file = open("temp.txt", "w")
        file.write(alphaToSignal.translate(text))
        file.close()
        if not fileConversion.fileConvert("temp.txt", argv[2]):
            raise(errorDefine.FileConvertError)
        #print(alphaToSignal.translate(text))
    except errorDefine.TargetNameError:
        print("Error, target file name missing")
    except FileNotFoundError:
        print("Error, file cannot find")
    except OSError:
        print("Error, target file open error")
    except errorDefine.FileConvertError:
        print("Error, writing final braille file")


if __name__ == "__main__":
    argument_handler()

    #text = "Translating text to Grade 2 Braille is a non-trivial task since it is not just a variant of the alphabet, it is an independent writing system. Iterating over a string and translating it one character at a time will not yield correct results for Grade 2 Braille. Many braille symbols have multiple meanings and this can lead to ambiguities. Furthermore, certain words and letters that are commonly seen in the English language can be represented by fewer braille symbols than there are letters (these are called contractions). The algorithm used in this software is summarized below."
    #text = "CHing"
    #print("Alpha: ", text)
    #print("Braille: ", alphaToSignal.translate(text))
    #print(alphaToBraille.translate(text))

