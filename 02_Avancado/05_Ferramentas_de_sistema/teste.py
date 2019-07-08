def fibonacci(input_number):
    previous, next = 0, 1
    for number in range(input_number):
        previous, next = next, previous + next
        
    return previous

if __name__ == "__main__":
    print("EXECUTEI")
    print(fibonacci(10))