number = int(input("What number do you want to check whether it's a prime? "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("Number is not a prime")
            break
    else:
        print("Number is prime!")
else:
    print("Number is not a prime!")