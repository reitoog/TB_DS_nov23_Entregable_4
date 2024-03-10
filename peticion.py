#Con Request

import requests
import json

url = "http://127.0.0.1:5000/api"

data = [[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0], # paso 2 registros de 13 features par mi prediccion 
[14.34, 1.68, 2.7, 25.0, 98.0, 2.8, 1.31, 0.53, 2.7, 13.0, 0.57, 1.96, 660.0]]         # Nosotros pasaremos otros valores diferentes para 
                                                                                       # hacer el predict

j_data = json.dumps(data) #Los vuelco  esta lista de listas y obtengo un json 

print(j_data)
print(type(j_data))
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers) # Aquí es donde lleva a cabo el paso de la informacion que tengo a mi endpoint 

print(r, r.text) #Muestrame que el request ha ido bien [200]  y lo que contiene

