times_table_number = int(input("What number do you want its times table of? "))
while (times_table_number < 0):
    times_table_number = int(input("Number can't be negative. Enter a new number: "))

for num in range(12):
    times_number = (num+1) * times_table_number
    print(str(times_number), end = " ")