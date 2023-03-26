### **Gmeproxy**

Asynchronous Python wrapper for [Gimmeproxy API](https://gimmeproxy.com/)

### **Example of use**
* main.py

    ```python
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
    ```

* Perform a request with an actual fetched proxy through [aiohttp](https://docs.aiohttp.org/en/stable/) to get current IP address

    ```python
    result = await proxy.get_proxy(**params)
    _proxy = f"http://{result['ipPort']}"

    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.ipify.org/", proxy=_proxy) as response:
            print(await response.text())
    ```
    Output:
    ```
    128.140.4.217
    ```