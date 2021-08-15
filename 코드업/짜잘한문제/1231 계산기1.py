expression = input()

for i in range(0, len(expression)):
    if(expression[i] == '+'):
        num1 = int(expression[:i])
        num2 = int(expression[i+1:])
        result = num1 + num2
        print(num1 + num2)
    elif(expression[i] == '-'):
        num1 = int(expression[:i])
        num2 = int(expression[i+1:])
        result = num1 - num2
        print(num1 - num2)
    elif(expression[i] == '*'):
        num1 = int(expression[:i])
        num2 = int(expression[i+1:])
        result = num1 * num2
        print(num1 * num2)
    elif(expression[i] == '/'):
        num1 = int(expression[:i])
        num2 = int(expression[i+1:])
        result = float(num1) / float(num2)
        print('%.2f' % result)