from textblob import TextBlob
from flask import Flask, request
from flask.templating import render_template
import textblob
import pycountry

#Instantiation of flask
app = Flask(__name__)

#Homepage 
@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/', methods = ['get', 'post'])
def result():
    input = request.form.get('paragraph')
    lang_code, value = request.form.get('languages').split('-')
    blob = TextBlob(input)
    iso_code = blob.detect_language()
    input_lang = pycountry.languages.get(alpha_2 = iso_code).name
    text = str(blob.translate(to=lang_code))
    print(text)
    return render_template('home_page.html', text=text, input = input, lang_code = lang_code, value = value, input_lang= input_lang)



if __name__ == '__main__' :
    app.run(debug = True)

