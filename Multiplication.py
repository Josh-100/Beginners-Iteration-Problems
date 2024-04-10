times_table_number = input("What number do you want its times table of? ")
for num in range(12):
    times_number = (num+1) * int(times_table_number)
    print(str(times_number), end = " ")