

# Calculator


def calc(a, b, op):

    if op not in '+-/*':
        return 'Please enter these: "+, -, *, /"!'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


def main():

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    print(calc(a, b, op))

if __name__ == '__main__':
    main()
