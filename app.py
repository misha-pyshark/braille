from flask import Flask, request, jsonify, render_template
import os

###Map English alphabet to braille

#Letters dictionary
letters = {
    'a': u'\u2801',
    'b': u'\u2803',
    'c': u'\u2809',
    'd': u'\u2819',
    'e': u'\u2811',
    'f': u'\u280b',
    'g': u'\u281b',
    'h': u'\u2813',
    'i': u'\u280a',
    'j': u'\u281a',
    'k': u'\u2805',
    'l': u'\u2807',
    'm': u'\u280d',
    'n': u'\u281d',
    'o': u'\u2815',
    'p': u'\u280f',
    'q': u'\u281f',
    'r': u'\u2817',
    's': u'\u280e',
    't': u'\u281e',
    'u': u'\u2825',
    'v': u'\u2827',
    'w': u'\u283a',
    'x': u'\u282d',
    'y': u'\u283d',
    'z': u'\u2835',
    'capital': u'\u2820'
}


#Numbers dictionary
numbers = {
    '#': u'\u283c',
    '1': u'\u2801',
    '2': u'\u2803',
    '3': u'\u2809',
    '4': u'\u2819',
    '4': u'\u2811',
    '6': u'\u280b',
    '7': u'\u281b',
    '8': u'\u2813',
    '9': u'\u280a',
    '0': u'\u281a'
}


#Characters dictionary
characters = {
    '!': chr(10262),
    '"': u'\u2810',
    '$': u'\u282b',
    '%': u'\u2829',
    '&': u'\u282f',
    "'": u'\u2804',
    '(': u'\u2837',
    ')': u'\u283e',
    '*': u'\u2821',
    '+': u'\u282c',
    ',': u'\u2820',
    '-': u'\u2824',
    '.': u'\u2828',
    '/': u'\u280c',
    ':': u'\u2831',
    ';': u'\u2830',
    '<': u'\u2823',
    '=': u'\u283f',
    '>': u'\u281c',
    '?': u'\u2839',
    '@': u'\u2808',
    '[': u'\u282a',
    ']': u'\u283b',
    '^': u'\u2818',
    '_': u'\u2838'
}


#App starts here
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def translation():
    '''
    For rendering results on HTML GUI
    '''
    text_input = [str(x) for x in request.form.values()][0]

    #Split the sentence by ' ' into a list or words
    def splitter(string):
        string=string.split(" ")
        return string

    def translate(sentence):
        #Create an empty list for translation results
        translation=[]

        #Go through each word in the list of words
        for word in sentence.split(" "):
            #Create an empty list to store each translated character
            trans_word=[]
            #Check if the word is all numbers, if not then continue
            if word.isnumeric()==False:
                #Go through each character in the word
                for char in word:
                    #Check if character is a letter
                    if char.isalpha():
                        #Check if the letter is uppercase, if yes, continue
                        if char.isupper():
                            #Add a specific character for uppercase letter
                            trans_word.append(letters['capital'])
                            #Convert the character to lowercase
                            char=char.lower()
                        #Seach for the letter character in the dictionary of letters
                        for key, value in letters.items():
                            #If there is a match, store it as translation
                            if char == key: 
                                braille=value
                                trans_word.append(braille)
                            #If no match, continue
                            else:
                                continue
                    #Check if character is a special character
                    elif char in characters.keys():
                        #Seach for the special character in the dictionary of characters
                        for key, value in characters.items():
                            #If there is a match, store it as translation
                            if char == key: 
                                braille=value
                                trans_word.append(braille)
                            #If no match, continue
                            else:
                                continue
                    #Check if character is a digit
                    elif char in numbers.keys():
                        #Add a specific character for digits
                        trans_word.append(numbers['#'])
                        #Seach for the digit in the dictionary of numbers
                        for key, value in numbers.items():
                            #If there is a match, store it as translation
                            if char == key: 
                                braille=value
                                trans_word.append(braille)
                            #If no match, continue
                            else:
                                continue
                #Add the translated word to the list
                translation.append(trans_word)

            #It only makes here is all characters in the word are digits
            else:
                #Add a specific character for digits
                trans_word.append(numbers['#'])
                #Go through each character in the word
                for char in word:
                    #Seach for the digit in the dictionary of numbers
                    for key, value in numbers.items():
                        #If there is a match, store it as translation
                        if char == key: 
                            braille=value
                            trans_word.append(braille)
                        #If no match, continue
                        else:
                            continue
                #Add the translated word to the list
                translation.append(trans_word)

        return translation    

    def final(user_input):
        new_t=[]
        for word in translate(user_input):
            new_t.append(''.join(word))

        return ' '.join(new_t)

    try:
        output = final(text_input)
    except:
        raise ValueError

    return render_template('index.html', prediction_text=output, translator_text=text_input)


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run()
