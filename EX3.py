print("For loop:")
for name in ["Alice", "Bob", "Charlie", "Dave", "Eve"]: print(name)

print("While loop:")
count = 1
while count <= 5: print(count); count += 1

print("Do-while loop (Factorial):")
n = int(input("Enter a number: "))
fact = 1
while n: fact *= n; n -= 1
print("Factorial:", fact)
