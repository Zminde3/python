from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ Nustatome laiką
lt_timezone = pytz.timezone('Europe/Vilnius')


# ✅ Lentelė "klase_mokinys"
class Mokinys(db.Model):
    __tablename__ = "klase_mokinys"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(100), nullable=False)
    pavarde = db.Column(db.String(100), nullable=False)
    klase = db.Column(db.Integer, nullable=False)
    sukurimo_data = db.Column(db.DateTime, default=lambda: datetime.now(lt_timezone))

    # ✅ Property metodas
    @property
    def sekanti_klase(self):
        return self.klase + 1 if self.klase < 12 else "Baigė mokyklą"


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.args.get('query', '')

    if query:
        mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f"%{query}%")).all()
    else:
        mokiniai = Mokinys.query.all()

    return render_template('index.html', mokiniai=mokiniai, query=query)


# ✅ Pridėti naują mokinį
@app.route('/prideti-mokini', methods=['GET', 'POST'])
def prideti_mokini():
    if request.method == 'POST':
        vardas = request.form.get('vardas')
        pavarde = request.form.get('pavarde')
        klase = request.form.get('klase')

        if vardas and pavarde and klase:
            naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=int(klase))
            db.session.add(naujas_mokinys)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('prideti_mokini.html')  # Rodo POST formą


if __name__ == '__main__':
    app.run(debug=True)
