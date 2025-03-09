from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vartotojai')
def vartotojai():
    vardai = ["Mindaugas", "Agnė", "Justinas", "Greta", "Rokas"]
    return render_template('vartotojai.html', vardai=vardai)

@app.route('/vartotojas/<vardas>')
def vartotojas(vardas):
    return f"<h2>Pasirinktas vartotojas: {vardas}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
