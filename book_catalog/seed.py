from flask import Flask
from models import db, Book, Category, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    cat1 = Category(name='Romanas')
    cat2 = Category(name='Pasaka')
    cat3 = Category(name='Mokslinė literatūra')
    db.session.add_all([cat1, cat2, cat3])
    db.session.commit()

    books = [
        Book(title='ALTORIŲ ŠĖŠĖLY', category_id=cat1.id, price=5.79, release_date='2021', author='VINCAS MYKOLAITIS PUTINAS'),
        Book(title='MAŽASIS PRINCAS', category_id=cat2.id, price=15.13, release_date='2021', author='ANTOINE DE SAINT-EXUPERY'),
        Book(title='TRUMPA LAIKO ISTORIJA', category_id=cat3.id, price=11.24, release_date='2018', author='STIVENAS HOKINGAS (STEPHEN HAWKING)'),
        Book(title='NEPATAISOMAS ROMANTIKAS', category_id=cat1.id, price=15.90, release_date='2018', author='FRANK TALLIS'),
        Book(title='PIKTAS MEDUS', category_id=cat1.id, price=27.29, release_date='2024', author='JODI PICOULT'),
        Book(title='EKONOMIKOS SMOGIKO IŠPAŽINTIS', category_id=cat3.id, price=10.90, release_date='2011', author='JOHN PERKINS'),
        Book(title='KOPA (MESIJAS)', category_id=cat1.id, price=21.99, release_date='2022', author='FRANK HERBERT'),
        Book(title='PINIGŲ PSICHOLOGIJA', category_id=cat1.id, price=17.99, release_date='2022', author='MORGAN HOUSEL'),
        Book(title='SURASIU TAVE', category_id=cat1.id, price=17.99, release_date='2023', author='HARLAN COBEN'),
        Book(title='ŠEŠI KAPAI', category_id=cat1.id, price=20.95, release_date='2022', author='ANGELA MARSONS'),
        Book(title='GYVAS LIKS TIK VIENAS. KITO KELIO NĖRA', category_id=cat1.id, price=12.49, release_date='2022', author='M.J. ARLIDGE'),
        Book(title='BEVARDĖ MERGINA', category_id=cat1.id, price=26.29, release_date='2023', author='LISA REGAN'),
        Book(title='ATSKAITOS TAŠKAS', category_id=cat1.id, price=23.89, release_date='2018', author='JORN LIER , THOMAS ENGER'),
        Book(title='MEILĖ MĖGSTA TYLĄ', category_id=cat1.id, price=19.99, release_date='2025', author='MINDAUGAS BERNOTAS'),
        Book(title='TRIUŠIŲ MEDŽIOTOJAS', category_id=cat1.id, price=17.49, release_date='2019', author='LARS KEPLER'),
        Book(title='KULTAS', category_id=cat1.id, price=25.39, release_date='2023', author='CAMILLA LÄCKBERG, HENRIK FEXEUS'),
        Book(title='DĖŽĖ', category_id=cat1.id, price=28.79, release_date='2022', author='CAMILLA LÄCKBERG, HENRIK FEXEUS'),
        Book(title='LIETUVOS ISTORIJA', category_id=cat3.id, price=109.99, release_date='2012', author='EVALDAS BAKONIS IR KITI')
    ]
    db.session.bulk_save_objects(books)

    admin = User(
        username='admin',
        password=generate_password_hash('admin123')
    )
    db.session.add(admin)

    db.session.commit()
