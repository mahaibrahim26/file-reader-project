def colorize(color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }

    def wrapper(func):
        def inner(*args, **kwargs):
            print(colors.get(color, ""), end="")  # Set color
            result = func(*args, **kwargs)
            print(colors["reset"], end="")        # Reset color
            return result
        return inner
    return wrapper