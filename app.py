from flask import Flask, render_template, request
from templates.script.morse import morse_encode, morse_decode
from templates.script.cesar import cesar_coder, cesar_decoder
from templates.script.pigpen import pigpen_encode, pigpen_decode
from templates.script.vigenere import vigenere_encode, vigenere_decode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/morse', methods=['GET', 'POST'])
def morse():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        decoder = morse_decode(phrase_a_decoder)
        return render_template("/morse/morse.html") + f'<h1 class="reponse">La Phrase décodée est: {decoder}</h1>'
    elif phrase_a_coder != None and phrase_a_decoder == None:
        coder = morse_encode(phrase_a_coder)
        return render_template("/morse/morse.html") + f'<h1 class="reponse">La Phrase codée est: {coder}</h1>'
    else:
        return render_template("/morse/morse.html")
    


@app.route('/cesar', methods=['GET', 'POST'])
def cesar():
    phrase_a_coder = request.form.get("cesar_code")
    phrase_a_decoder = request.form.get("cesar_decode")
    
    if phrase_a_coder == None and phrase_a_decoder != None:
        nombre = request.form.get("Nb_Code")
        decoder = cesar_decoder(phrase_a_decoder, nombre)
        return render_template("/cesar/cesar.html") + f"<h1>La Phrase décodée est: {decoder}</h1> "
    elif phrase_a_coder != None and phrase_a_decoder == None:
        nombre = request.form.get("Nb_Code")
        coder = cesar_coder(phrase_a_coder, nombre)
        return render_template("/cesar/cesar.html") + f"<h1>La Phrase codée est: {coder}</h1> "
    else:
        return render_template("/cesar/cesar.html")

@app.route('/pigpen', methods=['GET', 'POST'])
def pigpen():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        decoder = pigpen_decode(phrase_a_decoder)
        return render_template("/pigpen/pigpen.html") + f"<h1>La Phrase décodée est: {decoder}</h1>"
    elif phrase_a_coder != None and phrase_a_decoder == None:
        coder = pigpen_encode(phrase_a_coder)
        return render_template("/pigpen/pigpen.html") + f"<h1>La Phrase codée est: {coder}</h1> "
    else:
        return render_template("/pigpen/pigpen.html")
    
@app.route('/rsa', methods=['GET', 'POST'])
def rsa():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        decoder = cesar_decoder(phrase_a_decoder)
        return render_template("/rsa/rsa.html") + f"<h1>La Phrase décodée est: {decoder}</h1>" 
    elif phrase_a_coder != None and phrase_a_decoder == None:
        coder = cesar_coder(phrase_a_coder)
        return render_template("/rsa/rsa.html") + f"<h1>La Phrase codée est: {coder}</h1> "
    else:
        return render_template("/rsa/rsa.html")
    
@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    phrase_a_coder = request.form.get("a_coder")
    clef_code = request.form.get("clef_code")
    phrase_a_decoder = request.form.get("a_decoder")
    clef_decode = request.form.get("clef_decode")
    if phrase_a_coder == None and phrase_a_decoder != None:
        decoder = vigenere_decode(phrase_a_decoder, clef_decode)
        return render_template("/vigenere/vigenere.html") + f"<h1>La Phrase décodée est: {decoder}</h1>" 
    elif phrase_a_coder != None and phrase_a_decoder == None:
        coder = vigenere_encode(phrase_a_coder, clef_code)
        return render_template("/vigenere/vigenere.html") + f"<h1>La Phrase codée est: {coder}</h1> "
    else:
        return render_template("/vigenere/vigenere.html")




phrase_a_decoder = None
phrase_a_coder = None
app.run(debug=True) 