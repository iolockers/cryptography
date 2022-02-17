import matplotlib.pylab as plt

LETTERS = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 0

def crack_ceaser_v1(cipher_text):

    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index] 

        print('With the %s key, the result is %s' % (key, plain_text))

def frequency_analysis(cipher_text):
    cipher_text = cipher_text.upper()

    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in cipher_text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()

def crack_ceaser_v2(cipher_text):
    plain_text = ''
    freq = frequency_analysis(cipher_text)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    key = LETTERS.find(freq[0][0]) - LETTERS.find(' ')
    
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - key) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index] 

    print('With the %s key, the result is %s' % (key, plain_text))
        

if __name__ == '__main__':
    cipher_text = "NSEUZGQNXMNSLEFSIELWFUMNHEIJXNLSDEQTWJRENUXZRENXEFEUQFHJMTQIJWEYJBYEHTRRTSQCEZXJIEYTEIJRTSXYWFYJEYMJE NXZFQEKTWRETKEFEITHZRJSYETWEFEYCUJKFHJEANYMTZYEWJQCNSLETSERJFSNSLKZQEHTSYJSYDEQTWJRENUXZRERFCEGJEZXJIEFXEFEUQFHJMTQIJWEGJKTWJEYMJEKNSFQEHTUCENXEF FNQFGQJ"
    crack_ceaser_v2(cipher_text)
