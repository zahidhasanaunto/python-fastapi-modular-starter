from fastapi import APIRouter

def Controller(prefix: str):
    if not prefix.startswith("/"):
        prefix = "/" + prefix
        
    def decorator(cls):
        cls.router = APIRouter(prefix=prefix)
        instance = cls()

        for attr_name in dir(cls):
            method = getattr(instance, attr_name)
            if callable(method) and hasattr(method, "_route_settings"):
                for settings in method._route_settings:
                    method_type, path, response_model = settings
                    route_decorator = getattr(cls.router, method_type.lower())
                    route_decorator(path, response_model=response_model)(method.__get__(instance, cls))
        return cls
    return decorator


