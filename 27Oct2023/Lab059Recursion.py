def rec_count(number):
    print(number)
    if number == 0:
        return 0
    rec_count(number-1)


rec_count(5)

# fibonacci number at index using recusrion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(6)
print(result)
