"""
7 6 4 2 1

we first check if it's increasing or decreasing
its decreasing so all numbers should be below this number and the difference between should be less than eq to 3

pattern
check if first no is smaller or larger than second no
if first is smaller than second, the flag is asc else desc
the difference between the two should be not greater than 3
7 6
is 7 > 6 yes so its decending
if decending then minus second from first
7-6 1 <=3
6 4
6 > 4
"""
def is_safe(report):
    print("Report", report)
    """
    Check if a report is inherently safe.
    A report is safe if all levels are increasing or decreasing and adjacent
    differences are within the range [1, 3].
    """
    if len(report) < 2:
        return True  # A single-level report is inherently safe.

    # Check if the report is increasing or decreasing
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))

    return increasing or decreasing


def can_be_made_safe(report):
    """
    Check if a report can be made safe by removing one level.
    """
    for i in range(len(report)):
        # Create a modified report by removing the i-th level
        modified_report = report[:i] + report[i + 1:]
        print("mod", modified_report)
        if is_safe(modified_report):
            return True
    return False


with open("test.txt") as f:
    reports = [[int(x) for x in line.split()] for line in f.read().splitlines()]

safe_count = 0

for report in reports:
    if is_safe(report) or can_be_made_safe(report):
        safe_count += 1

print(safe_count)

