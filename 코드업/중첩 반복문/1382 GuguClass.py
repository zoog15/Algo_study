string = ''
for x in range(1, 10):
    for y in range(2, 6):
        if (y == 5):
            string += '%d x %d = %2d\n' % (y, x, x * y)
            break
        string += '%d x %d = %2d\t' % (y, x, x * y)

print(string)