import requests

url = "https://amzn.to/3AVb0VA"

#### https://amzn.to/ es el host y 3AVb0VA es el path_url donde queremos acceder ####

response = requests.get(url)  # Almaceno la respuesta del servidor en esta variable

# ############## ESTO HACE REFERENCIA A LA PETICION #######
# # Si queremos ver la informacion de la peticion:
# print("\nInformacion de la peticion")
# print(response.request)
#
# # Si hacemos un dir(response.request) vemos los atributos del mismo
# print("\nAtributos de la peticion")
# print(dir(response.request))
#
# # Si nos metemos por ejemplo en la cabecera, vemos que
#
# print("\nCabecera de la peticion")
# print(response.request.headers)  # aunque no hayamos definido cabecera en la peticion al
# # servidor, el propio python mete informacion en ese campo
#
# print("\nRecurso al que queremos acceder dentro del host del servidor")
# print(response.request.path_url)
#
# ############## ESTO HACE REFERENCIA A LA RESPUESTA #######
# print("Todos los atributos disponibles en la respuesta")
# print(dir(response))  # Vemos todos los atributos desponibles de la respuesta
#
# print("\nCodigo de la respuesta")
# print(response.status_code) # Es el CODIGO DE LA RESPUESTA
# print("\nExplicacion del codigo de la respuesta")
# print(response.reason)  # Es la razon o explicación de la respuesta
# print("\nCabeceras de la respuesta")
# print(response.headers)  # Cabeceras de la RESPUESTA

# Si queremos acceder al body de la respuesta podemos hacerlo de 3 maneras:
#### PRIMERA FORMA: Nos devuelve el body en bytes ####
# print(response.content) # En bytes

#### SEGUNDA FORMA: Nos devuelve el body en string ####
# print(response.text) # En string

#### TERCERA FORMA: Nos devuelve el body en estructura de datos json ####
print(response.json)  # En json
