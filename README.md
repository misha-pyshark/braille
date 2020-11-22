# braille
![GitHub Logo](/static/default.png =250x250)
# What?
My intention is to create a very simple and easily accessible [free online English to Braille translator](http://www.fastbraille.com/). There are similar products existing on the internet, yet some are paid or have signifant amounts of third party content or ads that make not the best user experience.<br>

The project includes the following:
* a web app (available at: http://www.fastbraille.com/)
* a RESTful API that can be used by developers to work on similar technology advancement in the field.


# Why?
Globally there are 285 million visually impaired people, of whom 39 million are blind. The majority of the 39 million are older people (aged 50+).
With the evolution of technology and smartphones using braille as a primary reading medium depreciated a lot (currently it's around 10%).

There are several tools that help visually impaired people in their daily life, such as built-in screen voice overs, braille embossers for item taggings, and much more.

Braille literate adults have a higher rate of employment compared to those who don't have proficiency in braille. The purpose of this app is to enhance the accessibility to braille for visually impaired society and their friends and families to allow for better communication and skill development.


# Sample
English: My goal is to create a free online English to Braille translator <br>
Braille: ⠠⠍⠽ ⠛⠕⠁⠇ ⠊⠎ ⠞⠕ ⠉⠗⠑⠁⠞⠑ ⠁ ⠋⠗⠑⠑ ⠕⠝⠇⠊⠝⠑ ⠠⠑⠝⠛⠇⠊⠎⠓ ⠞⠕ ⠠⠃⠗⠁⠊⠇⠇⠑ ⠞⠗⠁⠝⠎⠇⠁⠞⠕⠗


# Usage
To use the online version of the translator, simply go to http://www.fastbraille.com/ and use it like any other translator.

For programmers, the API should be use in the following format: http://fastbraille.com/api/?words=yourwordshere.<br>
Here is a sample Python code:
```python
import requests

mytext='I want to translate this text'

r = requests.get(f'http://fastbraille.com/api/?words={mytext}')
print(r.json())
```
Expected output:
```
{'braille': '⠠⠊ ⠺⠁⠝⠞ ⠞⠕ ⠞⠗⠁⠝⠎⠇⠁⠞⠑ ⠞⠓⠊⠎ ⠞⠑⠭⠞', 'original': 'I want to translate this text'}
```
You should get a dictionary with two key-value pairs, first entry is the braille translation and second entry is the original text.


# Technology
I used:
* Python (algorithm + app)
* CSS (style.css)
* HTML (index.html)
* Flask (app framework)
* PostgreSQL (tracking entries and usage)
* Heroku (deployment)
* Git Hub (code version control)


# Additional Information
The translations provided by this app aren't perfect as I don't know all of the rules for Braille translation. This app provides Grade 1 Braille translation.<br>
In the future, the functionality will be extended to more languages for translation.
