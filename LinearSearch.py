import random
a = [int(random.randint(0, 10)) for w in range(20)]
n = int(input("Enter the number you want to search: "))
for i in range(len(a)):
    if n != a[i]:
        if i < len(a):
            continue
        else:
            print("Not found!")
            break
    else:
        print("Your number is found at: ", i+1, "th location.")
print(a)