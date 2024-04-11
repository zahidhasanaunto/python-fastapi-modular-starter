from fastapi import FastAPI
from src.modules.example.example_module import ExampleModule

class Application:
    def __init__(self):
        self.app = FastAPI()
        self.modules = []

    def add_module(self, module_class):
        module = module_class(self.app)
        self.modules.append(module)

    def get_app(self):
        return self.app

app_instance = Application()

app_instance.add_module(ExampleModule)

app = app_instance.get_app()