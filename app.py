from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_talisman import Talisman, ALLOW_FROM
from dictionary_en import *



app = Flask(__name__)
api = Api(app)

talisman = Talisman(app, force_https=app.env != 'development', content_security_policy=False)

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://arjhncjjjotxbc:3b583653ee3754dba776fc3a488267c8269b6b8186eb5981056aa970cc707c8f@ec2-23-23-36-227.compute-1.amazonaws.com:5432/d6fks0t2bevn18'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Entries(db.Model):
    __tablename__ = 'all_entries'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))

    def __init__(self, text):
        self.text=text

@app.route('/')
@talisman(frame_options=ALLOW_FROM, frame_options_allow_from='*')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
@talisman(frame_options=ALLOW_FROM, frame_options_allow_from='*')
def translation():
    '''
    For rendering results on HTML GUI
    '''
    text_input = request.form['main_text']

    try:
        output = final(text_input)
        data = Entries(text_input)
        db.session.add(data)
        db.session.commit()
    except:
        raise ValueError

    return render_template('index.html', prediction_text=output, translator_text=text_input)


class TranslatorAPI(Resource):
    def get(self, text):
        return jsonify({'original': text, 'braille': final(text)})

api.add_resource(TranslatorAPI, '/api/<string:text>')



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


if __name__ == "__main__":
    app.run()
