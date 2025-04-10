from flask import Flask
from router.router import vitvini_bp

app = Flask(__name__)

app.register_blueprint(vitvini_bp)

if __name__ == "__main__":
    app.run(debug=True)