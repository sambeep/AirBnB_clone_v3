from flask import Flask
from models import storage
from api.v1.views import app_views

def create_app():
    app = Flask(__name__)
    
    # Register the blueprint
    app.register_blueprint(app_views)
    
    # Teardown context
    @app.teardown_appcontext
    def teardown(exception):
        storage.close()
    
    return app

app = create_app()

if __name__ == "__main__":
    from os import environ
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
