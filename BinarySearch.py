import random


def binary(arr, l, r, num):
    if r >= 1:
        mid = l+(r-l)//2
        if arr[mid] > num:
            return binary(arr, l, mid-1, num)
        elif arr[mid] < num:
            return binary(arr, mid+1, r, num)
        else:
            print("The number is located at", mid+1, "th location.")
    else:
        return "Entered number not found!"


a = [int(random.randint(0, 10)) for w in range(20)]
a = sorted(a)
n = int(input("Enter the number you want to search: "))
l = 0
r = len(a)-1
binary(a, l, r, n)
print(a)

