from typing import List
from src.modules.example.example_model import Example

class ExampleService:
    def __init__(self):
        self.database: List[Example] = []

    def get_examples(self) -> List[Example]:
        return self.database

    def add_example(self, example: Example) -> Example:
        self.database.append(example)
        return example
