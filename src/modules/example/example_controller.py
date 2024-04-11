from src.modules.example.example_service import ExampleService
from src.modules.example.example_model import Example
from src.decorators.controller_decorator import Controller
from src.decorators.routes_decorator import Get, Post

@Controller("example")
class ExampleController:
    def __init__(self):
        self.service = ExampleService() 
    
    @Get('examples', response_model=list[Example])
    def get_examples(self):
        return self.service.get_examples()

    @Post('examples', response_model=Example)
    def add_example(self, example: Example):
        return self.service.add_example(example)