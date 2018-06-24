#!/home/matt/projects/python/websockets/venv/bin/python3

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print("< name {}".format(name))

    greeting = "Hello {}!".format(name)

    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
