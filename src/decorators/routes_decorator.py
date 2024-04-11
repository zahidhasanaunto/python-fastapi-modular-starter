from typing import Callable, Type
from pydantic import BaseModel

def route(method: str, path: str, response_model: Type[BaseModel] = None):
    if not path.startswith("/"):
        path = "/" + path
    def decorator(func: Callable):
        if not hasattr(func, "_route_settings"):
            func._route_settings = []
        func._route_settings.append((method, path, response_model))
        return func
    return decorator

def Get(path: str, response_model: Type[BaseModel] = None):
    return route("GET", path, response_model)

def Post(path: str, response_model: Type[BaseModel] = None):
    return route("POST", path, response_model)

def Put(path: str, response_model: Type[BaseModel] = None):
    return route("PUT", path, response_model)

def Delete(path: str, response_model: Type[BaseModel] = None):
    return route("DELETE", path, response_model)

def Options(path: str, response_model: Type[BaseModel] = None):
    return route("OPTIONS", path, response_model)

def Head(path: str, response_model: Type[BaseModel] = None):
    return route("HEAD", path, response_model)

def Patch(path: str, response_model: Type[BaseModel] = None):
    return route("PATCH", path, response_model)
