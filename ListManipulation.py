x = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
y = [7, 8]
z = 1

x.sort()
x.extend(y)

while z in x:
    x.remove(z)

print(x)
