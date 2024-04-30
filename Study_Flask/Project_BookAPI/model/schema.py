import marshmallow as ma


# https://flask-smorest.readthedocs.io/en/latest/quickstart.html
# 마시멜로우 Quickstart

"""
2. **책 스키마 정의** (**`schemas.py`**)
    - Marshmallow를 사용하여 책 정보를 위한 스키마를 정의합니다. 
    - 책은 최소한 'title'(제목)과 'author'(저자) 필드를 가져야 합니다.
"""
class BookSchema(ma.Schema):
    book_id = ma.fields.Int(dump_only=True)
    title = ma.fields.String(required=True)
    author = ma.fields.String(required=True)
