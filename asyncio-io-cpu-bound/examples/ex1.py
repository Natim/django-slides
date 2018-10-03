import asyncio


async def my_coroutine():
    """The keyword async makes it a coroutine.
    In the end it looks like a Python function.
    """
    
    return "That's it"

loop = asyncio.get_event_loop()
result = loop.run_until_complete(my_coroutine())

print(result)
