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
mT,mK,mA,M=dis.matricesDistancia(datos)
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
                        filtro += 'and tema == "Ciencias exactas"'
                    if tema == 'medi':
                        filtro += 'and tema == "Medicina"'
                    if tema == 'sociales':
                        filtro += 'and tema == "Ciencias Sociales"'
                    if tema == 'compu':
                        filtro += 'and tema == "Computacion"'
            else:
                if tema == 'exactas':
                    filtro = 'tema == "Ciencias exactas"'
                if tema == 'medi':
                    filtro = 'tema == "Medicina"'
                if tema == 'sociales':
                    filtro = 'tema == "Ciencias Sociales"'
                if tema == 'compu':
                    filtro = 'tema == "Computacion"'
            datosfiltrados = datos.query(filtro)
    matriz = list(zip(datosfiltrados['titulo'].tolist(),datosfiltrados['keywords'].tolist(),datosfiltrados['abstract'].tolist()))
    return render_template('paginas/matriz.html',filas=len(matriz),matriz=matriz)

@bp.route('/graficos', methods=['GET','POST'])
def graficos():
    if request.method == 'POST':
        paper = request.form.get('paper',type=int)
        tipo = request.form.get('tipo')
        print(paper)
        if tipo == 'exactas':
            if paper == 1:
                codigo_img_total = graficoMapaCalor(M[0:15,0:15])
                codigo_img_titulos = graficoMapaCalor(mT[0:15,0:15])
                codigo_img_keywords = graficoMapaCalor(mK[0:15,0:15])
                codigo_img_abstracts = graficoMapaCalor(mA[0:15,0:15])
            elif paper == 2:
                codigo_img_total = graficoMapaCalor(M[16:31,16:31])
                codigo_img_titulos = graficoMapaCalor(mT[16:31,16:31])
                codigo_img_keywords = graficoMapaCalor(mK[16:31,16:31])
                codigo_img_abstracts = graficoMapaCalor(mA[16:31,16:31])
            elif paper == 3:
                codigo_img_total = graficoMapaCalor(M[32:47,32:47])
                codigo_img_titulos = graficoMapaCalor(mT[32:47,32:47])
                codigo_img_keywords = graficoMapaCalor(mK[32:47,32:47])
                codigo_img_abstracts = graficoMapaCalor(mA[32:47,32:47])
            else:
                codigo_img_total = graficoMapaCalor(M[0:47,0:47])
                codigo_img_titulos = graficoMapaCalor(mT[0:47,0:47])
                codigo_img_keywords = graficoMapaCalor(mK[0:47,0:47])
                codigo_img_abstracts = graficoMapaCalor(mA[0:47,0:47])

        elif tipo == 'medi':
            if paper == 1:
                codigo_img_total = graficoMapaCalor(M[48:63,48:63])
                codigo_img_titulos = graficoMapaCalor(mT[48:63,48:63])
                codigo_img_keywords = graficoMapaCalor(mK[48:63,48:63])
                codigo_img_abstracts = graficoMapaCalor(mA[48:63,48:63])
            elif paper == 2:
                codigo_img_total = graficoMapaCalor(M[64:79,64:79])
                codigo_img_titulos = graficoMapaCalor(mT[64:79,64:79])
                codigo_img_keywords = graficoMapaCalor(mK[64:79,64:79])
                codigo_img_abstracts = graficoMapaCalor(mA[64:79,64:79])
            elif paper == 3:
                codigo_img_total = graficoMapaCalor(M[80:95,80:95])
                codigo_img_titulos = graficoMapaCalor(mT[80:95,80:95])
                codigo_img_keywords = graficoMapaCalor(mK[80:95,80:95])
                codigo_img_abstracts = graficoMapaCalor(mA[80:95,80:95])
            else:
                codigo_img_total = graficoMapaCalor(M[48:95,48:95])
                codigo_img_titulos = graficoMapaCalor(mT[48:95,48:95])
                codigo_img_keywords = graficoMapaCalor(mK[48:95,48:95])
                codigo_img_abstracts = graficoMapaCalor(mA[48:95,48:95])
        elif tipo == 'compu':
            if paper == 1:
                codigo_img_total = graficoMapaCalor(M[96:111,96:111])
                codigo_img_titulos = graficoMapaCalor(mT[96:111,96:111])
                codigo_img_keywords = graficoMapaCalor(mK[96:111,96:111])
                codigo_img_abstracts = graficoMapaCalor(mA[96:111,96:111])
            elif paper == 2:
                codigo_img_total = graficoMapaCalor(M[112:127,112:127])
                codigo_img_titulos = graficoMapaCalor(mT[112:127,112:127])
                codigo_img_keywords = graficoMapaCalor(mK[112:127,112:127])
                codigo_img_abstracts = graficoMapaCalor(mA[112:127,112:127])
            elif paper == 3:
                codigo_img_total = graficoMapaCalor(M[128:143,128:143])
                codigo_img_titulos = graficoMapaCalor(mT[128:143,128:143])
                codigo_img_keywords = graficoMapaCalor(mK[128:143,128:143])
                codigo_img_abstracts = graficoMapaCalor(mA[128:143,128:143])
            else:
                codigo_img_total = graficoMapaCalor(M[96:143,96:143])
                codigo_img_titulos = graficoMapaCalor(mT[96:143,96:143])
                codigo_img_keywords = graficoMapaCalor(mK[96:143,96:143])
                codigo_img_abstracts = graficoMapaCalor(mA[96:143,96:143])
        elif tipo == 'sociales':
            if paper == 1:
                codigo_img_total = graficoMapaCalor(M[144:159,144:159])
                codigo_img_titulos = graficoMapaCalor(mT[144:159,144:159])
                codigo_img_keywords = graficoMapaCalor(mK[144:159,144:159])
                codigo_img_abstracts = graficoMapaCalor(mA[144:159,144:159])
            elif paper == 2:
                codigo_img_total = graficoMapaCalor(M[160:175,160:175])
                codigo_img_titulos = graficoMapaCalor(mT[160:175,160:175])
                codigo_img_keywords = graficoMapaCalor(mK[160:175,160:175])
                codigo_img_abstracts = graficoMapaCalor(mA[160:175,160:175])
            elif paper == 3:
                codigo_img_total = graficoMapaCalor(M[176:191,176:191])
                codigo_img_titulos = graficoMapaCalor(mT[176:191,176:191])
                codigo_img_keywords = graficoMapaCalor(mK[176:191,176:191])
                codigo_img_abstracts = graficoMapaCalor(mA[176:191,176:191])
            else:
                codigo_img_total = graficoMapaCalor(M[144:191,144:191])
                codigo_img_titulos = graficoMapaCalor(mT[144:191,144:191])
                codigo_img_keywords = graficoMapaCalor(mK[144:191,144:191])
                codigo_img_abstracts = graficoMapaCalor(mA[144:191,144:191])
        else:
            codigo_img_total = graficoMapaCalor(M)
            codigo_img_titulos = graficoMapaCalor(mT)
            codigo_img_keywords = graficoMapaCalor(mK)
            codigo_img_abstracts = graficoMapaCalor(mA)
    if request.method == 'GET':
        codigo_img_total = graficoMapaCalor(M)
        codigo_img_titulos = graficoMapaCalor(mT)
        codigo_img_keywords = graficoMapaCalor(mK)
        codigo_img_abstracts = graficoMapaCalor(mA)

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

@bp.route('/mds', methods=['GET'])
def mds():
    return render_template('paginas/mds.html')

@bp.route('/subir', methods=['GET'])
def subir():
    return render_template('paginas/subirCsv.html')

def graficoMapaCalor(matriz):
    labels = [i for i in range(1,len(matriz)+1)]
    data = pd.DataFrame(matriz,columns=labels,index=labels) 
    img = io.BytesIO()
    plt.figure(figsize = (27,10) )
    mapa1 = sns.heatmap(data,cmap="inferno")
    figure = mapa1.get_figure()
    figure.savefig(img,format='png')
    img.seek(0)
    codigo_img = base64.b64encode(img.getvalue()).decode()
    return codigo_img