from requests import Session


def get_response():
    with Session() as session:
        response = session.get(
            url='https://www.wildberries.by/webapi/menu/main-menu-by-ru.json'
        )
        print(response.json())


print(get_response())