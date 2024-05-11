from flask import Flask
from routes.network_routes import network_blueprint # type: ignore

app = Flask(__name__)

# Register blueprints
app.register_blueprint(network_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
