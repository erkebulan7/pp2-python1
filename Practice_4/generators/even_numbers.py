n = int(input("Enter number: "))

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

result = []

for number in even_numbers(n):
    result.append(str(number))

print(",".join(result))
