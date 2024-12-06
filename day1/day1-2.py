with open("input.text") as f:
    lines = f.read().splitlines()

left = []
right = []
for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

result = 0
for num in left:
    result = result + num * right.count(num)
print(result)