fp = open('text.txt', 'r')
print(fp.read())
fp.close()

# same thing but more pythonic
with open('text.txt', 'r') as fp:
    print(fp.read())

print('We are done, the context closed bu the indent')

# read the same file but line by line
with open('text.txt', 'r') as fp:
    line_number = 1
    for line in fp:
        # print(line, end='')
        print(f'{line_number}: {line.strip()}')
        line_number += 1