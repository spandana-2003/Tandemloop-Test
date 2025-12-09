'''PROBLEM–3: Conditional odd series
If number is even → stop at previous odd
If number is odd → print till that odd'''
a = int(input("Enter a number: "))
result = []

limit = a if a % 2 != 0 else a - 1

for i in range(1, limit*2, 2):
    result.append(i)

print(result)
