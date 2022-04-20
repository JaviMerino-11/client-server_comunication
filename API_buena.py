import aiohttp
from aiohttp import web


async def handler_get(request: web.Request):
    numero = request.match_info.get('number')
    url = "https://rickandmortyapi.com/api/character/" + numero
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response: #Tengo que crear sesion cliente porque llamo a otra API
            data = await response.json()  # Json response es el body de la respuesta

    return web.json_response(data)  # Devuelve formato json (diccionario)
    # return web.Response(text=data['name']) #Devuelve texto plano



#Aqui lo que llega es la peticion del postman, se almacena con todos los para-
#metros en request (header,body...) y comienza a ejecutarse la funcion; almaceno el body
#en .json para poder tratarlo como un diccionario. Ahora tengo que cogerlo y modificarlo
#y ese nuevo body modificado lo devuelvo a la web
#MUY IMPORTANTE: NO HACE FALTA VOLVER A DEFINIR UNA SESION DENTRO DE ESTE SERVIDOR PORQUE
#YA ACTUA COMO CLIENTE A POSTMAN CON EL WEB.X -- SI TUVIERA QUE ACCEDER A OTRO SERVIDOR, SI

async def handler_post(request: web.Request):
    body = await request.json()
    body['FirstName']='Javier'
    body['LastName']='Merino'
    return web.json_response(body)


app = web.Application()

app.add_routes(
    [
        web.get('/{number}', handler_get),
        web.post('/post', handler_post)
    ]
)

if __name__ == '__main__':
    web.run_app(app)
