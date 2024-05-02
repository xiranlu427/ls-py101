def greeting(name, status):
    name = " ".join(name)
    return (f"Hello, {name}! Nice to have a "
           f"{status["title"]} {status["occupation"]} around.")


name = ["John", "Q", "Doe"]
status = {"title": "Master", "occupation": "Plumber"}

print(greeting(name, status))