from flask_app import app
from flask_app.controllers import (book_controller, inquiry_controller,
                                   order_controller, user_controller)

if __name__ == "__main__":
    app.run(debug=True, port=5001)