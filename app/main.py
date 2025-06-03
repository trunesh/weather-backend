from flask import Flask
from routes import weather_bp
import os

app = Flask(__name__)
app.register_blueprint(weather_bp)

port = int(os.environ.get("PORT", 8080))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
