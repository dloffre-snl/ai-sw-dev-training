import asyncio
from aiohttp import web, ClientSession
from pprint import pprint

UPSTREAM = "http://localhost:8000"

async def handle(request):
    url = UPSTREAM + request.rel_url.path_qs

    headers = dict(request.headers)
    headers.pop("Host", None)

    body = await request.read()

    print(f"\n--- REQUEST --- {request.method} {request.rel_url}")
    pprint(headers)
    pprint(body)
    
    async with ClientSession() as session:
        async with session.request(
            method=request.method,
            url=url,
            headers=headers,
            data=body,
        ) as resp:

            print(f"--- RESPONSE --- {resp.status} {request.rel_url}")
            pprint(resp.headers)
            pprint(resp.content)
            proxy_resp = web.StreamResponse(
                status=resp.status,
                headers=resp.headers
            )
            await proxy_resp.prepare(request)

            async for chunk in resp.content.iter_chunked(8192):
                await proxy_resp.write(chunk)

            await proxy_resp.write_eof()
            return proxy_resp

app = web.Application()
app.router.add_route("*", "/{path:.*}", handle)

web.run_app(app, port=8080)