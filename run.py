from flask import Flask
from shared import db
from blueprints.base import blueprint as base_blueprint
from blueprints.classes import blueprint as classes_blueprint
from blueprints.athletes import blueprint as athletes_blueprint

# Setting up the application and the configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/alan.erwin/Databases/raxfit.db'
db.app = app
db.init_app(app)
app.register_blueprint(base_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(athletes_blueprint)
if __name__ == '__main__':
    app.run()
