from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pagrindinis')
def pagrindinis():
    return render_template('pagrindinis.html')

@app.route('/apie')
def apie():
    return render_template('apie.html')

@app.route('/vartotojas/<vardas>')
def vartotojas(vardas):
    return render_template('vartotojas.html', vardas=vardas)

@app.route('/skaicius/<int:nr>')
def skaicius(nr):
    return render_template('skaicius.html', nr=nr)

if __name__ == '__main__':
    app.run(debug=True)
