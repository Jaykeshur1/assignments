numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

    for i in range(5): 
     if i == 2:
        pass
    else:
        print(i)

        numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)

    numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully.")

    count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully.")