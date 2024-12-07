import cProfile
import re


def main():
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    file = open("input.txt", "r")
    line = file.read()
    ans = pattern.findall(line)
    ans = [[int(i) for i in a] for a in ans]
    final = []
    for i in ans:
        final.append(i[0] * i[1])
    print(sum(final))


cProfile.run('main()')





#170778545
