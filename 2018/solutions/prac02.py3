import sys

for line in sys.stdin:
    noun, verb = line.split()
    print(noun, "is", verb, "today!");
