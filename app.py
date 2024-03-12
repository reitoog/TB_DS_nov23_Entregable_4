#==============================================================================================================================
# ESTE ES EL CUERPO DE LA APP 
# AQUI SE DEFINEN LAS DISTINTAS ESTANCIAS DE LAS APP WEB 
# ACCIONES QUE SE REALIZARÁN EN LAS ESTANCIAS DEFINIDAS:
#    
#    1.Implementacion de modelos de Prediccion elegidos  y visualizacion de su scoring:
#                                                       a.Prediccion 1 mediante Regresion Lineal o similar 
#                                                       b.Prediccion 2 mediante XXX
#                                                       c.Prediccion 3 mediante XXX
#
#    En el proceso de implementacion se tienen que emplear 3 maneras para suministrar los datos al modelo   
#     1. A traves de la URL(http) de manera manual  (opcion request de flask )        
#     2. A traves de un paquete de datos json que estara en un tercer script que llamaremos ataque (opcion requests de peticiones)
#     3. A traves de una ruta que acepte ambos (habría que pensarla un poco)
#===============================================================================================================================

from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
import csv, sqlite3, json
from sklearn.model_selection import train_test_split  #Aquí no se hace un train test split 
from sklearn.metrics import mean_squared_error        #Empleo el modelo que aplique 
from sklearn.linear_model import LinearRegression     #Empleo el modelo que aplique 

app = Flask(__name__)
app.config["DEBUG"] = True

#===============================================================================================================================
# Endpoint HOME 

@app.route('/', methods=['GET'])
def home():
    return "<h1>This app has been developed by students of 'the Bridge' Data Science Bootcamp class (November 2023). " \
           "Throughout this project, a 'Proof of concept' where Flask, Git, " \
           "Cloud and PySpark are fully integrated, has been carried out.</h1>"
#==============================================================================================================================

#===============================================================================================================================
# Endpoint de VERIFICACION DE FUNCIONAMIENTO de mi app
 
@app.route('/health/', methods=['GET'])
def health():
    return "everything is here"

#==============================================================================================================================

# ==============================================================================================================================
# [1] PREDICCION  1 --> ( Empleamos solo 1 modelo. Los datos los pasamos por la URL )
# ==============================================================================================================================

"""
La petición sería:
http://127.0.0.1:5000/api/v1/adv_model/predict?param1=180&param2=15&param3=60    #Esta ruta la definimos nosotros así
"""

@app.route('/api/v1/adv_model/predict', methods = ['GET'])  #['GET']: Aquí coge los argumentos por param1,param2 y param3 por URL con 'request.arg'
def predict():
    args = request.args
    if 'param1' in args and 'param2' in args and 'param3' in args:
        with open('C:\Users\reito\Documents\GitHub\77_Miss_Cosas\Flasko\Flasko_v2\elmodeloguardado.model','rb') as archivo_entrada : 
            model = pickle.load(archivo_entrada) # Modelo cargado
        
        parametro1 = args.get('param1', None) #Coge lo que le pasas por el parametro 1 y sino coge 'None'
        parametro2 = args.get('param2', None)
        parametro3 = args.get('param3', None)

        if parametro1 is None or parametro2 is None or parametro3 is None:
            return "Error. Args empty"
        else:
            predictions = model.predict([[float(parametro1), float(parametro2), float(parametro3)]])
            return jsonify({"predictions": list(predictions)})
    else:
        return "Error in args"

# Aquí estamos haciendo la predicciones, las metricas de nuestro modelo las ponemos a parte en otra @app.route 
    
# ==============================================================================================================================
# [2] PREDICCION  2 --> ( Empleamos el mismo modelo,pero pasando los datos a traves de un script + requests + [POST] )
# ==============================================================================================================================
    
@app.route('/api/', methods=['POST']) # <-- Esta info me viene del requests
def makecalc():
    data = request.get_json() # tomo los valores que tengo en mi json y los guardo en data
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)


modelfile = r'C:\Users\reito\Documents\GitHub\77_Miss_Cosas\Flasko\Flasko_v2\elmodeloguardado.model' #ruta a donde tenemos el modelo guardado (Nube amazon?)
model = pickle.load(open(modelfile, 'rb'))


print(type(model))

if __name__ == "__main__":
    print("hello")
    app.run(debug=False)


app.run()
