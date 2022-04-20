import aiohttp
from aiohttp import web


async def handler_get(request: web.Request):
    # Buscar metodo para sacar body parecido a este (mirar documentacion request)
    numero = request.match_info.get('number')
    url = "https://rickandmortyapi.com/api/character/" + numero
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()  # Json response es el body de la respuesta

    return web.json_response(data)  # Devuelve formato json (diccionario)
    # return web.Response(text=data['name']) #Devuelve texto plano


async def handler_post(request: web.Request):
    local_url = 'http://0.0.0.0:8080/post'
    async with aiohttp.ClientSession() as session:
        async with session.post(local_url) as response:
            body = await response.json()
            return web.json_response(body)


app = web.Application()

app.add_routes(
    [
        web.get('/{number}', handler_get)
        # web.post('/post', handler_post)
    ]
)

# Esto significa que, cuando el cliente haga un get o un post, el servidor le va a responder con handler_get ó
# handler_post

if __name__ == '__main__':
    web.run_app(app)
