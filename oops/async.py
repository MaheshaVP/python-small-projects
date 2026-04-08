#Async functions

import asyncio

async def say_hello():
    print("Hello ")
    await asyncio.sleep(1)
    print("I love you")

asyncio.run(say_hello())
