import asyncio
import aiohttp


async def create_todo(title, description):
    auth = {"Authorization": "Basic YWRtaW46cGFzcw=="}
    async with aiohttp.ClientSession(headers=auth) as session:
        url = "https://kinto.dev.mozaws.net/v1/buckets/default/collections/todo/records"
        payload = {"title": title, "description": description}
        async with session.post(url, json={"data": payload}) as response:
            response.raise_for_status()
            return await response.json()


async def main():
    TODOS = (
        ("Ménage", "Passer un coup dans les sanitaires"),
        ("Lessive", "Changer les draps"),
    )
    actions = [create_todo(t, d) for t, d in TODOS]
    results = await asyncio.gather(*actions)
    print([r["data"]["id"] for r in results])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
