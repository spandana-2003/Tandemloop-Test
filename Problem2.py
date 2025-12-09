#PROBLEM–2: Print odd series till a
a = int(input("Enter a number: "))
result = []

for i in range(1, 2*a, 2):
    result.append(i)

print(result)
