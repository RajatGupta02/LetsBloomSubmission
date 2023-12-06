# LetsBloomSubmission

This is a basic implementation of RESTful Api using flask that simulates a library system.

There are 3 main operations the API supports:
* Retrieve All Books

    ```Endpoint: GET /api/books```
    
* Add a New Book

    ```Endpoint: POST /api/books```
* Update Book Details

    ```Endpoint: PUT /api/books/{id}```

    Request Body:
    JSON object with updated book details
    Example:
    ```
    {
        "author": "David Jones",
        "book_id": "4",
        "name": "In Search of Closure"
    }
    ```




## Run Locally

Clone the project

```bash
  git clone https://github.com/RajatGupta02/LetsBloomSubmission.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python api.py
```

Users can make the requests using postman or curl on the server url

