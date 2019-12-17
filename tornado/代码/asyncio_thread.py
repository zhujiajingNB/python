import asyncio
from threading import Thread

def run(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def time_sleep():
    print("await 2 secondes")
    await asyncio.sleep(2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    thread = Thread(target=run, args=(loop,))
    thread.start()
    asyncio.run_coroutine_threadsafe(time_sleep(), loop)
    asyncio.run_coroutine_threadsafe(time_sleep(), loop)
    asyncio.run_coroutine_threadsafe(time_sleep(), loop)