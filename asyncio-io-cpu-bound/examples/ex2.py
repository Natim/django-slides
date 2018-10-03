import asyncio

async def my_coroutine():
    """But this Python function has got a unique power.
    It can use the await keyword.
    """
    await asyncio.sleep(3)
    return "That's it"

loop = asyncio.get_event_loop()
result = loop.run_until_complete(my_coroutine())

print(result)
