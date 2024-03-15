import requests
import json

url = "http://13.60.46.54/api"

data = [[2010, 1.3, 0.1, 0.22],  #Año 2010, ventas NA = 1.3M , ventas JP = 0.1M y ventas resto del mundo = 0.22
[2023, 1.5, 0.2, 0.3]]           #Año 2023, ventas NA = 1.5M , ventas JP = 0.2M y ventas resto del mundo = 0.3
                                                                                       
j_data = json.dumps(data) 

print(j_data)
print(type(j_data))
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers) 

print(r) 
print("Las predicciones de ventas en Europa son:",r.text) #Predicción