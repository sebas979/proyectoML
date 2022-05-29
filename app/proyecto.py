from flask import (
    Blueprint,render_template,request
)
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import pandas as pd
from . import nlp

bp = Blueprint('proyecto',__name__,url_prefix='/')
datos = nlp.importarCSV('https://raw.githubusercontent.com/sebas979/archicosCSV/main/DataSet.csv');

@bp.route('/', methods=['GET'])
def index():
    return render_template('paginas/index.html')

@bp.route('/matriz', methods=['GET','POST'])
def matriz():
    datosfiltrados = datos
    if request.method == 'POST':
        filtro = ''
        tipo = request.form.get('tipo',type=int)
        tema = request.form.get('tema')
        if tipo != 2 or tema != 'todos':
            if tipo != 2:
                if tipo == 1:
                    filtro = 'tipo == 1'
                if tipo == 0:
                    filtro = 'tipo == 0'
                if tema != 'todos':
                    if tema == 'exactas':
                        filtro += 'and tema == "exactas"'
                    if tema == 'medi':
                        filtro += 'and tema == "Medi"'
                    if tema == 'sociales':
                        filtro += 'and tema == "social"'
                    if tema == 'compu':
                        filtro += 'and tema == "Computacion"'
            else:
                if tema == 'exactas':
                    filtro = 'tema == "exactas"'
                if tema == 'medi':
                    filtro = 'tema == "Medi"'
                if tema == 'sociales':
                    filtro = 'tema == "social"'
                if tema == 'compu':
                    filtro = 'tema == "Computacion"'
            print(filtro)
            datosfiltrados = datos.query(filtro)
    matriz = pd.DataFrame({
        'titulo' : datosfiltrados['titulo'].tolist(),
        'keywords' : datosfiltrados['keywords'].tolist(),
        'abstract' : datosfiltrados['abstract'].tolist()
    })
    matriz.to_html('app/templates/paginas/tabla.html',index=False)
    return render_template('paginas/matriz.html',filas=len(matriz['titulo']))

@bp.route('/graficos', methods=['GET'])
def graficos():
    return render_template('paginas/graficas.html')

@bp.route('/subir', methods=['GET'])
def subir():
    return render_template('paginas/subirCsv.html')