def health_check():
    return {"status": "healthy"}


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    print(health_check())
