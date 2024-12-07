import re

pattern = re.compile(r"mul\((\d+),(\d+)\)")


total = 0

with open("input.txt", "r") as file:
    for line in file:
        for match in pattern.finditer(line):
            num1, num2 = map(int, match.groups())
            total += num1 * num2

print(total)