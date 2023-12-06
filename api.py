from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

table = db['books']

def fetch_db(book_id): 
    return table.find_one(book_id=book_id)

def fetch_db_all():
    books = []
    for book in table:
        books.append(book)
    return books

@app.route('/api/addBooks', methods=['GET'])
def populate_db():
    table.insert({
        "book_id": "1",
        "name": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki and Sharon Lechter"
    })

    table.insert({
        "book_id": "2",
        "name": "Ikigai",
        "author": "Francesc Miralles"
    })

    table.insert({
        "book_id": "3",
        "name": "The Power of Your Subconscious Mind",
        "author": "Joseph Murphy"
    })

    return make_response(jsonify(fetch_db_all()),
                         200)


@app.route('/api/books', methods=['GET', 'POST'])
def process_books():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        book_id = content['book_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(book_id)), 201)


@app.route('/api/books/<book_id>', methods=['GET', 'PUT'])
def api_each_book(book_id):
    if request.method == "PUT":
        content = request.json
        table.update(content, ['book_id'])

        book_obj = fetch_db(book_id)
        return make_response(jsonify(book_obj), 200)


if __name__ == '__main__':
    app.run()