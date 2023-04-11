from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/morse')
def autre_page():
    return render_template("/morse/morse.html")
app.run(debug=True)