from tracer import tracer

@tracer
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("=== Факториал ===")
factorial(4)

print("\n" + "="*50 + "\n")

@tracer
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== Числа Фибоначчи ===")
fibonacci(3)