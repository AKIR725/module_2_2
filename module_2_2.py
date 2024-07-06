first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print(3)
elif third != second == first or second != third == first or first != second == third:
    print(2)
else:
    print(0)