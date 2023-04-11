from flask import Flask, render_template, request
from templates.script.morse import morse_encode, morse_decode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/morse', methods=['GET', 'POST'])
def autre_page():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        print(phrase_a_decoder)
        decoder = morse_decode(phrase_a_decoder)
        print(decoder)
        return render_template("/morse/morse.html") + f"<h1>La Phrase décoder est: {decoder}</h1> "
    elif phrase_a_coder != None and phrase_a_decoder == None:
        print(phrase_a_coder)
        coder = morse_encode(phrase_a_coder)
        print(coder)
        return render_template("/morse/morse.html") + f"<h1>La Phrase coder est: {coder}</h1> "
    else:
        return render_template("/morse/morse.html")
    


@app.route('/cesar')
def cesar():
    return render_template("/cesar/cesar.html")

phrase_a_decoder = None
phrase_a_coder = None
app.run(debug=True)