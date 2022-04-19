from aiohttp import web
import requests


async def handler_get(request):
    url = "https://rickandmortyapi.com/api/character/{}"
    return web.Response(text=url.format(request.match_info['number']))


async def handler_post(request):
    API_ENDPOINT = "https://rickandmortyapi.com/api/character/"
    headers = {'Localización': 'Málaga', 'Fecha': 'Martes 19 abril 2022'}
    API_KEY = "XXXXXXXXXXXXXXXXX"
    body = {
        "name": "Rick and Morty website",
        'api_code': API_KEY
    }
    r = requests.post(url=API_ENDPOINT, data=body, headers=headers)


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
