import sys

for line in sys.stdin:
    line = line.rstrip()

    if len(line) > 100:
        continue

    occur = {}

    for c in line:
        if c.isalpha():
            if c not in occur:
                occur[c] = 1
            else:
                occur[c] = occur[c] + 1

    # print number of characters.
    print(len(line.split(' ')))

    # print char freq.
    for k, v in sorted(occur.items(), key=lambda k: k[0].lower()):
        print(k + " : " + str(v))
