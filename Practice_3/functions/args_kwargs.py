def add_numbers(*numbers):
    return sum(numbers)

def show_info(**info):
    for key, value in info.items():
        print(key, value)

print(add_numbers(1, 5, 9))

show_info(name="Madina", city="Aktau", age=27)
