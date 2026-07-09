def print_kwargs (**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Virat",power="cover drive")
print_kwargs(name="Virat")
print_kwargs(name="Virat",power="cover drive",enemy="Outside off")