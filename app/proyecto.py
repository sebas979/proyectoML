from flask import (
    Blueprint,render_template,request
)
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from matplotlib.backends._backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import seaborn as sns

from . import nlp
from . import distancias as dis

datos = nlp.importarCSV('https://raw.githubusercontent.com/sebas979/archicosCSV/main/DataSet.csv');
# mT,mK,mA,M=dis.matricesDistancia(datos)
bp = Blueprint('proyecto',__name__,url_prefix='/')

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
            datosfiltrados = datos.query(filtro)
    matriz = pd.DataFrame({
        'titulo' : datosfiltrados['titulo'].tolist(),
        'keywords' : datosfiltrados['keywords'].tolist(),
        'abstract' : datosfiltrados['abstract'].tolist()
    })
    matriz.to_html('app/templates/paginas/tablas/tabla.html',index=False)
    return render_template('paginas/matriz.html',filas=len(matriz['titulo']))

@bp.route('/graficos', methods=['GET'])
def graficos():
    codigo_img_total = graficoMapaCalor(M,'todos.html')
    codigo_img_titulos = graficoMapaCalor(mT,'titulos.html')
    codigo_img_keywords = graficoMapaCalor(mK,'keyword.html')
    codigo_img_abstracts = graficoMapaCalor(mA,'abstract.html')
    return render_template('paginas/graficas.html',imagen={
        'todo':codigo_img_total,
        'titulo':codigo_img_titulos,
        'keywords':codigo_img_keywords,
        'abstract':codigo_img_abstracts
    })

# figure.savefig('mapa.png',dpi=400)
# plt.imshow(data, cmap ="inferno") 
# plt.colorbar() 
# plt.savefig(img,format='png')
# plt.show()
# plt.figure(figsize = (27,10) )
# plt.imshow(data, cmap ="inferno") 
# plt.colorbar() 
# plt.xticks(data.columns) 
# plt.yticks(range(len(data)), data.index) 



@bp.route('/subir', methods=['GET'])
def subir():
    return render_template('paginas/subirCsv.html')

def graficoMapaCalor(matriz,nombre):
    labels = [i for i in range(1,len(matriz)+1)]
    data = pd.DataFrame(matriz,columns=labels,index=labels)
    data.to_html('app/templates/paginas/tablas/'+nombre,index=False)
    img = io.BytesIO()
    plt.figure(figsize = (27,10) )
    mapa1 = sns.heatmap(data,cmap="inferno")
    figure = mapa1.get_figure()
    figure.savefig(img,format='png')
    img.seek(0)
    codigo_img = base64.b64encode(img.getvalue()).decode()
    return codigo_img