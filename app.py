from flask import Flask, request, jsonify, render_template
from dictionary_en import *


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
    app.debug = False
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
