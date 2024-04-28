from flask import Flask, request, render_template
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html", result="")

def analyze_sentence(sentence):
    words = word_tokenize(sentence)  
    excluded_keywords = ["under", "above","between","below"]

    stop_words = set(stopwords.words('english')) 
    for keyword in excluded_keywords:
        stop_words.discard(keyword)

    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    refined_sentence = ' '.join(filtered_words)
    
    return refined_sentence

original_text = ""

@app.route("/process", methods=["POST"])
def process_text():
    global original_text
    original_text = request.form["original_text"]
    refined_sentence = analyze_sentence(original_text)
    return render_template("index.html", result=refined_sentence)

if __name__ == "__main__":
    app.run(debug=True)
