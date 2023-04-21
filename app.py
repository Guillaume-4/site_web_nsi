from flask import Flask, render_template, request
from templates.script.morse import morse_encode, morse_decode
from templates.script.cesar import cesar_coder, cesar_decoder
from templates.script.pigpen import pigpen_encode, pigpen_decode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/morse', methods=['GET', 'POST'])
def morse():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        print(phrase_a_decoder)
        decoder = morse_decode(phrase_a_decoder)
        print(decoder)
        return render_template("/morse/morse.html") + f'<h1 class="reponse">La Phrase décodée est: {decoder}</h1>'
    elif phrase_a_coder != None and phrase_a_decoder == None:
        print(phrase_a_coder)
        coder = morse_encode(phrase_a_coder)
        print(coder)
        return render_template("/morse/morse.html") + f'<h1 class="reponse">La Phrase coder est: {coder}</h1>'
    else:
        return render_template("/morse/morse.html")
    


@app.route('/cesar', methods=['GET', 'POST'])
def cesar():
    phrase_a_coder = request.form.get("cesar_code")
    phrase_a_decoder = request.form.get("cesar_decode")
    
    if phrase_a_coder == None and phrase_a_decoder != None:
        nombre = request.form.get("Nb_Code")
        print(phrase_a_decoder)
        decoder = cesar_decoder(phrase_a_decoder, nombre)
        print(decoder)
        return render_template("/cesar/cesar.html") + f"<h1>La Phrase décodée est: {decoder}</h1> "
    elif phrase_a_coder != None and phrase_a_decoder == None:
        nombre = request.form.get("Nb_Code")
        print(phrase_a_coder)
        coder = cesar_coder(phrase_a_coder, nombre)
        print(coder)
        return render_template("/cesar/cesar.html") + f"<h1>La Phrase coder est: {coder}</h1> "
    else:
        return render_template("/cesar/cesar.html")

@app.route('/pigpen', methods=['GET', 'POST'])
def pigpen():
    phrase_a_coder = request.form.get("a_coder")
    phrase_a_decoder = request.form.get("a_decoder")
    if phrase_a_coder == None and phrase_a_decoder != None:
        print(phrase_a_decoder)
        decoder = pigpen_decode(phrase_a_decoder)
        print(decoder)
        return render_template("/pigpen/pigpen.html") + f"<h1>La Phrase décodée est: {decoder}</h1> "
    elif phrase_a_coder != None and phrase_a_decoder == None:
        print(phrase_a_coder)
        coder = pigpen_encode(phrase_a_coder)
        print(coder)
        return render_template("/pigpen/pigpen.html") + f"<h1>La Phrase coder est: {coder}</h1> "
    else:
        return render_template("/pigpen/pigpen.html")




phrase_a_decoder = None
phrase_a_coder = None
app.run(debug=True) 