from random import choices


def fruit():
    fruits = [
        "apple",
        "pear",
        "banana",
        "kiwi",
        "strawberry",
        "cherry",
        "blueberry",
        "peach",
    ]
    return choices(fruits)[0]


# x = 1
# x = x
