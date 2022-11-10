from requests import Session
from http import HTTPStatus

from aiohttp import ClientSession


async def get_response() -> list | None:
    async with ClientSession(base_url='https://www.wildberries.by') as session:
        response = await session.get(
            url='/webapi/menu/main-menu-by-ru.json'
        )
        if response.status == HTTPStatus.OK:
            return await response.json()


# result = get_response()
# for _ in result:
#     if 'seo' in _:
#         print(_)
# print(type(get_response()))
