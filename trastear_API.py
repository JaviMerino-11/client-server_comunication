import aiohttp
from aiohttp import web


async def handler_post_query(request: web.Request):
    body_cliente = await request.json()
    parametro_query = {
        'username': body_cliente['FirstName'],
        'user_surname': body_cliente['LastName']
    }
    url = 'https://rickandmortyapi.com/api/character/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=parametro_query) as response:
            a = response.url
    return web.Response(text=str(a))


app = web.Application()

app.add_routes(
    [
        web.post('/post', handler_post_query)
    ]
)

if __name__ == '__main__':
    web.run_app(app)
