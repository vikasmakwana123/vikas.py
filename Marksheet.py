f = 7
i = 0
for k in range(0,f):
    while True:
        a =int(input("Please enter mark you got in your subject (not greater than 100): "))
        if 0 <= a <= 100:
            break
        else:
            print("The mark you entered should be between 0 and 100.")

    i = i + a

j = (i / 700) * 100
print(f"Your average percentage is: {j}%")
