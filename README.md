# English to Braille Translator
<img src="https://github.com/misha-pyshark/braille/blob/main/static/default.png" alt="FastBraille" align="center" width="250"/>


# What?
My intention is to create a very simple and easily accessible [free online English to Braille translator](https://www.fastbraille.com/). There are similar products existing on the internet, yet some are paid or have significant amounts of third-party content or ads that make not the best user experience.<br>

The project includes the following:
* a web app (available at: https://www.fastbraille.com/)
* a RESTful API that can be used by developers to work on similar technology advancement in the field.


# Why?
Globally there are 285 million visually impaired people, of whom 39 million are blind. The majority of the 39 million are older people (aged 50+).
With the evolution of technology and smartphones using braille as a primary reading medium depreciated a lot (currently it's around 10%).

There are several tools that help visually impaired people in their daily life, such as built-in screen voice-overs, braille embossers for item taggings, and much more.

Braille literate adults have a higher rate of employment compared to those who don't have proficiency in braille. The purpose of this app is to enhance the accessibility to braille for visually impaired society and their friends and families to allow for better communication and skill development.


# Sample
English: My goal is to create a free online English to Braille translator <br>
Braille: ⠠⠍⠽ ⠛⠕⠁⠇ ⠊⠎ ⠞⠕ ⠉⠗⠑⠁⠞⠑ ⠁ ⠋⠗⠑⠑ ⠕⠝⠇⠊⠝⠑ ⠠⠑⠝⠛⠇⠊⠎⠓ ⠞⠕ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠞⠗⠁⠝⠎⠇⠁⠞⠕⠗

# Requirements
- Python 3 (or newer)
- virtualenv (optional)
- PostgreSQL

# Installation
It's recommended to run with virtualenv, make sure you are running a python3 environment. Installing via pip3 in a v2 environment will not configure the environment to run installed modules from the command line.

```bash
python3 -m virtualenv env
source env/bin/activate
```

- Install the dependencies:
```bash
pip3 install -r requirements.txt
```

- Running local:
```bash
export FLASK_ENV=development
python3 app.py
```

# Usage
To use the online version of the translator, simply go to https://www.fastbraille.com/ and use it like any other translator.

For programmers, the API should be use in the following format: https://fastbraille.com/api/yourwordshere.<br>
- Example using python code:
```python
import requests

mytext='I want to translate this text'

r = requests.get(f'https://fastbraille.com/api/{mytext}')
print(r.json())
```
- Example using curl:
```shell
# using %20 to replace space characters
export MY_TEXT=$(echo 'I want to translate this text' | sed 's/ /%20/g')
curl -X GET "https://fastbraille.com/api/{$MY_TEXT}"
```

Expected output:
```shell
{'braille': '⠠⠊ ⠺⠁⠝⠞ ⠞⠕ ⠞⠗⠁⠝⠎⠇⠁⠞⠑ ⠞⠓⠊⠎ ⠞⠑⠭⠞', 'original': 'I want to translate this text'}
```
You should get a dictionary with two key-value pairs, first entry is the braille translation and second entry is the original text.


# Technology
I used:
* Python (algorithm + app)
* CSS (style.css)
* HTML (index.html)
* Flask (app framework + RESTful API)
* PostgreSQL (tracking entries and usage)
* Heroku (deployment)
* Git Hub (code version control)


# Additional Information
The translations provided by this app aren't perfect as I don't know all of the rules for Braille translation. This app provides Grade 1 Braille translation.<br>
In the future, the functionality will be extended to more languages for translation.
