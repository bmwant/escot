import asyncio

from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest

import config


async def main():
    print(config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)
    client = TelegramClient(
        'session_id',
        api_id=config.TELEGRAM_API_ID,
        api_hash=config.TELEGRAM_API_HASH,
    )
    await client.connect()

    channel_hash = '<this does not work>'
    result = await client(ImportChatInviteRequest(channel_hash))
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
