i = 1
list1 = []

while (i <= 5):
    number = int(input("Number : "))
    list1.append(number)
    i += 1

def func(a):
    return a*a-20

list1.sort(key=func)
print(list1)