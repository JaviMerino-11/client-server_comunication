import json

import aiohttp
import requests
from aiohttp import web


async def handler_get(request):
    numero = request.match_info.get('number')
    url = "https://rickandmortyapi.com/api/character/" + numero
    response = requests.get(url)
    data = response.json()
    return web.Response(text=data['name'])


async def handler_post(request):
    url = "http://0.0.0.0:8080/post"
    header={
    'Accept': 'application/json',
    'Content-Type': 'multipart/form-data'
    }
    body_modificado = {
        'FirstName': 'Javier',
        'LastName': 'Merino'
    }

    response = requests.post(url, data=json.dumps(body_modificado),headers=header)
    return web.Response(text=response)


app = web.Application()

app.add_routes(
    [
        web.get('/{number}', handler_get),
        web.post('/post', handler_post)
    ]
)

# Esto significa que, cuando el cliente haga un get o un post, el servidor le va a responder con handler_get ó
# handler_post

if __name__ == '__main__':
    web.run_app(app)
