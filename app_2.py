from aiohttp import web
import requests


# Este codiguillo nos devuelve el nombre del personaje dependiendo del numero que tenga

async def handler_get(request):
    url = "https://rickandmortyapi.com/api/character/1"
    response = requests.get(url)
    data = response.json()
    return web.Response(text=data['name'])


app = web.Application()

app.add_routes(
    [
        web.get('/get', handler_get)
        # web.post('/post', handler_post)
    ]
)

# Esto significa que, cuando el cliente haga un get o un post, el servidor le va a responder con handler_get ó
# handler_post

if __name__ == '__main__':
    web.run_app(app)
