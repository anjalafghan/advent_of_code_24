with open("input.text") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

result = 0
for x, y in zip(sorted(left), sorted(right)):
    result = result + abs(x - y)
print(result)
