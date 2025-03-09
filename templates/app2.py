from flask import Flask, request, render_template, redirect, url_for, flash
import re  # Reguliarios išraiškos el. pašto validacijai

app = Flask(__name__)
app.secret_key = 'slaptas_raktas'


# Pagrindinis puslapis
@app.route('/')
def home():
    return render_template('index.html')


# 1. GET forma paieškai
@app.route('/paieska', methods=['GET', 'POST'])
def paieska():
    if request.method == 'POST':
        fraze = request.form.get('fraze')
        return render_template('paieskos_rezultatas.html', fraze=fraze)
    return render_template('forma_get.html')


# 2. POST forma prisijungimui
@app.route('/prisijungti', methods=['GET', 'POST'])
def prisijungti():
    if request.method == 'POST':
        vartotojas = request.form.get('vartotojas')
        return render_template('prisijungimo_rezultatas.html', vartotojas=vartotojas)
    return render_template('forma_post.html')


# 3. Registracijos forma su išplėstine validacija
@app.route('/registracija', methods=['GET', 'POST'])
def registracija():
    if request.method == 'POST':
        vartotojas = request.form.get('vartotojas')
        el_pastas = request.form.get('el_pastas')  # El. pašto laukas
        slaptazodis = request.form.get('slaptazodis')
        slaptazodis_pakartotas = request.form.get('slaptazodis_pakartotas')

        # 1️⃣ Tikriname, ar visi laukai užpildyti
        if not vartotojas or not el_pastas or not slaptazodis or not slaptazodis_pakartotas:
            flash('⚠️ Užpildykite visus laukus!')

        # 2️⃣ Tikriname, ar el. paštas tinkamo formato
        elif not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', el_pastas):
            flash('⚠️ Netinkamas el. pašto formatas!')

        # 3️⃣ Tikriname slaptažodžio ilgį
        elif len(slaptazodis) < 6:
            flash('⚠️ Slaptažodis turi būti bent 6 simbolių ilgio!')

        # 4️⃣ Tikriname, ar slaptažodyje yra bent viena didžioji raidė
        elif not any(c.isupper() for c in slaptazodis):
            flash('⚠️ Slaptažodyje turi būti bent viena didžioji raidė!')

        # 5️⃣ Tikriname, ar slaptažodyje yra bent vienas skaičius
        elif not any(c.isdigit() for c in slaptazodis):
            flash('⚠️ Slaptažodyje turi būti bent vienas skaičius!')

        # 6️⃣ Tikriname, ar slaptažodyje yra bent vienas specialus simbolis
        elif not any(c in '!@#$%^&*()_+' for c in slaptazodis):
            flash('⚠️ Slaptažodyje turi būti bent vienas specialus simbolis (!@#$%^&*)!')

        # 7️⃣ Tikriname, ar abu slaptažodžiai sutampa
        elif slaptazodis != slaptazodis_pakartotas:
            flash('⚠️ Slaptažodžiai nesutampa!')

        # 8️⃣ Jei viskas tvarkoje – registracija sėkminga
        else:
            flash('✅ Sėkmingai užsiregistravote!')
            return redirect(url_for('registracija'))

    return render_template('registracija.html')


if __name__ == '__main__':
    app.run(debug=True)
