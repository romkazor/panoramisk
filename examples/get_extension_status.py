from pprint import pprint
import asyncio
from panoramisk import Manager


async def extension_status():
    manager = Manager(loop=asyncio.get_event_loop(),
                      host='127.0.0.1', port=5039,
                      username='user', secret='password')
    await manager.connect()
    extension = await manager.send_action({'Action': 'ExtensionState',
                                           'Exten': '2001',
                                           'Context': 'default'})
    manager.close()
    pprint(extension)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(extension_status())
    loop.close()


if __name__ == '__main__':
    main()
