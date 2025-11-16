import functools

def tracer(func):
    depth = 0
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = "  " * depth
        print(f"{indent}→ {func.__name__}({', '.join(repr(arg) for arg in args)})")
        
        depth += 1
        try:
            result = func(*args, **kwargs)
        finally:
            depth -= 1
        indent = "  " * depth
        print(f"{indent}← {func.__name__}({', '.join(repr(arg) for arg in args)}) = {repr(result)}")
        
        return result
    
    return wrapper
