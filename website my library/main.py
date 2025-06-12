from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png"]
app.config["UPLOAD_PATH"] = "image_uploads"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(300), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template('index.html', books=books)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['name']
        author = request.form['author']
        rating = request.form['rating']
        image = request.form['image']
        with app.app_context():
            book = Book(
                title=title,
                author=author,
                rating=rating,
                image=image
            )
            db.session.add(book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit_rating():
    book_id = request.args.get('book_id')
    book_selected = db.get_or_404(Book, book_id)
    if request.method == 'POST':
        # Update record
        book_selected.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete_book():
    book_id = request.args.get('book_id')
    book_selected = db.get_or_404(Book, book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

