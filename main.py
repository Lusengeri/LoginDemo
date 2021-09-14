import os
import logging

from flask import Flask, jsonify, send_from_directory
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
#from flask_swagger import swagger
#from flask_swagger_ui import get_swaggerui_blueprint

from api.config import config

from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp
#from api.utils.email import mail

#from api.routes.authors import author_routes
#from api.routes.books import book_routes
from api.routes.users import user_routes

app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = config.ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = config.TestingConfig
else:
    app_config = config.DevelopmentConfig

app.config.from_object(app_config)

# START GLOBAL HTTP CONFIGURATIONS
#app.register_blueprint(author_routes, url_prefix='/api/authors')
#app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')

#@app.route('/avatar/<filename>')
#def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.after_request
def add_header(response):
    return response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

#@app.route('/api/spec')
#def spec():
    #swag = swagger(app, prefix='/api')
    #swag['info']['base'] = "http://localhost:5000"
    #swag['info']['version'] = "1.0"
    #swag['info']['title'] = "Flask Author DB"
    #return jsonify(swag)

#swaggerui_blueprint = get_swaggerui_blueprint('/api/docs', '/api/spec', config={'app_name': "Flask Author DB"})
#app.register_blueprint(swaggerui_blueprint) 

jwt = JWTManager(app)
#mail.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)

    # START GLOBAL HTTP CONFIGURATIONS
    #app.register_blueprint(author_routes, url_prefix='/api/authors')
    #app.register_blueprint(book_routes, url_prefix='/api/books')
    app.register_blueprint(user_routes, url_prefix='/api/users')

    #@app.route('/avatar/<filename>')
    #def uploaded_file(filename):
        #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    #@app.route('/api/spec')
    #def spec():
        #swag = swagger(app, prefix='/api')
        #swag['info']['base'] = "http://localhost:5000"
        #swag['info']['version'] = "1.0"
        #swag['info']['title'] = "Flask Author DB"
        #return jsonify(swag)

    #swaggerui_blueprint = get_swaggerui_blueprint('/api/docs', '/api/spec', config={'app_name': "Flask Author DB"})
    #app.register_blueprint(swaggerui_blueprint) 

    jwt = JWTManager(app)
    mail.init_app(app)
    #db.init_app(app)
    #with app.app_context():
        #db.create_all()

    return app

if __name__ == "__main__":
    app.run()
