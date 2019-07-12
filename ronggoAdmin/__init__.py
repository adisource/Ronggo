from flask import Flask
from importlib import import_module
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def register_blueprints(app):
    for module_name in ('base','admin','models','nasabah','buku_tabungan','transaksi','sampah','laporan'):
        module = import_module('ronggoAdmin.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def create_app(selenium=False):
    app = Flask(__name__, static_folder='base/static')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@0.0.0.0/data_ronggo'
    

    
    db.init_app(app)
    migrate.init_app(app, db)
    app.secret_key = "c984c6d6f19316dbf8f2a5211bc98263"
 
    register_blueprints(app)

    return app

db = SQLAlchemy()
migrate = Migrate()