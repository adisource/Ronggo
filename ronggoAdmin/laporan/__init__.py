from flask import Blueprint

blueprint = Blueprint(
    'laporan_blueprint',
    __name__,
    url_prefix='/',
    template_folder='templates',
    static_folder='static'
)
