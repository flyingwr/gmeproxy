from aiohttp import ClientSession
from gmeproxy import __client__

from .urls import BASE_URL

accepted_params = ( 
    "get", "post", "cookies", "referer", "user-agent",
    "supportHttps", "anonymityLevel", "protocol", "country",
    "maxCheckPeriod", "minSpeed", "notCountry"
)

def filter_params(params):
    _params = {}
    for param, value in params.items():
        if param in accepted_params:
            if isinstance(value, bool):
                _params[param] = str(value).lower()
            else:
                _params[param] = value
    return _params

async def get_proxy(**kwargs):
    global __client__
    if __client__ is None:
        __client__ = ClientSession()

    result = {}
    
    async with __client__.get(BASE_URL, params=filter_params(kwargs)) as response:
        if response.ok:
            result.update(await response.json())
        elif response.status == 429:
            result["error"] = "Too many requests"
        else:
            result["error"] = "Unknown error"
            result["status"] = response.status

    return result