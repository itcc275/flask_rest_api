 # type: ignore

from flask import Flask
from controllers.item_controller import item_controller

app = Flask(__name__)
app.register_blueprint(item_controller)

if __name__ == '__main__':
    app.run(host='127.0.1', port=5000, debug=True)