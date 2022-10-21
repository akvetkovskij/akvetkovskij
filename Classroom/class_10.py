from csv import DictReader
from typing import List


def from_categories() -> List[dict]:
    with open('categories.csv', 'r', encoding='utf-8') as file:
        reader = DictReader(file)
        new_dict = []
        for data in reader:
            new_dict.append(data)
        return new_dict


print(from_categories())