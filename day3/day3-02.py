import re

main_pattern = re.compile(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)")

total = 0
enabled = True

with open("input.txt", "r") as file:
    for line in file:
        iterator = re.finditer(main_pattern, line)
        for match in iterator:
            if match.group(0) == "don't()":
                enabled = False
            elif match.group(0) == "do()":
                enabled = True
            elif match.group(0).startswith("mul") and enabled:
                num1, num2 = map(int, match.groups())
                total += num1 * num2

print(total)