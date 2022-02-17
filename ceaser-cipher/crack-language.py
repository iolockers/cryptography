from msilib.schema import Directory

ENGLISH_WORDS = []
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain_text = 'Testing if this text is in English. It will approve texts that are seventy percent or more in English'
plain_text_pt = 'Testando se este texto está em português. Serão aprovados textos que contenham pelo menos setenta porcento ou mais em português'
cipher_text = 'YJXYNSLENKEYMNXEYJBYENXENSEJSLQNXMENYEANQQEFUUWT JEYJBYXEYMFYEFWJEXJ JSYCEUJWHJSYETWERTWJENSEJSLQNXM'
cipher_text_pt = 'YJXYFSITEXJEJXYJEYJBYTEJXYFEJREUTWYZLZJXEXJWFTEFUWT FITXEYJBYTXEVZJEHTSYJSMFREUJQTERJSTXEXJYJSYFEUTWHJSYTETZERFNXEJREUTWYZLZJX'

def get_data():
    dictionary = open("english_words.txt") 

    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictionary.close()

def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0

    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1

    return matches

def is_text_english(text):
    matches = count_words(text)
    if (float(matches) / len(text.split(' '))) * 100 >= 70:
        return True
    return False

def ceaser_crack_english(cipher_text):
    for key in range(len(ALPHABET)):
        text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            text = text + ALPHABET[index] 

        if(is_text_english(text)):
            print('With the %s key, the result is %s' % (key, text))
            return

    print('No valid text in English has been found!')

if __name__ == '__main__':
    dictionary = get_data()
    ceaser_crack_english(cipher_text_pt)
