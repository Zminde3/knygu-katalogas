from flask import Flask, render_template, request, redirect, url_for
from models import db, Book, Category, User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import os
import sys

app = Flask(__name__)

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

db_path = resource_path("books.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'slaptazodis'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    search = request.args.get('search', '')
    if search:
        books = Book.query.filter(
            (Book.title.ilike(f'%{search}%')) |
            (Book.author.ilike(f'%{search}%'))
        ).all()
    else:
        books = Book.query.all()
    return render_template('index.html', books=books, search=search)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    categories = Category.query.all()
    if request.method == 'POST':
        new_book = Book(
            title=request.form['title'],
            category_id=request.form['category_id'],
            price=request.form['price'],
            release_date=request.form['release_date'],
            author=request.form['author']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', categories=categories)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_book(id):
    book = Book.query.get_or_404(id)
    categories = Category.query.all()
    if request.method == 'POST':
        book.title = request.form['title']
        book.category_id = request.form['category_id']
        book.price = request.form['price']
        book.release_date = request.form['release_date']
        book.author = request.form['author']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', book=book, categories=categories)

@app.route('/delete/<int:id>')
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Neteisingi prisijungimo duomenys.")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    message = None
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']

        if not check_password_hash(current_user.password, current_password):
            message = "❌ Neteisingas dabartinis slaptažodis."
        else:
            current_user.password = generate_password_hash(new_password)
            db.session.commit()
            message = "✅ Slaptažodis sėkmingai pakeistas."
    return render_template('change_password.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
