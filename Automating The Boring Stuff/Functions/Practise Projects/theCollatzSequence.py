def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print(collatz(10))
print(collatz(15))
    
    
