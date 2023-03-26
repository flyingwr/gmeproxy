from gmeproxy import proxy

import asyncio

async def main():
    params = {
        "get": True,
        "post": True,
        "cookies": True,
        "user-agent": True,
        "supportHttps": True,
        "maxCheckPeriod": 600,
        "protocol": "http",
        "minSpeed": 50
    }

    result = await proxy.get_proxy(**params)
    if (error := result.get("error")) is not None:
        print(f"An error occurred: {error}")
    else:
        print(result)

    await proxy.__client__.close() # This prevents aiohttp from throwing an unclosed session warning

if __name__ == "__main__":
    asyncio.run(main())