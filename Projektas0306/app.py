from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.secret_key = "super_saugus_raktas"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///darbovietes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
lt_timezone = pytz.timezone("Europe/Vilnius")

# ✅ Darboviečių modelis su darbuotojų skaičiaus atnaujinimu
class Darboviete(db.Model):
    __tablename__ = "darbovietes"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(100), nullable=False, unique=True)
    miestas = db.Column(db.String(100), nullable=False)
    darbuotoju_skaicius = db.Column(db.Integer, default=0)
    darbuotojai = db.relationship('Darbuotojas', backref='darboviete', lazy=True, cascade="all, delete-orphan")

# ✅ Darbuotojų modelis su ištrynimo žyma
class Darbuotojas(db.Model):
    __tablename__ = "darbuotojai"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(100), nullable=False)
    pavarde = db.Column(db.String(100), nullable=False)
    pareigos = db.Column(db.String(100), nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey('darbovietes.id', ondelete="CASCADE"), nullable=False)
    sukurimo_data = db.Column(db.DateTime, default=lambda: datetime.now(lt_timezone))
    is_aktyvus = db.Column(db.Boolean, default=True)  # ✅ Pridėta neaktyvaus įrašo žyma

# ✅ Automatinis darbuotojų skaičiaus atnaujinimas
@app.after_request
def update_employee_count(response):
    with app.app_context():
        for darboviete in Darboviete.query.all():
            darboviete.darbuotoju_skaicius = Darbuotojas.query.filter_by(darboviete_id=darboviete.id, is_aktyvus=True).count()
        db.session.commit()
    return response

# ✅ Sukuriame naują duomenų bazę
with app.app_context():
    db.create_all()

# ✅ Pagrindinis puslapis
@app.route('/')
def index():
    darbovietes = Darboviete.query.all()
    darbuotojai = Darbuotojas.query.all()
    return render_template("index.html", darbovietes=darbovietes, darbuotojai=darbuotojai)

# ✅ Pridėti darbovietę
@app.route("/prideti-darboviete", methods=["GET", "POST"])
def prideti_darboviete():
    if request.method == "POST":
        pavadinimas = request.form["pavadinimas"]
        miestas = request.form["miestas"]
        nauja_darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas)
        db.session.add(nauja_darboviete)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("prideti_darboviete.html")

# ✅ Pridėti darbuotoją
@app.route("/prideti-darbuotoja", methods=["GET", "POST"])
def prideti_darbuotoja():
    darbovietes = Darboviete.query.all()
    if request.method == "POST":
        vardas = request.form["vardas"]
        pavarde = request.form["pavarde"]
        pareigos = request.form["pareigos"]
        darboviete_id = request.form["darboviete_id"]
        naujas_darbuotojas = Darbuotojas(
            vardas=vardas, pavarde=pavarde, pareigos=pareigos, darboviete_id=darboviete_id
        )
        db.session.add(naujas_darbuotojas)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("prideti_darbuotoja.html", darbovietes=darbovietes)

# ✅ Redaguoti darbovietę
@app.route("/redaguoti-darboviete/<int:id>", methods=["GET", "POST"])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    if request.method == "POST":
        darboviete.pavadinimas = request.form["pavadinimas"]
        darboviete.miestas = request.form["miestas"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("redaguoti_darboviete.html", darboviete=darboviete)

# ✅ Redaguoti darbuotoją
@app.route("/redaguoti-darbuotoja/<int:id>", methods=["GET", "POST"])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    darbovietes = Darboviete.query.all()
    if request.method == "POST":
        darbuotojas.vardas = request.form["vardas"]
        darbuotojas.pavarde = request.form["pavarde"]
        darbuotojas.pareigos = request.form["pareigos"]
        darbuotojas.darboviete_id = request.form["darboviete_id"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("redaguoti_darbuotoja.html", darbuotojas=darbuotojas, darbovietes=darbovietes)

# ✅ Trinti darbuotoją (dabar tik žymi kaip neaktyvų)
@app.route("/trinti-darbuotoja/<int:id>", methods=["POST"])
def trinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    darbuotojas.is_aktyvus = False  # ✅ Vietoj trynimo pažymima kaip neaktyvus
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
