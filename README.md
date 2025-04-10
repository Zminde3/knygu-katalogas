
# 📚 Knygų katalogas – Flask aplikacija 

Šis projektas – tai pilnai veikianti Flask aplikacija, leidžianti valdyti knygų katalogą per naršyklę. Jame įgyvendintos šios funkcijos:

- ✅ Knygų peržiūra, pridėjimas, redagavimas ir trynimas
- 🔍 Paieška pagal pavadinimą ar autorių
- 🔐 Vartotojo autentifikacija (prisijungimas / atsijungimas)
- 🛡️ Slaptažodžio keitimas
- 🎨 Šiuolaikiškas dizainas su Bootstrap ir gradientiniu fonu
- 💾 Duomenų saugojimas SQLite duomenų bazėje
- 🧾 Pilna dokumentacija `.docx` formatu
- 💥 Galimybė konvertuoti į `.exe` (desktop programą)

---

## 🚀 Paleidimo instrukcijos

### 1. Virtualios aplinkos kūrimas:

```bash
python -m venv .venv
```

### 2. Aktyvavimas (Windows):

```bash
.venv\Scripts\activate
```

### 3. Reikalingų paketų įdiegimas:

```bash
pip install -r requirements.txt
```

### 4. Duomenų bazės sukūrimas su pradiniais duomenimis:

```bash
python book_catalog/seed.py
```

### 5. Projekto paleidimas:

```bash
python book_catalog/app.py
```

Aplikacija bus pasiekiama naršyklėje:
```
http://127.0.0.1:5000
```

---

## 🔐 Prisijungimo duomenys

- **Vartotojas:** admin
- **Slaptažodis:** admin123

---

## 📂 Projekto struktūra

```
book_catalog/
├── app.py                # Flask aplikacijos logika
├── models.py             # SQLAlchemy modeliai
├── seed.py               # Duomenų bazės užpildymas
├── run.py                # Paleidžia serverį ir naršyklę
├── books.db              # SQLite DB
├── templates/            # HTML šablonai
│   ├── index.html
│   ├── login.html
│   ├── add.html
│   ├── edit.html
│   └── change_password.html
├── static/               # CSS ir paveikslėliai
│   ├── style.css
│   └── objects.jpg
```

---

## 🧰 Papildomi įrankiai

### 🔹 `build_exe.bat`

```bat
@echo off
call .venv\Scripts\activate.bat
pyinstaller --onefile ^
--add-data "book_catalog\templates;book_catalog\templates" ^
--add-data "book_catalog\static;book_catalog\static" ^
--add-data "book_catalog\books.db;book_catalog" ^
book_catalog/run.py
pause
```

> Sugeneruoja `dist/run.exe` – paleidžiamą versiją be Python

---

### 🔹 `run.bat`

```bat
@echo off
call .venv\Scripts\activate.bat
python book_catalog/run.py
pause
```

> Paleidžia projektą automatiškai

---

## 📦 Reikalavimai (`requirements.txt`)

```
flask
flask_sqlalchemy
flask_login
werkzeug
```

---

## 📄 Dokumentacija

Projekte yra papildomi `.docx` failai su **detaliu kiekvieno failo paaiškinimu**:

- `Projektas_paaiskinimas.docx`
- `Papildomi_failai_paaiskinimas.docx`

---

## 👨‍💻 Autorius

Projektas sukurtas praktikos/egzamino pagrindu.  
Paruošta  demonstracija kaip realus naudotinas sprendimas.
