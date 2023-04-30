def hello_world():
    print("Hello world")


def hello_world_name(first_name):
    print(f"Hello, {first_name}")


def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    print(f"Hello, {first_name} / {second_name} / {third_name} !")


def hello_world_keyword_args(first_person, second_person):
    print(f"Hello, {first_person} / {second_person}")


def hello_world_arbitrary_keyword_args(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']} !")


# hello_world()
# hello_world_name("Luis")
# hello_world_name("Humberto")
# hello_world_args("Luis", "Humberto", "Sarah")
# hello_world_keyword_args(first_person="Luis", second_person="Humberto")

hello_world_arbitrary_keyword_args(first_person="Sarah", second_person="Luis")
