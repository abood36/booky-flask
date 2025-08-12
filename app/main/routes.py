from flask import render_template, redirect, url_for, flash, request, abort
from . import main
from ..extensions import db
from ..models import Book
from .forms import BookForm, DeleteForm

@main.route("/")
def index():
    books = Book.query.order_by(Book.created_at.desc()).all()
    return render_template("index.html", books=books)

@main.route("/book/<int:book_id>")
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book_detail.html", book=book)

@main.route("/book/create", methods=["GET", "POST"])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data.strip(),
            author=form.author.data.strip(),
            description=form.description.data.strip() if form.description.data else None,
            rating=form.rating.data
        )
        db.session.add(book)
        db.session.commit()
        flash("Book created successfully.", "success")
        return redirect(url_for("main.index"))
    return render_template("book_form.html", form=form, form_action="Create")

@main.route("/book/<int:book_id>/edit", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data.strip()
        book.author = form.author.data.strip()
        book.description = form.description.data.strip() if form.description.data else None
        book.rating = form.rating.data
        db.session.commit()
        flash("Book updated.", "success")
        return redirect(url_for("main.book_detail", book_id=book.id))
    return render_template("book_form.html", form=form, form_action="Edit")

@main.route("/book/<int:book_id>/delete", methods=["GET", "POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted.", "warning")
        return redirect(url_for("main.index"))
    return render_template("confirm_delete.html", book=book, form=form)
