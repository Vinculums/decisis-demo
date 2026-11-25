from bookshop.db.models import Book
from bookshop.db.session import open_session


def order_total(book_ids):
    with open_session() as session:
        books = [session.get(Book, book_id) for book_id in book_ids]
    return sum(book.price for book in books)


def render_total(book_ids):
    return f"Total: {order_total(book_ids):.2f}"
