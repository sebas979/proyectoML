from flask import (
    Blueprint,render_template
)
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.wrappers import response

bp = Blueprint('proyecto',__name__,url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('paginas/index.html')

@bp.route('/matriz', methods=['GET'])
def matriz():
    return render_template('paginas/matriz.html')

@bp.route('/graficos', methods=['GET'])
def graficos():
    return render_template('paginas/graficas.html')

@bp.route('/subir', methods=['GET'])
def subir():
    return render_template('paginas/subirCsv.html')
