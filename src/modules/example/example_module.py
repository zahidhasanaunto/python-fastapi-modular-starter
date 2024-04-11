from fastapi import FastAPI
from src.modules.example.example_controller import ExampleController

controllers = [
    ExampleController
]

class ExampleModule:
    def __init__(self, app: FastAPI):
        for controller in controllers:
            controller_instance = controller()
            app.include_router(controller_instance.router)
