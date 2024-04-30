from flask_smorest import Blueprint, abort
from flask.views import MethodView

from model.schema import BookSchema

"""
3. **API 엔드포인트 구현** (**`api.py`**)
    - 책 목록을 보여주는 GET 엔드포인트를 만듭니다.
    - 새 책을 추가하는 POST 엔드포인트를 만듭니다.
    - 특정 책의 정보를 업데이트하는 PUT 엔드포인트를 만듭니다.
    - 특정 책을 삭제하는 DELETE 엔드포인트를 만듭니다.
"""

# temp data storage
books = []

# Instantiate a Blueprint.
blp = Blueprint("books", "books", url_prefix="/books", description="Operations on books")


# use MethodView class to **organize resources**
# Books Class - GET / POST
@blp.route("/")
class Books(MethodView):

    # To inject arguments into a view function, use the Blueprint.arguments decorator
    # Handle a GET request that returns all items
    @blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    # Process a POST request to add a new item
    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1
        books.append(new_data)
        return new_data


@blp.route("/<int:book_id>")
class BookById(MethodView):
    @blp.response(200, BookSchema)
    def get(self, book_id):
        # handle a GET request that returns an item with a specific ID
        # next() => 반복문에서 값이 있으면 값을 반환하고 없으면 None을 반환
        # next는 조건을 만족하는 첫 번째 아이템을 반환하고, 그 이후의 아이템은 무시합니다.

        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        return book

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema, description="Book updated")
    def put(self, new_book, book_id):
        # Process a PUT request to update a book with a specific ID
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Item not found")
        book.update(new_book)
        return book

    @blp.response(204, description="Book deleted")
    def delete(self, book_id):
        # Handling DELETE requests that delete items with a specific ID
        global books
        if not any(book for book in books if book['id'] == book_id):
            abort(404, message="Item not found")
        books = [book for book in books if book['id'] != book_id]
        return ''
