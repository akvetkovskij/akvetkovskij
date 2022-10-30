from csv import DictReader
from typing import List

from Homework_10.models import Category
from crud.category import CRUDCategory


def from_categories_csv() -> List[dict]:
    with open('categories.csv', 'r', encoding='utf-8') as file:
        # reader = DictReader(file)
        # new_dict = []
        # for data in reader:
        #     new_dict.append(data)
        # return new_dict
        return [data for data in DictReader(file)]


def sending_to_category_model(from_csv: List[dict]) -> List[Category]:
    return list(map(lambda x: Category(**x), from_csv))


def sending_to_sql(upload_models: List[Category]) -> List[Category]:
    result = []
    for upload_model in upload_models:
        category = CRUDCategory.add(category=upload_model)
        if category:
            result.append(category)
    return result


print(sending_to_sql(sending_to_category_model(from_categories_csv())))
