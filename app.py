from aiohttp import web

# import request


url = "https://rickandmortyapi.com/api/character/{}"


async def handler_get(request):
    return web.Response(text=url.format(request.match_info['number']))


# async def handler_post(self,request):


app = web.Application()

app.add_routes(
    [
        web.get('/{number}', handler_get)
        # web.post('/post',handler.post)
    ]
)

# Esto significa que, cuando el cliente haga un get o un post, el servidor le va a responder con handler_get ó
# handler_post

if __name__ == '__main__':
    web.run_app(app)
