from requests import Session


def get_response():
    with Session() as session:
        response = session.get(
            url='https://www.wildberries.by/webapi/menu/main-menu-by-ru.json'
        )
        return response.json()
        # print(response.json())


# result = get_response()
# for _ in result:
#     if 'seo' in _:
#         print(_)
# print(type(get_response()))
