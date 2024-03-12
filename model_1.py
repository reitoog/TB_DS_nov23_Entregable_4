# ====================================================================================
#  MODELO: En este script se cargan los datos y se entrena el modelo. 
#  En el enunciado del ejercicio se le llama: [1]Ruta para entrenar tu modelo
# ==================================================================================== 

#ESTE PUEDO DEJARLO PARA QUE TRABAJE CON REGRESOR 1 (LO COMENTAMOS) 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import pickle
data = pd.read_csv('data/Advertising.csv') # Esta info de dónde la tomamos, está en la nube?? 

X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['sales']),
                                                    data['sales'],
                                                    test_size = 0.20,
                                                    random_state=42)

# lin_reg = LinearRegression() --> Estanciamos el regresor
# lin_reg.fit(X_train, y_train)-->  Hacemos el fit del estimador con datos de train --> Hay validación??

# print("MSE: ", mean_squared_error(y_test, lin_reg.predict(X_test)))  --> Definir las métricas de error  y justificacion de las mismas 
# print("RMSE: ", np.sqrt(mean_squared_error(y_test, lin_reg.predict(X_test))))

# Aquí faltaría guardar el pickle que despues empleamos en la app -->En que ubicacion , local?, nube? 

# Ejemplo de guardado en local :
# pickle.dump(lin_reg, open('6_1-Flask/1-Routing/ejercicios/ejercicio 2 Flask_API_retrain_db\ejercicio/advertising.model', 'wb'))

# En vez de un script puede ser perfectamente un notebook