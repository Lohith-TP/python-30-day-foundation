# day3_decorators.py

import time
from functools import wraps

# --- Exercise 1: Logger Decorator ---


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args}, kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

# --- Exercise 2: Timer Decorator ---


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# --- Exercise 3: Repeat Decorator with Arguments ---


def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# --- Exercise 4: Preserve Metadata Example ---


@logger
def sample_function():
    """Sample docstring for metadata test."""
    return "Function run"

# --- Exercise 5: Restrict Function to One User ---


def require_user(required_username):
    def decorator(func):
        @wraps(func)
        def wrapper(username, *args, **kwargs):
            if username != required_username:
                print("Access denied.")
                return None
            return func(username, *args, **kwargs)
        return wrapper
    return decorator


@require_user("admin")
def delete_db(user):
    print("Database deleted.")

# --- Bonus: Combine Logger and Timer ---


@timer
@logger
def compute():
    time.sleep(1)
    return "done"


# --- Test Calls ---
if __name__ == "__main__":
    print("--- Exercise 1 ---")

    @logger
    def greet(name):
        return f"Hi {name}"
    print(greet("Lohith"))

    print("\n--- Exercise 2 ---")

    @timer
    def long_task():
        time.sleep(2)
        return "done"
    print(long_task())

    print("\n--- Exercise 3 ---")

    @repeat(3)
    def wave():
        print("👋")
    wave()

    print("\n--- Exercise 4 ---")
    print(sample_function.__name__)
    print(sample_function.__doc__)

    print("\n--- Exercise 5 ---")
    delete_db("guest")  # Access denied
    delete_db("admin")  # Should work

    print("\n--- Bonus ---")
    print(compute())
