from aiohttp import web
import requests


async def handler_get(request):
    numero = request.match_info.get('number')
    url = "https://rickandmortyapi.com/api/character/"+numero
    response = requests.get(url)
    data = response.json()
    return web.Response(text=data['name'])




app = web.Application()

app.add_routes(
    [
        web.get('/{number}', handler_get)
    ]
)

# Esto significa que, cuando el cliente haga un get o un post, el servidor le va a responder con handler_get ó
# handler_post

if __name__ == '__main__':
    web.run_app(app)
